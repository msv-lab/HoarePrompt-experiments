from collections import deque
def solve(arr,n,d):
    q = deque()
    q.append((1,n - 1))
    for i in range(n - 2,-1,-1):
        if q[0][1] == i + d + 2:
            q.popleft()
        cur = arr[i] + q[0][0] + 1
        while len(q) > 0 and cur <= q[-1][0]:
            q.pop()
        q.append((cur,i))
        if i == 0:return cur
for _ in range(int(input())):
    n,m,k,d = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split()])
    ans = [0] * n
    for i in range(n):
        ans[i] = solve(arr[i],m,d)
    cur = 0
    res = int(1e10)
    for i in range(n):
        cur += ans[i]
        if i >= k:
            cur -= ans[i - k]
        if i >= k - 1:
            res = min(res,cur)
    print(res)