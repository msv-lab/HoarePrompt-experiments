import json

def save_results(result_file, results):
    with open(result_file, 'w') as f:
        json.dump(results, f)

def load_json(input_file):
    with open(input_file, 'r') as f:
        return json.load(f)
