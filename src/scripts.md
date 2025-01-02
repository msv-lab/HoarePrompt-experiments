# Scipt : `main_confidence.py` 

The `main_confidence.py` script evaluates the confidence of generated code examples using two methods:
1. **Direct Model Confidence**: Obtains the model's self-reported confidence.
2. **Log Probabilities**: Derives confidence from the log probabilities of tokens in the response.

The script processes a dataset in JSON format, computes metrics, and logs detailed results.

---

## Features

- **Confidence Calculation**:
  - Uses direct feedback (`confidence1`) and token probabilities (`confidence2`).
- **Correctness Evaluation**:
  - Assesses the correctness of generated responses against expected outcomes.
- **Detailed Logging**:
  - Saves comprehensive logs, including configurations, results, and failed tasks.
- **Metrics**:
  - Computes Matthews Correlation Coefficient (MCC) and correctness rates.
- **Version Tracking**:
  - Records repository commit hashes and configuration details for reproducibility.

---

## Input and Output

### Inputs:
1. **Configuration File (`--config`)**:
   - JSON file specifying model settings.
   - Example: `default_config.json`.

2. **Dataset File (`--data`)**:
   - JSON dataset containing tasks, descriptions, and generated code.
   - Example dataset structure:
     ```json
     [
       {
         "task_id": "example_task_1",
         "model": "gpt-3",
         "dataset": "apps",
         "generated_code": "def example(): pass",
         "description": "Example task description",
         "correct": true
       }
     ]
     ```

3. **Log Directory (`--log`)**:
   - Directory for storing results and logs. Defaults to `Results/`.

### Outputs:
1. **Log Directory**:
   - Task-specific logs (e.g., descriptions, code, postconditions).
   - Example structure:
     ```
     Results/
     ├── failed_tasks.csv
     ├── VERSIONS
     ├── confidences.csv
     ├── example_task_1/
         ├── description.txt
         ├── program.py
         ├── result.txt
     ```

2. **CSV Log**:
   - Aggregates task results with confidence and correctness metrics.
   - Example:
     ```csv
     Task ID, Dataset, model_created, model_run, description, Code, Test Result, Post, original correctness, confidence1, confidence2, correctness1, correctness2, data file
     example_task_1, apps, gpt-3, gpt-3, Example task description, ..., True, 0.85, 0.92, True, True, data.json
     ```

3. **Failed Tasks**:
   - Logs skipped or failed tasks in `failed_tasks.csv`.

4. **Version Log**:
   - Includes library version, repository commit hash, and configuration details.

---

## Usage

### Command-Line Syntax:
```bash
python main_confidence.py --config <config_path> --data <data_path> --log <log_directory>
```

# Script : `main_confidence_simple.py` 

This script `main_confidence_simple.py` , evaluates the confidence of a model's responses by repeatedly querying the LLM with the same input. The confidence is measured based on how consistently the LLM produces the same response over multiple runs.

---

## Features

### Core Functionality
- **Repeated Assessments**: The script runs the same LLM query multiple times to measure response consistency.
- **Confidence Metrics**:
  - Captures how many of the responses are identical across runs.
  - Stores each run's results for detailed analysis.
- **Error Handling**:
  - Skips unparsable tasks and logs reasons for failure.
- **Comprehensive Logging**:
  - Saves detailed logs of task results, including preconditions, postconditions, and confidence values.

### Key Metrics
- **Confidence Calculation**:
  - Counts the frequency of identical responses across runs.
- **Correctness Tracking**:
  - Evaluates whether the responses match expected outcomes.

---

## Input and Output

### Inputs:
1. **Configuration File (`--config`)**:
   - Specifies the model and other runtime parameters.
   - Default: `default_config.json`.

2. **Dataset File (`--data`)**:
   - JSON file containing tasks and their associated code.
   - Example structure:
     ```json
     [
       {
         "task_id": "example_task",
         "model": "gpt-3",
         "dataset": "apps",
         "generated_code": "def example(): pass",
         "description": "This is a sample task",
         "correct": true
       }
     ]
     ```

