def dir(a,x):
    distL = 1e9 if x == 0 else a[x] - a[x - 1]
    distR = 1e9 if x + 1 == len(a) else a[x + 1]-a[x]
    if distL < distR:
        return 'L'
    if distL > distR:
        return 'R'

def solve():
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int, input().split()))
        l=[0]*n
        r=[0]*n
        for i in range(1,n):
            r[i] = r[i-1] + (1 if dir(a,i-1)=='R' else a[i]-a[i-1])
        for i in range(n-2,-1,-1):
            l[i] = l[i + 1] + (1 if dir(a, i + 1)=='L' else a[i+1]-a[i])
        m=int(input())
        for _ in range(m):
            x, y=map(int, input().split())
            x, y=x-1,y-1
            if x<y:
                print(r[y]-r[x])
            else:
                print(l[y]-l[x])
solve()