import json
import ast
from datasets import load_dataset
import random

# export HF_ENDPOINT=https://hf-mirror.com

dataset = load_dataset("deepmind/code_contests", split="train")
final_dataset = []
all_num = 0

for data in dataset:
    if 1 in data["solutions"]["language"] and 1 in data["incorrect_solutions"]["language"]:
        random_int = random.randint(0, 1)
        all_num += 1
        selected_data = {
            "description": data["description"],
            "task_name": data["name"],
            "dataset": "code_contests",
            "model": "human"
        }
        get_sample = False
        if random_int:
            python_num = [index for index, value in enumerate(data["incorrect_solutions"]["language"]) if value == 1]
            while python_num:
                sampled_elements = random.sample(python_num, 1)[0]
                candidate_code = data["incorrect_solutions"]["solution"][int(sampled_elements)]
                try:
                    ast.parse(candidate_code)
                    selected_data["generated_code"] = candidate_code
                    selected_data["correct"] = False
                    get_sample = True
                    break
                except SyntaxError:
                    python_num.remove(sampled_elements)
        if random_int == 0 or not get_sample:
            python_num = [index for index, value in enumerate(data["solutions"]["language"]) if value == 1]
            while python_num:
                sampled_elements = random.sample(python_num, 1)[0]
                candidate_code = data["solutions"]["solution"][int(sampled_elements)]
                try:
                    ast.parse(candidate_code)
                    selected_data["generated_code"] = candidate_code
                    selected_data["correct"] = True
                    get_sample = True
                    break
                except SyntaxError:
                    python_num.remove(sampled_elements)
        if get_sample:
            final_dataset.append(selected_data)

# final_dataset = random.sample(final_dataset, 50)

for idx, dict in enumerate(final_dataset, start=0):
    dict['task_id'] = str(idx).zfill(4)

with open("sampled_elements_all.json", "w") as json_file:
    json.dump(final_dataset, json_file, indent=4)

