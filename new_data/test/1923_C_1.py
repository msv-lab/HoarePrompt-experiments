import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

T = int(input())

while T:
    T -= 1
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    numOne = [0]
    pSum = [0]

    for el in arr:
        numOne.append(numOne[-1] + (el == 1))
        pSum.append(pSum[-1] + el)

    while q:
        q -= 1
        l, r = map(int, input().split())
        if l == r:
            print("NO")
            continue
        o = numOne[r] - numOne[l - 1]
        s = pSum[r] - pSum[l - 1]
        n_nums = r - l + 1
        stand = (n_nums + 1) // 2 * 2 + (n_nums - (n_nums + 1) // 2)

        if stand < s:
            print("YES")
            continue

        if stand == s and (n_nums == 3 or o <= (n_nums + 1) // 2):
            print("YES")
            continue

        print("NO")
