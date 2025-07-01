def solve(n, a):
    ans = 0
    start = 100000
    end = 100000
    for i in range(n):

        if start > end:
            start, end = end, start
        if a[i] <= start:
            start = a[i]
        elif a[i] <= end:
            end = a[i]
        else:
            ans += 1;start = a[i]
        # print("start = ",start,"and end = ",end, " at i = ",i)
    return ans


t = int(input())
for i in range(t):
    # n,x = map(int,input().split())
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(ans)