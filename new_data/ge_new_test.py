import os
import re
import subprocess

import requests
import json

import add_json

other = 'You are a professional program tester. I will provide you with the problem description of a certain competition problem, which will explain the content of the problem. In addition, it will also explain the scope and requirements that valid inputs need to meet. You need to help me generate 10 different test inputs for edge cases (note: only provide the inputs, no need to provide the outputs). '

txt2 = """
You are a professional program tester. I will provide you with the problem description of a certain competition problem, which will explain the problem content. In addition, it will specify the range and constraints that valid inputs must meet. 

Your task is to generate 10 diverse and well-considered test inputs focusing on the most important edge cases involved in the problem. You only need to provide the inputs, not the outputs. The inputs you provide don't necessarily have to be large in size, but please choose them carefully to ensure diversity and comprehensive coverage.

You need to follow the following format.
# **Input 1**
```

```
# **Input 2**
```

```
# **Input 3**
```

```
# **Input 4**
```

```
# **Input 5**
```

```
# **Input 6**
```

```
# **Input 7**
```

```
# **Input 8**
```

```
# **Input 9**
```

```
# **Input 10**
```

```
Now I will give you the problem description:
{description}
"""

txt = """
You are a professional program tester. I will provide you with the problem description of a certain competition problem, which will explain the problem content as well as the input constraints.

Your task is to generate 20 diverse and well-considered test inputs. These test cases should focus on:

Covering the most important edge cases based on the constraints and problem details.
Ensuring that all key functionalities and aspects of the problem description are thoroughly tested.
The inputs do not necessarily need to be large, but they should be carefully chosen to maximize coverage of edge behaviors, special cases, and typical scenarios that validate the correctness and robustness of the implementation.

You only need to provide the inputs, not the expected outputs.

Please follow the following format.
# **Input 1**
```

```
# **Input 2**
```

```
# **Input 3**
```

```
# **Input 4**
```

```
# **Input 5**
```

```
# **Input 6**
```

```
# **Input 7**
```

```
# **Input 8**
```

```
# **Input 9**
```

```
# **Input 10**
```

```
Now I will give you the problem description:
{description}
"""

url = "https://api.302.ai/v1/chat/completions"

def run_python_code(code, input_data):
    temp_file_path = "temp_program.py"
    with open(temp_file_path, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["python3", temp_file_path],
            input=input_data.encode(),
            capture_output=True,
            timeout=10  # Prevent infinite loops
        )
        output = result.stdout.decode().strip()
        error = result.stderr.decode().strip()
        return output, error
    except subprocess.TimeoutExpired:
        return "", "Timeout"
    finally:
        os.remove(temp_file_path)

def run_all_solutions_on_inputs(solutions, input_list, ignore_case):
    all_results = []

    for idx, input_data in enumerate(input_list, 1):
        print(f"\n--- Running Test Input {idx} ---\nInput:\n{input_data}\n")
        input_results = []

        outputs_set = set()
        has_error = False
        outputs_list = []

        for sol_idx, code in enumerate(solutions, 1):
            print(f"Running Solution {sol_idx}...")
            output, error = run_python_code(code, input_data)

            outputs_list.append(output)
            input_results.append({
                "solution_index": sol_idx,
                "output": output,
                "error": error
            })

            if error:
                has_error = True
            else:
                if ignore_case:
                    output = output.lower()
                print(output)
                outputs_set.add(output)

        # Determine if the current input is valid
        is_valid = (not has_error) and (len(outputs_set) == 1)

        all_results.append({
            "input_index": idx,
            "input": input_data,
            "results": input_results,
            "is_valid": is_valid
        })

    return all_results

def api_call_for_test(name, prob_des, solutions, anycase):
    name_num = name.split("_")[0]
    name_alp = name.split("_")[1]
    payload = json.dumps({
        "model": "o1",  # gpt-4o or o1
        "messages": [
            {
                "role": "user",
                "content": txt.format(description=prob_des),
            }
        ]
    })
    headers = {
        'Accept': 'application/json',
        'Authorization': 'sk-g9aImgg6dDoeoHLvrxUA3kQWtvblpOOZiO6mhad7rfWSjmSB',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    content = json.loads(response.text)
    print("Response received!")

    # Extract test inputs
    test_inputs_text = content['choices'][0]['message']['content']
    pattern = r"# \*\*Input \d+\*\*\n```(.*?)```"
    matches = re.findall(pattern, test_inputs_text, re.DOTALL)

    input_list = [block.strip() for block in matches]

    print(f"\nExtracted {len(input_list)} test inputs\n")

    # Run all solutions
    test_results = run_all_solutions_on_inputs(solutions, input_list, anycase)

    # Filter valid inputs
    valid_inputs = [res for res in test_results if res['is_valid']]

    print(f"\n===== Number of Valid Inputs: {len(valid_inputs)} / {len(input_list)} =====\n")

    # Print valid inputs info
    for v in valid_inputs:
        print(f"Input {v['input_index']} is considered valid")
        print(f"Input Content:\n{v['input']}\n")
        print(f"Outputs from all solutions:\n{v['results'][0]['output']}\n")
        add_json.add_to_jsonl(name_num, name_alp, v['input'], v['results'][0]['output'])

    # If you want to save to file
    # with open("valid_inputs.json", "w", encoding="utf-8") as f:
    #     json.dump(valid_inputs, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    file_path = "./filtered_merged_cor.json"
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            problems = json.load(f)
            for idx, problem in enumerate(problems, 1):
                name = problem.get('task_name')
                # if int(name.split("_")[0]) < 1948:
                #     continue
                description = problem.get('description')
                solutions = problem.get('generated_code')
                print(f"\n================== Running Task: {name} ==================\n")
                if 'any case' in description:
                    anycase = True
                else:
                    anycase = False
                print(anycase)
                api_call_for_test(name, description, solutions, anycase)

                # break  # Remove this if you want to process all tasks
    except Exception as e:
        print(e)