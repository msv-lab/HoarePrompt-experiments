def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    pref = [0] * (n + 1)
    ones = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + arr[i]
        ones[i + 1] = ones[i] + (1 if arr[i] == 1 else 0)

    # print(ones)

    for _ in range(q):
        l, r = map(int, input().split())

        if l == r:
            print("NO")
            continue

        s = pref[r] - pref[l - 1]
        o = ones[r] - ones[l - 1]
        maj = (r - l + 1) // 2

        if s >= 2 * (r - l + 1) - 1 or not (o >= maj + 1):
            print("YES")
        else:
            print("NO")


t = int(input())
for _ in range(t):
    solve()
