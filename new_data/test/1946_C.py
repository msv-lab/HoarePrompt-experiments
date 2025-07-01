from collections import deque
for _ in range(int(input())):
    n,k=map(int,input().split())
    d=[[] for _ in range(n+1)]
    for i in range(n-1):
        x,y=map(int,input().split())
        d[x].append(y)
        d[y].append(x)
    node=[]
    for i in range(1,n+1):
        if len(d[i])==1:
            node.append(i)
    def fun(mid):
        vis=[-1 for _ in range(n+1)]
        cnt=[1 for _ in range(n+1)]
        attach=[0 for _ in range(n+1)]
        q=deque()
        for j in node:
            vis[j]=1
            q.append(j)
        rem=0
        a=False
        while len(q)!=0:
            x=q.popleft()
            if cnt[x]>=mid :
                rem+=1
                if len(q)==0:
                    a=True
                for o in d[x]:
                    if vis[o]==-1:
                        if len(d[o])==2:
                            vis[o]=1
                            q.append(o)
                        else:
                            if attach[o]==len(d[o])-2:
                                vis[o]=1
                                q.append(o)
                            else:
                                attach[o]+=1
            elif cnt[x]<mid:
                for o in d[x]:
                    if vis[o]==-1:
                        cnt[o]+=cnt[x]
                        if len(d[o])==2:
                            vis[o]=1
                            q.append(o)
                        else:
                            if attach[o]==len(d[o])-2:
                                vis[o]=1
                                q.append(o)
                            else:
                                attach[o]+=1
            if rem==k:
                break
        cnti=0
        maxi=0
        for i in range(1,n):
            if vis[i]==-1:
                cnti+=1
        for i in q:
            cnti+=cnt[i]
        if rem>k:
            return True
        if rem<k:
            return False
        if cnti>=mid:
            return True
        return False
    low=1
    high=n//(k+1)
    while(low<=high):
        mid=(low+high)//2
        if fun(mid):
            low=mid+1
        else:
            high=mid-1
    print(high)