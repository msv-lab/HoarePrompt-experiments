import ast
from datetime import datetime
from math import sqrt
import csv
import os

from complete import analyze_code_with_precondition_non_cot, analyze_code_with_precondition_cot, chat_with_groq
from prompt import CHECK_CODE_PROMPT_WITH_EXPLANATION, CHECK_CODE_PROMPT
from file_io import load_json
from logger_setup import logger_setup
from extractor import extract_correctness_from_response

DATA_FILE = 'data/mixtral_20240715(complex).json'
MODEL = "mixtral-8x7b-32768"
DEFAULT_TEMPERATURE = 0.7


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
        return correctness, model_answer

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
        return correctness, model_answer


def calculate_mcc(tp, tn, fp, fn):
    numerator = tp * tn - fp * fn
    denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    if denominator == 0:
        return 0
    return numerator / denominator


def update_metrics(correctness, test_result, tp, tn, fp, fn):
    if correctness == test_result:
        if test_result:
            tp += 1
        else:
            tn += 1
    else:
        if test_result:
            fn += 1
        else:
            fp += 1
    return tp, tn, fp, fn


def main(data, logger):
    total = 0
    non_cot_correct = 0
    cot_correct = 0
    no_explanation_correct = 0

    # use for MCC
    tp_cot, tn_cot, fp_cot, fn_cot = 0, 0, 0, 0
    tp_non_cot, tn_non_cot, fp_non_cot, fn_non_cot = 0, 0, 0, 0
    tp_no_explanation, tn_no_explanation, fp_no_explanation, fn_no_explanation = 0, 0, 0, 0

    # CSV logger header
    columns = [
        "Task ID", "Specification", "Code", "Test Result",
        "COT Correctness", "non-COT Correctness", "No Explanation Correctness",
        "COT Response", "non-COT Response", "No Explanation Response"
    ]
    if not os.path.exists(logger.csv_file):
        with open(logger.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

    # main loop, iterate each task in data
    for task_id, task_data in data.items():
        specification = task_data["specification"]
        precondition = task_data["precondition"]
        code = task_data["code"]
        test_result = task_data["test_result"] == 1

        logger.debug(f"Start Task {task_id}")

        # if connot parse, skip this task
        try:
            parsed_code = ast.parse(code).body
        except Exception as e:
            logger.debug(f"Task {task_id} skip due to parse error: {e}\n\n\n")
            continue

        try:
            # get cot and non-cot postcondition
            non_cot_explanation = analyze_code_with_precondition_non_cot(parsed_code, precondition)
            cot_explanation = analyze_code_with_precondition_cot(parsed_code, precondition)

            # use postcondition to analyse code correctness
            total += 1
            cot_correctness_str, cot_response = check_program(specification, code, cot_explanation)
            non_cot_correctness_str, non_cot_response = check_program(specification, code, non_cot_explanation)
            no_explanation_correctness_str, no_explanation_response = check_program(specification, code)
        except Exception as e:
            logger.error(f"Error: {e}")
            break

        # if connot extract correctness, add a warning to logger. Need to manually fix it after finish.
        if cot_correctness_str not in ["True", "False"]:
            logger.warning(f"Unexpected correctness value for COT. Task ID: {task_id}")
            cot_correctness_str = "False"
        if non_cot_correctness_str not in ["True", "False"]:
            logger.warning(f"Unexpected correctness value for non-COT. Task ID: {task_id}")
            non_cot_correctness_str = "False"
        if no_explanation_correctness_str not in ["True", "False"]:
            logger.warning(
                f"Unexpected correctness value for no explanation. Task ID: {task_id}")
            no_explanation_correctness_str = "False"

        cot_correctness_bool = cot_correctness_str == "True"
        non_cot_correctness_bool = non_cot_correctness_str == "True"
        no_explanation_correctness_bool = no_explanation_correctness_str == "True"

        # update variables
        if cot_correctness_bool == test_result:
            cot_correct += 1
        if non_cot_correctness_bool == test_result:
            non_cot_correct += 1
        if no_explanation_correctness_bool == test_result:
            no_explanation_correct += 1

        tp_cot, tn_cot, fp_cot, fn_cot = update_metrics(cot_correctness_bool, test_result, tp_cot, tn_cot, fp_cot,
                                                        fn_cot)
        tp_non_cot, tn_non_cot, fp_non_cot, fn_non_cot = update_metrics(non_cot_correctness_bool, test_result,
                                                                        tp_non_cot, tn_non_cot, fp_non_cot, fn_non_cot)
        tp_no_explanation, tn_no_explanation, fp_no_explanation, fn_no_explanation = update_metrics(
            no_explanation_correctness_bool, test_result, tp_no_explanation, tn_no_explanation, fp_no_explanation,
            fn_no_explanation)

        # write to logger
        logger.debug(f"Specification: {specification}")
        logger.debug(f"Code:\n{code}")
        logger.debug(f"Test Pass Rate {task_data['test_result']}")
        logger.debug(f"CoT Postcondition: {cot_explanation}")
        logger.debug(f"non-CoT Postcondition: {non_cot_explanation}")
        logger.debug(f"CoT Correctness: {cot_correctness_bool}")
        logger.debug(f"non-CoT Correctness: {non_cot_correctness_bool}")
        logger.debug(f"No Explanation Correctness: {no_explanation_correctness_bool}")
        logger.debug(f"CoT Response: {cot_response}")
        logger.debug(f"non-CoT Response: {non_cot_response}")
        logger.debug(f"No Explanation Response: {no_explanation_response}\n")

        logger.debug(f"Total Test: {total}")
        logger.debug(f"CoT Total Correct: {cot_correct}")
        logger.debug(f"non-CoT Total Correct: {non_cot_correct}")
        logger.debug(f"No Explanation Total Correct: {no_explanation_correct}\n\n\n")

        # write to csv logger
        result = {
            "Task ID": task_id,
            "Specification": specification,
            "Code": code,
            "Test Result": test_result,
            "COT Correctness": cot_correctness_str,
            "non-COT Correctness": non_cot_correctness_str,
            "No Explanation Correctness": no_explanation_correctness_str,
            "COT Response": cot_response,
            "non-COT Response": non_cot_response,
            "No Explanation Response": no_explanation_response
        }

        with open(logger.csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(result)

    # calculate final result and write to logger
    cot_rate = cot_correct / total
    non_cot_rate = non_cot_correct / total
    no_explanation_rate = no_explanation_correct / total
    mcc_cot = calculate_mcc(tp_cot, tn_cot, fp_cot, fn_cot)
    mcc_non_cot = calculate_mcc(tp_non_cot, tn_non_cot, fp_non_cot, fn_non_cot)
    mcc_no_explanation = calculate_mcc(tp_no_explanation, tn_no_explanation, fp_no_explanation, fn_no_explanation)

    logger.info(f"CoT Accuracy: {cot_rate}")
    logger.info(f"non-CoT Accuracy: {non_cot_rate}")
    logger.info(f"No Explanation Accuracy: {no_explanation_rate}\n")

    logger.info(f"CoT Confusion Matrix: tp-{tp_cot}, fp-{fp_cot}, fn-{fn_cot}, tn-{tn_cot}")
    logger.info(f"non-CoT Confusion Matrix: tp-{tp_non_cot}, fp-{fp_non_cot}, fn-{fn_non_cot}, tn-{tn_non_cot}")
    logger.info(f"No Explanation Confusion Matrix: tp-{tp_no_explanation}, fp-{fp_no_explanation}, fn-{fn_no_explanation}, tn-{tn_no_explanation}")
    logger.info(f"CoT MCC: {mcc_cot}")
    logger.info(f"non-CoT MCC: {mcc_non_cot}")
    logger.info(f"No Explanation MCC: {mcc_no_explanation}")


if __name__ == "__main__":
    data = load_json(DATA_FILE)
    base = datetime.now().strftime("%Y%m%d-%H%M%S")
    logger = logger_setup(base, f"{MODEL[:5]}_correctness")
    main(data, logger)
