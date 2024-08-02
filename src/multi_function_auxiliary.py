import ast
import astor

from hoare_triple import Triple, State
from prompt import AUX_PRECONDITION_EXTRACTION_PROMPT
from extractor import extract_precondition_from_response

DEFAULT_TEMPERATURE = 0.7
MODEL = "mixtral-8x7b-32768"

class FunctionDefVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_defs = {}

    def visit_FunctionDef(self, node):
        self.function_defs[node.name] = node
        self.generic_visit(node)

    def get_func_defs_map(self):
        return self.function_defs

def get_called_function_name(func):
    if isinstance(func, ast.Name):
        return func.id
    # TODO: for class method later
    elif isinstance(func, ast.Attribute):
        return func.attr
    else:
        raise Exception("Not a function call")


def find_function_calls(node):
    calls = []
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            calls.append(child)
    return calls

def get_func_triple(func_map, func_name, precondition, call_node):
    from complete import chat_with_groq
    if func_name not in func_map:
        return []
    elif isinstance(func_map[func_name], tuple):
        return func_map[func_name][1]
    else:
        function = func_map[func_name]
        user_message = {
            "role": "user",
            "name": "user",
            "content": f"Context: {precondition}\nCaller: {astor.to_source(call_node)}\nCallee:\n{astor.to_source(function)}"
        }
        print(user_message["content"])
        messages = AUX_PRECONDITION_EXTRACTION_PROMPT.copy()
        messages.append(user_message)
        response = chat_with_groq(model=MODEL, messages=messages, temperature=DEFAULT_TEMPERATURE)
        model_answer = response.choices[0].message.content
        precondition = extract_precondition_from_response(model_answer)

        return Triple(precondition, function, State.UNKNOWN)
