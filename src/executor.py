# executor.py

import subprocess


def execute_code(code_str):
    try:
        result = subprocess.run(['python3', '-c', code_str], capture_output=True,
                                text=True, timeout=3)
        return result.stdout, result.stderr
    except Exception as e:
        return '', str(e)


def execute_test(test_imports, code, test):
    test_code = '\n'.join(test_imports) + '\n' + code + '\n' + test
    _, err = execute_code(test_code)
    if err:
        return False, {'test': test, 'error': err.strip()}
    else:
        return True, {'test': test, 'status': 'Passed'}


def execute_tests(item: dict, code):
    test_imports = item.get('test_imports', [])
    test_list = item.get('test_list', [])
    item_results = {'task_id': item.get('task_id', ''), 'tests': [],
                    'errors': []}
    passed_tests = 0
    for test in test_list:
        ok, res = execute_test(test_imports, code, test)
        if ok:
            passed_tests += 1
            item_results['tests'].append(res)
        else:
            item_results['errors'].append(res)
    return len(test_list), passed_tests, item_results


def summary(passed_tests, total_tests):
    pass_rate = passed_tests / total_tests if total_tests else 0
    return pass_rate


