def max_sum(a):
    max_current = a[0]
    max_possible = 0
    s = 0

    for i in range(1, len(a)):
        s += a[i]
        max_possible = max_possible + a[i]

        if (max_current < max_possible):
            max_current = max_possible

        if max_possible < 0:
            max_possible = 0

    return max_current, s


for t in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = []

    for x in input().split():
        x = int(x)
        a.append(x)

    a.insert(0, 0)

    m, s = max_sum(a)
    y = 10 ** 9 + 7

    v = s + (-m * (1 - 2 ** k))
    v = (v % y) if v >= 0 else y - (abs(v) % y)

    print(v)





