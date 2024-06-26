import os

from complete import chat_with_groq
from prompt import CODE_GEN_PROMPT, PRECONDITION_EXTRACTION_PROMPT
from executor import execute_tests, summary
from extractor import extract_precondition_from_response, extract_code_from_response
from file_io import load_json, save_results

MODEL = "mixtral-8x7b-32768"
DEFAULT_TEMPERATURE = 0.7
MAX_CONCURRENT_TASKS = 15


def gen_code(task):
    task_id = task['task_id']
    specification = task['prompt']
    test_case = task['test_list'][0]
    user_message = {
        "role": "user",
        "name": "user",
        "content": f"Specification:\n{specification}\nTest case:\n{test_case}"
    }
    messages = CODE_GEN_PROMPT.copy()
    messages.append(user_message)

    print(f"Processing task ID: {task_id}")
    response = chat_with_groq(model=MODEL, messages=messages, temperature=DEFAULT_TEMPERATURE)
    model_answer = response.choices[0].message.content
    generated_code = extract_code_from_response(model_answer)
    total_tests, passed_tests, _ = execute_tests(task, generated_code)
    test_result = summary(passed_tests, total_tests)
    print(f"Finished task ID {task_id} code gen.")
    result = {
        "specification": specification,
        "code": generated_code,
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "test_result": test_result,
        "task_id": task_id
    }
    return result


def gen_precondition(task_result):
    task_id = task_result["task_id"]
    code = task_result["code"]
    if code == "":
        return ""
    specification = task_result["specification"]
    user_message = {
        "role": "user",
        "name": "user",
        "content": f"Specification:\n{specification}\nCode:\n{code}"
    }
    messages = PRECONDITION_EXTRACTION_PROMPT.copy()
    messages.append(user_message)
    response = chat_with_groq(model=MODEL, messages=messages, temperature=DEFAULT_TEMPERATURE)
    model_answer = response.choices[0].message.content
    precondition = extract_precondition_from_response(model_answer)
    task_result["precondition"] = precondition
    print(f"Extracted precondition for task ID {task_id}")
    return task_result


def gen_code_and_precondition(data):
    results = {}
    for task in data:
        task_result = gen_code(task)
        results[task_result["task_id"]] = task_result

    for result in results.values():
        task_result = gen_precondition(result)
        results[task_result["task_id"]] = task_result

    return results


if __name__ == "__main__":
    # Load the sanitized MBPP data
    sanitized_mbpp_data = load_json("sanitized-mbpp.json")

    # Generate and test code from the sanitized MBPP data
    results = gen_code_and_precondition(sanitized_mbpp_data)

    # Save results to JSON file in the data folder
    output_file = os.path.join('data', 'mixtral_250624.json')
    save_results(output_file, results)
    print(f"Results saved to {output_file}")
