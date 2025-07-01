import math

T = int(input())
s = []
p = []
facs = []


def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def find_inverse_element(a, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        return None  # обратный элемент не существует
    return (x % m + m) % m


def division_mod_p(dividend, divisor, prime):
    # Находим обратный элемент по модулю prime
    inv_divisor = find_inverse_element(divisor, prime)

    # Выполняем целочисленное деление с остатком по модулю prime
    return (dividend * inv_divisor) % prime


def fact(n):
    global facs
    if n == 0:
        return 1
    return facs[n]


def c_n_k(k, n):
    return (math.factorial(n) // math.factorial(k) // math.factorial(n - k)) % 1000000007


def loc(num, n):
    global p
    if num == -1:
        return 1
    pos = p[num]
    return ((c_n_k(n - pos - 1, n - 1) * fact(n - pos - 1) % 1000000007) * loc(num - 1, pos)) % 1000000007


for t in range(T):
    n, m1, m2 = map(int, input().split())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))
    facs = [1]
    for i in range(1, n + 1):
        facs.append((facs[-1] * i) % 1000000007)
    if p[-1] != s[0]:
        print(0)
        continue
    for i in range(m1):
        p[i] -= 1
    for i in range(m2):
        s[i] -= 1
    res = c_n_k(p[-1], n - 1) * loc(m1 - 2, p[-1])
    res = res % 1000000007
    p = [n - 1 - i for i in s]
    p = p[::-1]
    res *= loc(m2 - 2, p[-1])
    res = res % 1000000007
    print(res)





