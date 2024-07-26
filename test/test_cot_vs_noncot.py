import ast

from correctness_main import check_program
from complete import analyze_code_with_precondition_non_cot, analyze_code_with_precondition_cot
from extractor import replace_function_name

specification = "Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not."
code = "def is_Sum_Of_Powers_Of_Two(n):\r\n    while n != 0:\r\n        if n & 1:\r\n            return True\r\n        n = n >> 1\r\n    return False\n"
replaced_code = replace_function_name(code)
print(replaced_code)
parse_code = ast.parse(replaced_code).body
precondition = "n is an integer."

cot_post = analyze_code_with_precondition_cot(parse_code, precondition)
non_cot_post = analyze_code_with_precondition_non_cot(parse_code, precondition)

cot_correctness_str, cot_response = check_program(specification, code, cot_post)
non_cot_correctness_str, non_cot_response = check_program(specification, code, non_cot_post)

print('='*50)
print(f"Result:")
print(f"CoT result: {cot_correctness_str}")
print(f"non-CoT result: {non_cot_correctness_str}")
print('='*50)
print(f"CoT Post: {cot_post}")
print(f"non-CoT Post: {non_cot_post}")
print('='*50)
print(f"CoT Response: {cot_response}")
print(f"non-CoT Response: {non_cot_response}")


