import re

from src.common.communication import chat_with_llm, Model

CHECK_CODE_PROMPT_WITH_EXPLANATION = [
    {'role': 'system',
     'content': 'You have been assigned the role of a program verifier. Your task is to determine the correctness of a given Python program based on the provided natural language specification and explanation. If the program meets the specification, provide "True" as the Correctness; otherwise, provide "False". Partially correct programs should be considered incorrect. You need to strictly follow the format.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a python function to identify non-prime numbers.\nCode:\n```\ndef is_not_prime(n):\r\n    if n < 2:\r\n        return True\r\n    for i in range(2, n):\r\n        if n % i == 0:\r\n            return True\r\n    return False\n```\nExplanation: The function returns True if n is less than 2 or if n is divisible by any integer in the range [2, n). Otherwise, it returns False.'},
    {'role': 'assistant',
     'content': 'Explanation: According to the explanation, the function returns True if `n` is less than 2 or if `n` is divisible by any integer in the range [2, n). Otherwise, it returns False. Since the smallest prime number is 2 and prime numbers can only be divided by 1 and themselves, this approach correctly identifies non-prime numbers as per the given specification. \nCorrectness: **True**.'},
    {'role': 'user', 'name': 'example_user',
     'content': "Specification: Write a python function to count all the substrings starting and ending with same characters.\nCode:\n```\ndef count_Substring_With_Equal_Ends(s):\r\n    count = 0\r\n    for i in range(len(s)-1):\r\n        for j in range(i,len(s)-1):\r\n            if s[i] == s[j+1]:\r\n                count += 1\r\n    return count\n```\nExplanation: The function returns the value of the variable 'count', which is equal to the number of times a character at position 'i' in the string 's' is equal to a character at position 'j + 1' for some 'j' in the range '[i, len(s) - 2]'. This implies that 'count' represents the number of consecutive occurrences of identical characters in the string 's' that may form a substring with equal ending and beginning characters, excluding the last character of the string from this comparison."},
    {'role': 'assistant',
     'content': 'Explanation: According to the explanation, the function returns the value of the variable `count`, which is equal to the number of times a character at position `i` in the string `s` is equal to a character at position `j + 1` for some `j` in the range `[i, len(s) - 2]`. This does not account for substrings of length 1, so it is incorrect.\nCorrectness: **False**.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a python function to check whether the given number can be represented as difference of two squares or not.\nCode:\n```\nimport math\r\ndef dif_Square(n):\r\n    for i in range(int(math.sqrt(n)), -1, -1):\r\n        for j in range(i, -1, -1):\r\n            if i*i - j*j == n:\r\n                return True\r\n    return False\n```\nExplanation: The function `dif_Square(n)` returns True if and only if there exist integers i and j, where i is in the range [⌈√n⌉, 0] (inclusive) and j is in the range [i, 0] (inclusive), such that i * i - j * j equals n. If no such i and j exist, then the function returns False. Furthermore, the loop invariant holds for both loops: for all i in the range [⌈√n⌉, 1] and for all j in the range [i, 1], i * i - j * j is not equal to n. This invariant implies that if the function returns False, then there is no i and j in the specified ranges for which i * i - j * j is equal to n. Additionally, the function does not modify any external state, and its behavior is solely determined by the input n. Precondition: n is an integer.'},
    {'role': 'assistant',
     'content': 'Explanation: According to the explanation, i is in the range [⌈√n⌉, 0] (inclusive) and j is in the range [i, 0] (inclusive), this range is incorrect. It can only detect the case when n is a perfect square, i.e., when √n * √n - 0 = n, therefore it does not meet the specification.\nCorrectness: **False**.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.\nCode:\n```\ndef find_Rotations(str1):\r\n    n = len(str1)\r\n    for i in range(1,n+1):\r\n        if str1[i:] + str1[:i] == str1:\r\n            return i\n```\nExplanation: If the string is a palindrome, the function does not return a value and the variable n remains unchanged, holding the length of the string str1. If the string is not a palindrome, then the function returns an integer i such that 0 < i < n, where n is the length of the string str1, and i represents the length of the shortest non-empty rotation of str1 to return to its original state.. If no such rotation exists, then the function does not return a value.'},
    {'role': 'assistant',
     'content': 'Explanation: According to the explanation, if the string is a palindrome, the function does not return a value, and the variable `n` remains unchanged, holding the length of the string `str1`. This behavior is correct as the specification states that the rotation count must be greater than 0. If the string is not a palindrome, then the function returns an integer `i` such that `0 < i < n`, where `n` is the length of the string `str1`. The value `i` represents the length of the shortest non-empty rotation of str1 to return to its original state.. However, the code iterates from `1` to `n-1`, meaning it does not include `n`. This omission is problematic because it fails to check the complete rotation case, where `i` could be equal to `n`. Consequently, the function does not meet the specification as it should return the rotation count up to `n` times. Therefore, it does not meet the specification.\nCorrectness: **False**.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a function to check if the given number is woodball or not.\nCode:\n```\ndef is_woodall(n):\r\n    return n == (n*(2**(n-1)))\n```\nExplanation: The function returns a boolean value indicating whether n is a Woodall number (a number of the form n\*2^(n-1) for some integer n > 0). Additionally, if the function returns True, then n has the value of a Woodall number, and if the function returns False, then n does not have the value of a Woodall number.'},
    {'role': 'assistant',
     'content': 'Explanation: According to the explanation, the function returns a boolean value indicating whether n is a Woodall number (a number of the form n\*2^(n-1) for some integer n > 0). However, the formula `n * 2^(n-1)` is incorrect for determining Woodall numbers. The correct formula for a Woodall number is `n * 2^n - 1`, where `n` is a positive integer. To check if a given number `m` is a Woodall number, you should verify whether `m` equals `n * 2^n - 1` for some integer `n`. Therefore, the function does not correctly check for Woodall numbers.\nCorrectness: **False**.'}
]

