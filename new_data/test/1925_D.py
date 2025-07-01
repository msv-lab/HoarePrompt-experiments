mod = 1000000007

def inv(a):
    if a <= 1:
        return a
    return mod - (mod // a) * inv(mod % a) % mod

def main():
    tes = int(input())
    for fuck in range(1, tes + 1):
        n, m, k = map(int, input().split())
        sum_val = 0
        ans = 0
        for _ in range(m):
            a, b, c = map(int, input().split())
            sum_val += c
        N = inv((n * (n - 1)) // 2)
        for i in range(k):
            ans += (i * m * N * N + sum_val * N) % mod
        print(ans % mod)

if __name__ == "__main__":
    main()
