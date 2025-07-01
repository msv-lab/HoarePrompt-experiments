import collections
from collections import Counter
from collections import defaultdict
import math
from math import log

def solve():
    n,k=map(int, input().split())
    s='abcdefghijklmnopqrstuvw'
    return s[:k]*(n)
t = int(input())
for i in range(t):
    res = solve()
    print(res)


