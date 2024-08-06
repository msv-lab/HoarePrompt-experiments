import ast

from correctness_main import check_program
from complete import analyze_code_with_precondition_non_cot, analyze_code_with_precondition_cot
from extractor import replace_function_name

specification = "Write a python function to find the number of divisors of a given integer."
code = """
import math
def divisor(n):
    count = 0
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == (n // i):
                count += 1
            else:
                count += 2
    return count
"""
replaced_code = replace_function_name(code)
print(replaced_code)
parse_code = ast.parse(replaced_code).body
precondition = "n is an integer."

hoare_cot_post = analyze_code_with_precondition_cot(parse_code, precondition)
cot_post = analyze_code_with_precondition_non_cot(parse_code, precondition)

hoare_cot_correctness_str, hoare_cot_response = check_program(specification, code, hoare_cot_post)
cot_correctness_str, cot_response = check_program(specification, code, cot_post)

print('='*50)
print(f"Result:")
print(f"HoareCoT Result: {hoare_cot_correctness_str}")
print(f"CoT Result: {cot_correctness_str}")
print('='*50)
print(f"HoareCoT Post: {hoare_cot_post}")
print(f"CoT Post: {cot_post}")
print('='*50)
print(f"HoareCoT Response: {hoare_cot_response}")
print(f"CoT Response: {cot_response}")


