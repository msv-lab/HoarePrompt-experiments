t = int(input())
for n in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    score = sum(arr[0:n])
    print(score)