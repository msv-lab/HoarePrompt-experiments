for i in range(int(input())):
    a , b ,c = map(int,input().split())
    leu = a
    dung = True
    while b % 3 != 0:
        b = b + 1
        c = c - 1
        if c == 0 and b % 3 != 0:
            print(-1)
            dung = False
            break
    leu += (b // 3)
    if c % 3 == 0:
        leu += (c // 3)
    else:
        leu += (c // 3 + 1)
    if dung:
        print(leu)