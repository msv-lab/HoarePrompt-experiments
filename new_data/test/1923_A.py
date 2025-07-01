tests = int(input())

for _ in range(tests):
    length = int(input())
    strg = input().split()

    moves = 0
    left = 0
    right = length - 1

    while strg[left] == "0":
        left += 1

    while strg[right] == "0":
        right -= 1

    while left <= right:
        if strg[left] == "1":
            left += 1
        else:
            moves += 1
            right -= 1
            left += 1

    print(moves)
