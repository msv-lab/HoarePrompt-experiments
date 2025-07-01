import math


def factors(q, x):
    M = []
    w = math.sqrt(q)
    if w == w // 1 and w >= x - 1:
        M += [w]
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if (q // i) >= x - 1:
                M += [q // i]
    return M


t = int(input())
for _ in range(t):
    L = list(map(int, input().split()))
    n = L[0]
    x = L[1]
    ans = 0
    y = (n + x)
    if y % 2 != 0:
        print(0)
        continue
    else:
        L1 = factors((y - 2) // 2, x)
        if n >= 3 * x - 2:
            L1 += factors((n - x) // 2, x)
        L1 = list(set(L1))
        print(len(L1))
        continue









