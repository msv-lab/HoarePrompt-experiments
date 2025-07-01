from sys import stdin, stdout

def solve():
    a,b = map(int, stdin.readline().split())
    if a==b==1: return "NO"
    return "NO" if max(a,b)//2 == min(a,b) and min(a,b)%2==1 else "YES"

t = int(input())
for _ in range(t):
    stdout.write(str(solve())+"\n")
