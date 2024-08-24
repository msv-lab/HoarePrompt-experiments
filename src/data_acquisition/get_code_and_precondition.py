import os
from datetime import datetime
from model import get_model
import argparse
from pathlib import Path

from src.common.file_io import save_results, load_json
from src.data_acquisition.code_generation import gen_code
from src.data_acquisition.precondition_generation import gen_precondition


def gen_code_and_precondition(data: list, config: dict) -> dict:
    model = get_model(config["model"], config["temperature"], None)
    results = {}
    for task in data:
        task_result = gen_code(task, model)
        results[task_result["task_id"]] = task_result

    for result in results.values():
        task_result = gen_precondition(result, model)
        results[task_result["task_id"]] = task_result

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MBPP code Generation")
    parser.add_argument('--config', type=str, help="Path to custom configuration file")

    args = parser.parse_args()

    if args.config:
        config_file = Path(args.config)
    else:
        config_file = Path("default_config.json")
    config = load_json(config_file)

    sanitized_mbpp_data = load_json("sanitized-mbpp.json")

    results = gen_code_and_precondition(sanitized_mbpp_data, config)
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = os.path.join('data', f'{config["model"]}_{timestamp}.json')
    save_results(output_file, results)
    print(f"Results saved to {output_file}")
