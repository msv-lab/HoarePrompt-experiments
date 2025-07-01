t=int(input())

for _ in range(t):
    a=[]
    n=int(input())
    for i in range(n):
        s=str(input())
        if '1' in s:
            a.append(s)
        else:
            pass
    if not a:
        print("SQUARE")
        continue
    a1=a[0]
    a2=a[-1]
    k=len(a)
    is_square=True
    for x in a:
        p=x.count("1")
        if p!=k:
            is_square=False
            break
        q=x.index('1')
        if q!=n-k:
            is_square=False
            break

    if is_square==True:
        print('SQUARE')
    else:
        print('TRIANGLE')
