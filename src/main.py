# main.py

import ast
from datetime import datetime

from complete import complete_triple, complete_triple_cot, chat_with_groq
from hoare_triple import State, Triple
from prompt import CHECK_CODE_PROMPT_WITH_EXPLANATION, CHECK_CODE_PROMPT
from file_io import load_json
from logger_setup import logger_setup
from extractor import extract_correctness_from_response

DATA_FILE = 'data/mixtral_250624.json'
MODEL = "mixtral-8x7b-32768"
DEFAULT_TEMPERATURE = 0.7


def analyze_code_with_precondition_non_cot(parsed_code, precondition: str) -> str:
    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple(triple)
    return postcondition

def analyze_code_with_precondition_cot(parsed_code, precondition: str) -> str:
    triple = Triple(precondition, parsed_code, State.UNKNOWN)
    postcondition = complete_triple_cot(triple)
    return postcondition


def check_program(specification, code, explanation=None):
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
        return correctness == "True", model_answer

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
        return correctness == "True", model_answer


def main(data, logger):
    total = 0
    non_cot_correct = 0
    cot_correct = 0
    no_explanation_correct = 0


    for task_id, task_data in data.items():
        print("="*50)
        print(f"start task {task_id}")
        specification = task_data["specification"]
        precondition = task_data["precondition"]
        code = task_data["code"]
        test_result = task_data["test_result"] == 1
        print(f"test result {task_data['test_result']}")

        try:
            parsed_code = ast.parse(code).body
        except Exception as e:
            print(f"task {task_id} skip due to parse error: {e}")
            continue

        result_non_cot = analyze_code_with_precondition_non_cot(parsed_code, precondition)
        result_cot = analyze_code_with_precondition_cot(parsed_code, precondition)

        total += 1
        is_cot_correct, cot_response = check_program(specification, code, result_cot)
        is_non_cot_correct, non_cot_response = check_program(specification, code, result_non_cot)
        is_no_explanation_correct, no_explanation_response = check_program(specification, code)

        print(f"cot result: {is_cot_correct}")
        print(f"non-cot result: {is_non_cot_correct}")
        print(f"no explanation result: {is_no_explanation_correct}")

        if is_cot_correct == test_result:
            cot_correct += 1
        if is_non_cot_correct == test_result:
            non_cot_correct += 1
        if is_no_explanation_correct == test_result:
            no_explanation_correct += 1

        if is_cot_correct != is_non_cot_correct:
            logger.info(f"Task ID: {task_id}")
            logger.info(f"Specification: {specification}")
            logger.info(f"Code:\n{code}")
            logger.info(f"Test Result: {task_data['test_result']}")
            logger.info(f"COT Explanation: {result_cot}")
            logger.info(f"non-COT Explanation: {result_non_cot}")
            logger.info(f"COT Correct: {is_cot_correct}")
            logger.info(f"non-COT Correct: {is_non_cot_correct}")
            logger.info(f"COT Response: {cot_response}")
            logger.info(f"non-COT Response: {non_cot_response}")
            logger.info("=" * 50)
        print(f"total test: {total}")
        print(f"cot total correct: {cot_correct}")
        print(f"non-cot total correct: {non_cot_correct}")
        print(f"no explanation total correct: {no_explanation_correct}")

    non_cot_rate, cot_rate, no_explanation_rate = non_cot_correct / total, cot_correct / total, no_explanation_correct / total

    print(cot_rate)
    print(non_cot_rate)
    print(no_explanation_rate)
    return non_cot_rate, cot_rate, no_explanation_rate


if __name__ == "__main__":
    data = load_json(DATA_FILE)
    base = datetime.now().strftime("%Y%m%d-%H%M%S")
    logger = logger_setup(base, "code_correctness")
    main(data, logger)
