for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()));
    L = list(set(L))
    L.sort()
    n = len(L)
    ans = 0
    for i in range(n):
        j = i + 1
        while j < n:
            if L[j] >= L[i] + N or N - j < ans:
                break
            j += 1
        ans = max(ans, j - i)
    print(ans)

