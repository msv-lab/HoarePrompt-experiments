import time
from collections import defaultdict


def h(x):
    x += int(time.time())
    x += 0x9e3779b97f4a7c15
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb
    return x ^ (x >> 31)


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_map = defaultdict(int)
    b_map = defaultdict(int)
    for x in b:
        b_map[h(x)] += 1

    good = 0
    count = 0
    for i in range(n):
        if i >= m:
            a_map[h(a[i - m])] -= 1
            if a_map.get(h(a[i - m]), 0) < b_map.get(h(a[i - m]), 0):
                count -= 1
        if a_map.get(h(a[i]), 0) < b_map.get(h(a[i]), 0):
            count += 1
        a_map[h(a[i])] += 1
        if i >= m - 1 and count >= k:
            good += 1

    print(good)
