for _ in range(int(input())):
    n, k = map(int, input().split())

    max_edges = (n * (n - 1)) // 2
    x = n - 1
    if k < x:
        print(n)
    elif k == x:
        print(n - 1)
    elif k == max_edges:
        print(1)
    else:
        cnt = 0
        while True:
            if k > x:
                cnt += 1
                k -= n - 1
                x -= 1
            else:break
        print(cnt)