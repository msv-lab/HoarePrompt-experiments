test_cases = int(input())

for _ in range(test_cases):

    v = int(input())

    q = v // 26
    r = v % 26

    a = ""
    for _ in range(3 - q):
        a += chr(97)
        r -= 1

    if r > 0:
        a = a[:-1] + chr(97 + r)

    if q > 0:
        a += 'z' * q

    print(a)