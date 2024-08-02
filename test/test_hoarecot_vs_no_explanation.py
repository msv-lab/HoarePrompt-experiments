import ast

from correctness_main import check_program
from complete import analyze_code_with_precondition, analyze_code_with_precondition_hoarecot
from extractor import replace_function_name

specification = "Write a python function to find the volume of a triangular prism."
code = "def find_Volume(a, b, c):\r\n    s = (a + b + c) / 2\r\n    area = math.sqrt(s*(s-a)*(s-b)*(s-c))\r\n    return area * c\n"
replaced_code = replace_function_name(code)
print(replaced_code)
parse_code = ast.parse(replaced_code).body
precondition = "a, b, and c are positive real numbers such that a, b, and c are the lengths of the sides of a triangle."

cot_post = analyze_code_with_precondition_hoarecot(parse_code, precondition)
no_explanation_pos = analyze_code_with_precondition(parse_code, precondition)

cot_correctness_str, cot_response = check_program(specification, replaced_code, cot_post)
no_explanation_correctness_str, no_explanation_response = check_program(specification, code)

print('='*50)
print(f"Result:")
print(f"HoareCoT Result: {cot_correctness_str}")
print(f"No explanation Result: {no_explanation_correctness_str}")
print('='*50)
print(f"HoareCoT Post: {cot_post}")
print('='*50)
print(f"HoareCoT Response: {cot_response}")
print(f"No explanation Response: {no_explanation_response}")


