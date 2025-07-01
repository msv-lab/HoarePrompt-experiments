a = int(input())
while a != 0:
    a -= 1
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]

    c = 0
    f = 1
    d = 2
    ans = True
    while ans:
        s = 1
        e = (n - s) // d + 1
        # print(f"{s} {e} {f} {d} {c}")
        while s <= e:

            mid = (s + e) // 2
            v = f + (mid - 1) * d
            if c + mid == k:
                print(v)
                ans = False
                break
            elif c + mid > k:
                e = mid - 1
            else:
                s = mid + 1
        c += (n - f) // d + 1
        f *= 2
        d *= 2












