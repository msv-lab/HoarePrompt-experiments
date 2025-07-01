def problem():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        numbers.append(n)

    values = [0 for _ in range(max(numbers + [10]) + 1)]
    sum_values = [0 for _ in range(max(numbers + [10]) + 1)]

    total = 0
    for i in range(10):
        values[i] = i
        total += i
        sum_values[i] = total

    for i in range(10, n + 1):
        word = str(i)
        last = int(word[len(word) - 1])
        remainder = int(word[:-1])
        values[i] = values[last] + values[remainder]
        sum_total = values[i] + sum_values[i - 1]
        sum_values[i] = sum_total

    for n in numbers:
        print(sum_values[n])


problem()

