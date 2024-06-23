# hoare_triple.py

from dataclasses import dataclass
from enum import Enum, auto
import ast
import astor

class State(Enum):
    TOP = auto()
    BOTTOM = auto()
    UNKNOWN = auto()

def print_state(s):
    if s == State.UNKNOWN:
        return "the state is unknown"
    if s == State.TOP:
        return "variables can hold any values"
    if s == State.BOTTOM:
        return "the state is unreachable"
    return s

@dataclass
class Triple:
    precondition: str
    command: ast.AST
    postcondition: str

    def __str__(self):
        return f"{{ {print_state(self.precondition)} }}\n{pprint_cmd(self.command)}{{ {print_state(self.postcondition)} }}"

    def with_postcondition(self, pc):
        return Triple(self.precondition, self.command, pc)

def parse_stmt(source):
    return ast.parse(source).body[0]

def pprint_cmd(cmd):
    if isinstance(cmd, list):
        return "\n".join([astor.to_source(c) for c in cmd])
    else:
        return astor.to_source(cmd)
