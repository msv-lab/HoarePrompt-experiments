import math

t = int(input())
for _ in range(t):
    a, b, m = map(int, input().split())
    print(math.floor(m / a) + math.floor(m / b) + 2)