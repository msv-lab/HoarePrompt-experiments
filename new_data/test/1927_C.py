mylist = [2,3,2,2,4,1]

t = int(input())
for i in range(t):
    line1 = input().split()
    n = int(line1[0])
    m = int(line1[1])
    k = int(line1[2])
    arraya = input().split()
    arraya = [int(value) for value in arraya]
    arraya = list(set(arraya))
    arrayb = input().split()
    arrayb = [int(value) for value in arrayb]
    arrayb = list(set(arrayb))
    together = list(set(arraya + arrayb))
    if len(together) >= k and together[k-1] == k and len(arraya) >= int(k/2) and arraya[int(k/2)-1] <= k and len(arrayb) >= int(k/2) and arrayb[int(k/2)-1] <= k:
        print("YES")
    else:
        print("NO")