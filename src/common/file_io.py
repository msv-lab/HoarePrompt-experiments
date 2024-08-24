import json
from pathlib import Path


def save_results(result_file: str | Path, results):
    if isinstance(result_file, str):
        with open(result_file, 'w') as f:
            json.dump(results, f)
    if isinstance(result_file, Path):
        with result_file.open() as f:
            json.dump(results, f)


def load_json(input_file: str | Path):
    if isinstance(input_file, str):
        with open(input_file, 'r') as f:
            return json.load(f)
    if isinstance(input_file, Path):
        with input_file.open() as f:
            return json.load(f)
