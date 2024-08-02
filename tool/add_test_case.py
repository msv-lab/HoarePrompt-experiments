import json

def save_results(result_file, results):
    with open(result_file, 'w') as f:
        json.dump(results, f, indent=4)

def load_json(input_file):
    with open(input_file, 'r') as f:
        return json.load(f)

def update_json_with_test_cases(json_path, sanitized_json_path):
    data = load_json(json_path)
    sanitized_data = load_json(sanitized_json_path)

    sanitized_test_cases = {item['task_id']: item['test_list'] for item in sanitized_data}

    for task_id, task_data in data.items():
        task_id_int = int(task_id)
        if task_id_int in sanitized_test_cases:
            test_list = sanitized_test_cases[task_id_int]
            task_data["test_list"] = test_list

    save_results(json_path, data)


json_path = '../data/mixtral_20240715(complex).json'
sanitized_json_path = '../sanitized-mbpp.json'

update_json_with_test_cases(json_path, sanitized_json_path)