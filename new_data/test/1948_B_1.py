def lstIn(dataType=int, itType=list):
    return itType(map(dataType, input().split()))


def mapIn(dataType=int):
    return map(dataType, input().split())


def mtrxIn(row, col, dataType=int, itType=list):
    mat = []
    for _ in range(row):
        colo = lstIn(dataType, itType)
        mat.append(colo)
    return mat


def split(arr, dtaType, itType=list):
    temp = str(arr)
    res = [dtaType(i) for i in temp]
    return itType(res)


def solve():
    n = int(input())
    nums = lstIn()

    ans = []

    def merge(left, right):
        if left[-1] > right[0] and left[-1] // 10 > 0:
            sus = str(left.pop())
            left.append(int(sus[0]))
            left.append(int(sus[1:]))

        res = []
        res.extend(left)
        res.extend(right)

        ans.extend(res)
        return res

    def split(l, r, arr):
        if l == r:
            return [arr[l]]

        mid = (l + r) // 2

        left = split(l, mid, arr)
        right = split(mid + 1, r, arr)

        return merge(left, right)

    ans = split(0, n - 1, nums)
    rans = split(0, len(ans) - 1, ans)

    # print(rans)
    if sorted(rans) == rans:
        print("YES")
    else:
        print("NO")


testcase = 1
T = int(input()) if testcase else 1
for _ in range(T):
    solve()