CHECK_CODE_PROMPT = [
    {'role': 'system',
     'content': 'You have been assigned the role of a program verifier. Your task is to determine the correctness of a given Python program based on the provided natural language specification. If the program meets the specification, provide "True" as the Correctness; otherwise, provide "False". Partially correct programs should be considered incorrect. You need to strictly follow the format.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a python function to identify non-prime numbers.\nCode:\n```\ndef is_not_prime(n):\r\n    if n < 2:\r\n        return True\r\n    for i in range(2, n):\r\n        if n % i == 0:\r\n            return True\r\n    return False\n```'},
    {'role': 'assistant',
     'content': 'Explanation: The function `is_not_prime` accepts an integer `n`. If `n` is less than 2, the function immediately returns `True`, as numbers less than 2 are not considered prime. Otherwise, the function iterates through all numbers from 2 to `n-1`. If any of these numbers divides `n` without a remainder, the function returns `True`, indicating that `n` is not a prime number. If no such divisor is found, the function returns `False`, correctly identifying `n` as a prime number. The function correctly implements the specification to identify non-prime numbers.\nCorrectness: **True**.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a function to count the most common words in a dictionary.\nCode:\n```from collections import Counter\r\ndef count_common(words):\r\n    counter = Counter(words)\r\n    most_common = counter.most_common(1)\r\n    return most_common\n```'},
    {'role': 'assistant',
     'content': 'Explanation: The function `count_common` imports the `Counter` class from the `collections` module, then creates a `Counter` object from the input list `words` to count the frequency of each word. It calls `most_common(1)` on the `Counter` object to find and return a list containing the most common word and its count. This process ensures that the function correctly identifies and returns the most frequently occurring word in the input list. \nCorrectness: **True**.'},
    {'role': 'user', 'name': 'example_user',
     'content': "Specification: Write a python function to count all the substrings starting and ending with same characters.\nCode:\n```def count_Substring_With_Equal_Ends(s):\r\n    count = 0\r\n    for i in range(len(s)-1):\r\n        for j in range(i,len(s)-1):\r\n            if s[i] == s[j+1]:\r\n                count += 1\r\n    return count\n```"},
    {'role': 'assistant',
     'content': 'Explanation: The function `count_Substring_With_Equal_Ends` accepts a string `s`. A counter `count` is initialized to zero. The function iterates over the starting positions of the substrings with the loop `for i in range(len(s)-1)`, and for each starting position, it iterates over the ending positions of the substrings with the loop `for j in range(i, len(s)-1)`. If the characters at the starting and ending positions are the same (`if s[i] == s[j+1]`), the counter is incremented by 1. However, this function does not consider substrings of length 1, which should also be counted as they start and end with the same character. \nCorrectness: **False**.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a python function to check whether the given number can be represented as difference of two squares or not.\nCode:\n```import math\r\ndef dif_Square(n):\r\n    for i in range(int(math.sqrt(n)), -1, -1):\r\n        for j in range(i, -1, -1):\r\n            if i*i - j*j == n:\r\n                return True\r\n    return False\n```.'},
    {'role': 'assistant',
     'content': 'Explanation: The function `dif_Square` accepts an integer `n` and iterates over `i` from the integer square root of `n` down to 0, with a step of -1. For each `i`, the function iterates over `j` from `i` down to 0, with a step of -1. If at any point `i^2 - j^2 = n`, the function returns `True`. However, the range of `i` is too narrow, and the function only returns `True` when `i*i = n` and `j = 0`. If `i*i < n` (i.e., after the first iteration), the function cannot detect any `i` and `j` that satisfy the condition, leading to incorrect results.\n Correctness: **False**.'},
    {'role': 'user', 'name': 'example_user',
     'content': 'Specification: Write a function to check if the given number is woodball or not.\nCode:\n```\ndef is_woodall(n):\r\n    return n == (n*(2**(n-1)))\n```'},
    {'role': 'assistant',
     'content': 'Explanation: The function `is_woodall` accepts an integer `n` and returns the result of the comparison `n == (n*(2**(n-1)))`. However, this formula is incorrect for determining whether a number is a Woodall number. The correct formula for a Woodall number is `m = n * 2^n - 1`. To properly check if a number is a Woodall number, the function should verify whether a given `m` equals `n * 2^n - 1` for some integer `n`. Therefore, the current function does not meet the specification and does not correctly identify Woodall numbers.\nCorrectness: **False**.'}
]


