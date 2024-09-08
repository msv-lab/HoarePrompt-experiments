import ast
from datetime import datetime
from math import sqrt
import csv
import os
import argparse
import shutil
from pathlib import Path
from hoareprompt import compute_postcondition, check_entailment, extract_precondition
from importlib.metadata import version

from src.file_io import load_json
from src.logger_setup import logger_setup
from src.preprocessing import replace_function_name, count_function_defs


def save_to_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)


def calculate_mcc(tp, tn, fp, fn):
    # for calculate mcc result
    numerator = tp * tn - fp * fn
    denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    if denominator == 0:
        return 0
    return numerator / denominator


def main(data: dict, config: dict, logger):
    # basic data
    total = 0
    correct = 0

    # MCC data
    tp, tn, fp, fn = 0, 0, 0, 0

    # CSV logger header
    columns = [
        "Task ID", "Dataset", "Model", "Specification", "Code", "Test Result",
        f"{config['postcondition-mode']} Correctness", f"{config['postcondition-mode']} Post"]
    if not os.path.exists(logger.csv_file):
        with open(logger.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

    # main loop, iterate each task in data
    for data_pair in data:
        for task_data in data_pair:
            task_id = task_data["task_id"]
            model = task_data["model"]
            dataset = task_data["dataset"]
            code = task_data["generated_code"]
            replaced_code = replace_function_name(code)
            if dataset == "apps":
                specification = task_data["question"]
                pass_rate = task_data.get("pass_rate", 0)
                test_result = pass_rate == 1

            elif dataset == "mbpp":
                specification = task_data["specification"]
                base_accuracy = task_data.get("base_accuracy", 0)
                plus_accuracy = task_data.get("plus_accuracy", 0)
                assertion_accuracy = task_data.get("assertion_accuracy", 0)
                test_result = (base_accuracy == 1.0 and
                               plus_accuracy == 1.0 and
                               assertion_accuracy == 1.0)

            logger.debug(f"Start Task {task_id}")

            try:
                # if connot parse, skip this task
                parsed_code = ast.parse(replaced_code).body
            except Exception as e:
                logger.debug(f"Task {task_id} skip due to parse error: {e}\n\n\n")
                continue

            # if mult functions, skip this task
            if count_function_defs(code) > 1:
                logger.debug(f"Task {task_id} skip due to mult functions.\n\n\n")
                continue

            detail_log_directory = logger.log_dir / "detail" / task_id / model
            pre_directory = detail_log_directory / "extract-precondition"
            post_directory = detail_log_directory / "compute-postconditon"
            check_directory = detail_log_directory / "check-entailment"
            pre_directory.mkdir(parents=True, exist_ok=True)
            post_directory.mkdir(parents=True, exist_ok=True)
            check_directory.mkdir(parents=True, exist_ok=True)

            precondition = extract_precondition(specification, code, config, pre_directory)
            try:
                # get hoarecot and cot postcondition
                post = compute_postcondition(precondition, replaced_code, config, post_directory)

                # use postcondition to analyse code correctness
                total += 1
                result = check_entailment(specification, post, code, config, check_directory)
            except Exception as e:
                # if any api error, break and calculate result directly
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

            # save to log dir
            save_to_file(specification, detail_log_directory / "description.txt")
            save_to_file(code, detail_log_directory / "program.py")
            save_to_file(precondition, detail_log_directory / "precondition.txt")
            save_to_file(post, detail_log_directory / "postcondition.txt")

            # write to logger
            logger.debug(f"Dataset: {dataset}")
            logger.debug(f"Model: {model}")
            logger.debug(f"Specification: {specification}")
            logger.debug(f"Code:\n{code}")
            if dataset == "apps":
                logger.debug(f"Test Pass Rate {task_data['pass_rate']}")
            elif dataset == "mbpp":
                logger.debug(f"Base Test Pass Rate: {task_id['base_accuracy']}")
                logger.debug(f"Plus Test Pass Rate: {task_id['plus_accuracy']}")
                logger.debug(f"Assertion Pass Rate: {task_id['assertion_accuracy']}")
            logger.debug(f"Postcondition: {post}")
            logger.debug(f"Correctness: {result}")

            logger.debug(f"Total Test: {total}")
            logger.debug(f"Total Correct: {correct}\n\n\n")

            # write to csv logger
            result = {
                "Task ID": task_id,
                "Dataset": dataset,
                "Model": model,
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
    parser = argparse.ArgumentParser(description="HoarePrompt Experiment")
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
        raise ValueError("Cannot find data file.")
    data = load_json(data_file)

    if args.log:
        log_directory = Path(args.log)
    else:
        log_directory = Path("logs")
    base = datetime.now().strftime("%Y%m%d-%H%M%S")
    logger = logger_setup(log_directory, base, f"{config['model']}_correctness")

    # copy config to log dir
    shutil.copy(config_file, logger.log_dir / config_file.name)

    # save hoareprompt version to log dir
    hoareprompt_version = version("hoareprompt")
    version_file = logger.log_dir / "HOAREPROMPT_VERSION"
    with open(version_file, 'w') as f:
        f.write(f"hoareprompt version: {hoareprompt_version}\n")

    main(data, config, logger)
