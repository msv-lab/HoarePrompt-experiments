# Envio realizado con IA para el LLM Feedback

def max_min_pair_score(test_cases):
    results = []
    for n, arr in test_cases:
        arr.sort()
        score = sum(arr[:n])
        results.append(score)
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# Compute and print results
for result in max_min_pair_score(test_cases):
    print(result)
