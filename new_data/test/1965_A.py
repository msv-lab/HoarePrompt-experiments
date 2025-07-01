for _ in range(int(input())):
    n=int(input())
    lis=list(map(int,input().split()))
    lis.sort()
    for i in range(n-1,0,-1):
        lis[i]-=lis[i-1]
    s=1
    i=n-1
    while i>=0 and lis[i]==0:
        i-=1
    if i==-1:
        print('Alice')
        continue
    if i==0:
        if lis[0]==1:
            print('Bob')
        else:
            print('Alice')
        continue
    for j in range(i-1,0,-1):
        if lis[j]==0:
            continue
        if lis[j]==1:
            s=1-s
        else:
            continue
    if s==1:
        if lis[0]>1:
            print('Alice')
        else:
            print('Bob')
    else:
        print('Alice')