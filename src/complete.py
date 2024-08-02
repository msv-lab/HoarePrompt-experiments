import os
from tenacity import retry, stop_after_attempt, wait_random_exponential
from groq import Groq
import openai
import ast

from hoare_triple import State, Triple, parse_stmt, pprint_cmd, print_state
from prompt import VERIFYER_SYSTEM_PROMPT
from extractor import extract_postcondition
from multi_function_auxiliary import FunctionDefVisitor, get_called_function_name, get_func_triple, find_function_calls

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
openai.api_key = os.environ.get("OPENAI_API_KEY")

DEFAULT_TEMPERATURE = 0.7
MODEL = "mixtral-8x7b-32768"
# MODEL = "gpt-3.5-turbo-0125"

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
    return post


def format_prompt(triple: Triple) -> str:
    return f"Precondition: {print_state(triple.precondition)}\nProgram fragment:\n```\n{pprint_cmd(triple.command)}```"


def complete_triple_cot(triple: Triple, func_map: dict) -> str:
    assert triple.postcondition == State.UNKNOWN
    if isinstance(triple.command,
                  (ast.Assign, ast.AugAssign, ast.Expr, ast.Return, ast.Raise, ast.Pass, ast.Break, ast.Continue)):
        call_nodes = find_function_calls(triple.command)
        if call_nodes:
            ctx = []
            for call_node in call_nodes:
                func_name = get_called_function_name(call_node.func)
                func_triple = get_func_triple(func_map, func_name, triple.precondition, call_node)
                if func_triple == []:
                    continue
                elif func_triple.postcondition == State.UNKNOWN:
                    func_post = complete_triple_cot(func_triple, func_map)
                    ctx.append(Triple(func_triple.postcondition, func_triple.command, func_post))
                else:
                    ctx.append(func_triple)
            post = complete_triple(triple, ctx)
        else:
            post = complete_triple(triple)
        return post
    if isinstance(triple.command, list):
        pre = triple.precondition
        # if len(triple.command) == 1 and isinstance(
        #         triple.command[0],
        #         (ast.Assign, ast.AugAssign, ast.Expr, ast.Return, ast.Raise, ast.Pass, ast.Break, ast.Continue)):
        #     overall_post = complete_triple(triple)
        #     return overall_post

        ctx = []
        for subcmd in triple.command:
            completion = complete_triple_cot(Triple(pre, subcmd, State.UNKNOWN), func_map)
            ctx.append(Triple(pre, subcmd, completion))
            pre = completion
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.If):
        pre = triple.precondition
        then_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), func_map)
        ctx = [Triple(pre, triple.command.body, then_completion)]
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(pre, triple.command.orelse, State.UNKNOWN), func_map)
            ctx.append(Triple(pre, triple.command.orelse, else_completion))
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.Try):
        pre = triple.precondition
        try_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), func_map)
        except_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.body, State.UNKNOWN), func_map)
        ctx = [Triple(pre, triple.command.body, try_completion),
               Triple(State.UNKNOWN, triple.command.body, except_completion)]
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(try_completion, triple.command.orelse, State.UNKNOWN), func_map)
            ctx.append(Triple(pre, triple.command.orelse, else_completion))
        if triple.command.finalbody:
            finally_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.finalbody, State.UNKNOWN), func_map)
            ctx.append(Triple(State.UNKNOWN, triple.command.orelse, finally_completion))
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.For):
        pre = triple.precondition
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), func_map)
        ctx = [Triple(pre, triple.command.body, body_completion)]
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.While):
        pre = triple.precondition
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), func_map)
        ctx = [Triple(pre, triple.command.body, body_completion)]
        return complete_triple(triple, ctx)
    if isinstance(triple.command, ast.FunctionDef):
        pre = triple.precondition
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), func_map)
        ctx = [Triple(pre, triple.command.body, body_completion)]
        return complete_triple(triple, ctx)
    if isinstance(triple.command, (ast.Import, ast.ImportFrom, ast.Assert)):
        return triple.precondition
    raise ValueError(f"unsupported statement type: {triple.command} {pprint_cmd(triple.command)}")


def analyze_code_with_precondition(parsed_code, precondition: str) -> str:
    triple = Triple(precondition, parsed_code.body, State.UNKNOWN)
    postcondition = complete_triple(triple)
    return postcondition


def analyze_code_with_precondition_hoarecot(parsed_code, precondition: str) -> str:
    visitor = FunctionDefVisitor()
    visitor.visit(parsed_code)
    func_map = visitor.get_func_defs_map()
    main_function = func_map["func"]

    triple = Triple(precondition, main_function, State.UNKNOWN)

    postcondition = complete_triple_cot(triple, func_map)
    return postcondition