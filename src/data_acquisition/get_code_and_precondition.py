import os
from datetime import datetime

from src.common.file_io import save_results, load_json
from src.data_acquisition.code_generation import gen_code
from src.data_acquisition.precondition_generation import gen_precondition
from src.data_acquisition.communication import Model, chat_with_llm

MODEL = Model.GPT_4O_MINI
TEMPERATURE = 0.7


def gen_code_and_precondition(data: list, model: Model, temperature: float) -> dict:
    results = {}
    for task in data:
        task_result = gen_code(task, model, temperature)
        results[task_result["task_id"]] = task_result

    for result in results.values():
        task_result = gen_precondition(result, model, temperature)
        results[task_result["task_id"]] = task_result

    return results


if __name__ == "__main__":
    sanitized_mbpp_data = load_json("sanitized-mbpp.json")
    results = gen_code_and_precondition(sanitized_mbpp_data, MODEL, TEMPERATURE)
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = os.path.join('data', f'{MODEL.value}_{timestamp}.json')
    save_results(output_file, results)
    print(f"Results saved to {output_file}")
