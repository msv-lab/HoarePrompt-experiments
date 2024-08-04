import os
from tenacity import retry, stop_after_attempt, wait_random_exponential
from groq import Groq
import openai
import ast

from hoare_triple import State, Triple, IfTriple, WhileTriple, parse_stmt, pprint_cmd, print_state
from prompt import VERIFYER_SYSTEM_PROMPT, VERIFYER_SYSTEM_PROMPT_IF, VERIFYER_SYSTEM_PROMPT_LOOP
from extractor import extract_postcondition

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
openai.api_key = os.environ.get("OPENAI_API_KEY")

DEFAULT_TEMPERATURE = 0.7
MODEL = "mixtral-8x7b-32768"
# MODEL = "gpt-3.5-turbo-0125"

generic_ctx = [
    Triple(
        "str is a string",
        parse_stmt("n = int(input())"),
        "str is a string, n is an input integer"),
    Triple(
        State.TOP,
        parse_stmt("i += 1"),
        "variable i is increased by 1"
    ),
    Triple(
        "n is either 3 or 5",
        parse_stmt("m = n + 1"),
        "n is either 3 or 5; m is either 4 or 6"),
    Triple(
        State.TOP,
        parse_stmt("return True"),
        "The function return True"),
    Triple(
        "i is integer",
        parse_stmt("j += len(str1)"),
        "i is integer and j is the length of str1"),
    Triple(
        "n is a positive integer",
        parse_stmt("memo = [-1] * (n + 1)"),
        "n is a positive integer, memo is a list of length n+1 with all initial values set to -1."),
]

generic_if_ctx = [
    IfTriple(
        "str is a string",
        parse_stmt('''
if len(str) < 3:
    return None
    '''),
        "The function returns None",
        "there is no else part in the code",
        "str is a string, if the length of str is less then 3, the function return None"),
    IfTriple(
        State.TOP,
        parse_stmt('''
if isinstance(n, int):
    return n
else:
    return int(n)
    '''),
        "The function returns n",
        "The function returns int(n)",
        "if n is integer, then the function returns n itself. Otherwise, the function return int(n)"),
    IfTriple(
        "x is an positive integer",
        parse_stmt('''
if x < 2:
    return False
else:
    return True
    '''),
        "The function return False",
        "The function return True",
        "x is a positive integer, if x is less then 2, the function return False. Otherwise, the function return True"),
    IfTriple(
        "m is 0, n is an integer",
        parse_stmt('''
if n < 0:
    n = -n
    m += 1
elif n == 0:
    return m
else:
    n -= 13
    m += 1
    '''),
        "The variable n is updated to its negation.",
        "If n is 0, the function returns 0. Otherwise, n has been decreased by 13 and m is increased by 1.",
        "n is an integer. If n < 0, m is 1 and n is negated. If n == 0, the function returns m which is 0. Otherwise, n is decreased by 13 and m is 1."),
]

generic_while_ctx = [
    WhileTriple(
        "n is 5, factorial is 1",
        parse_stmt('''
while n > 0:
    factorial *= n
    n -= 1
    '''),
    "factorial is updated to its previous value multiplied by n, and n is decremented by 1.",
    "n is 0 and variable factorial holds the value of the factorial of 5, which is 120."
    ),
    WhileTriple(
        State.TOP,
        parse_stmt('''
while i * i <= n:
    i += 1
    '''),
    "i is increased by 1",
    "If i squared is greater than n before the loop, i remains unchanged. If i squared is less than or equal to n, i increments by 1 each iteration. After the loop, i is the smallest integer whose square is strictly greater than n."
    ),
]


@retry(wait=wait_random_exponential(min=1, max=300), stop=stop_after_attempt(15))
def chat_with_groq(**kwargs):
    return client.chat.completions.create(**kwargs)


@retry(wait=wait_random_exponential(min=1, max=300), stop=stop_after_attempt(15))
def chat_with_gpt(**kwargs):
    return openai.Completion.creat(**kwargs)


def complete_triple(incomplete_triple, context_triples=generic_ctx, example_number=5):
    if len(context_triples) < example_number:
        context_triples = generic_ctx[:example_number - len(context_triples)] + context_triples
    msgs = [{"role": "system", "content": VERIFYER_SYSTEM_PROMPT}]
    for ctx in context_triples:
        msgs.append({"role": "system", "name": "example_user", "content": format_prompt(ctx)})
        msgs.append({"role": "assistant", "content": f"Postcondition: **{ctx.postcondition}**"})
    msgs.append({"role": "user", "content": format_prompt(incomplete_triple)})
    response = chat_with_groq(model=MODEL, messages=msgs, temperature=DEFAULT_TEMPERATURE)
    post = extract_postcondition(response.choices[0].message.content)
    # print("+" * 50)
    # print(incomplete_triple)
    # print(post)
    return post


