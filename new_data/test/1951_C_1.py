from math import ceil
n= int(input())
for i in range(n):
    n,m,k = map(int, input().split())
    a=list(map(int, input().split()))
    if k<=m:
        print(min(a)*k)
    else:
        if k%m==0:
            s=set(sorted(a)[:k//m])
            b=[]
            leng=0
            for i in range(n):
                if a[i] in s and leng<k//m:
                    b.append(a[i])
                    leng+=1
            c=0
            res=0
            for i in range(len(b)):
                res+=(b[i]+c)*m
                c+=m
        else:
            s=set(sorted(a)[:k//m+1])
            b=[]
            leng=0
            for i in range(n):
                if a[i] in s and leng<k//m+1:
                    b.append(a[i])
                    leng+=1
            c=0
            res=0
            mx=max(b)
            cur=0
            for i in range(len(b)):
                if b[i]==mx and cur==0:
                    res+=(b[i]+c)*(k%m)
                    c+=(k%m)
                    cur=1
                else:
                    res+=(b[i]+c)*m
                    c+=m
        print(res)