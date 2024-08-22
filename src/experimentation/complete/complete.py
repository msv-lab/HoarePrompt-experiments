import ast

from src.experimentation.complete.hoare_triple import State, Triple, IfTriple, LoopTriple, FuncTriple, pprint_cmd
from src.experimentation.complete.general import complete_triple
from src.experimentation.complete.if_statement import complete_if_triple
from src.experimentation.complete.loop import complete_while_triple, complete_for_triple
from src.experimentation.complete.function_definition import complete_func_triple
from src.common.communication import Model


def complete_triple_cot(triple: Triple, model: Model, temperature: float) -> str:
    # This function selects different processing logic based on various AST nodes and recursively obtains the overall postcondition.
    assert triple.postcondition == State.UNKNOWN
    if isinstance(triple.command,
                  (ast.Assign, ast.AugAssign, ast.Expr, ast.Return, ast.Raise, ast.Pass, ast.Break, ast.Continue)):
        post = complete_triple(triple, model, temperature)
        return post
    if isinstance(triple.command, list):
        pre = triple.precondition
        for subcmd in triple.command:
            completion = complete_triple_cot(Triple(pre, subcmd, State.UNKNOWN), model, temperature)
            pre = completion
        return pre
    if isinstance(triple.command, ast.If):
        pre = triple.precondition
        then_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), model, temperature)
        if_post = then_completion

        else_post = None
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(pre, triple.command.orelse, State.UNKNOWN), model, temperature)
            else_post = else_completion

        if_triple = IfTriple(pre, triple.command, if_post, else_post, State.UNKNOWN)
        return complete_if_triple(if_triple, model, temperature)
    if isinstance(triple.command, ast.Try):
        # TODO: this is a very old version.
        pre = triple.precondition
        try_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), model, temperature)
        except_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.body, State.UNKNOWN), model,
                                                temperature)
        ctx = [Triple(pre, triple.command.body, try_completion),
               Triple(State.UNKNOWN, triple.command.body, except_completion)]
        if triple.command.orelse:
            else_completion = complete_triple_cot(Triple(try_completion, triple.command.orelse, State.UNKNOWN), model,
                                                  temperature)
            ctx.append(Triple(pre, triple.command.orelse, else_completion))
        if triple.command.finalbody:
            finally_completion = complete_triple_cot(Triple(State.UNKNOWN, triple.command.finalbody, State.UNKNOWN),
                                                     model, temperature)
            ctx.append(Triple(State.UNKNOWN, triple.command.orelse, finally_completion))
        return complete_triple(triple, ctx, model, temperature)
    if isinstance(triple.command, ast.For):
        pre = State.TOP
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), model, temperature)
        while_triple = LoopTriple(triple.precondition, triple.command, body_completion, State.UNKNOWN)
        return complete_for_triple(while_triple, model, temperature)
    if isinstance(triple.command, ast.While):
        pre = State.TOP
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), model, temperature)
        while_triple = LoopTriple(triple.precondition, triple.command, body_completion, State.UNKNOWN)
        return complete_while_triple(while_triple, model, temperature)
    if isinstance(triple.command, ast.FunctionDef):
        pre = triple.precondition
        body_completion = complete_triple_cot(Triple(pre, triple.command.body, State.UNKNOWN), model, temperature)
        func_triple = FuncTriple(triple.precondition, triple.command, body_completion, State.UNKNOWN)
        return complete_func_triple(func_triple, model, temperature)
    if isinstance(triple.command, (ast.Import, ast.ImportFrom, ast.Assert)):
        return triple.precondition
    raise ValueError(f"unsupported statement type: {triple.command} {pprint_cmd(triple.command)}")


def analyze_code_with_precondition(parsed_code: ast.AST | list, precondition: str, model, temperature: float) -> str:
    # For external calls
    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple(triple, model, temperature)
    return postcondition


def analyze_code_with_precondition_cot(parsed_code: ast.AST | list, precondition: str, model: Model,
                                       temperature: float) -> str:
    # For external calls to HoareCoT
    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple_cot(triple, model, temperature)
    return postcondition
