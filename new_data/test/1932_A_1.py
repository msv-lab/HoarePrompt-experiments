t = int(input())
for tc in range(t):
    n = int(input())
    p =str(input())
    a =[]
    b=[]
    c=[]
    l=[]
    s=[]
    for i in range(n):
        l.append(i)
    for i in range(len(p)):
        if(p[i]=='@'):
            a.append(i)
        if(p[i]=='.'):
            b.append(i)
        if(p[i]=='*'):
            c.append(i)
    # print(a)
    # print(b)
    # print(c)
    for i in l:
        if i not in a:
            s.append(i)
    # print(s)
    # e = set(s)
    # f= set(b)
    o = set(s).intersection(b)
    y = set(s)-o
    f=list(y)
    # print(list(y))
    k=0
    # print(f)
    for i in range(len(f)-1):
        if(f[i]==f[i+1]-1):
            k=f[i]
            break
    v=0
    for i in a:
        if(i<k):
            v=v+1
        if(k==0):
            v=len(a)
    print(v)