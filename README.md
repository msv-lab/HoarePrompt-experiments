# HoarePrompt-mbpp-correctness

## Introduction
HoarePrompt-mbpp-correctness aims to determine whether large language models (LLMs) can accurately judge if a program correctly implements specifications without running the tests, relying solely on natural language reasoning.

## Preparation
Before running the project, ensure the `GROQ_API_KEY` and `OPENAI_API_KEY` is set as an environment variable.

## Running the Project
The project consists of two runnable parts:

1. **Generating Code and Information**:
   To generate a set of sanitized-mbpp codes and related information, run the following command in the project root directory:
   ```bash
   python3 -m src.data_acquisition.get_code_and_precondition
   ```
   This will create the necessary files in the `data` folder.

2. **Testing Code Correctness**:
   To test the LLM's ability to determine if the code meets the given specifications under CoT, non-CoT, and no explanation scenarios, run the following command in the project root directory:
   ```bash
   python3 -m src.experimentation.correctness_main
   ```
   Before running this, make sure to set the `DATA_FILE` variable in the script to the path of the data file you want to test in the `data` folder.
