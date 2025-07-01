t=int(input())
for i in range(t):
    n=int(input())
    c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','e','u','w','x','y','z']
    ans=0
    b=[]
    d=[0]*26
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]==0:
            b.append(c[ans])
            d[ans]+=1
            ans+=1
        else:
            for p in range(len(d)):
                if d[p]==a[j]:
                    b.append(c[p])
                    d[p]+=1
                    break
    print(*b,sep='')