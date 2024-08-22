import re

from src.common.communication import chat_with_llm, Model

PRECONDITION_EXTRACTION_PROMPT = [
    {'role': 'system',
     'content': 'You are assigned the role of a program verifier, responsible for extracting the precondition from natural language specifications and Python programs.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].\nCode:\n```\nR = 3\r\nC = 3\r\ndef min_cost(cost, m, n): \r\n\ttc = [[0 for x in range(C)] for x in range(R)] \r\n\ttc[0][0] = cost[0][0] \r\n\tfor i in range(1, m+1): \r\n\t\ttc[i][0] = tc[i-1][0] + cost[i][0] \r\n\tfor j in range(1, n+1): \r\n\t\ttc[0][j] = tc[0][j-1] + cost[0][j] \r\n\tfor i in range(1, m+1): \r\n\t\tfor j in range(1, n+1): \r\n\t\t\ttc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] \r\n\treturn tc[m][n]\n```\n'},
    {'role': 'assistant',
     'content': 'Precondition: **cost is a 2D list of non-negative integers, m and n are non-negative integers such that 0 <= m < len(cost) and 0 <= n < len(cost[0]).**'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a function to find the similar elements from the given two tuple lists.\nCode:\n```\ndef similar_elements(test_tup1, test_tup2):\r\n  res = tuple(set(test_tup1) & set(test_tup2))\r\n  return (res) \n```\n'},
    {'role': 'assistant',
     'content': 'Precondition: **test_tup1 and test_tup2 are tuples.**'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a python function to identify non-prime numbers.\nCode:\n```\nimport math\r\ndef is_not_prime(n):\r\n    result = False\r\n    for i in range(2,int(math.sqrt(n)) + 1):\r\n        if n % i == 0:\r\n            result = True\r\n    return result\n```\n'},
    {'role': 'assistant',
     'content': 'Precondition: **n is an integer greater than 1.**'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a function to find the largest integers from a given list of numbers using heap queue algorithm.\nCode:\n```\nimport heapq as hq\r\ndef heap_queue_largest(nums,n):\r\n  largest_nums = hq.nlargest(n, nums)\r\n  return largest_nums\n```\n'},
    {'role': 'assistant',
     'content': 'Precondition: **nums is a list of integers, and n is a non-negative integer such that 0 <= n <= len(nums).**'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a function to find the number of ways to fill it with 2 x 1 dominoes for the given 3 x n board.\nCode:\n```\ndef count_ways(n): \r\n\tA = [0] * (n + 1) \r\n\tB = [0] * (n + 1) \r\n\tA[0] = 1\r\n\tA[1] = 0\r\n\tB[0] = 0\r\n\tB[1] = 1\r\n\tfor i in range(2, n+1): \r\n\t\tA[i] = A[i - 2] + 2 * B[i - 1] \r\n\t\tB[i] = A[i - 1] + B[i - 2] \r\n\treturn A[n] \n```\n'},
    {'role': 'assistant',
     'content': 'Precondition: **n is a non-negative integer.**'}]


def extract_precondition_from_response(response_content: str) -> str:
    pattern = r"Precondition:\s*\*\*(.*?)\*\*|Precondition:\s*(.*)"
    match = re.search(pattern, response_content)
    if match:
        if match.group(1):
            return match.group(1).strip()
        elif match.group(2):
            return match.group(2).strip()
    return response_content


def gen_precondition(task_result: dict, model: Model, temperature: float):
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
    messages = PRECONDITION_EXTRACTION_PROMPT
    messages.append(user_message)

    response = chat_with_llm(model=model.value, messages=messages, temperature=temperature)
    model_answer = response.choices[0].message.content
    precondition = extract_precondition_from_response(model_answer)
    task_result["precondition"] = precondition
    print(f"Extracted precondition for task ID {task_id}")
    return task_result
