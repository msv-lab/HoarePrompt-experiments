import math
from collections import defaultdict


def find_trailing_zeros(n):
    count = 0
    while n and not n % 10:
        count += 1
        n //= 10
    return count


def func(b, a):
    n, m = b

    tot_digs = 0

    t_zeros = [0 for i in range(10)]

    for i in a:
        tot_digs += int(math.log(i, 10)) + 1
        t_zeros[find_trailing_zeros(i)] += 1

    # print(tot_digs)
    # print(t_zeros)

    f = 1

    for i in range(9, 0, -1):
        if t_zeros[i] <= 0:
            continue
        if f == 1:
            tot_digs -= (math.ceil(t_zeros[i] / 2) * i)
            if t_zeros[i] % 2 == 1:
                f = f * (-1)
        else:
            tot_digs -= (math.floor(t_zeros[i] / 2) * i)
            if t_zeros[i] % 2 == 1:
                f = f * (-1)

    # print(tot_digs,m)

    if tot_digs >= (m + 1):
        return ("Sasha")
    else:
        return ("Anna")


q = int(input())
for i in range(q):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(func(a, b))