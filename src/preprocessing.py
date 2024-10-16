import re

# Replaces the original function names in the provided code with generic names like func1, func2 etc.
# This is useful to reduce the impact of specific function names in LLMS not to skew our results
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

# The function returns the number of function definitions in the code as the projects handles only single-function scripts at this point
def count_function_defs(code: str) -> int:
    pattern = r'\bdef\s+\w+\s*\('
    matches = re.findall(pattern, code)
    return len(matches)
