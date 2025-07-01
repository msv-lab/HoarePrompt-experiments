import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    x=a.count('1')
    # print(x)
    if not x&1 or x==0:
        print("Yes")
    else:
        print("No")

