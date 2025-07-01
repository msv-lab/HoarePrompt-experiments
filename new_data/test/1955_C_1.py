u = int(input())
for _ in range(u):
    n1 = list(map(int, input().split()))
    l = list(map(int, input().split()))
    n=n1[0]
    k=n1[1]
    if k>sum(l):
        ans=n
    elif n>1000 and l[0]+l[-1]>k:
        ans=0
    else:
        i=1
        while i<=k:
            if i%2==1:
                l[0]=l[0]-1
                if l[0]==0:
                    l.pop(0)
            else:
                l[-1]=l[-1]-1
                if l[-1]==0:
                    l.pop()
            i+=1
        ans=n-len(l)
    print(ans)