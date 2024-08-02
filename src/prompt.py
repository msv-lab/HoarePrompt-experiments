VERIFYER_SYSTEM_PROMPT = """You are assigned the role of a program verifier, responsible for completing Hoare triples. Each Hoare triple is made up of three components: a precondition, a program fragment, and a postcondition. The precondition and the postcondition are expressed in natural language.

Precondition: describes the initial state of the program variables before the execution of the program fragment. This description should only include the values of the variables, without detailing the operational aspects of the program.

Program Fragment: This is a given part of the task and is not something you need to create or modify.

Postcondition: describes the state of the program variables after the execution of the program fragment with the initial state described in the precondition. This description should include both the values of the variables and the relationships between them. Similar to the precondition, avoid explaining how the program operates; concentrate solely on the variable values and their interrelations."""

CODE_GEN_PROMPT = [{'role': 'system',
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

PRECONDITION_EXTRACTION_PROMPT = [{'role': 'system',
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

AUX_PRECONDITION_EXTRACTION_PROMPT = [
    {'role': 'system',
     'content': 'You are assigned the role of a program verifier, responsible for extracting the precondition from the calling context described in natural language and the corresponding called Python function code. You need to infer the precondition of the function by combining the context and the Python function code.'},
    {'role': 'user', 'name': 'example_user',
     'content': '''Context: n is an integer.
Caller: is_prime(n)
Callee:
```
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```
'''},
    {'role': 'assistant',
     'content': 'Precondition: **m is an integer.**'},
    {'role': 'user', 'name': 'example_user',
     'content': '''Context: n is an integer greater than or equal to 0. memo is a list of length n+1, initialized with -1
Caller: count_ways_util(n, memo)
Collee:
```
def count_ways_util(n, memo):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 3
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = 3 * count_ways_util(n - 2, memo)
    for i in range(4, n + 1, 2):
        memo[n] += 2 * count_ways_util(n - i, memo)
    
    return memo[n]
```
'''},
    {'role': 'assistant',
     'content': 'Precondition: **n is an integer greater than or equal to 0. memo is a list of length n+1, initialized with -1**'},
    {'role': 'user', 'name': 'example_user',
     'content': '''Context: x and y are integers. xor is an integer; xor has the value of the bitwise XOR operation between x and y.
Caller: count_set_bits(xor)
Collee:
```
def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count
```
'''},
    {'role': 'assistant',
     'content': 'Precondition: **n is an integer.**'},
]

CHECK_CODE_PROMPT_WITH_EXPLANATION = [{'role': 'system',
                                       'content': 'You have been assigned the role of a program verifier. Your task is to determine the correctness of a given Python program based on the provided natural language specification and explanation. If the program meets the specification, provide "True" as the Correctness; otherwise, provide "False". Partially correct programs should be considered incorrect.'},
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
                                       'content': 'Explanation: According to the explanation, the function returns a boolean value indicating whether n is a Woodall number (a number of the form n\*2^(n-1) for some integer n > 0). However, the formula `n * 2^(n-1)` is incorrect for determining Woodall numbers. The correct formula for a Woodall number is `n * 2^n - 1`. Therefore, the function does not correctly check for Woodall numbers.\nCorrectness: **False**.'}
                                      ]

CHECK_CODE_PROMPT = [{'role': 'system',
                      'content': 'You have been assigned the role of a program verifier. Your task is to determine the correctness of a given Python program based on the provided natural language specification. If the program meets the specification, provide "True" as the Correctness; otherwise, provide "False". Partially correct programs should be considered incorrect.'},
                     {'role': 'user', 'name': 'example_user',
                      'content': 'Specification: Write a function to count the most common words in a dictionary.\nCode:\n```from collections import Counter\r\ndef count_common(words):\r\n    counter = Counter(words)\r\n    most_common = counter.most_common(1)\r\n    return most_common\n```'},
                     {'role': 'assistant',
                      'content': 'Correctness: **True**.'},
                     {'role': 'user', 'name': 'example_user',
                      'content': "Specification: Write a python function to count all the substrings starting and ending with same characters.\nCode:\n```def count_Substring_With_Equal_Ends(s):\r\n    count = 0\r\n    for i in range(len(s)-1):\r\n        for j in range(i,len(s)-1):\r\n            if s[i] == s[j+1]:\r\n                count += 1\r\n    return count\n```"},
                     {'role': 'assistant',
                      'content': 'Correctness: **False**.'},
                     {'role': 'user', 'name': 'example_user',
                      'content': 'Specification: Write a python function to check whether the given number can be represented as difference of two squares or not.\nCode:\n```import math\r\ndef dif_Square(n):\r\n    for i in range(int(math.sqrt(n)), -1, -1):\r\n        for j in range(i, -1, -1):\r\n            if i*i - j*j == n:\r\n                return True\r\n    return False\n```.'},
                     {'role': 'assistant',
                      'content': 'Correctness: **False**.'},
                     ]
