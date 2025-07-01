from collections import defaultdict

t = int(input())
for k in range(t):
    n, x, y = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    D = defaultdict(int)
    answer = 0

    for i in range(n):
        xx = (x - arr[i] % x) % x
        yy = arr[i] % y
        hg = xx * (1e9 + 7) + yy
        hp = arr[i] % x * (1e9 + 7) + arr[i] % y

        answer += D[hg]
        D[hp] += 1

    print(answer)