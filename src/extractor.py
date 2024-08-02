import re


def extract_postcondition(s: str) -> str:
    pattern = r"Postcondition:\s*\*\*(.*?)\*\*"
    match = re.search(pattern, s, re.DOTALL)
    if match:
        return match.group(1)
    return s


def extract_code_from_response(response_content):
    code_pattern = r"```(?:python)?\n(.*?)```"
    match = re.search(code_pattern, response_content, re.DOTALL)
    if match:
        return match.group(1)
    return response_content


def extract_precondition_from_response(response_content):
    pattern = r"Precondition:\s*\*\*(.*?)\*\*|Precondition:\s*(.*)"
    match = re.search(pattern, response_content)
    if match:
        if match.group(1):
            return match.group(1).strip()
        elif match.group(2):
            return match.group(2).strip()
    return response_content


def extract_correctness_from_response(response_content: str) -> str:
    pattern = r"Correctness:\s*\*\*(.*?)\*\*|Correctness:\s*(True|False)"
    match = re.search(pattern, response_content)
    if match:
        if match.group(1):
            return match.group(1).strip()
        elif match.group(2):
            return match.group(2).strip()
    return response_content


def extract_function_name_from_test_case(test_case: str) -> str:
    match = re.search(r'assert\s+(\w+)\s*\(', test_case)
    if match:
        return match.group(1)
    else:
        return test_case


def replace_function_name(code: str, main_func_name: str) -> str:
    code = code.replace('\\_', '_')

    pattern = r'\bdef\s+(\w+)\s*\('
    matches = re.findall(pattern, code)

    if len(matches) == 1:
        only_func_name = matches[0]
        code = re.sub(rf'\b{only_func_name}\b', 'func', code)
        return code

    func_map = {}
    counter = 1
    main_name_found = False
    for func_name in matches:
        if func_name == main_func_name:
            func_map[func_name] = 'func'
            main_name_found = True
        else:
            func_map[func_name] = f'func{counter}'
            counter += 1

    if not main_name_found:
        last_func_name = matches[-1]
        func_map[last_func_name] = 'func'

    # Replace all function definitions with new names
    def replace_func(match):
        old_name = match.group(1)
        return f'def {func_map[old_name]}('

    replaced_code = re.sub(pattern, replace_func, code)

    # Replace all function calls with new names
    for old_name, new_name in func_map.items():
        call_pattern = rf'\b{old_name}\b'
        replaced_code = re.sub(call_pattern, new_name, replaced_code)

    return replaced_code