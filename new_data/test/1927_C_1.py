import collections
from collections import Counter
from collections import defaultdict
import math
from math import log
from math import floor
def med(lst):
    x=sum(lst)
    return x//len(lst)
def solve():
    n,m,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    x=list(set(a+b))
    x1=list(set(a))
    x2=list(set(b))
    test=[i+1 for i in range(k)]
    if x[:k]!=test:
        return 'NO'
    ct,ct1=0,0
    for i in range(len(x1)):
        if x1[i] in test:
            ct+=1
    for i in range(len(x2)):
        if x2[i] in test:
            ct1+=1
    if ct1>=(k//2) and ct>=(k//2):
        return 'YES'
    return 'NO'

t = int(input())
for i in range(t):
    res = solve()
    print(res)
