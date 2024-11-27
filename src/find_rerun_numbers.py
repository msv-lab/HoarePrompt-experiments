import math
from scipy.stats import binom

def calculate_reruns_majority_voting(X, P, C):
    """
    Calculate the number of reruns R needed to achieve a desired confidence level C
    for a dataset of size X, where majority voting is used.

    Parameters:
    X (int): Number of programs in the dataset.
    P (float): Consistency probability (0 < P <= 1).
    C (float): Desired total confidence level (e.g., 0.95 for 95% confidence).

    Returns:
    int: Minimum number of reruns (R).
    """
    # Compute required majority confidence for each program
    target_majority_confidence = C**(1 / X)

    # Increment R until the majority voting confidence meets the target
    R = 1
    while True:
        # Compute probability of majority voting being correct
        majority_threshold = math.ceil(R / 2)
        p_majority = sum(binom.pmf(k, R, P) for k in range(majority_threshold, R + 1))

        if p_majority >= target_majority_confidence:
            return R
        R += 1

def calculate_reruns_aggregate(X, P, C, epsilon):
    """
    Calculate the number of reruns R needed to achieve a given confidence level C.

    Parameters:
    X (int): Number of programs in the dataset.
    P (float): Consistency probability (0 < P <= 1).
    C (float): Confidence level (e.g., 0.95 for 95% confidence).
    epsilon (float): Tolerance for error in the estimation of P.

    Returns:
    float: Number of reruns (R).
    """
    # Critical Z-value for the given confidence level
    Z_values = {
        0.9: 1.645,
        0.95: 1.96,
        0.99: 2.576
    }

    if C not in Z_values:
        raise ValueError("Supported confidence levels are 0.9, 0.95, and 0.99.")

    Z = Z_values[C]

    # Total dataset size required
    N = (Z**2 * P * (1 - P)) / (epsilon**2)

    # Calculate number of reruns
    R = N / X

    return math.ceil(R)  # Return the ceiling to ensure sufficient reruns

# Example usage
if __name__ == "__main__":
    X = 300  # Number of programs in the dataset
    P = 0.9  # Consistency of response
    C = 0.95  # Confidence level (95%)
    epsilon = 0.02  # Margin of error (2%)

    R = calculate_reruns_aggregate(X, P, C, epsilon)
    print(f"Number of reruns needed for aggregate version: {R}")

    R2 = calculate_reruns_majority_voting(X, P, C)
    print(f"Number of reruns needed for majority version: {R2}")