for _ in range(int(input())):
    n, k, x = map(int, input().split())
    a = sorted(map(int,input().split()))
    a.reverse()
    p = 0
    prefix = [0]
    for i in range(n):
        p += a[i]
        prefix.append(p)
    m = min([2*prefix[min(i+x,n)] - prefix[i] for i in range(k+1)])
    print(prefix[n] - min(2*10**8 + 1, m))