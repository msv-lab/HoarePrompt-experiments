import ast
from datetime import datetime
from math import sqrt
import csv
import os
import argparse
import shutil
import subprocess
from pathlib import Path
from hoareprompt import compute_postcondition, check_entailment, extract_precondition, compute_postcondition_naive, \
    assess
from importlib.metadata import version
import importlib.util
from src.file_io import load_json
from src.logger_setup import logger_setup
from src.preprocessing import replace_function_name, count_function_defs

import json


# Writes the provided content to a specified file
def save_to_file(content, file_path):
    with open(file_path, 'w') as file:
        #if content i boolean, convert it to string
        content = str(content)
        file.write(content)


# Calculates the Matthews Correlation Coefficient for evaluating binary classification results
def calculate_mcc(tp, tn, fp, fn):
    numerator = tp * tn - fp * fn
    denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    if denominator == 0:
        return 0
    return numerator / denominator


def main(data: dict, config: dict, logger, model, run_number, datafile):
    # These variables are used for tracking the number of tasks and accuracy
    total = 0
    correct = 0

    # These counters are used for calculating MCC
    tp, tn, fp, fn = 0, 0, 0, 0

    # Failed tasks list to store failure details
    failed_tasks = []
    columns = [
        "Task ID", "unique_id", "Dataset", "model_created", "model_run", "description", "Code", "run_number", "original correctness",
        "naive_test"]
    if not os.path.exists(logger.csv_file):
        with open(logger.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
    config["annotated"] = False
    config["fsl"] = False
    config_annotated = config.copy()
    config_annotated["assessment-mode"] = "naive-test"
    # This is the main loop where the work is done, it tterates over each task in the provided data
    #for loop to include the index and the task in the data
    for index, task_data in enumerate(data):
        print(f"Running task {index} out of {len(data)}")
        task_id = task_data["task_id"]
        task_id = task_id.replace("/", "_")
        model_created = task_data["model"]
        dataset = task_data["dataset"]
        code = task_data["generated_code"]
        description = task_data["description"]
        unique_id = task_data["unique_id"]
        original_correctness = task_data["correct"]

        # Here we replace the function name to avoid conflicts in parsing
        replaced_code = replace_function_name(code)
        logger.debug(f"Start Task {task_id}")

        try:
            # if you connot parse the code in ast , skip this task
            parsed_code = ast.parse(replaced_code).body
        except Exception as e:
            logger.debug(f"Task {task_id} skip due to parse error: {e}\n\n\n")
            # Add this task to a failed tasks list with the fail reason being parse error
            failed_tasks.append({
                "task_id": task_id,
                "model_created": model_created,
                "dataset": dataset,
                "model_run": model,
                "code": code,
                "fail_reason": f"Parse error: {e}",
                "type_of_run": "parse_error"
            })
        #     continue
        detail_log_directory = logger.log_dir / unique_id / model_created
        detail_log_directory.mkdir(parents=True, exist_ok=True)
        # pre_directory = detail_log_directory / "extract-precondition"
        # post_directory = detail_log_directory / "compute-postconditon"
        # check_directory = detail_log_directory / "check-entailment"
        # naive_directory = detail_log_directory / "naive"
        # pre_directory.mkdir(parents=True, exist_ok=True)
        # post_directory.mkdir(parents=True, exist_ok=True)
        # check_directory.mkdir(parents=True, exist_ok=True)
        # naive_directory.mkdir(parents=True, exist_ok=True)
        try:
            total += 1
            print(f"Running task {task_id} with log directory {detail_log_directory}")
            result = assess(description, code, task_id, config_annotated, detail_log_directory, None)

            save_to_file(description, detail_log_directory / "description.txt")
            save_to_file(code, detail_log_directory / "program.py")
            save_to_file(result, detail_log_directory / "naive.txt")

            # write to logger
            logger.debug(f"Dataset: {dataset}")
            logger.debug(f"model_created: {model_created}")
            logger.debug(f"model_run: {model}")
            logger.debug(f"description: {description}")
            logger.debug(f"Correctness: {result}")

            # # Write task result to CSV logger

            result = {
                "Task ID": task_id,
                "unique_id": unique_id,
                "Dataset": dataset,
                "model_created": model_created,
                "model_run": model,
                "description": description,
                "Code": code,
                "run_number": run_number,
                "original correctness": original_correctness,
                "naive_test": result
            }

            with open(logger.csv_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writerow(result)

            # result = check_entailment(description, post, code, task_id, config, check_directory)
        except Exception as e:
            # Handle any errors like API issues and log them also add the task to the failed tasks list
            failed_tasks.append({
                "task_id": task_id,
                "unique_id": unique_id,
                "model_created": model_created,
                "dataset": dataset,
                "model_run": model,
                "code": code,
                "fail_reason": f"Error: {e}",
                "type_of_run": "hoareprompt"
            })

            logger.error(f"Error: {e}")
            # break

    # Only save the failed tasks if there are any
    if failed_tasks:
        failed_tasks_file = logger.log_dir / 'failed_tasks.csv'

        # Define the headers for the CSV file
        failed_tasks_headers = ['task_id', 'unique_id', 'model_created', 'dataset', 'model_run', 'code', 'fail_reason',
                                'type_of_run']

        # Write the failed tasks to a CSV file
        with open(failed_tasks_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=failed_tasks_headers)
            writer.writeheader()
            for task in failed_tasks:
                writer.writerow(task)


if __name__ == "__main__":
    # Initialize the argument parser with descriptions for expected command-line arguments
    parser = argparse.ArgumentParser(description="HoarePrompt Experiment")
    parser.add_argument('--config', type=str, help="Path to custom configuration file")
    parser.add_argument('--data', type=str, help="Path to read data")
    parser.add_argument('--log', type=str, help="Directory to save detailed logs")

    #add another argument but make it optional
    parser.add_argument('--run_number', type=str, help="which repetition of the run this is", default=1)
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
        log_directory = Path("Results")

    # if log_directory does not end with underscore and the run_number then add that to the final name in the path
    if not str(log_directory).endswith("_" + str(args.run_number)):
        log_directory = Path(str(log_directory) + f"_{args.run_number}")
        print(f"Log directory: {log_directory}")
    #if the log directory does not exist, create it
    log_directory.mkdir(parents=True, exist_ok=True)

    base = datetime.now().strftime("%Y%m%d-%H%M%S")

    logger = logger_setup(log_directory, base)

    # copy config to log dir
    shutil.copy(config_file, logger.log_dir / config_file.name)

    # save hoareprompt version to log dir
    hoareprompt_version = version("hoareprompt")
    spec = importlib.util.find_spec("hoareprompt")
    # Get the directory where Hoareprompt is installed
    if spec is not None:
        # this is the python script path
        hoareprompt_path = spec.origin
        # this is the source dir
        hoareprompt_dir = os.path.dirname(hoareprompt_path)
        # this is the git repo
        repo_path = os.path.abspath(os.path.join(hoareprompt_dir, ".."))
        #print(f"HoarePrompt is installed at: {repo_path}")
    else:
        print("HoarePrompt is not installed.")
    #Check if it's a Git repository
    if os.path.exists(os.path.join(repo_path, ".git")):
        try:
            # Run git command to get the latest commit hash
            commit_hash_hoare = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=repo_path
            ).strip().decode('utf-8')
        except subprocess.CalledProcessError:
            print("Failed to get the current commit hash.")
    else:
        print(f"{repo_path} is not a Git repository.")
    #keep the file name form the data_file path string, the name is the last file in the path
    data_file_name = os.path.basename(data_file)
    # find the commit of the git repo we are in
    commit_hash_exp = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode()
    model = config['model']
    version_file = logger.log_dir / "VERSIONS"
    with open(version_file, 'w') as f:
        f.write(f"hoareprompt version: {hoareprompt_version}\n")
        f.write(f"HoarePrompt commit hash: {commit_hash_hoare}\n")
        f.write(f"HoarePrompt experiments commit hash: {commit_hash_exp}\n")
        f.write(f"model version: {config['model']}\n")
        f.write(f"data file: {data_file_name}\n")

    main(data, config, logger, model, args.run_number, datafile=data_file_name)
