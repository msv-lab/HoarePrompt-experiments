import pandas as pd
import sys
import json
import os
import math

def preprocess_correctness(value, task_id):
    """Normalize correctness values to boolean."""
    normalized_value = str(value).strip().lower()
    if normalized_value in ["correct", "true"]:
        return True
    elif normalized_value in ["incorrect", "false"]:
        return False
    else:
        print(f"Error: Task ID {task_id} has an unrecognized correctness value '{value}'")
        return None

def calculate_mcc(tp, tn, fp, fn):
    """Calculate Matthews correlation coefficient (MCC)."""
    # print(tp, tn, fp, fn)

    numerator = (tp * tn) - (fp * fn)
    # print(numerator)
    denominator = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    # print(denominator)
    res= numerator / denominator if denominator != 0 else 0
    # print(res)
    return res

def calculate_agreement(df, col1, col2):
    """Calculate agreement count and percentage between two columns."""
    agreement_count = (df[col1] == df[col2]).sum()
    total_rows = len(df)
    agreement_pct = (agreement_count / total_rows) * 100 if total_rows > 0 else 0
    return agreement_count, agreement_pct

def calculate_confusion_matrix(df, col1, col2):
    """Calculate TP, TN, FP, FN between two columns."""
    tp = ((df[col1] == True) & (df[col2] == True)).sum()
    tn = ((df[col1] == False) & (df[col2] == False)).sum()
    fp = ((df[col1] == False) & (df[col2] == True)).sum()
    fn = ((df[col1] == True) & (df[col2] == False)).sum()
    return tp, tn, fp, fn

def process_correctness_columns(df, columns):
    """Preprocess correctness-related columns."""
    for col in columns:
        df[col] = df.apply(lambda row: preprocess_correctness(row[col], row['Task ID']), axis=1)
    return df.dropna(subset=columns)

def make_json_serializable(data):
    """Recursively convert data types to Python-native types for JSON serialization."""
    if isinstance(data, dict):
        return {key: make_json_serializable(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [make_json_serializable(item) for item in data]
    elif isinstance(data, (int, float, str, bool)) or data is None:
        return data
    elif pd.isnull(data):  # Handle NaN or None from pandas
        return None
    else:
        return str(data)  # Convert any unsupported types to strings

def calculate_accuracy(tp, tn, fp, fn):
    """
    Calculate accuracy.
    :param tp: True Positives
    :param tn: True Negatives
    :param fp: False Positives
    :param fn: False Negatives
    :return: Accuracy score
    """
    total = tp + tn + fp + fn
    if total == 0:
        return 0  # Avoid division by zero
    return (tp + tn) / total


def calculate_precision(tp, fp):
    """
    Calculate precision.
    :param tp: True Positives
    :param fp: False Positives
    :return: Precision score
    """
    total = tp + fp
    if total == 0:
        return 0  # Avoid division by zero
    return tp / total


def calculate_recall(tp, fn):
    """
    Calculate recall (sensitivity).
    :param tp: True Positives
    :param fn: False Negatives
    :return: Recall score
    """
    total = tp + fn
    if total == 0:
        return 0  # Avoid division by zero
    return tp / total


def calculate_f1_score(tp, fp, fn):
    """
    Calculate F1 score.
    :param tp: True Positives
    :param fp: False Positives
    :param fn: False Negatives
    :return: F1 score
    """
    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)
    if precision + recall == 0:
        return 0  # Avoid division by zero
    return 2 * (precision * recall) / (precision + recall)


def calculate_balanced_accuracy(tp, tn, fp, fn):
    """
    Calculate balanced accuracy.
    :param tp: True Positives
    :param tn: True Negatives
    :param fp: False Positives
    :param fn: False Negatives
    :return: Balanced Accuracy score
    """
    sensitivity = calculate_recall(tp, fn)  # Recall for positive class
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0  # Recall for negative class
    return (sensitivity + specificity) / 2



def analyze_correctness(file_path):
    # Load CSV and preprocess
    df = pd.read_csv(file_path)
    columns_to_preprocess = ['Correctness', 'naive correctness', 'original correctness', 
                             'annotated correctness', 'annotated correctness simple', 
                             'naive no fsl correctness']
    valid_df = process_correctness_columns(df, columns_to_preprocess)
    total_rows = len(valid_df)

    # Initialize result container
    analysis_report = {
        "total_valid_rows": {
            "value": total_rows,
            "description": "Total number of valid rows after preprocessing and removing invalid entries."
        }
    }

    # Agreement analysis
    comparisons = [
        ('Correctness', 'original correctness'),
        ('naive correctness', 'original correctness'),
        ('annotated correctness', 'original correctness'),
        ('annotated correctness simple', 'original correctness'),
        ('naive no fsl correctness', 'original correctness')
    ]
    for col1, col2 in comparisons:
        count, pct = calculate_agreement(valid_df, col1, col2)
        tp, tn, fp, fn = calculate_confusion_matrix(valid_df, col2, col1)
        mcc = calculate_mcc(tp, tn, fp, fn)
        accuracy = calculate_accuracy(tp, tn, fp, fn)
        precision = calculate_precision(tp, fp)
        recall = calculate_recall(tp, fn)
        f1_score = calculate_f1_score(tp, fp, fn)
        balanced_accuracy = calculate_balanced_accuracy(tp, tn, fp, fn)
        analysis_report[col1] = {
            "agreement_count": count,
            "agreement_percentage": pct,
            "mcc": mcc,
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score,
            'balanced_accuracy': balanced_accuracy,
            "description": f"Agreement analysis between '{col1}' and '{col2}'."
        }

    # Naive correctness difference analysis
    naive_diff = valid_df[valid_df['naive correctness'] != valid_df['Correctness']]
    naive_same = valid_df[valid_df['naive correctness'] == valid_df['Correctness']]
    
    analysis_report["naive_correctness_vs_correctness_diff"] = {
        "description": "Analysis of cases where 'naive correctness' and 'Correctness' differ.",
        "count": len(naive_diff),
        "original_agreement_count": (naive_diff['original correctness'] == naive_diff['naive correctness']).sum(),
        "original_agreement_percentage": (
            (naive_diff['original correctness'] == naive_diff['naive correctness']).sum() / len(naive_diff) * 100
            if len(naive_diff) > 0 else 0
        )
    }

    analysis_report["naive_correctness_vs_correctness_same"] = {
        "description": "Analysis of cases where 'naive correctness' and 'Correctness' are the same.",
        "count": len(naive_same),
        "original_agreement_count": (naive_same['original correctness'] == naive_same['Correctness']).sum(),
        "original_disagreement_count": len(naive_same) - (naive_same['original correctness'] == naive_same['Correctness']).sum(),
    }

    # Save analysis report to JSON
    output_file_path = os.path.join(os.path.dirname(file_path), "analysis_report.json")
    # At the end of the analyze_correctness function
    serializable_report = make_json_serializable(analysis_report)
    with open(output_file_path, "w") as json_file:
        json.dump(serializable_report, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_correctness.py <csv_file_path>")
    else:
        file_path = sys.argv[1]
        analyze_correctness(file_path)
