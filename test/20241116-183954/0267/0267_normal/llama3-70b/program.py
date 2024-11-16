MOD = 998244353
def count_numbers(l, r, k):
    def count(n, k, dp):
        if k == 0:
            return 0
        if (n, k) in dp:
            return dp[(n, k)]
        if n < 10**k:
            dp[(n, k)] = n
        else:
            dp[(n, k)] = 9
            for i in range(1, k):
                dp[(n, k)] += 9 * 10**(i-1) * (10**(k-i) - 10**(i-1))
            dp[(n, k)] += (10**(k-1) - 10**(k-2)) * (n // 10**(k-1) - 1)
            dp[(n, k)] %= MOD
        return dp[(n, k)]

    dp = {}
    return (count(r, k, dp) - count(l-1, k, dp)) % MOD

l, r, k = map(int, input().split())
print(count_numbers(l, r, k))
