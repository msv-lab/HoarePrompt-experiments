t = int(input())
for _ in range(t):
    L = list(map(int, input().split()))
    M = list(map(int, input().split()))
    n = L[0]
    k = L[1]
    if n == 1:
        if k >= M[0]:
            print(1)
        else:
            print(0)
        continue
    if len(list(set(M))) == 1:
        if k >= M[0] * n:
            print(n)
        else:
            if k >= M[0] * 2:
                a = (k // (M[0] * 2)) * 2
                if k % M[0] != k - 1:
                    print(a)
                else:
                    print(a + 1)
            elif k == M[0] * 2 - 1:
                print(1)
            else:
                print(0)
        continue
    count = 0
    while k > 0 and len(M) > 0:
        if len(M) > 1:
            q = min(M[0], M[-1])
            if 2 * q <= k:
                k -= 2 * q
                if M[0] == M[-1]:
                    count += 2
                else:
                    count += 1
                M[0] -= q
                M[-1] -= q
            elif 2 * q - 1 == k:
                if M[0] <= M[-1]:
                    k -= 2 * q - 1
                    count += 1
                    break
                else:
                    break
            else:
                break
            if M[0] == 0:
                M.pop(0)
            if M[-1] == 0:
                M.pop()
        else:
            if M[0] <= k:
                count += 1
            break
    print(count)
    continue




