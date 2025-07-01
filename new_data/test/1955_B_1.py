# cook your dish here
for t in range(int(input())):
    n,c,d=map(int,input().split())
    s=list(map(int,input().split()))
    poop=sum(s)
    a=min(s)
    z=int(a*n**2+(n*n*(n-1)*c)/2+(n*n*(n-1)*d)/2)
    print('yes' if poop==z else 'no')