3. **Log Directory (`--log`)**:
   - Directory to save logs and results. Default: `Results/`.

### Outputs:
1. **CSV Log**:
   - Aggregates task results and confidence metrics.
   - Example:
     ```csv
     Task ID,Dataset,unique_id,model_created,model_run,description,Code,Test Result,Post,original correctness,naive no fsl correctness,data file
     example_task,apps,example_task_gpt-3,gpt-3,gpt-3,This is a sample task,def example(): pass,True,post,True,True,data.json
     ```

2. **Task Logs**:
   - Task-specific directories with detailed logs for each run.
   - Example structure:
     ```
     Results/
     ├── failed_tasks.csv
     ├── VERSIONS
     ├── confidence.csv
     ├── example_task/
         ├── description.txt
         ├── program.py
         ├── naive_no_fsl_1.txt
         ├── naive_no_fsl_2.txt
         ├── ...
     ```

3. **Failed Tasks**:
   - Records details of tasks that failed parsing or execution in `failed_tasks.csv`.

---


## Example Usage

### Command-Line Syntax:
```bash
python main_confidence.py --config <config_path> --data <data_path> --log <log_directory>
```

# Script : `main_confidence_logprobs.py` 

This script `main_confidence_logprobs.py` , evaluates the confidence of a model's responses by repeatedly querying the LLM with the same input. The confidence is measured based on how consistently the LLM produces the same response over multiple runs.

---

## Features

### Core Functionality
- **Repeated Assessments**: The script runs the same LLM query multiple times to measure response consistency.
- **Confidence Metrics**:
  - Gets the lobgprobability of the token returned. The token is gonna be either TRUE or FALSE, and only on token is gonna be in the response.
  - Turns the token probability to actual probabilioty from 0 to 1.
  - Stores each run's results for detailed analysis.
- **Error Handling**:
  - Skips unparsable tasks and logs reasons for failure.
- **Comprehensive Logging**:
  - Saves detailed logs of task results, including preconditions, postconditions, and confidence values.

### Key Metrics
- **Confidence Calculation**:
  - Caclulates the confidence in each response.
- **Correctness Tracking**:
  - Evaluates whether the responses match expected outcomes.

---

## Input and Output

### Inputs:
1. **Configuration File (`--config`)**:
   - Specifies the model and other runtime parameters.
   - Default: `default_config.json`.

2. **Dataset File (`--data`)**:
   - JSON file containing tasks and their associated code.
   - Example structure:
     ```json
     [
       {
         "task_id": "example_task",
         "model": "gpt-3",
         "dataset": "apps",
         "generated_code": "def example(): pass",
         "description": "This is a sample task",
         "correct": true
       }
     ]
     ```

3. **Log Directory (`--log`)**:
   - Directory to save logs and results. Default: `Results/`.

### Outputs:
1. **CSV Log**:
   - Aggregates task results and confidence metrics.
   - Example:
     ```csv
     Task ID,Dataset,unique_id,model_created,model_run,description,Code,Test Result,Post,original correctness,naive no fsl correctness,data file
     example_task,apps,example_task_gpt-3,gpt-3,gpt-3,This is a sample task,def example(): pass,True,post,True,True,data.json
     ```

2. **Task Logs**:
   - Task-specific directories with detailed logs for each run.
   - Example structure:
     ```
     Results/
     ├── failed_tasks.csv
     ├── VERSIONS
     ├── confidence.csv
     ├── example_task/
         ├── description.txt
         ├── program.py
         ├── naive_no_fsl_1.txt
         ├── naive_no_fsl_2.txt
         ├── ...
     ```

3. **Failed Tasks**:
   - Records details of tasks that failed parsing or execution in `failed_tasks.csv`.

---


