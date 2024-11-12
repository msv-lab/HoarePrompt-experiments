import pandas as pd
import sys
import json
import os
import math

def preprocess_correctness(value, task_id):
    normalized_value = str(value).strip().lower()
    if normalized_value in ["correct", "true"]:
        return True
    elif normalized_value in ["incorrect", "false"]:
        return False
    else:
        print(f"Error: Task ID {task_id} has an unrecognized correctness value '{value}'")
        return None

def calculate_mcc(tp, tn, fp, fn):
    numerator = (tp * tn) - (fp * fn)
    denominator = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return numerator / denominator if denominator != 0 else 0

def analyze_correctness(file_path):
    df = pd.read_csv(file_path)
    df['Correctness'] = df.apply(lambda row: preprocess_correctness(row['Correctness'], row['Task ID']), axis=1)
    df['naive correctness'] = df.apply(lambda row: preprocess_correctness(row['naive correctness'], row['Task ID']), axis=1)
    df['original correctness'] = df.apply(lambda row: preprocess_correctness(row['original correctness'], row['Task ID']), axis=1)
    df['annotated_correctness'] = df.apply(lambda row: preprocess_correctness(row['annotated correctness'], row['Task ID']), axis=1)
    df['annotated_correctness_simple'] = df.apply(lambda row: preprocess_correctness(row['annotated correctness simple'], row['Task ID']), axis=1)
    df['naive_correctness_no_fsl'] = df.apply(lambda row: preprocess_correctness(row['naive no fsl correctness'], row['Task ID']), axis=1)
    valid_df = df.dropna(subset=['Correctness', 'naive correctness', 'original correctness', 'annotated_correctness','annotated_correctness_simple', 'naive_correctness_no_fsl'])
    total_rows = int(len(valid_df))

    correct_agreement = int((valid_df['original correctness'] == valid_df['Correctness']).sum())
    naive_agreement = int((valid_df['original correctness'] == valid_df['naive correctness']).sum())
    correct_agreement_pct = float((correct_agreement / total_rows) * 100 if total_rows > 0 else 0)
    naive_agreement_pct = float((naive_agreement / total_rows) * 100 if total_rows > 0 else 0)
    correct_annotated_agreement = int((valid_df['original correctness'] == valid_df['annotated_correctness']).sum())
    correct_annotated_agreement_pct = float((correct_annotated_agreement / total_rows) * 100 if total_rows > 0 else 0)
    correct_annotated_simple_agreement = int((valid_df['original correctness'] == valid_df['annotated_correctness_simple']).sum())
    correct_annotated_simple_agreement_pct = float((correct_annotated_simple_agreement / total_rows) * 100 if total_rows > 0 else 0)
    naive_no_fsl_agreement = int((valid_df['original correctness'] == valid_df['naive_correctness_no_fsl']).sum())
    naive_no_fsl_agreement_pct = float((naive_no_fsl_agreement / total_rows) * 100 if total_rows > 0 else 0)
    

    tp_correctness = int(((valid_df['original correctness'] == True) & (valid_df['Correctness'] == True)).sum())
    tn_correctness = int(((valid_df['original correctness'] == False) & (valid_df['Correctness'] == False)).sum())
    fp_correctness = int(((valid_df['original correctness'] == False) & (valid_df['Correctness'] == True)).sum())
    fn_correctness = int(((valid_df['original correctness'] == True) & (valid_df['Correctness'] == False)).sum())

    tp_correctness_annotated = int(((valid_df['original correctness'] == True) & (valid_df['annotated_correctness'] == True)).sum())
    tn_correctness_annotated = int(((valid_df['original correctness'] == False) & (valid_df['annotated_correctness'] == False)).sum())
    fp_correctness_annotated = int(((valid_df['original correctness'] == False) & (valid_df['annotated_correctness'] == True)).sum())
    fn_correctness_annotated = int(((valid_df['original correctness'] == True) & (valid_df['annotated_correctness'] == False)).sum())
    
    tp_correctness_annotated_simple = int(((valid_df['original correctness'] == True) & (valid_df['annotated_correctness_simple'] == True)).sum())
    tn_correctness_annotated_simple = int(((valid_df['original correctness'] == False) & (valid_df['annotated_correctness_simple'] == False)).sum())
    fp_correctness_annotated_simple = int(((valid_df['original correctness'] == False) & (valid_df['annotated_correctness_simple'] == True)).sum())
    fn_correctness_annotated_simple = int(((valid_df['original correctness'] == True) & (valid_df['annotated_correctness_simple'] == False)).sum())


    tp_naive = int(((valid_df['original correctness'] == True) & (valid_df['naive correctness'] == True)).sum())
    tn_naive = int(((valid_df['original correctness'] == False) & (valid_df['naive correctness'] == False)).sum())
    fp_naive = int(((valid_df['original correctness'] == False) & (valid_df['naive correctness'] == True)).sum())
    fn_naive = int(((valid_df['original correctness'] == True) & (valid_df['naive correctness'] == False)).sum())

    tp_naive_no_fsl = int(((valid_df['original correctness'] == True) & (valid_df['naive_correctness_no_fsl'] == True)).sum())
    tn_naive_no_fsl = int(((valid_df['original correctness'] == False) & (valid_df['naive_correctness_no_fsl'] == False)).sum())
    fp_naive_no_fsl = int(((valid_df['original correctness'] == False) & (valid_df['naive_correctness_no_fsl'] == True)).sum())
    fn_naive_no_fsl = int(((valid_df['original correctness'] == True) & (valid_df['naive_correctness_no_fsl'] == False)).sum())
    
    mcc_correctness = calculate_mcc(tp_correctness, tn_correctness, fp_correctness, fn_correctness)
    mcc_naive = calculate_mcc(tp_naive, tn_naive, fp_naive, fn_naive)
    mcc_correctness_annotated = calculate_mcc(tp_correctness_annotated, tn_correctness_annotated, fp_correctness_annotated, fn_correctness_annotated)
    mcc_correctness_annotated_simple = calculate_mcc(tp_correctness_annotated_simple, tn_correctness_annotated_simple, fp_correctness_annotated_simple, fn_correctness_annotated_simple)
    mcc_naive_no_fsl = calculate_mcc(tp_naive_no_fsl, tn_naive_no_fsl, fp_naive_no_fsl, fn_naive_no_fsl)

    naive_correctness_diff = valid_df[valid_df['naive correctness'] != valid_df['Correctness']]
    naive_correctness_with_original_in_diff = int((naive_correctness_diff['original correctness'] == naive_correctness_diff['naive correctness']).sum())
    naive_correctness_with_original_in_diff_pct = float((naive_correctness_with_original_in_diff / len(naive_correctness_diff)) * 100 if len(naive_correctness_diff) > 0 else 0)
    correctness_with_original_in_diff = int((naive_correctness_diff['original correctness'] == naive_correctness_diff['Correctness']).sum())
    correctness_with_original_in_diff_pct = float((correctness_with_original_in_diff / len(naive_correctness_diff)) * 100 if len(naive_correctness_diff) > 0 else 0)

    naive_correctness_same = valid_df[valid_df['naive correctness'] == valid_df['Correctness']]
    same_correctness_original_agreement = int((naive_correctness_same['original correctness'] == naive_correctness_same['Correctness']).sum())
    same_correctness_original_disagreement = int(len(naive_correctness_same) - same_correctness_original_agreement)
    same_correctness_original_agreement_pct = float((same_correctness_original_agreement / len(naive_correctness_same)) * 100 if len(naive_correctness_same) > 0 else 0)
    same_correctness_original_disagreement_pct = float((same_correctness_original_disagreement / len(naive_correctness_same)) * 100 if len(naive_correctness_same) > 0 else 0)

    difference_in_agreement = float(correct_agreement_pct - naive_agreement_pct)

    analysis_report = {
        "total_valid_rows": {
            "value": total_rows,
            "description": "Total number of valid rows after preprocessing and removing invalid entries."
        },
        "original_correctness_agreement": {
            "correctness": {
                "count": correct_agreement,
                "percentage": correct_agreement_pct,
                "mcc": mcc_correctness,
                "description": "Number, percentage, and MCC for 'Correctness' agreement with 'original correctness'."
            },
            "naive_correctness": {
                "count": naive_agreement,
                "percentage": naive_agreement_pct,
                "mcc": mcc_naive,
                "description": "Number, percentage, and MCC for 'naive correctness' agreement with 'original correctness'."
            },
            "annotated_correctness": {
                "count": correct_annotated_agreement,
                "percentage": correct_annotated_agreement_pct,
                "mcc": mcc_correctness_annotated,
                "description": "Number, percentage, and MCC for 'annotated correctness' agreement with 'original correctness'."
            },
            "naive_no_fsl_correctness": {
                "count": naive_no_fsl_agreement,
                "percentage": naive_no_fsl_agreement_pct,
                "mcc": mcc_naive_no_fsl,
                "description": "Number, percentage, and MCC for 'naive no fsl correctness' agreement with 'original correctness'."
            },
            "annotated_correctness_simple": {
                "count": correct_annotated_simple_agreement,
                "percentage": correct_annotated_simple_agreement_pct,
                "mcc": mcc_correctness_annotated_simple,
                "description": "Number, percentage, and MCC for 'annotated correctness' agreement with 'original correctness'."
            }
        },
        "false_positives": {
            "naive_correctness": {
                "count": fp_naive,
                "description": "Number of cases where 'original correctness' is True but 'naive correctness' is False."
            },
            "correctness": {
                "count": fp_correctness,
                "description": "Number of cases where 'original correctness' is True but 'Correctness' is False."
            }
        },
        "false_negatives": {
            "naive_correctness": {
                "count": fn_naive,
                "description": "Number of cases where 'original correctness' is False but 'naive correctness' is True."
            },
            "correctness": {
                "count": fn_correctness,
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

    print("Analysis Report")
    print(json.dumps(analysis_report, indent=4))

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
