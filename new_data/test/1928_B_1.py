t=int(input())
k=[]
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    le=0
    ri=0
    ans=1
    pre=1
    l.sort()
    # print(l)
    while le+ans<=n and ri<n:
        # print("hi",le,ri,ans)
        # if ri==n-1:
        #     le+=1
        if le==ri:
            pre=1
            ri+=1
        else:
            check=l[ri]-l[le]
            if check>0 and check<n:
                if l[ri]!=l[ri-1]:
                    pre+=1
                    ans=max(ans,pre)
                    ri+=1
                else:
                    ri+=1
            else:
                le+=1
                pre-=1
    print(ans)