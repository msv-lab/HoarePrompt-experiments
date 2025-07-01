def problem():
    t = int(input())
    numbers = []

    for _ in range(t):
        n = int(input())
        numbers.append(n)

    max_value = max(numbers) + 1
    sum_values = [0 for _ in range(max_value)]

    for i in range(1, n + 1):
        sum_values[i] = digits_sum(i) + sum_values[i - 1]

    for n in numbers:
        print(sum_values[n])


def digits_sum(n):
    sum_t = 0
    for digit in str(n):
        sum_t += int(digit)
    return sum_t


problem()