## Example Usage

### Command-Line Syntax:
```bash
python main_confidence_logprobs.py --config <config_path> --data <data_path> --log <log_directory>
```



# Script: `main_fast.py` 

This script evaluates Python code examples using various classifiers from the HoarePrompt library (`naive`, `naive no fsl`, `simple tree`, `complex tree`, `function summary`). It optimizes performance by reusing HoarePrompt's internal states, reducing redundant computation for multiple classifiers.

---

## Features

### Core Functionality
- **Multi-Classifier Support**:
  - Runs experiments for the following classifiers:
    - `naive`
    - `naive no fsl`
    - `simple tree`
    - `complex tree`
    - `function summary`

- **Performance Optimization**:
  - Reuses extracted preconditions and HoarePrompt states across all classifiers.

- **Error Handling**:
  - Skips tasks with unparsable code or unsupported structures.
  - Logs errors and failed tasks for debugging.

- **Detailed Logging**:
  - Saves intermediate states such as preconditions, postconditions, and classifier results.
  - Logs detailed task-level results.

---

## Input and Output

### Inputs:
1. **Configuration File (`--config`)**:
   - Defines runtime parameters and classifier settings.
   - Default: `default_config.json`.

2. **Dataset File (`--data`)**:
   - JSON file containing tasks to evaluate.
   - Example structure:
     ```json
     [
       {
         "task_id": "example_task",
         "model": "gpt-3",
         "dataset": "apps",
         "generated_code": "def example(): pass",
         "description": "This is a sample task",
         "correct": true
       }
     ]
     ```

3. **Log Directory (`--log`)**:
   - Directory for saving logs and outputs. Default: `Results/`.

### Outputs:
1. **CSV Log**:
   - Logs results for each classifier and task in CSV format.
   - Example:
     ```csv
     Task ID,Dataset,model_created,model_run,description,Code,Correctness,Post,original correctness,naive correctness,annotated correctness,annotated correctness simple,naive no fsl correctness,Correctness no fsl,data file
     example_task,apps,gpt-3,gpt-3,This is a sample task,def example(): pass,True,post,True,True,True,True,True,True,data.json
     ```

