num = int(input())
out = []
for x in range(num):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    lo = 0
    hi = n-1
    g = n
    while lo < hi:
        if arr[lo] + arr[hi] == 2**31 - 1:
            g -= 1
            lo += 1
            hi -=1
        elif arr[lo] -1 + arr[hi] <= 2*(2**30-1)+1:
            lo += 1
        else:
            hi -= 1
    out.append(g)
for i in out: print(i)