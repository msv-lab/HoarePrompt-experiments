from collections import defaultdict


def helper(n, x, y, arr):
    hash = defaultdict(list)
    ans = 0
    pairs = set()
    for i in range(0, n):
        ele = arr[i] % x
        if ele in hash:
            for index in hash[ele]:
                # print(i, index)
                pairs.add(str(i) + str(index))
        hash[(x - ele) % x].append(i)

    hash = defaultdict(list)
    # print(pairs)

    for i in range(0, n):
        ele = arr[i] % y
        if ele in hash:
            for index in hash[ele]:
                # print(i, index)
                if str(i) + str(index) in pairs:
                    ans += 1
        hash[(y + ele) % y].append(i)

    return ans


# n = 9
# x = 5
# y = 6
# arr = [10 ,7 ,6 ,7 ,9 ,7 ,7 ,10 ,10]
# print('ans = ', helper(n,x, y, arr))


T = int(input())
for t in range(0, T):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    print(helper(n, x, y, arr))
