## Scipt : `main_confidence.py` 

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
     ├── confidences.json
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