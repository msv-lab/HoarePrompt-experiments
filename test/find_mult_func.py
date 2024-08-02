import re

from file_io import load_json

DATA_FILE = '../data/mixtral_20240630(complex).json'

data = load_json(DATA_FILE)
for task_id, task_data in data.items():
    code = task_data["code"]
    function_count = len(re.findall(r'\bdef\b', code))
    if function_count > 1:
        print(f"Task id {task_id} contains multiple function definition.")