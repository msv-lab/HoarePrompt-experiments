import re


def replace_function_name(code: str) -> str:
    # This function replaces the original function name with 'func' to reduce its impact on the LLM.
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


def count_function_defs(code: str) -> int:
    # The function returns the number of function definitions in the code.
    pattern = r'\bdef\s+\w+\s*\('
    matches = re.findall(pattern, code)
    return len(matches)
