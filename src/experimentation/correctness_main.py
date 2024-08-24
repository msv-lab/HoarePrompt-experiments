import ast
from datetime import datetime
from math import sqrt
import csv
import os
import argparse
from pathlib import Path
from hoareprompt import compute_postcondition, check_entailment

from src.common.file_io import load_json
from src.common.logger_setup import logger_setup
from src.experimentation.preprocessing import replace_function_name, count_function_defs

# Settings
DATA_FILE = Path('data') / 'mixtral_20240630(complex).json'


def calculate_mcc(tp, tn, fp, fn):
    # for calculate mcc result
    numerator = tp * tn - fp * fn
    denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    if denominator == 0:
        return 0
    return numerator / denominator


def update_metrics(correctness, test_result, tp, tn, fp, fn):
    # for update confusion matrix
    if correctness == test_result:
        if test_result:
            tp += 1
        else:
            tn += 1
    else:
        if test_result:
            fn += 1
        else:
            fp += 1
    return tp, tn, fp, fn


def main(data: dict, config: dict, logger):
    # basic data
    total = 0
    correct = 0

    # MCC data
    tp, tn, fp, fn = 0, 0, 0, 0

    # CSV logger header
    columns = [
        "Task ID", "Specification", "Code", "Test Result", f"{config['postcondition-mode']} Correctness",
        f"{config['postcondition-mode']} Post"]
    if not os.path.exists(logger.csv_file):
        with open(logger.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

    # main loop, iterate each task in data
    for task_id, task_data in data.items():
        specification = task_data["specification"]
        precondition = task_data["precondition"]
        code = task_data["code"]
        replaced_code = replace_function_name(code)
        test_result = task_data["test_result"] == 1

        logger.debug(f"Start Task {task_id}")

        # if connot parse, skip this task
        try:
            parsed_code = ast.parse(replaced_code).body
        except Exception as e:
            logger.debug(f"Task {task_id} skip due to parse error: {e}\n\n\n")
            continue

        # if mult functions, skip this task
        if count_function_defs(code) > 1:
            logger.debug(f"Task {task_id} skip due to mult functions.\n\n\n")
            continue

        detail_log_directory = logger.log_dir / "detail" / task_id
        detail_log_directory.mkdir(parents=True, exist_ok=True)

        try:
            # get hoarecot and cot postcondition
            post = compute_postcondition(precondition, replaced_code, config, detail_log_directory)

            # use postcondition to analyse code correctness
            total += 1
            result = check_entailment(specification, post, code, config, detail_log_directory)
            # if any api error, break and calculate result directly
        except Exception as e:
            logger.error(f"Error: {e}")
            break

        # update accuracy variables
        if result == test_result:
            correct += 1

        # update mcc variables
        if result == test_result:
            if test_result:
                tp += 1
            else:
                tn += 1
        else:
            if test_result:
                fn += 1
            else:
                fp += 1

        # write to logger
        logger.debug(f"Specification: {specification}")
        logger.debug(f"Code:\n{code}")
        logger.debug(f"Test Pass Rate {task_data['test_result']}")
        logger.debug(f"Postcondition: {post}")
        logger.debug(f"Correctness: {result}")

        logger.debug(f"Total Test: {total}")
        logger.debug(f"Total Correct: {correct}\n\n\n")

        # write to csv logger
        result = {
            "Task ID": task_id,
            "Specification": specification,
            "Code": code,
            "Test Result": test_result,
            f"{config['postcondition-mode']} Correctness": result,
            f"{config['postcondition-mode']} Post": post,
        }

        with open(logger.csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(result)

    # calculate final result and write to logger
    rate = correct / total
    mcc = calculate_mcc(tp, tn, fp, fn)

    logger.info(f"{config['postcondition-mode']} Accuracy: {rate}")
    logger.info(f"{config['postcondition-mode']} Confusion Matrix: tp-{tp}, fp-{fp}, fn-{fn}, tn-{tn}")
    logger.info(f"{config['postcondition-mode']} MCC: {mcc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HoarePrompt: Structural Reasoning About Programs in Natural Language")
    parser.add_argument('--config', type=str, help="Path to custom configuration file")
    parser.add_argument('--data', type=str, help="Path to read data")
    parser.add_argument('--log', type=str, help="Directory to save detailed logs")

    args = parser.parse_args()

    if args.config:
        config_file = Path(args.config)
    else:
        config_file = Path("default_config.json")

    config = load_json(config_file)

    if args.data:
        data_file = Path(args.data)
    else:
        data_file = Path(DATA_FILE)

    data = load_json(data_file)

    if args.log:
        log_directory = Path(args.log)
    else:
        log_directory = Path("logs")

    base = datetime.now().strftime("%Y%m%d-%H%M%S")
    logger = logger_setup(log_directory, base, f"{config['model']}_correctness")
    main(data, config, logger)
