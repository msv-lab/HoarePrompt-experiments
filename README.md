
<table>
  <tr>
    <td style="width: 20%; text-align: center;">
      <img src="./assets/HoarePrompt_logo.png" alt="HoarePrompt Logo" width="100"/>
    </td>
    <td style="width: 80%; text-align: left;">
      <h1>HoarePrompt-expirement: Experiments guide for the HoarePrompt tool</h1>
    </td>
  </tr>
</table>

## Introduction

The **HoarePrompt-experiment** aims to determine whether large language models (LLMs) can accurately judge if a program correctly implements specifications without executing the tests. The experiment relies solely on natural language reasoning to make these determinations. This project assists users to run multiple experiments on larger datasets of programs using the HoarePrompt tool, the repository of which can be found [here](https://github.com/msv-lab/HoarePrompt).


## Preparation

Before running the project, make sure to set the necessary environment variables such as `GROQ_API_KEY` and `OPENAI_API_KEY`. These keys are essential for accessing the respective APIs, which power the LLM services used in this experiment.

### 1. Set up a Virtual Environment

It is recommended to create a virtual environment to ensure proper dependency isolation and avoid conflicts with other projects. Follow these steps to create and activate the virtual environment:

```bash
# Create a virtual environment
python3 -m venv hoareprompt-env

# Activate the virtual environment
source hoareprompt-env/bin/activate
```

### 2. Install Dependencies

Once your virtual environment is activated, install the necessary dependencies for the project:

```bash
pip install -r requirements.txt
```

Additionally, install the `hoareprompt` package locally using an editable install:

```bash
pip install -e /path/to/hoareprompt
```

> Replace `/path/to/hoareprompt` with the actual path to the `hoareprompt` directory from the git  [repo](https://github.com/msv-lab/HoarePrompt).
  
> The `-e` flag stands for **editable** mode, meaning that any changes you make to the `hoareprompt` package will immediately be reflected without needing to reinstall it.

### 3. Set API Keys

Depending on the LLM service you intend to use, set the appropriate environment variables for your API keys:

For **OpenAI** models:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

For **Groq** models:
```bash
export GROQ_API_KEY="your-groq-api-key"
```

You can add these `export` commands to your `.bashrc` or `.zshrc` files to avoid having to set them every time you start a new terminal session.

## Running the Project

To run the project, execute the following command, specifying the data, log, and configuration file paths:

```bash
python3 -m src.main --data /path/to/data/file --log /path/to/log/dir --config /path/to/config/file
```

- `--data` : Path to the data file.
- `--log` : Directory where logs will be stored.
- `--config` : Path to the configuration file.

Example:
```bash
python3 -m src.main --data data/input.json --log logs/experiment1 --config configs/custom_config.json
```

If you do not provide the `--config` argument, the default configuration file (`default_config.json`) will be used.

## Directory Structure

The experiment are dependent and will create various directories to organize configuration, data, and logs:

Visit **Path:** [scripts/scripts.md](scripts/scripts.md) for documentation on the different scripts you can use to run experiments.
All the bash scripts in the helper runners folder of the repo are used to schedule experiments.

1. **Data File**: The data file  is read from the path specified with `--data`. For potential data to use you can consider the sanitized-mbpp.json or you can use the example data in the [input_data folder](./input_data)

2. **Configuration File**: Passed via `--config`, this file contains parameters that guide the behavior of the experiment (model type, training options, etc.). If not provided, `default_config.json` will be used.
3. **Log Directory**: If the log directory doesn't already exist, it will be created automatically. If no log directory is provided the `Results` directory will be used. Inside the log directory, a folder with the current datetime will be created inside which the following will be saved:
    - **Logs**: Log files documenting the detailed execution of the experiment.
    - **Configuration Copy**: A copy of the configuration file used for the experiment, saved for future reference.
    - **Potential failed_tasks_file** : A file detailing any tasks that failed and the failure reason and error code
    - **CSVs with the tasks and the results of the experiment** : detailed csvs with all the information of the tasks, the HoarePrompt result, potential counter examples etc
    - **Versioning Information**: A `VERSIONS` file is generated, containing version details of the `hoareprompt` package (the version), the commit hash of the 2 git directories (the HoarePrompt and the HoarePrompt-experiments one), and the LLM model used.

    Our proposal is that you also clone our [data repository](https://github.com/msv-lab/HoarePrompt-data) and use the Results folder in there to store the logs and the results of your experimental run. So using  `--log ../HoarePrompt-data/Results` is advised assuming you have cloned the [data repository](https://github.com/msv-lab/HoarePrompt-data) first.


## Contributions
This is a project of Peking Univeristy. Feel free to contribute to HoarePrompt-data by opening issues or submitting pull requests on GitHub. Your contributions are highly appreciated!

<div style="display: flex; justify-content: center;">
  <table style="table-layout: fixed; text-align: center;">
    <tr>
      <td style="width: 50%; text-align: center;">
        <img src="./assets/PKU.png" alt="Image 1" width="300"/>
      </td>
      <td style="width: 50%; text-align: center;">
        <img src="./assets/HoarePrompt_logo.png" alt="Image 2" width="300"/>
      </td>
    </tr>
  </table>
</div>