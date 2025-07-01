# import sys
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
# code starts below
######
######
#####

arr = []
flag = []
ops = []


def main():
    n = int(input())
    for i in input().split():
        arr.append(int(i))
        flag.append(False)

    # mark every element possible for improvement
    for i in range(n):
        for j in range(i, n):
            k = j - i + 1
            if sum(arr[i:j + 1]) < k * k:
                for idx in range(i, j + 1):
                    flag[idx] = True

                # lets get the connected compoenents in array
    on = False
    l, r = -1, -1
    for idx, i in enumerate(flag):
        if not on and i:
            on = True
            l = idx
        if on and not i:
            r = idx - 1
            on = False
            # process l...r
            mex_max(l, r)
            l, r = -1, -1
        # if end with on , process everything left
    if on:
        mex_max(l, n - 1)
    print(sum(arr), len(ops))
    for l, r in ops:
        print(l + 1, r + 1)


def mex_seq(l, r):
    """converts the subarray arr[l:r+1] to 0,1,...k-1"""
    # base case k=1
    k = r - l + 1
    if k == 1:
        if arr[l] != 0:
            ops.append((l, l))
            arr[l] = 0
        return

    # if k >= 2
    mex_max(l + 1, r)
    mex_seq(l, r - 1)


def mex_max(l, r):
    """converts the subarray arr[l:r+1] to k,k,k,.."""

    # base case where k = 1
    k = r - l + 1
    if k == 1:
        mex_seq(l, l)
        mex_op(l, l)
        return

    # if k >= 2
    mex_max(l + 1, r)
    mex_seq(l, r - 1)
    mex_op(l, r)


def mex_op(l, r):
    ops.append((l, r))
    s = set(arr[l:r + 1])
    mex = -1
    for i in range(100):
        if i not in s:
            mex = i
            break

    for i in range(l, r + 1):
        arr[i] = mex
    return arr


if __name__ == '__main__':
    main()