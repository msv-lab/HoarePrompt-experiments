import json
import os
import subprocess

def run_code(file_path, input_data):
    try:
        process = subprocess.Popen(
            ['python3', file_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate(input=input_data, timeout=5)
        return output.strip()
    except subprocess.TimeoutExpired:
        return "Timeout"
    except Exception as e:
        return f"Error: {e}"

def load_testcases(task_name):
    testcase_file = f"./test/{task_name}.jsonl"
    if not os.path.exists(testcase_file):
        print(f"[Skipped] Test case file does not exist: {testcase_file}")
        return []

    testcases = []
    with open(testcase_file, "r", encoding="utf-8") as f:
        for line in f:
            test = json.loads(line.strip())
            testcases.append(test)

    return testcases

def main():
    test_dir = "./test"
    task_names = set()

    # Automatically detect tasks (those that have both task.py and task_1.py)
    for file in os.listdir(test_dir):
        if file.endswith(".py") and not file.endswith("_1.py"):
            task_name = file[:-3]  # Remove .py extension
            if os.path.exists(os.path.join(test_dir, f"{task_name}_1.py")):
                task_names.add(task_name)

    total_tasks = 0
    total_avg_pass_rate = 0.0
    fully_passed_tasks = []  # Store tasks where at least one solution fully passes

    for task_name in sorted(task_names):
        test_inputs = load_testcases(task_name)
        if not test_inputs:
            continue

        print(f"\nTask: {task_name}")
        file_paths = [
            os.path.join(test_dir, f"{task_name}.py"),
            os.path.join(test_dir, f"{task_name}_1.py")
        ]

        task_pass_rates = []
        solution_fully_passed = False

        for idx, file_path in enumerate(file_paths):
            if not os.path.exists(file_path):
                print(f"  [Skipped] File does not exist: {file_path}")
                task_pass_rates.append(0.0)
                continue

            pass_count = 0
            for test_case in test_inputs:
                input_data = test_case['input'].replace("\\n", "\n")
                expected_output = test_case['output']

                output = run_code(file_path, input_data)

                if output == expected_output:
                    pass_count += 1

            pass_rate = pass_count / len(test_inputs)
            task_pass_rates.append(pass_rate)
            print(f"  Solution {idx + 1} ({os.path.basename(file_path)}) Pass Rate: {pass_rate:.1%}")

            if pass_rate == 1.0:
                print(f"===> 🎉 {os.path.basename(file_path)} passed all test cases!")
                solution_fully_passed = True

        avg_rate = sum(task_pass_rates) / len(task_pass_rates)
        total_avg_pass_rate += avg_rate
        total_tasks += 1
        print(f"===> Task Average Pass Rate: {avg_rate:.1%}")

        if solution_fully_passed:
            fully_passed_tasks.append(task_name)
        else:
            print(f"===> ❌ No solution for this task fully passed all test cases.")

    print("\n===============================")
    print(f"Total Tasks Evaluated: {total_tasks}")
    if total_tasks > 0:
        print(f"Overall Average Pass Rate: {(total_avg_pass_rate / total_tasks):.1%}")

    print("\nTasks with at least one 100% correct solution:")
    if fully_passed_tasks:
        for task in fully_passed_tasks:
            print(f"- {task}")
    else:
        print("None")

if __name__ == "__main__":
    main()