def complete_if_triple(incomplete_triple, context_triples=generic_if_ctx):
    msgs = [{"role": "system", "content": VERIFYER_SYSTEM_PROMPT_IF}]
    for ctx in context_triples:
        msgs.append({"role": "system", "name": "example_user", "content": format_prompt(ctx)})
        msgs.append({"role": "assistant", "content": f"Postcondition: **{ctx.postcondition}**"})
    msgs.append({"role": "user", "content": format_prompt(incomplete_triple)})
    response = chat_with_groq(model=MODEL, messages=msgs, temperature=DEFAULT_TEMPERATURE)
    post = extract_postcondition(response.choices[0].message.content)
    # print("*" * 50)
    # print(incomplete_triple)
    # print(post)
    return post

def complete_while_triple(incomplete_triple, context_triples=generic_while_ctx):
    msgs = [{"role": "system", "content": VERIFYER_SYSTEM_PROMPT_LOOP}]
    for ctx in context_triples:
        msgs.append({"role": "system", "name": "example_user", "content": format_prompt(ctx)})
        msgs.append({"role": "assistant", "content": f"Postcondition: **{ctx.postcondition}**"})
    msgs.append({"role": "user", "content": format_prompt(incomplete_triple)})
    response = chat_with_groq(model=MODEL, messages=msgs, temperature=DEFAULT_TEMPERATURE)
    post = extract_postcondition(response.choices[0].message.content)
    # print("*" * 50)
    # print(incomplete_triple)
    # print(post)
    return post


def format_prompt(triple) -> str:
    if isinstance(triple, Triple):
        return f"Precondition: {print_state(triple.precondition)}\nProgram fragment:\n```\n{pprint_cmd(triple.command)}```"

    if isinstance(triple, IfTriple):
        return f"Precondition: {print_state(triple.precondition)}\nProgram fragment:\n```\n{pprint_cmd(triple.command)}```\nPostcondition for if: {triple.if_postcondition}\nPostcondition for else: {'there is no else part in the code' if triple.else_postcondition is None else triple.else_postcondition}"

    if isinstance(triple, WhileTriple):
        return f"Precondition: {print_state(triple.precondition)}\nProgram fragment:\n```\n{pprint_cmd(triple.command)}```\nPostcondition loop body: {triple.body_postcondition}"

def complete_triple_cot(triple: Triple) -> str:
    assert triple.postcondition == State.UNKNOWN
    if isinstance(triple.command,
                  (ast.Assign, ast.AugAssign, ast.Expr, ast.Return, ast.Raise, ast.Pass, ast.Break, ast.Continue)):
        post = complete_triple(triple)
        return post
    if isinstance(triple.command, list):
        pre = triple.precondition
        if len(triple.command) == 1 and isinstance(
                triple.command[0],
                (ast.Assign, ast.AugAssign, ast.Expr, ast.Return, ast.Raise, ast.Pass, ast.Break, ast.Continue)):
            overall_post = complete_triple(triple)
            return overall_post

        ctx = []
        for subcmd in triple.command:
            completion = complete_triple_cot(Triple(pre, subcmd, State.UNKNOWN))
            ctx.append(Triple(pre, subcmd, completion))
            pre = completion
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.If):
        pre = State.TOP
        then_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        if_post = Triple(pre, triple.command.body, then_completion)

        else_post = None
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(pre, triple.command.orelse, State.UNKNOWN))
            else_post = Triple(pre, triple.command.orelse, else_completion)

        if_triple = IfTriple(triple.precondition, triple.command, if_post, else_post, State.UNKNOWN)
        return complete_if_triple(if_triple)
    if isinstance(triple.command, ast.Try):
        pre = triple.precondition
        try_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        except_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.body, State.UNKNOWN))
        ctx = [Triple(pre, triple.command.body, try_completion),
               Triple(State.UNKNOWN, triple.command.body, except_completion)]
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(try_completion, triple.command.orelse, State.UNKNOWN))
            ctx.append(Triple(pre, triple.command.orelse, else_completion))
        if triple.command.finalbody:
            finally_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.finalbody, State.UNKNOWN))
            ctx.append(Triple(State.UNKNOWN, triple.command.orelse, finally_completion))
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.For):
        pre = State.TOP
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        while_triple = WhileTriple(triple.precondition, triple.command, body_completion, State.UNKNOWN)
        return complete_while_triple(while_triple)
    if isinstance(triple.command, ast.While):
        pre = State.TOP
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        while_triple = WhileTriple(triple.precondition, triple.command, body_completion, State.UNKNOWN)
        return complete_while_triple(while_triple)
    if isinstance(triple.command, ast.FunctionDef):
        pre = triple.precondition
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        ctx = [Triple(pre, triple.command.body, body_completion)]
        return complete_triple(triple, ctx)
    if isinstance(triple.command, (ast.Import, ast.ImportFrom, ast.Assert)):
        return triple.precondition
    raise ValueError(f"unsupported statement type: {triple.command} {pprint_cmd(triple.command)}")


def analyze_code_with_precondition_non_cot(parsed_code, precondition: str) -> str:
    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple(triple)
    return postcondition


def analyze_code_with_precondition_cot(parsed_code, precondition: str) -> str:
    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple_cot(triple)
    return postcondition
