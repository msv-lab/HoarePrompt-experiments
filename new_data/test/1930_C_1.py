def li(): return [int(i) for i in input().split()]


from collections import defaultdict
from heapq import heapify, heappop, heappush

for x in range(int(input())):
    n, = li()
    a = li()
    ans = [];
    l = sorted([(a[i] + 1 + i, a[i]) for i in range(n)])
    be = l[-1][0] + 1
    l = [(0, 0)] + l
    h = [];
    heapify(h)
    #	print(l)
    for e in l[::-1]:
        e, i = e
        i = e - i
        if e == be:
            heappush(h, -a[i - 1] - 1)
        else:
            d = be - e - 1
            #	print("heap ",h)
            for i in range(1, d + 1):
                if not h: break
                v = be - i
                while h:
                    q = abs(heappop(h))
                    if q <= v: ans += [v];break
            ans += [e]
        be = e
    ans.sort(reverse=1)
    ans.pop()
    print(*ans)


