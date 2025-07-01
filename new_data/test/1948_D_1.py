t = int(input())

for i in range(t):
    s = input().strip()
    n = len(s)
    for j in range(n // 2, 0, -1):
        count = 0
        for k in range(0, n - j):
            if s[k] == '?' or s[k + j] == '?' or s[k] == s[k + j]:
                count += 1
            else:
                count = 0
            if count == j:
                break
        if count == j:
            break

    print(count * 2)
