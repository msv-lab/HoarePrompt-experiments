# HoarePrompt-experiment

## Introduction
This HoarePrompt-experiment aims to determine whether large language models (LLMs) can accurately judge if a program correctly implements specifications without running the tests, relying solely on natural language reasoning.

## Preparation
Before running the project, ensure the `GROQ_API_KEY`, `OPENAI_API_KEY` and all relative api keys are set as an environment variable.




## Installation

To install the necessary dependencies and `hoareprompt` package, run the following commands:

```zsh
pip install -r requirements.txt
```
```zsh
pip install -e /path/to/hoareprompt
```

Replace `/path/to/hoareprompt` with the actual path to the `hoareprompt` package directory.

## Running the Project

You can run the project using the following command:

```bash
python3 -m src.main --data /path/to/data/file --log /path/to/log/dir --config /path/to/config/file
```

- `--data` : Path to the data file.
- `--log` : Directory where logs will be stored.
- `--config` : Path to the configuration file.
