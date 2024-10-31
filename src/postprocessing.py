import pandas as pd
import sys
import json
import os

def preprocess_correctness(value, task_id):
    # Normalize string by removing spaces and converting to lowercase
    normalized_value = str(value).strip().lower()
    if normalized_value in ["correct", "true"]:
        return True
    elif normalized_value in ["incorrect", "false"]:
        return False
    else:
        print(f"Error: Task ID {task_id} has an unrecognized correctness value '{value}'")
        return None

def analyze_correctness(file_path):
    # Load CSV file
    df = pd.read_csv(file_path)

    # Preprocess columns and handle invalid values
    df['Correctness'] = df.apply(lambda row: preprocess_correctness(row['Correctness'], row['Task ID']), axis=1)
    df['naive correctness'] = df.apply(lambda row: preprocess_correctness(row['naive correctness'], row['Task ID']), axis=1)
    df['original correctness'] = df.apply(lambda row: preprocess_correctness(row['original correctness'], row['Task ID']), axis=1)

    # Filter out rows with None values due to unrecognized correctness entries
    valid_df = df.dropna(subset=['Correctness', 'naive correctness', 'original correctness'])

    # Basic info
    total_rows = int(len(valid_df))

    # Original correctness agreement with correctness and naive_correctness
    correct_agreement = int((valid_df['original correctness'] == valid_df['Correctness']).sum())
    naive_agreement = int((valid_df['original correctness'] == valid_df['naive correctness']).sum())

    correct_agreement_pct = float((correct_agreement / total_rows) * 100 if total_rows > 0 else 0)
    naive_agreement_pct = float((naive_agreement / total_rows) * 100 if total_rows > 0 else 0)

    # False positives and false negatives for naive correctness
    false_positives_naive = int(((valid_df['original correctness'] == True) & (valid_df['naive correctness'] == False)).sum())
    false_negatives_naive = int(((valid_df['original correctness'] == False) & (valid_df['naive correctness'] == True)).sum())

    # False positives and false negatives for correctness
    false_positives_correctness = int(((valid_df['original correctness'] == True) & (valid_df['Correctness'] == False)).sum())
    false_negatives_correctness = int(((valid_df['original correctness'] == False) & (valid_df['Correctness'] == True)).sum())

    # Cases where naive_correctness and correctness differ
    naive_correctness_diff = valid_df[valid_df['naive correctness'] != valid_df['Correctness']]

    # Agreement of naive_correctness with original_correctness in cases of difference
    naive_correctness_with_original_in_diff = int((naive_correctness_diff['original correctness'] == naive_correctness_diff['naive correctness']).sum())
    naive_correctness_with_original_in_diff_pct = float((naive_correctness_with_original_in_diff / len(naive_correctness_diff)) * 100 if len(naive_correctness_diff) > 0 else 0)

    # Agreement of correctness with original_correctness in cases of difference
    correctness_with_original_in_diff = int((naive_correctness_diff['original correctness'] == naive_correctness_diff['Correctness']).sum())
    correctness_with_original_in_diff_pct = float((correctness_with_original_in_diff / len(naive_correctness_diff)) * 100 if len(naive_correctness_diff) > 0 else 0)

    # Cases where naive_correctness and correctness are the same
    naive_correctness_same = valid_df[valid_df['naive correctness'] == valid_df['Correctness']]

    # Agreement with original_correctness in cases where naive_correctness and correctness are the same
    same_correctness_original_agreement = int((naive_correctness_same['original correctness'] == naive_correctness_same['Correctness']).sum())
    same_correctness_original_disagreement = int(len(naive_correctness_same) - same_correctness_original_agreement)

    # Calculate percentages
    same_correctness_original_agreement_pct = float((same_correctness_original_agreement / len(naive_correctness_same)) * 100 if len(naive_correctness_same) > 0 else 0)
    same_correctness_original_disagreement_pct = float((same_correctness_original_disagreement / len(naive_correctness_same)) * 100 if len(naive_correctness_same) > 0 else 0)

    # Additional Analysis: Difference in agreement rates
    difference_in_agreement = float(correct_agreement_pct - naive_agreement_pct)

    # Compile report with explanations
    analysis_report = {
        "total_valid_rows": {
            "value": total_rows,
            "description": "Total number of valid rows after preprocessing and removing invalid entries."
        },
        "original_correctness_agreement": {
            "correctness": {
                "count": correct_agreement,
                "percentage": correct_agreement_pct,
                "description": "Number and percentage of times 'Correctness' agrees with 'original correctness'."
            },
            "naive_correctness": {
                "count": naive_agreement,
                "percentage": naive_agreement_pct,
                "description": "Number and percentage of times 'naive correctness' agrees with 'original correctness'."
            }
        },
        "false_positives": {
            "naive_correctness": {
                "count": false_positives_naive,
                "description": "Number of cases where 'original correctness' is True but 'naive correctness' is False."
            },
            "correctness": {
                "count": false_positives_correctness,
                "description": "Number of cases where 'original correctness' is True but 'Correctness' is False."
            }
        },
        "false_negatives": {
            "naive_correctness": {
                "count": false_negatives_naive,
                "description": "Number of cases where 'original correctness' is False but 'naive correctness' is True."
            },
            "correctness": {
                "count": false_negatives_correctness,
                "description": "Number of cases where 'original correctness' is False but 'Correctness' is True."
            }
        },
        "naive_correctness_vs_correctness_diff": {
            "description": "Analysis of cases where 'naive correctness' and 'Correctness' differ.",
            "naive_correctness_with_original_in_diff": {
                "count": naive_correctness_with_original_in_diff,
                "percentage": naive_correctness_with_original_in_diff_pct,
                "description": "Number and percentage of times 'naive correctness' agrees with 'original correctness' when 'naive correctness' and 'Correctness' differ."
            },
            "correctness_with_original_in_diff": {
                "count": correctness_with_original_in_diff,
                "percentage": correctness_with_original_in_diff_pct,
                "description": "Number and percentage of times 'Correctness' agrees with 'original correctness' when 'naive correctness' and 'Correctness' differ."
            }
        },
        "naive_correctness_vs_correctness_same": {
            "description": "Analysis of cases where 'naive correctness' and 'Correctness' are the same.",
            "same_correctness_original_agreement": {
                "count": same_correctness_original_agreement,
                "percentage": same_correctness_original_agreement_pct,
                "description": "Number and percentage of times both 'naive correctness' and 'Correctness' agree with 'original correctness' when they are the same."
            },
            "same_correctness_original_disagreement": {
                "count": same_correctness_original_disagreement,
                "percentage": same_correctness_original_disagreement_pct,
                "description": "Number and percentage of times both 'naive correctness' and 'Correctness' do not agree with 'original correctness' when they are the same."
            }
        },
        "additional_analysis": {
            "difference_in_agreement_with_original": {
                "value": difference_in_agreement,
                "description": "Difference in agreement percentage between 'Correctness' and 'naive correctness' with 'original correctness'."
            }
        }
    }

    # Print report to console
    print("Analysis Report")
    print(json.dumps(analysis_report, indent=4))

    # Save report as JSON
    output_file_path = os.path.join(os.path.dirname(file_path), "analysis_report.json")
    with open(output_file_path, "w") as json_file:
        json.dump(analysis_report, json_file, indent=4)
    print(f"\nAnalysis report saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_correctness.py <csv_file_path>")
    else:
        file_path = sys.argv[1]
        analyze_correctness(file_path)
