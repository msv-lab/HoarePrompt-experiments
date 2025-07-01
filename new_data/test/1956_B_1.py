t=int(input(""))
for _ in range(t):
    n=input("")
    ans=0
    x=list(map(int,input("").split()))
    for y in x:
        x.remove(y)
        if y in x:
            ans+=1
            x.remove(y)
    print(ans)
