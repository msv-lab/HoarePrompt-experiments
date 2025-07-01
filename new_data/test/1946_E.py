t = int(input())
mod = 10 ** 9 + 7


def count(k, m):
    res = 1
    for i in range(k):
        res *= m
        res %= mod
        m -= 1
    return res


def debug(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(args, res)
        return res

    return wrapper


for i in range(t):
    n, m1, m2 = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    if a1[-1] != a2[0]:
        print(0)
        continue


    def dp(i, j):
        # print return value before return
        if i == -1 and j == m2:
            return 1
        if i < 0:
            if j >= m2:
                return 1
            return (count(a2[j] - a2[j - 1] - 1, a1[i + 1] - 1 + (n - a2[j - 1]) - 1) * dp(i, j + 1)) % mod

        if j >= m2:
            if i < 0:
                return 1
            return (count(a1[i + 1] - a1[i] - 1, a1[i + 1] - 1 + (n - a2[j - 1]) - 1) * dp(i - 1, j)) % mod

        return (count(a1[i + 1] - a1[i] - 1, a1[i + 1] - 1 + (n - a2[j - 1]) - 1) * dp(i - 1, j) + count(
            a2[j] - a2[j - 1] - 1, a1[i + 1] - 1 + (n - a2[j - 1]) - 1) * dp(i, j + 1)) % mod


    print(dp(m1 - 2, 1))