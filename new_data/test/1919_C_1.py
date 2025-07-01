import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))

    cost = 0
    L = 100000
    H = 100000

    for x in A:
        if x <= L:
            L = x
        elif x <= H:
            H = x
        else:
            cost += 1
            L = H
            H = x

    print(cost)
