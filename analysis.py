import pandas as pd
import json
import numpy as np
from sklearn.metrics import matthews_corrcoef

# Function to convert int64 to int
def convert_int64_to_int(d):
    if isinstance(d, np.int64):
        return int(d)
    elif isinstance(d, dict):
        return {k: convert_int64_to_int(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [convert_int64_to_int(i) for i in d]
    else:
        return d

# Function to calculate MCC and percentage
def calculate_mcc_and_percentage(true_values, pred_values):
    mcc = matthews_corrcoef(true_values, pred_values)
    count = np.sum(true_values == pred_values)
    percentage = (count / len(true_values)) * 100
    return count, percentage, mcc

# Read the CSV file
df = pd.read_csv('combined_output_code_contests_3point5_total_runs.csv')

# Ensure valid rows (not containing NaN or invalid data)
valid_df = df.dropna(subset=['original correctness', 'Correctness', 'naive correctness', 'annotated correctness', 'naive no fsl correctness'])

# Get original correctness values (1 for 'True', 0 for 'False')
original_correctness = valid_df['original correctness'].apply(lambda x: 1 if x is True else 0)

# Initialize dictionary to store the results
results = {
    "total_valid_rows": {
        "value": len(valid_df),
        "description": "Total number of valid rows after preprocessing and removing invalid entries."
    }
}

# Define the columns to compare with 'original correctness'
columns_to_compare = ['Correctness', 'naive correctness', 'annotated correctness', 'naive no fsl correctness']

# Calculate agreement and MCC for each comparison
original_correctness_agreement = {}

for column in columns_to_compare:
    pred_values = valid_df[column].apply(lambda x: 1 if x is True else 0)
    count, percentage, mcc = calculate_mcc_and_percentage(original_correctness, pred_values)
    original_correctness_agreement[column] = {
        "count": count,
        "percentage": percentage,
        "mcc": mcc,
        "description": f"Number, percentage, and MCC for '{column}' agreement with 'original correctness'."
    }

results['original_correctness_agreement'] = original_correctness_agreement

# Calculate false positives and false negatives for 'naive correctness' and 'Correctness'
false_positives = {
    'naive_correctness': np.sum((original_correctness == 1) & (valid_df['naive correctness'].apply(lambda x: x is False))),
    'Correctness': np.sum((original_correctness == 1) & (valid_df['Correctness'].apply(lambda x: x is False)))
}

false_negatives = {
    'naive_correctness': np.sum((original_correctness == 0) & (valid_df['naive correctness'].apply(lambda x: x is True))),
    'Correctness': np.sum((original_correctness == 0) & (valid_df['Correctness'].apply(lambda x: x is True)))
}

results['false_positives'] = {
    'naive_correctness': {"count": false_positives['naive_correctness'], "description": "Number of cases where 'original correctness' is True but 'naive correctness' is False."},
    'Correctness': {"count": false_positives['Correctness'], "description": "Number of cases where 'original correctness' is True but 'Correctness' is False."}
}

results['false_negatives'] = {
    'naive_correctness': {"count": false_negatives['naive_correctness'], "description": "Number of cases where 'original correctness' is False but 'naive correctness' is True."},
    'Correctness': {"count": false_negatives['Correctness'], "description": "Number of cases where 'original correctness' is False but 'Correctness' is True."}
}

# Calculate analysis for differences between 'naive correctness' and 'Correctness'
naive_correctness_vs_correctness_diff = {
    'naive_correctness_with_original_in_diff': {
        "count": np.sum(((valid_df['naive correctness'].apply(lambda x: x is True)) != (valid_df['Correctness'].apply(lambda x: x is True))) & (original_correctness == 1)),
        "percentage": np.sum(((valid_df['naive correctness'].apply(lambda x: x is True)) != (valid_df['Correctness'].apply(lambda x: x is True))) & (original_correctness == 1)) / len(valid_df) * 100,
        "description": "Number and percentage of times 'naive correctness' agrees with 'original correctness' when 'naive correctness' and 'Correctness' differ."
    },
    'correctness_with_original_in_diff': {
        "count": np.sum(((valid_df['Correctness'].apply(lambda x: x is True)) != (valid_df['naive correctness'].apply(lambda x: x is True))) & (original_correctness == 1)),
        "percentage": np.sum(((valid_df['Correctness'].apply(lambda x: x is True)) != (valid_df['naive correctness'].apply(lambda x: x is True))) & (original_correctness == 1)) / len(valid_df) * 100,
        "description": "Number and percentage of times 'Correctness' agrees with 'original correctness' when 'naive correctness' and 'Correctness' differ."
    }
}

results["naive_correctness_vs_correctness_diff"] = naive_correctness_vs_correctness_diff

# Calculate cases where both 'naive correctness' and 'Correctness' are the same
naive_correctness_vs_correctness_same = {
    'same_correctness_original_agreement': {
        "count": np.sum(((valid_df['naive correctness'].apply(lambda x: x is True)) == (valid_df['Correctness'].apply(lambda x: x is True))) & (original_correctness == 1)),
        "percentage": np.sum(((valid_df['naive correctness'].apply(lambda x: x is True)) == (valid_df['Correctness'].apply(lambda x: x is True))) & (original_correctness == 1)) / len(valid_df) * 100,
        "description": "Number and percentage of times both 'naive correctness' and 'Correctness' agree with 'original correctness' when they are the same."
    },
    'same_correctness_original_disagreement': {
        "count": np.sum(((valid_df['naive correctness'].apply(lambda x: x is True)) == (valid_df['Correctness'].apply(lambda x: x is True))) & (original_correctness == 0)),
        "percentage": np.sum(((valid_df['naive correctness'].apply(lambda x: x is True)) == (valid_df['Correctness'].apply(lambda x: x is True))) & (original_correctness == 0)) / len(valid_df) * 100,
        "description": "Number and percentage of times both 'naive correctness' and 'Correctness' do not agree with 'original correctness' when they are the same."
    }
}

results["naive_correctness_vs_correctness_same"] = naive_correctness_vs_correctness_same

# Calculate the difference in agreement percentage
difference_in_agreement_with_original = {
    "value": np.sum(original_correctness == valid_df['Correctness'].apply(lambda x: 1 if x is True else 0)) / len(valid_df) * 100 - np.sum(original_correctness == valid_df['naive correctness'].apply(lambda x: 1 if x is True else 0)) / len(valid_df) * 100,
    "description": "Difference in agreement percentage between 'Correctness' and 'naive correctness' with 'original correctness'."
}

results["additional_analysis"] = {
    "difference_in_agreement_with_original": difference_in_agreement_with_original
}

# Convert int64 to int
results = convert_int64_to_int(results)

# Save results to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("JSON output has been saved to 'output.json'")