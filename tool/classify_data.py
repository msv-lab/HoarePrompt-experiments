import pandas as pd
import os
import argparse

def classify_data(model, date):
    folder_path = os.path.join('logs', f'{model}_correctness_' + date)
    input_file_path = os.path.join(folder_path, f'{date}.csv')

    df = pd.read_csv(input_file_path)

    required_columns = ['Test Result', 'HoareCoT Correctness', 'CoT Correctness', 'No Explanation Correctness']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Input file must contain the column: {col}")

    cot_correct = df[
        (df['HoareCoT Correctness'] == df['Test Result']) & (df['CoT Correctness'] != df['Test Result'])]
    non_cot_correct = df[
        (df['HoareCoT Correctness'] != df['Test Result']) & (df['CoT Correctness'] == df['Test Result'])]
    no_explanation_correct = df[
        (df['HoareCoT Correctness'] != df['Test Result']) & (df['No Explanation Correctness'] == df['Test Result'])]

    hoarecot_correct_file = os.path.join(folder_path, f'hoarecot_correct.csv')
    cot_correct_file = os.path.join(folder_path, f'cot_correct.csv')
    no_explanation_correct_file = os.path.join(folder_path, f'no_explanation_correct.csv')

    cot_correct.to_csv(hoarecot_correct_file, index=False)
    non_cot_correct.to_csv(cot_correct_file, index=False)
    no_explanation_correct.to_csv(no_explanation_correct_file, index=False)

    print(f"Data classified and saved to {folder_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify data based on correctness columns")
    parser.add_argument("model", type=str, help="The model in the name.")
    parser.add_argument("date", type=str, help="Date used to find file and directory paths")

    args = parser.parse_args()

    classify_data(args.model, args.date)
