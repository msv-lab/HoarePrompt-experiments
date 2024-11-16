MOD = 998244353

def contains_at_most_k_unique_digits(n, k):
    return len(set(str(n))) <= k

def sum_of_numbers_with_k_unique_digits(l, r, k):
    total_sum = 0
    for num in range(l, r + 1):
        if contains_at_most_k_unique_digits(num, k):
            total_sum = (total_sum + num) % MOD
    return total_sum

# Read input
l, r, k = map(int, input().split())

# Calculate and print the result
print(sum_of_numbers_with_k_unique_digits(l, r, k))
