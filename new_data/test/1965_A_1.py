A = int(input())
for t in range(A):
    n = input()
    arr = list(map(int, input().split()))
    arr = [x for x in set(arr)]
    arr.sort()
    ans = 1
    if arr[0] == 1:
        for t in range(1, len(arr)):
            if arr[t] == arr[t - 1] + 1:
                ans += 1
        if ans == len(arr) and len(arr) % 2 == 0:
            print("Bob")
        elif ans == len(arr):
            print("Alice")
        elif ans % 2 == 0:
            print("Alice")
        else:
            print("Bob")
    else:
        print("Alice")
