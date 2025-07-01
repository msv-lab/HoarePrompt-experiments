u = int(input())
for _ in range(u):
    n1 = list(map(int, input().split()))
    l = list(map(int, input().split()))
    m=l.copy()
    n=n1[0]
    c=n1[1]
    d=n1[2]
    i=min(l)
    a=0
    if n>400:
        print('YES')
    else:
        while a<n:
            b=0
            while b<n:
                try:
                    i=min(m)+(a*c+b*d)
                    l.remove(i)
                    b+=1
                except ValueError:
                    a=n
                    break
            a+=1
        if l==[]:
            print('YES')
        else:
            print('NO')