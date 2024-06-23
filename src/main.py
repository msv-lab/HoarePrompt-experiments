# main.py

import ast
import re

from complete import complete_triple, complete_triple_cot, chat_with_groq
from hoare_triple import State, Triple
from prompt import CHECK_CODE_PROMPT_WITH_EXPLANATION, CHECK_CODE_PROMPT
from file_io import load_json

DATA_FILE = 'data/mixtral_200624.json'
MODEL = "mixtral-8x7b-32768"
DEFAULT_TEMPERATURE = 0.7



def analyze_code_with_precondition_non_cot(code: str, precondition: str) -> str:
    try:
        parsed_code = ast.parse(code).body
    except Exception as e:
        return "parse_error"

    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple(triple)
    return postcondition


def analyze_code_with_precondition_cot(code: str, precondition: str) -> str:
    try:
        parsed_code = ast.parse(code).body
    except Exception as e:
        return "parse_error"

    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple_cot(triple)
    return postcondition

def extract_correctness_from_response(response_content: str) -> str:
    pattern = r"Correctness:\s*\*\*(.*?)\*\*"
    match = re.search(pattern, response_content)
    if match:
        return match.group(1)
    return ""


def check_program(specification, code, explanation = None):
    if explanation:
        user_message = {
            "role": "user",
            "name": "user",
            "content": f"Specification: {specification}\nCode:\n```\n{code}\n```\nExplanation: {explanation}"
        }
        messages = CHECK_CODE_PROMPT_WITH_EXPLANATION.copy()
        messages.append(user_message)
        response = chat_with_groq(model=MODEL, messages=messages, temperature=DEFAULT_TEMPERATURE)
        model_answer = response.choices[0].message.content
        correctness = extract_correctness_from_response(model_answer)
        if correctness == "True":
            return 1
        else:
            return 0

    else:
        user_message = {
            "role": "user",
            "name": "user",
            "content": f"Specification: {specification}\nCode:\n```\n{code}\n```"
        }
        messages = CHECK_CODE_PROMPT.copy()
        messages.append(user_message)
        response = chat_with_groq(model=MODEL, messages=messages, temperature=DEFAULT_TEMPERATURE)
        model_answer = response.choices[0].message.content
        correctness = extract_correctness_from_response(model_answer)
        if correctness == "True":
            return 1
        else:
            return 0


def analyze_and_print_results(data):
    total = 0
    non_cot_correct = 0
    cot_correct = 0
    no_explanation_correct = 0

    for task_id, task_data in data.items():
        print(f"start task {task_id}")
        specification = task_data["specification"]
        precondition = task_data["precondition"]
        code = task_data["code"]

        result_non_cot = analyze_code_with_precondition_non_cot(code, precondition)
        if result_non_cot == "parse_error":
            print(f"task {task_id} skip")
            continue
        result_cot = analyze_code_with_precondition_cot(code, precondition)

        total += 1
        cot_correct += check_program(specification, code, result_cot)
        non_cot_correct += check_program(specification, code, result_non_cot)
        no_explanation_correct += check_program(specification, code)
        print(f"total test: {total}")
        print(f"cot correct: {cot_correct}")
        print(f"non cot correct: {non_cot_correct}")
        print(f"no explanation correct: {no_explanation_correct}")
        print(f"finished task {task_id}")

    non_cot_rate, cot_rate, no_explanation_rate = non_cot_correct/total, cot_correct/total, no_explanation_correct/total

    print(non_cot_rate)
    print(cot_rate)
    print(no_explanation_rate)
    return non_cot_rate, cot_rate, no_explanation_rate



if __name__ == "__main__":
    data = load_json(DATA_FILE)
    analyze_and_print_results(data)
