import os
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential
from groq import Groq
import ast

from hoare_triple import State, Triple, parse_stmt, pprint_cmd
from prompt import VERIFYER_SYSTEM_PROMPT
from extractor import extract_postcondition

client1 = Groq(api_key=os.environ.get("GROQ_API_KEY1"))
client2 = Groq(api_key=os.environ.get("GROQ_API_KEY2"))

DEFAULT_TEMPERATURE = 0.7
MODEL = "mixtral-8x7b-32768"

generic_ctx = [
    Triple(
        State.TOP,
        parse_stmt("n = int(input())"),
        "n is an input integer"),
    Triple(
        "n is either 3 or 5",
        parse_stmt("m = n + 1"),
        "n is either 3 or 5; m is either 4 or 6"),
    Triple(
        "x is greater than zero",
        parse_stmt("x = x + 1"),
        "x greater than one"),
    Triple(
        "i is integer",
        parse_stmt("i += 1"),
        "i is integer and i is increased by 1"),
    Triple(
        State.TOP,
        parse_stmt("raise ValueError('An error occurred')"),
        "ValueError is raised"),
    Triple(
        "x is odd number, y is positive float",
        parse_stmt("break"),
        "x is odd number, y is positive float, loop is break"),
]


@retry(wait=wait_random_exponential(min=1, max=240), stop=stop_after_attempt(15))
def chat_with_groq1(**kwargs):
    return client1.chat.completions.create(**kwargs)


@retry(wait=wait_random_exponential(min=1, max=240), stop=stop_after_attempt(15))
def chat_with_groq2(**kwargs):
    return client2.chat.completions.create(**kwargs)



def complete_triple(incomplete_triple, context_triples=generic_ctx):
    msgs = []
    msgs.append({"role": "system", "content": VERIFYER_SYSTEM_PROMPT})
    for ctx in context_triples:
        msgs.append({"role": "system", "name": "example_user", "content": format_prompt(ctx)})
    msgs.append({"role": "user", "content": format_prompt(incomplete_triple)})
    response = chat_with_groq1(model=MODEL, messages=msgs, temperature=DEFAULT_TEMPERATURE)
    post = extract_postcondition(response.choices[0].message.content)
    return post


def format_prompt(triple: Triple) -> str:
    if triple.postcondition is State.UNKNOWN:
        return f"Precondition: {triple.precondition}\nProgram statement:\n```\n{pprint_cmd(triple.command)}```"
    return f"Precondition: {triple.precondition}\nProgram statement:\n```\n{pprint_cmd(triple.command)}```\nPostcondition: {triple.postcondition}"


def complete_triple_cot(triple: Triple) -> str:
    assert triple.postcondition == State.UNKNOWN
    if isinstance(triple.command,
                  (ast.Assign, ast.AugAssign, ast.Expr, ast.Return, ast.Raise, ast.Pass, ast.Break, ast.Continue)):
        post = complete_triple(triple)
        return post
    if isinstance(triple.command, list):
        pre = triple.precondition
        ctx = []
        for subcmd in triple.command:
            completion = complete_triple_cot(Triple(pre, subcmd, State.UNKNOWN))
            ctx.append(Triple(pre, subcmd, completion))
            pre = completion
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.If):
        pre = triple.precondition
        then_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        ctx = [Triple(pre, triple.command.body, then_completion)]
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(pre, triple.command.orelse, State.UNKNOWN))
            ctx.append(Triple(pre, triple.command.orelse, else_completion))
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.Try):
        pre = triple.precondition
        try_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        except_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.body, State.UNKNOWN))
        ctx = [Triple(pre, triple.command.body, try_completion), Triple(State.UNKNOWN, triple.command.body, except_completion)]
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(try_completion, triple.command.orelse, State.UNKNOWN))
            ctx.append(Triple(pre, triple.command.orelse, else_completion))
        if triple.command.finalbody:
            finally_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.finalbody, State.UNKNOWN))
            ctx.append(Triple(State.UNKNOWN, triple.command.orelse, finally_completion))
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.For):
        pre = triple.precondition
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        ctx = [Triple(pre, triple.command.body, body_completion)]
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.While):
        pre = triple.precondition
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN))
        ctx = [Triple(pre, triple.command.body, body_completion)]
        return complete_triple(triple, ctx)
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