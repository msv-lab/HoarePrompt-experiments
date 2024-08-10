import ast

from correctness_main import check_program
from complete import analyze_code_with_precondition, analyze_code_with_precondition_cot
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
parse_code = ast.parse(replaced_code).body
precondition = "n is an integer."

hoare_cot_post = analyze_code_with_precondition_cot(parse_code, precondition)

hoare_cot_correctness_str, hoare_cot_response = check_program(specification, replaced_code, hoare_cot_post)
no_explanation_correctness_str, no_explanation_response = check_program(specification, code)

print('='*50)
print(f"Result:")
print(f"HoareCoT result: {hoare_cot_correctness_str}")
print(f"No Explanation Result: {no_explanation_correctness_str}")
print('='*50)
print(f"HoareCoT Post: {hoare_cot_post}")
print('='*50)
print(f"CoT Response: {hoare_cot_response}")
print(f"No Explanation Response: {no_explanation_response}")


