from collections import *
from math import log, log2, pow, gcd, ceil, floor
from heapq import *
import sys


def sol():
    N = int(input())
    nums = input().split()

    d = Counter(nums)

    cnt = 0
    ans = 0
    for i in sorted(d):
        v = d.get(i)
        if v == 1:
            cnt += d.get(i)
            continue
        if v == 2:
            ans += cnt
        if v > 2:
            ans += cnt * v * (v - 1) // 2
            ans += v * (v - 1) * (v - 2) // 6
        cnt += d.get(i)

    print(ans)


for _ in range(int(input())):
    sol()