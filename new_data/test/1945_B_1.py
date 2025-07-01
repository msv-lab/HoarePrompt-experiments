t=int(input())
A=[]
for i in range(t):
    a,b,m=map(int, input().split())
    sum=2+int(m/a)+int(m/b)
    A.append(sum)
for i in A:
    print(i)