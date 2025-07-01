t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 0:
        print(n)
    elif k == n:
        print(1)
    elif k == ((n) * (n - 1)) // 2:
        print(1)
    else:
        while k >= n - 1:
            k -= (n - 1)
            n -= 1
        print(n)
