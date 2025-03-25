<table>
  <tr>
    <td style="width: 20%; text-align: center;">
      <img src="./assets/hoareprompt_logo.png" alt="HoarePrompt Logo" width="100"/>
    </td>
    <td style="width: 80%; text-align: left;">
      <h1>HoarePrompt-Experiment: Guide for Running Experiments with HoarePrompt</h1>
    </td>
  </tr>
</table>

## Introduction

The **HoarePrompt-Experiment** guide provides instructions on how to run the HoarePrompt tool for processing an entire dataset.

---

## Preparation

Before running the project, ensure that the necessary environment variables are set, including `GROQ_API_KEY` and `OPENAI_API_KEY`. These keys are essential for accessing the respective APIs that power the LLM services used in this experiment.

### 1. Set Up a Virtual Environment

It is recommended to create a virtual environment to ensure dependency isolation and avoid conflicts with other projects. Follow these steps:

```bash
# Create a virtual environment
python3 -m venv hoareprompt-env

# Activate the virtual environment
source hoareprompt-env/bin/activate
```

### 2. Install Dependencies

Once your virtual environment is activated, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Additionally, install the `hoareprompt` package locally using an editable install:

```bash
pip install -e /path/to/hoareprompt
```

> Replace `/path/to/hoareprompt` with the actual path to the `hoareprompt` directory from the [GitHub repository](https://github.com/msv-lab/HoarePrompt).
> The `-e` flag enables **editable mode**, meaning any changes made to the `hoareprompt` package are immediately reflected without requiring reinstallation.

### 3. Set API Keys

Depending on the LLM service you intend to use, set the appropriate environment variables:

For **OpenAI** models:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

For **Groq** models:
```bash
export GROQ_API_KEY="your-groq-api-key"
```

To persist these variables across terminal sessions, add the above export commands to your `.bashrc` or `.zshrc` file.

---

## Running the Project

This guide helps run multiple test cases in JSON format efficiently. Configuration options are the same as those detailed in the main HoarePrompt README (`../README.md`).

### Input Data Format

The input data file should be a JSON file containing test cases with the following fields:
- `description`: Natural language description of the problem.
- `correct`: Ground truth label indicating correctness.
- `unique_id`: Unique identifier for the test case.
- `task_id`: Identifier related to the problem set.
- `generated_code`: The program code to be evaluated.

You can use our dataset located at `../Results/Dataset`.

### Running the Verification Script

Execute the following command, specifying the data file, log directory, and configuration file paths:

```bash
python3 -m src.main_verify --data /path/to/data/file --log /path/to/log/dir --config /path/to/config/file
```

#### Command-Line Arguments:
- `--data` : Path to the input JSON data file.
- `--log` : Directory where logs will be stored.
- `--config` : Path to the configuration file.

#### Example Usage:
```bash
python3 -m src.main_verify --data data/input.json --log logs/experiment1 --config configs/custom_config.json
```

If you do not provide the `--config` argument, the default configuration file (`default_config.json`) will be used.

### Running Different HoarePrompt Configurations

The `main_verify` script should be used for running HoarePrompt with all available classifiers **except** for `tester`.

If you want to use the `tester` classifier, run the following command with the corresponding tester configuration:

```bash
python3 -m src.main_tester --data /path/to/data/file --log /path/to/log/dir --config /path/to/config/file
```

This ensures compatibility when testing HoarePrompt or HoarePrompt-No-Unroll configurations depending on the specified setup.

---

This guide provides a streamlined approach for executing HoarePrompt experiments efficiently. Refer to the main HoarePrompt documentation (`../README.md`) for more in-depth details on configuration options and parameter settings.



## Related Repositories

The HoarePrompt project consists of multiple repositories, each serving a specific function:

1. **[HoarePrompt (Main Repo)](https://github.com/msv-lab/HoarePrompt)**  
   - The core repository containing the implementation of HoarePrompt, including the logic for analyzing programs, state propagation, and correctness verification.
   
2. **[HoarePrompt-data](https://github.com/msv-lab/HoarePrompt-data)**  
   - A dedicated repository for storing experimental results and datasets related to HoarePrompt evaluations. This includes correctness assessments, counterexamples, and other findings from our testing.
   
3. **[HoarePrompt-experiments](https://github.com/msv-lab/HoarePrompt-experiments)**  
   - This repository provides scripts and configurations to run large-scale experiments with HoarePrompt on various datasets. It includes automated evaluation scripts and batch processing tools.

These repositories collectively support the development, evaluation, and reproducibility of HoarePrompt, making it easy for researchers and developers to experiment with and extend its capabilities.