def extract_correctness_from_response(response_content: str) -> str:
    pattern = r"Correctness:\s*\*\*(.*?)\*\*|Correctness:\s*(True|False)"
    match = re.search(pattern, response_content)
    if match:
        if match.group(1):
            return match.group(1).strip()
        elif match.group(2):
            return match.group(2).strip()
    return response_content


def check_program(specification: str, code: str, logger, model: Model, temperature: float, explanation=None):
    # This function analyzes whether the program meets the natural language specification, with or without postconditions.
    if explanation:
        user_message = {
            "role": "user",
            "name": "user",
            "content": f"Specification: {specification}\nCode:\n```\n{code}\n```\nExplanation: {explanation}"
        }
        messages = CHECK_CODE_PROMPT_WITH_EXPLANATION.copy()
        messages.append(user_message)
        response = chat_with_llm(model=model.value, messages=messages, temperature=temperature)
        model_answer = response.choices[0].message.content
        correctness = extract_correctness_from_response(model_answer)

    else:
        user_message = {
            "role": "user",
            "name": "user",
            "content": f"Specification: {specification}\nCode:\n```\n{code}\n```"
        }
        messages = CHECK_CODE_PROMPT.copy()
        messages.append(user_message)
        response = chat_with_llm(model=model.value, messages=messages, temperature=temperature)
        model_answer = response.choices[0].message.content
        correctness = extract_correctness_from_response(model_answer)

    if correctness not in ["True", "False"]:
        logger.warning(f"Cannot extract correctness value.")
    return correctness == "True", model_answer
