cases = int(input())
for i in range(cases):
    length = int(input())
    array = [int(n) for n in input().split()]
    maxN = 0
    minN = 9999
    for i in array:
        if i > maxN:
            maxN = i
        if i < minN:
            minN = i
    print(maxN-minN)