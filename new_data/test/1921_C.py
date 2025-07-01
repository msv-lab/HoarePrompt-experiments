n = int(input())
listt = []
arr = []
for i in range(n):
    x = list(map(int, input().split()))
    listt.append(x)

    arr.append(list(map(int, input().split())))

for i in range(n):

    a = listt[i][2]
    b = listt[i][3]
    newarr = arr[i]
    newarr.sort()
    charge = listt[i][1]

    charge = charge - min(newarr[0], b)

    for i in range(1, len(newarr)):
        charge = charge - min((newarr[i] - newarr[i - 1]) * a, b)

    if charge <= 0:
        print('NO')
    else:
        print('YES')