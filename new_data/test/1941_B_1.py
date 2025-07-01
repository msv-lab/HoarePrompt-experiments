t = int(input())
for i in range(t):
    n = int(input())
    l = [int(i) for i in input().split()]
    l.reverse()
    for j in range(200):
        m = max(l)
        ix = l.index(m)
        if (ix != 0 and ix < n - 1):
            l[ix - 1] = l[ix - 1] - 1
            l[ix + 1] = l[ix + 1] - 1
            l[ix] = l[ix] - 2
    if (l.count(0) == n):
        print("YES")
    else:
        print("NO")

