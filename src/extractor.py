# extractor.py

import re


def extract_postcondition(s: str) -> str:
    pattern = r"Postcondition:\s*\*\*(.*?)\*\*|Postcondition:\s*(.*)"
    match = re.search(pattern, s)
    if match:
        if match.group(1):
            return match.group(1).strip()
        elif match.group(2):
            return match.group(2).strip()
    return s


def extract_code_from_response(response_content):
    code_pattern = r"```(?:python)?\n(.*?)```"
    match = re.search(code_pattern, response_content, re.DOTALL)
    if match:
        return match.group(1)
    return response_content


def extract_precondition_from_response(response_content):
    pattern = r"Precondition:\s*\*\*(.*?)\*\*"
    match = re.search(pattern, response_content)
    if match:
        return match.group(1)
    return response_content

def extract_correctness_from_response(response_content: str) -> str:
    pattern = r"Correctness:\s*\*\*(.*?)\*\*"
    match = re.search(pattern, response_content)
    if match:
        return match.group(1)
    return response_content