2. **Task Logs**:
   - Saves intermediate states for each task:
     - Preconditions
     - Postconditions
     - Classifier results
   
     ```

3. **Failed Tasks**:
   - Logs skipped or failed tasks in `failed_tasks.csv`.

---


## Example Usage

### Command-Line Syntax:
```bash
python main_fast.py --config <config_path> --data <data_path> --log <log_directory>
```

# Script: `main_verify.py` 

This script evaluates Python code examples using a comprehensive set of classifiers from the HoarePrompt library. It extends the functionality of `main_fast.py` by including additional verification-based classifiers to analyze and verify the correctness of the code examples.

---

## Features

### Core Functionality
- **Expanded Classifier Support**:
  - Evaluates tasks using the following classifiers:
    - `naive`
    - `naive no fsl`
    - `simple tree`
    - `complex tree`
    - `function summary`
    - `function summary no fsl`
    - `verify simple`
    - `verify complex`
    - `verify function summary`
    - `verify simple no fsl`
    - `verify complex no fsl`
    - `verify function summary no fsl`

- **Performance Optimization**:
  - Reuses HoarePrompt's internal states to avoid redundant computation across classifiers.

- **Error Handling**:
  - Skips tasks with unparsable code or unsupported structures.
  - Logs errors and failed tasks for debugging.

- **Detailed Logging**:
  - Saves intermediate states such as preconditions, postconditions, and classifier results.
  - Logs detailed task-level results.

---

## Input and Output

### Inputs:
1. **Configuration File (`--config`)**:
   - Defines runtime parameters and classifier settings.
   - Default: `default_config.json`.

2. **Dataset File (`--data`)**:
   - JSON file containing tasks to evaluate.
   - Example structure:
     ```json
     [
       {
         "task_id": "example_task",
         "model": "gpt-3",
         "dataset": "apps",
         "generated_code": "def example(): pass",
         "description": "This is a sample task",
         "correct": true
       }
     ]
     ```

3. **Log Directory (`--log`)**:
   - Directory for saving logs and outputs. Default: `Results/`.

### Outputs:
1. **CSV Log**:
   - Logs results for each classifier and task in CSV format.
   - Example:
     ```csv
     Task ID,Dataset,model_created,model_run,description,Code,Correctness,Post,original correctness,naive correctness,annotated correctness,annotated correctness simple,naive no fsl correctness,Correctness no fsl,verify simple,verify complex,verify function summary,verify simple no fsl,verify complex no fsl,verify function summary no fsl,data file
     example_task,apps,gpt-3,gpt-3,This is a sample task,def example(): pass,True,post,True,True,True,True,True,True,True,True,True,True,True,True,data.json
     ```

2. **Task Logs**:
   - Saves intermediate states for each task:
     - Preconditions
     - Postconditions
     - Classifier results
  

3. **Failed Tasks**:
   - Logs skipped or failed tasks in `failed_tasks.csv`.

---


## Example Usage

### Command-Line Syntax:
```bash
python main_verify.py --config <config_path> --data <data_path> --log <log_directory>
```

# Script : `main.py`

This script evaluates Python code examples using a set of classifiers from the HoarePrompt library. Unlike `main_fast.py`, this script recalculates the HoarePrompt states separately for each non-naive classifier, making it less optimized but suitable for independent evaluations.

---

## Features

### Core Functionality
- **Classifier Support**:
  - Evaluates tasks using the following classifiers:
    - `naive`
    - `naive no fsl`
    - `simple tree`
    - `complex tree`
    - `function summary`

- **Independent State Calculations**:
  - HoarePrompt states are recalculated for `simple tree`, `complex tree`, and `function summary` classifiers.

- **Detailed Logging**:
  - Saves results for each classifier, including intermediate states and correctness evaluations.

- **Error Handling**:
  - Skips tasks with unparsable or unsupported code structures.
  - Logs errors and failed tasks for debugging.

---

## Input and Output

### Inputs:
1. **Configuration File (`--config`)**:
   - Defines runtime parameters and classifier settings.
   - Default: `default_config.json`.

2. **Dataset File (`--data`)**:
   - JSON file containing tasks to evaluate.
   - Example structure:
     ```json
     [
       {
         "task_id": "example_task",
         "model": "gpt-3",
         "dataset": "apps",
         "generated_code": "def example(): pass",
         "description": "This is a sample task",
         "correct": true
       }
     ]
     ```

3. **Log Directory (`--log`)**:
   - Directory for saving logs and outputs. Default: `Results/`.

### Outputs:
1. **CSV Log**:
   - Logs results for each classifier and task in CSV format.
   - Example:
     ```csv
     Task ID,Dataset,model_created,model_run,description,Code,Correctness,Post,original correctness,naive correctness,annotated correctness,annotated correctness simple,naive no fsl correctness,Correctness no fsl,data file
     example_task,apps,gpt-3,gpt-3,This is a sample task,def example(): pass,True,post,True,True,True,True,True,True,data.json
     ```

2. **Task Logs**:
   - Saves intermediate states and results for each task.
   - Example structure:
     ```
     Results/
     ├── failed_tasks.csv
     ├── VERSIONS
     ├── example_task/
         ├── description.txt
         ├── program.py
         ├── naive.txt
         ├── naive_no_fsl.txt
         ├── result_simple.txt
         ├── result_complex.txt
         ├── result_function_summary.txt
     ```

3. **Failed Tasks**:
   - Logs skipped or failed tasks in `failed_tasks.csv`.

---


## Example Usage

### Command-Line Syntax:
```bash
python main.py --config <config_path> --data <data_path> --log <log_directory>
```