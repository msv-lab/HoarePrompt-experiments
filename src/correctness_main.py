import ast
from datetime import datetime

from complete import analyze_code_with_precondition_non_cot, analyze_code_with_precondition_cot, chat_with_groq2
from prompt import CHECK_CODE_PROMPT_WITH_EXPLANATION, CHECK_CODE_PROMPT
from file_io import load_json
from logger_setup import logger_setup
from extractor import extract_correctness_from_response

DATA_FILE = 'data/mixtral_20240620(simple).json'
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
        response = chat_with_groq2(model=MODEL, messages=messages, temperature=DEFAULT_TEMPERATURE)
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
        response = chat_with_groq2(model=MODEL, messages=messages, temperature=DEFAULT_TEMPERATURE)
        model_answer = response.choices[0].message.content
        correctness = extract_correctness_from_response(model_answer)
        return correctness, model_answer


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
        cot_correctness, cot_response = check_program(specification, code, result_cot)
        non_cot_correctness, non_cot_response = check_program(specification, code, result_non_cot)
        no_explanation_correctness, no_explanation_response = check_program(specification, code)

        if cot_correctness not in ["True", "False"]:
            logger.warning(f"Unexpected correctness value for COT. Task ID: {task_id}")
            cot_correctness = "False"
        if non_cot_correctness not in ["True", "False"]:
            logger.warning(f"Unexpected correctness value for non-COT. Task ID: {task_id}")
            non_cot_correctness = "False"
        if no_explanation_correctness not in ["True", "False"]:
            logger.warning(
                f"Unexpected correctness value for no explanation. Task ID: {task_id}")
            no_explanation_correctness = "False"

        is_cot_correct = cot_correctness == "True"
        non_cot_analysis_result = non_cot_correctness == "True"
        no_explanation_analysis_result = no_explanation_correctness == "True"

        print(f"cot result: {is_cot_correct}")
        print(f"non-cot result: {non_cot_analysis_result}")
        print(f"no explanation result: {no_explanation_analysis_result}")

        if is_cot_correct == test_result:
            cot_correct += 1
        if non_cot_analysis_result == test_result:
            non_cot_correct += 1
        if no_explanation_analysis_result == test_result:
            no_explanation_correct += 1

        if is_cot_correct != non_cot_analysis_result:
            logger.info(f"Task ID: {task_id}")
            logger.info(f"Specification: {specification}")
            logger.info(f"Code:\n{code}")
            logger.info(f"Test Result: {task_data['test_result']}")
            logger.info(f"COT Postcondition: {result_cot}")
            logger.info(f"non-COT Postcondition: {result_non_cot}")
            logger.info(f"COT Result: {is_cot_correct}")
            logger.info(f"non-COT Result: {non_cot_analysis_result}")
            logger.info(f"COT Explanation: {cot_response}")
            logger.info(f"non-COT Explanation: {non_cot_response}")
            logger.info("=" * 50)
        print(f"total test: {total}")
        print(f"cot total correct: {cot_correct}")
        print(f"non-cot total correct: {non_cot_correct}")
        print(f"no explanation total correct: {no_explanation_correct}")

    non_cot_rate, cot_rate, no_explanation_rate = non_cot_correct / total, cot_correct / total, no_explanation_correct / total

    print(cot_rate)
    print(non_cot_rate)
    print(no_explanation_rate)
    logger.info(f"COT Correct Rate: {cot_rate}")
    logger.info(f"non-COT Correct Rate: {non_cot_rate}")
    logger.info(f"No Explanation Correct Rate: {no_explanation_rate}")


if __name__ == "__main__":
    data = load_json(DATA_FILE)
    base = datetime.now().strftime("%Y%m%d-%H%M%S")
    logger = logger_setup(base, f"{MODEL[:3]}_code_correctness")
    main(data, logger)
