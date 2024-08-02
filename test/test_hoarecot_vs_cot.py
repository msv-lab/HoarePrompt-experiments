import ast

from correctness_main import check_program
from complete import analyze_code_with_precondition, analyze_code_with_precondition_hoarecot
from extractor import replace_function_name

specification = "Write a function to check if the given number is woodball or not."
code = 'def is\\_woodall(n):\r\n    result = False\r\n    for i in range(1, n)\r\n        if n \\* 2 ** i - 1 == math.factorial(i):\r\n            result = True\r\n    return result\n'
replaced_code = replace_function_name(code, "is_woodall")
parse_code = ast.parse(replaced_code)
precondition = "n is integer."

hoarecot_post = analyze_code_with_precondition_hoarecot(parse_code, precondition)
cot_post = analyze_code_with_precondition(parse_code, precondition)

hoarecot_correctness_str, hoarecot_response = check_program(specification, replaced_code, hoarecot_post)
cot_correctness_str, cot_response = check_program(specification, replaced_code, cot_post)

print('='*50)
print(f"Result:")
print(f"HoareCoT result: {hoarecot_correctness_str}")
print(f"CoT result: {cot_correctness_str}")
print('='*50)
print(f"HoareCoT Post: {hoarecot_post}")
print(f"CoT Post: {cot_post}")
print('='*50)
print(f"HoareCoT Response: {hoarecot_response}")
print(f"CoT Response: {cot_response}")


