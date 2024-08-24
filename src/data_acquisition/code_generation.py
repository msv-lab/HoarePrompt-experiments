import re

from src.data_acquisition.communication import Model, chat_with_llm
from src.data_acquisition.executor import execute_tests, summary

CODE_GEN_PROMPT = [
    {'role': 'system',
     'content': 'You are assigned the role of a Python programmer. Your task is to write the corresponding Python program based on the given natural language specifications and test case.'},
    {'role': 'system', 'name': 'example_user',
     'content': 'Specification:\nWrite a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].\nTest case:\nassert min_cost([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8'},
    {'role': 'assistant',
     'content': 'Program:\n```\nR = 3\r\nC = 3\r\ndef min_cost(cost, m, n): \r\n\ttc = [[0 for x in range(C)] for x in range(R)] \r\n\ttc[0][0] = cost[0][0] \r\n\tfor i in range(1, m+1): \r\n\t\ttc[i][0] = tc[i-1][0] + cost[i][0] \r\n\tfor j in range(1, n+1): \r\n\t\ttc[0][j] = tc[0][j-1] + cost[0][j] \r\n\tfor i in range(1, m+1): \r\n\t\tfor j in range(1, n+1): \r\n\t\t\ttc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] \r\n\treturn tc[m][n]\n```'},
    {'role': 'system', 'name': 'example_user',
     'content': 'Specification:\nWrite a function to find the similar elements from the given two tuple lists.\nTest case:\nassert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)'},
    {'role': 'assistant',
     'content': 'Program:\n```\ndef similar_elements(test_tup1, test_tup2):\r\n  res = tuple(set(test_tup1) & set(test_tup2))\r\n  return (res) \n```'},
    {'role': 'system', 'name': 'example_user',
     'content': 'Specification:\nWrite a python function to identify non-prime numbers.\nTest case:\nassert is_not_prime(2) == False'},
    {'role': 'assistant',
     'content': 'Program:\n```\nimport math\r\ndef is_not_prime(n):\r\n    result = False\r\n    for i in range(2,int(math.sqrt(n)) + 1):\r\n        if n % i == 0:\r\n            result = True\r\n    return result\n```'}]


def extract_code_from_response(response_content):
    code_pattern = r"```(?:python)?\n(.*?)```"
    match = re.search(code_pattern, response_content, re.DOTALL)
    if match:
        return match.group(1)
    return response_content


def gen_code(task, model: Model, temperature: float):
    task_id = task['task_id']
    specification = task['prompt']
    test_case = task['test_list'][0]
    user_message = {
        "role": "user",
        "name": "user",
        "content": f"Specification:\n{specification}\nTest case:\n{test_case}"
    }
    messages = CODE_GEN_PROMPT
    messages.append(user_message)

    response = chat_with_llm(model=model.value, messages=messages, temperature=temperature)
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
        "task_id": task_id,
        "test_list": task['test_list']
    }
    return result
