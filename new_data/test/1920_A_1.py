def solve():
    n=int(input())
    a=1e9;b=0;c=[]
    for i in range (n):
        s=input()
        if s[0]=="2" :
            a=min(a,int(s[2:]))
        elif s[0]=="1":
            b=max(b,int(s[2:]))
        else :
            c.append(int(s[2:]))
    r=a-b+1
    for i in c :
        if b<=i<=a :
            r-=1
    print(max(r,0))
for test in range(int(input())):
    solve()