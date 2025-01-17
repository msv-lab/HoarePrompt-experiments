import ast
from datetime import datetime
from math import sqrt
import csv
import os
import argparse
import shutil
import subprocess
from pathlib import Path
from hoareprompt import compute_postcondition, check_entailment, extract_precondition, compute_postcondition_naive, assess
from importlib.metadata import version
import importlib.util
from src.file_io import load_json
from src.logger_setup import logger_setup
from src.preprocessing import replace_function_name, count_function_defs

 # Writes the provided content to a specified file
def save_to_file(content, file_path):
    with open(file_path, 'w') as file:
        # If content is boolean, convert it to string
        file.write(str(content))

# Calculates the Matthews Correlation Coefficient for evaluating binary classification results
def calculate_mcc(tp, tn, fp, fn):
    numerator = tp * tn - fp * fn
    denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    if denominator == 0:
        return 0
    return numerator / denominator


def main(data: dict, config: dict, logger, model, datafile):
    # These variables are used for tracking the number of tasks and accuracy
    total = 0
    correct = 0

    # These counters are used for calculating MCC
    tp, tn, fp, fn = 0, 0, 0, 0

    # Failed tasks list to store failure details
    failed_tasks = []

    columns = [
        "Task ID", "Dataset", "unique_id", "model_created", "model_run", "description", "Code", "Test Result",
        "Post", "original correctness" ,"vanilla" , "data file", "probability"]
    if not os.path.exists(logger.csv_file):
        with open(logger.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
    config["annotated"] = False
    config["fsl"] = True
    config_naive = config.copy()
    config_naive["assessment-mode"] = "naive"
    # config_annotated = config.copy()
    # config_annotated["annotated"] = True
    # config_annotated["annotated-type"]="complex"
    # config_annotated_simple = config_annotated.copy()
    # config_annotated_simple["annotated-type"]="simple"
    config_naive_no_fsl = config_naive.copy()
    config_naive_no_fsl["fsl"] = False
    config_naive_no_fsl["confidence"] = True

    # This is the main loop where the work is done, it tterates over each task in the provided data
    for index, task_data in enumerate(data):
        print(f"Running task {index} out of {len(data)}")
        task_id = task_data["task_id"]
        task_id =str(task_id)
        task_id = task_id.replace("/", "_")
        model_created = task_data["model"]
        dataset = task_data["dataset"]
        code = task_data["generated_code"]
        description = task_data["description"]
        original_correctness = task_data["correct"]

        # Here we replace the function name to avoid conflicts in parsing
        replaced_code = replace_function_name(code)

        # For apps dataset, determine test correctness based on pass rate
        # if dataset == "apps":
        #     specification = task_data["question"]
        #     pass_rate = task_data.get("pass_rate", 0)
        #     test_result = pass_rate == 1

        # For mbpp dataset, determine test correctness based on various accuracy metrics
        # elif dataset == "mbpp":
        #     specification = task_data["specification"]
        #     base_accuracy = task_data.get("base_accuracy", 0)
        #     plus_accuracy = task_data.get("plus_accuracy", 0)
        #     assertion_accuracy = task_data.get("assertion_accuracy", 0)
        #     test_result = (base_accuracy == 1.0 and
        #                     plus_accuracy == 1.0 and
        #                     assertion_accuracy == 1.0)

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
            continue
        #We added handling for multiple function
        # # if mult functions, skip this task
        # if count_function_defs(code) > 1:
        #     logger.debug(f"Task {task_id} skip due to mult functions.\n\n\n")
        #     # Add this task to a failed tasks list with the fail reason being multiple functions error
        #     failed_tasks.append({
        #         "task_id": task_id,
        #         "model_created": model_created,
        #         "dataset": dataset,
        #         "model_run": model,
        #         "code": code,
        #         "fail_reason": "Multiple functions error"
        #     })
        #     continue
        # Create log directories for saving the results like precondition, postcondition, entailment check
        detail_log_directory = logger.log_dir  / task_id/ f"{task_id}_normal" / model_created
        pre_directory = detail_log_directory / "extract-precondition"
        post_directory = detail_log_directory / "compute-postconditon"
        check_directory = detail_log_directory / "check-entailment"
        naive_directory = detail_log_directory / "naive"
        pre_directory.mkdir(parents=True, exist_ok=True)
        post_directory.mkdir(parents=True, exist_ok=True)
        check_directory.mkdir(parents=True, exist_ok=True)
        naive_directory.mkdir(parents=True, exist_ok=True)
        # detail_log_directory_annotated = logger.log_dir  /  task_id/ f"{task_id}_annotated" / model_created
        # detail_log_directory_annotated.mkdir(parents=True, exist_ok=True)
        # detail_log_directory_annotated_simple = logger.log_dir  /  task_id/ f"{task_id}_annotated_simple" / model_created
        # detail_log_directory_annotated_simple.mkdir(parents=True, exist_ok=True)
        detail_log_directory_naive = logger.log_dir  / task_id/  f"{task_id}_naive" / model_created
        detail_log_directory_naive.mkdir(parents=True, exist_ok=True)
        detail_log_directory_naive_no_fsl = logger.log_dir  / task_id/  f"{task_id}_naive_no_fsl" / model_created
        detail_log_directory_naive_no_fsl.mkdir(parents=True, exist_ok=True)
        # Extract precondition using HoarePrompt

        # precondition = extract_precondition(description, code, config, pre_directory)
        for i in range(1,13):
            try:
                # Compute postcondition using the precondition and code bycinvoking hoareprompt
                # post = compute_postcondition(precondition, replaced_code, config, post_directory)

                # Check entailment to determine if the postcondition satisfies the description by invoking HoarePrompt
                print(f"Running task {index} out of {len(data)}")
                result_naive_no_fsl, confidence =assess(description, code, task_id, config_naive_no_fsl, detail_log_directory_naive_no_fsl, None)
                # result = check_entailment(description, post, code, task_id, config, check_directory)
            except Exception as e:
                # Handle any errors like API issues and log them also add the task to the failed tasks list
                failed_tasks.append({
                    "task_id": task_id,
                    "model_created": model_created,
                    "dataset": dataset,
                    "model_run": model,
                    "code": code,
                    "fail_reason": f"Error: {e}",
                    "type_of_run": "naive no fsl"
                })

                #if an nexception occurs go to the next task
                break

        # try:
        #     # Compute postcondition using the precondition and code bycinvoking hoareprompt
        #     # post = compute_postcondition(precondition, replaced_code, config, post_directory)

        #     # Check entailment to determine if the postcondition satisfies the description by invoking HoarePrompt
        #     total += 1
        #     print(f"Running task {task_id} with log directory {detail_log_directory}")
        #     result=assess(description, code, task_id, config, detail_log_directory, None)
        #     # result = check_entailment(description, post, code, task_id, config, check_directory)
        # except Exception as e:
        #     # Handle any errors like API issues and log them also add the task to the failed tasks list
        #     failed_tasks.append({
        #         "task_id": task_id,
        #         "model_created": model_created,
        #         "dataset": dataset,
        #         "model_run": model,
        #         "code": code,
        #         "fail_reason": f"Error: {e}",
        #         "type_of_run": "hoareprompt"
        #     })

        #     logger.error(f"Error: {e}")
        #     break

        # try:
        #     # Compute postcondition using the precondition and code bycinvoking hoareprompt
        #     # post = compute_postcondition(precondition, replaced_code, config, post_directory)

        #     # Check entailment to determine if the postcondition satisfies the description by invoking HoarePrompt
            
        #     result_annotated=assess(description, code, task_id, config_annotated, detail_log_directory_annotated, None)
        #     # result = check_entailment(description, post, code, task_id, config, check_directory)
        # except Exception as e:
        #     # Handle any errors like API issues and log them also add the task to the failed tasks list
        #     failed_tasks.append({
        #         "task_id": task_id,
        #         "model_created": model_created,
        #         "dataset": dataset,
        #         "model_run": model,
        #         "code": code,
        #         "fail_reason": f"Error: {e}",
        #         "type_of_run": "hoareprompt annotated"
        #     })

        #     logger.error(f"Error: {e}")
        #     break

        # try:
        #     # Compute postcondition using the precondition and code bycinvoking hoareprompt
        #     # post = compute_postcondition(precondition, replaced_code, config, post_directory)

        #     # Check entailment to determine if the postcondition satisfies the description by invoking HoarePrompt
            
        #     result_annotated_simple=assess(description, code, task_id, config_annotated_simple, detail_log_directory_annotated_simple, None)
        #     # result = check_entailment(description, post, code, task_id, config, check_directory)
        # except Exception as e:
        #     # Handle any errors like API issues and log them also add the task to the failed tasks list
        #     failed_tasks.append({
        #         "task_id": task_id,
        #         "model_created": model_created,
        #         "dataset": dataset,
        #         "model_run": model,
        #         "code": code,
        #         "fail_reason": f"Error: {e}",
        #         "type_of_run": "hoareprompt annotated simple"
        #     })

        #     logger.error(f"Error: {e}")
        #     break

        


        # # # update accuracy variables
        # # if result == test_result:
        # #     correct += 1

        # # # Update accuracy and MCC tracking counters based on result
        # # if result == test_result:
        # #     if test_result:
        # #         tp += 1
        # #     else:
        # #         tn += 1
        # # else:
        # #     if test_result:
        # #         fn += 1
        # #     else:
        # #         fp += 1
        
            # try:
            #     # Check entailment using naive approach
            #     # naive_result = compute_postcondition_naive(description, code, config, naive_directory)
            #     print(f"Running task {index} out of {len(data)}")
            #     naive_result = assess(description, code, task_id, config_naive, detail_log_directory_naive,None)
            # except Exception as e:
            #     # Handle any errors like API issues and log them also add the task to the failed tasks list
            #     failed_tasks.append({
            #         "task_id": task_id,
            #         "model_created": model_created,
            #         "dataset": dataset,
            #         "model_run": model,
            #         "code": code,
            #         "fail_reason": f"Error: {e}",
            #         "type_of_run": "naive"
            #     })

            #     logger.error(f"Error: {e}")
            #     break



            # save to log dir
            save_to_file(description, detail_log_directory / "description.txt")
            save_to_file(code, detail_log_directory / "program.py")
            # save_to_file(precondition, detail_log_directory / "precondition.txt")
            # save_to_file(post, detail_log_directory / "postcondition.txt")
            # save_to_file(naive_result, detail_log_directory / "naive.txt")
            save_to_file(result_naive_no_fsl, detail_log_directory / f"naive_no_fsl_{i}.txt")
            # save_to_file(naive_result, detail_log_directory / f"naive_{i}.txt")
            # save_to_file(result_annotated, detail_log_directory / "annotated.txt")
            # save_to_file(result, detail_log_directory / "result.txt")

            # write to logger
            logger.debug(f"Dataset: {dataset}")
            logger.debug(f"model_created: {model_created}")
            logger.debug(f"model_run: {model}")
            logger.debug(f"description: {description}")
            # logger.debug(f"Code:\n{code}")
            # if dataset == "apps":
            #     logger.debug(f"Test Pass Rate {task_data['pass_rate']}")
            # elif dataset == "mbpp":
            #     logger.debug(f"Base Test Pass Rate: {task_id['base_accuracy']}")
            #     logger.debug(f"Plus Test Pass Rate: {task_id['plus_accuracy']}")
            #     logger.debug(f"Assertion Pass Rate: {task_id['assertion_accuracy']}")
            # logger.debug(f"Postcondition: {post}")
            # logger.debug(f"Correctness: {result}")

            # logger.debug(f"Total Test: {total}")
            # logger.debug(f"Total Correct: {correct}\n\n\n")

            # # Write task result to CSV logger
            result = {
                "Task ID": task_id,
                "Dataset": dataset,
                "unique_id":task_id+"_"+ model_created,
                "model_created": model_created,
                "model_run": model,
                "description": description,
                "Code": code,
                # "Correctness": result,
                "Post": "post",
                "original correctness": original_correctness,
                # "naive correctness": naive_result,
                # "annotated correctness": result_annotated,
                # "annotated correctness simple": result_annotated_simple,
                "vanilla": result_naive_no_fsl,
                "data file": datafile,
                "probability": confidence
            }

            with open(logger.csv_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writerow(result)

     # Final accuracy and MCC logging
    # rate = correct / total
    # mcc = calculate_mcc(tp, tn, fp, fn)

    # logger.info(f"{config['postcondition-mode']} Accuracy: {rate}")
    # logger.info(f"{config['postcondition-mode']} Confusion Matrix: tp-{tp}, fp-{fp}, fn-{fn}, tn-{tn}")
    # logger.info(f"{config['postcondition-mode']} MCC: {mcc}")

        # Only save the failed tasks if there are any
        if failed_tasks:
            failed_tasks_file = logger.log_dir / 'failed_tasks.csv'
            
            # Define the headers for the CSV file
            failed_tasks_headers = ['task_id', 'model_created','dataset', 'model_run' , 'code', 'fail_reason', 'type_of_run']

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
    data_file_name =os.path.basename(data_file)
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

    main(data, config, logger, model, datafile=data_file_name)
