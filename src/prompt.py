VERIFYER_SYSTEM_PROMPT = """
You are assigned the role of a program verifier, responsible for completing Hoare triples. Each Hoare triple is made up of three components: a precondition, a program fragment, and a postcondition. The precondition and the postcondition are expressed in natural language.

Precondition: describes the initial state of the program variables before the execution of the program fragment. This description should only include the values of the variables, without detailing the operational aspects of the program.

Program Fragment: This is a given part of the task and is not something you need to create or modify.

Postcondition: describes the state of the program variables after the execution of the program fragment with the initial state described in the precondition. This description should include both the values of the variables and the relationships between them. Similar to the precondition, avoid explaining how the program operates; concentrate solely on the variable values and their interrelations.
"""

CODE_GEN_SYSTEM_PROMPT = """
You are assigned the role of a Python programmer. Your task is to write the corresponding Python program based on the given natural language specifications.

You cannot change the provided function name.
"""

CODE_GEN_PROMPT = [{'role': 'system',
                    'content': 'You are assigned the role of a Python programmer. Your task is to write the corresponding Python program based on the given natural language specifications.'},
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

PRECONDITION_EXTRACTION_SYSTEM_PROMPT = """
You are assigned the role of a program verifier, responsible for extracting the precondition from natural language specifications and Python programs.
"""

PRECONDITION_EXTRACTION_PROMPT_COMPLEX = [{'role': 'system',
                                           'content': 'You are assigned the role of a program verifier, responsible for extracting the precondition from natural language specifications and Python programs.'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].\nCode:\n```\nR = 3\r\nC = 3\r\ndef min_cost(cost, m, n): \r\n\ttc = [[0 for x in range(C)] for x in range(R)] \r\n\ttc[0][0] = cost[0][0] \r\n\tfor i in range(1, m+1): \r\n\t\ttc[i][0] = tc[i-1][0] + cost[i][0] \r\n\tfor j in range(1, n+1): \r\n\t\ttc[0][j] = tc[0][j-1] + cost[0][j] \r\n\tfor i in range(1, m+1): \r\n\t\tfor j in range(1, n+1): \r\n\t\t\ttc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] \r\n\treturn tc[m][n]\n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **cost is a 2D list of non-negative integers, m and n are non-negative integers such that 0 <= m < len(cost) and 0 <= n < len(cost[0]).**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the similar elements from the given two tuple lists.\nCode:\n```\ndef similar_elements(test_tup1, test_tup2):\r\n  res = tuple(set(test_tup1) & set(test_tup2))\r\n  return (res) \n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **test_tup1 and test_tup2 are tuples.**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a python function to identify non-prime numbers.\nCode:\n```\nimport math\r\ndef is_not_prime(n):\r\n    result = False\r\n    for i in range(2,int(math.sqrt(n)) + 1):\r\n        if n % i == 0:\r\n            result = True\r\n    return result\n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **n is an integer greater than 1.**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the largest integers from a given list of numbers using heap queue algorithm.\nCode:\n```\nimport heapq as hq\r\ndef heap_queue_largest(nums,n):\r\n  largest_nums = hq.nlargest(n, nums)\r\n  return largest_nums\n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **nums is a list of integers, and n is a non-negative integer such that 0 <= n <= len(nums).**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the number of ways to fill it with 2 x 1 dominoes for the given 3 x n board.\nCode:\n```\ndef count_ways(n): \r\n\tA = [0] * (n + 1) \r\n\tB = [0] * (n + 1) \r\n\tA[0] = 1\r\n\tA[1] = 0\r\n\tB[0] = 0\r\n\tB[1] = 1\r\n\tfor i in range(2, n+1): \r\n\t\tA[i] = A[i - 2] + 2 * B[i - 1] \r\n\t\tB[i] = A[i - 1] + B[i - 2] \r\n\treturn A[n] \n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **n is a non-negative integer.**'}]

PRECONDITION_EXTRACTION_PROMPT_COMPLEX = [{'role': 'system',
                                           'content': 'You are assigned the role of a program verifier, responsible for extracting the precondition from natural language specifications and Python programs.'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].\nCode:\n```\nR = 3\r\nC = 3\r\ndef min_cost(cost, m, n): \r\n\ttc = [[0 for x in range(C)] for x in range(R)] \r\n\ttc[0][0] = cost[0][0] \r\n\tfor i in range(1, m+1): \r\n\t\ttc[i][0] = tc[i-1][0] + cost[i][0] \r\n\tfor j in range(1, n+1): \r\n\t\ttc[0][j] = tc[0][j-1] + cost[0][j] \r\n\tfor i in range(1, m+1): \r\n\t\tfor j in range(1, n+1): \r\n\t\t\ttc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] \r\n\treturn tc[m][n]\n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **cost is a 2D list of non-negative integers, m and n are non-negative integers such that 0 <= m < len(cost) and 0 <= n < len(cost[0]).**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the similar elements from the given two tuple lists.\nCode:\n```\ndef similar_elements(test_tup1, test_tup2):\r\n  res = tuple(set(test_tup1) & set(test_tup2))\r\n  return (res) \n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **test_tup1 and test_tup2 are tuples.**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a python function to identify non-prime numbers.\nCode:\n```\nimport math\r\ndef is_not_prime(n):\r\n    result = False\r\n    for i in range(2,int(math.sqrt(n)) + 1):\r\n        if n % i == 0:\r\n            result = True\r\n    return result\n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **n is an integer greater than 1.**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the largest integers from a given list of numbers using heap queue algorithm.\nCode:\n```\nimport heapq as hq\r\ndef heap_queue_largest(nums,n):\r\n  largest_nums = hq.nlargest(n, nums)\r\n  return largest_nums\n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **nums is a list of integers, and n is a non-negative integer such that 0 <= n <= len(nums).**'},
                                          {'role': 'system', 'name': 'example_user',
                                           'content': 'Specification: Write a function to find the number of ways to fill it with 2 x 1 dominoes for the given 3 x n board.\nCode:\n```\ndef count_ways(n): \r\n\tA = [0] * (n + 1) \r\n\tB = [0] * (n + 1) \r\n\tA[0] = 1\r\n\tA[1] = 0\r\n\tB[0] = 0\r\n\tB[1] = 1\r\n\tfor i in range(2, n+1): \r\n\t\tA[i] = A[i - 2] + 2 * B[i - 1] \r\n\t\tB[i] = A[i - 1] + B[i - 2] \r\n\treturn A[n] \n```\n'},
                                          {'role': 'assistant',
                                           'content': 'Precondition: **n is a non-negative integer.**'}]

CHECK_CODE_SYSTEM_PROMPT = '''
You have been assigned the role of a program verifier. Your task is to determine the correctness of a given Python program based on the provided natural language specification and the explanation.
'''

CHECK_CODE_PROMPT_WITH_EXPLANATION = [{'role': 'system',
                                       'content': 'You have been assigned the role of a program verifier. Your task is to determine the correctness of a given Python program based on the provided natural language specification and the explanation.'},
                                      {'role': 'system', 'name': 'example_user',
                                       'content': 'Specification: Write a function to count the most common words in a dictionary.\nCode:\n```from collections import Counter\r\ndef count_common(words):\r\n    counter = Counter(words)\r\n    most_common = counter.most_common(1)\r\n    return most_common\n```\nExplanation: The function `count_common` takes a list of strings `words` as input and returns a list containing a single tuple. This tuple represents the key-value pair of the most frequent element in the counter object. If there is a tie for the most frequent element, the first element encountered will be selected. The `counter` object is a dictionary with string keys and integer values, where the keys represent words from the `words` list, and the values represent the frequency of each word in the `words` list. Additionally, the program does not modify the original `words` list.'},
                                      {'role': 'assistant',
                                       'content': 'According to the explanation, the code correctly implements the specification. Correctness: **True**.'},
                                      {'role': 'system', 'name': 'example_user',
                                       'content': "Specification: Write a python function to count all the substrings starting and ending with same characters.\nCode:\n```def count_Substring_With_Equal_Ends(s):\r\n    count = 0\r\n    for i in range(len(s)-1):\r\n        for j in range(i,len(s)-1):\r\n            if s[i] == s[j+1]:\r\n                count += 1\r\n    return count\n```\nExplanation: The function returns the value of the variable 'count', which is equal to the number of times a character at position 'i' in the string 's' is equal to a character at position 'j + 1' for some 'j' in the range '[i, len(s) - 2]'. This implies that 'count' represents the number of consecutive occurrences of identical characters in the string 's' that may form a substring with equal ending and beginning characters, excluding the last character of the string from this comparison."},
                                      {'role': 'assistant',
                                       'content': 'According to the explanation, the function returns the value of the variable `count`, which is equal to the number of times a character at position `i` in the string `s` is equal to a character at position `j + 1` for some `j` in the range `[i, len(s) - 2]`. This does not account for substrings of length 1, so it is incorrect. Correctness: **False**.'},
                                      {'role': 'system', 'name': 'example_user',
                                       'content': 'Specification: Write a python function to check whether the given number can be represented as difference of two squares or not.\nCode:\n```import math\r\ndef dif_Square(n):\r\n    for i in range(int(math.sqrt(n)), -1, -1):\r\n        for j in range(i, -1, -1):\r\n            if i*i - j*j == n:\r\n                return True\r\n    return False\n```\nExplanation: The function `dif_Square(n)` returns True if and only if there exist integers i and j, where i is in the range [⌈√n⌉, 0] (inclusive) and j is in the range [i, 0] (inclusive), such that i * i - j * j equals n. If no such i and j exist, then the function returns False. Furthermore, the loop invariant holds for both loops: for all i in the range [⌈√n⌉, 1] and for all j in the range [i, 1], i * i - j * j is not equal to n. This invariant implies that if the function returns False, then there is no i and j in the specified ranges for which i * i - j * j is equal to n. Additionally, the function does not modify any external state, and its behavior is solely determined by the input n. Precondition: n is an integer.'},
                                      {'role': 'assistant',
                                       'content': 'According to the explanation, i is in the range [⌈√n⌉, 0] (inclusive) and j is in the range [i, 0] (inclusive), this range is incorrect. It can only detect the case when n is a perfect square, i.e., when √n * √n - 0 = n, therefore it does not meet the specification. Correctness: **False**.'}
                                      ]

CHECK_CODE_PROMPT = [{'role': 'system',
                      'content': 'You have been assigned the role of a program verifier. Your task is to determine the correctness of a given Python program based on the provided natural language specification.'},
                     {'role': 'system', 'name': 'example_user',
                      'content': 'Specification: Write a function to count the most common words in a dictionary.\nCode:\n```from collections import Counter\r\ndef count_common(words):\r\n    counter = Counter(words)\r\n    most_common = counter.most_common(1)\r\n    return most_common\n```'},
                     {'role': 'assistant',
                      'content': 'Correctness: **True**.'},
                     {'role': 'system', 'name': 'example_user',
                      'content': "Specification: Write a python function to count all the substrings starting and ending with same characters.\nCode:\n```def count_Substring_With_Equal_Ends(s):\r\n    count = 0\r\n    for i in range(len(s)-1):\r\n        for j in range(i,len(s)-1):\r\n            if s[i] == s[j+1]:\r\n                count += 1\r\n    return count\n```"},
                     {'role': 'assistant',
                      'content': 'Correctness: **False**.'},
                     {'role': 'system', 'name': 'example_user',
                      'content': 'Specification: Write a python function to check whether the given number can be represented as difference of two squares or not.\nCode:\n```import math\r\ndef dif_Square(n):\r\n    for i in range(int(math.sqrt(n)), -1, -1):\r\n        for j in range(i, -1, -1):\r\n            if i*i - j*j == n:\r\n                return True\r\n    return False\n```.'},
                     {'role': 'assistant',
                      'content': 'Correctness: **False**.'}
                     ]
