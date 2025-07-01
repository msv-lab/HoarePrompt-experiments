import math

t = int(input())

M = 10 ** 9 + 7

for i in range(t):
    n, m, k = map(int, input().split())
    sum_f = 0
    for j in range(m):
        a, b, f = map(int, input().split())
        sum_f += f
    cn2 = n * (n - 1) // 2
    p = 2 * k * cn2 * sum_f + m * k * (k - 1)
    q = 2 * (cn2 ** 2)
    gcd = math.gcd(p, q)
    p = int(p / gcd)
    q = int(q / gcd)
    # print(p, q)
    print(int((p * pow(q, -1, M)) % M))