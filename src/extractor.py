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


def replace_function_name(code: str) -> str:
    pattern = r'\bdef\s+(\w+)\s*\('
    matches = re.findall(pattern, code)

    func_map = {}
    for i, func_name in enumerate(matches):
        func_map[func_name] = f'func{i + 1 if i != 0 else ""}'

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