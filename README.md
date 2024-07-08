# HoarePrompt-mbpp-correctness

## Introduction
HoarePrompt-mbpp-correctness aims to determine whether large language models (LLMs) can accurately judge if a program correctly implements specifications without running the tests, relying solely on natural language reasoning.

## Preparation
Before running the project, ensure the `GROQ_API_KEY` is set as an environment variable, as the script uses `os.environ.get("GROQ_API_KEY")`.

## Running the Project
The project consists of two runnable parts:

1. **Generating Code and Information**:
   To generate a set of sanitized-mbpp codes and related information, run the following command in the project root directory:
   ```bash
   python3 src/get_code_and_precondition.py
   ```
   This will create the necessary files in the `data` folder.

2. **Testing Code Correctness**:
   To test the LLM's ability to determine if the code meets the given specifications under CoT, non-CoT, and no explanation scenarios, run the following command in the project root directory:
   ```bash
   python3 src/correctness_main.py
   ```
   Before running this, make sure to set the `DATA_FILE` variable in the script to the path of the data file you want to test in the `data` folder.

## Configuration
You can adjust the following constants to change the model and temperature settings for different parts of the project:

- **Postcondition Generation**:
  Modify the `DEFAULT_TEMPERATURE` and `MODEL` constants in `complete.py` to change the model and temperature used for generating postconditions.

- **Code Correctness Evaluation**:
  Modify the `DEFAULT_TEMPERATURE` and `MODEL` constants in `correctness_main.py` to change the model and temperature used for evaluating whether the code meets the specifications.

- **Code and Precondition Generation**:
  Modify the `DEFAULT_TEMPERATURE` and `MODEL` constants in `get_code_and_precondition.py` to change the model and temperature used for generating code and preconditions.
