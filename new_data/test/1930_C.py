from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    mp = defaultdict(int)
    for i in range(n):
        if a[i] + i + 1 in mp:
            ans.append(a[i] + i + 1 - mp[a[i] + i + 1])
            mp[a[i] + i + 1 - mp[a[i] + i + 1]] += 1
        else:
            ans.append(a[i] + i + 1)
            mp[a[i] + i + 1] += 1

    ans.sort(reverse=1)
    print(*ans)
