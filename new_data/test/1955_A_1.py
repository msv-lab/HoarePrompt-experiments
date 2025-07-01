t = int(input())
for i in range(t):
    n,a,b = map(int, input().split())
    if n == a == b:
        print(a)
    elif n < a > b:
        print(a)
    elif a*2 > b:
        o = 0
        k_op = n//2
        o += b
        if n%2 == 0:
            o = o
        else:
            o += a
        print(o)
    else:
        print(n*a)