from math import *
from collections import *

for _ in range(int(input())):
    n = int(input())
    s = input()
    l = []
    l1 = []
    l2 = []
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if s[i] == '<':
            l1.append(i)
            cnt1 += 1
        else:
            l2.append(i)
            cnt2 += 1
    a = 0
    b = 0
    for j in range(n):
        sec = 0
        p = j
        if s[j] == '<':
            a += 1
        else:
            b += 1
        j_copy = j
        if s[j] == '>':
            c = cnt1 - a
            if c >= j + 1:
                x = a
                for k in range(j + 1):
                    if s[j_copy] != s[j]:
                        sec += 1
                        j_copy -= 1
                        continue
                    sec += 2 * (l1[x] - j_copy) + 1
                    x += 1
                    j_copy -= 1
            else:
                x = a
                for k in range(c + 1):
                    if s[j_copy] != s[j]:
                        sec += 1
                    elif k == c:
                        sec += n - j_copy
                    else:
                        sec += 2 * (l1[x] - j_copy) + 1
                        x += 1
                    j_copy -= 1

        else:
            c = b
            if c >= n - j:
                ind = c - 1
                for k in range(n - j - 1, -1, -1):
                    if s[j_copy] != s[j]:
                        sec += 1
                        j_copy += 1
                        continue
                    sec += 2 * (j_copy - l2[ind]) + 1
                    ind -= 1
                    j_copy += 1

            else:
                ind = c - 1
                for k in range(c + 1):
                    if s[j_copy] != s[j]:
                        sec += 1
                    elif k == c:
                        sec += j_copy + 1
                    else:
                        sec += 2 * (j_copy - l2[ind]) + 1
                        ind -= 1
                    j_copy += 1

        l.append(sec)
    print(*l)









