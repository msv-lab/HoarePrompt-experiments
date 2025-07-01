t_num = int(input())
r = []

mod = 10 ** 9 + 7


def solve():
    # n, q = list(map(int, input().split()))
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    st = 0
    for i in arr:
        st ^= i

    if st > x:
        return -1

    cx = x
    goal = []
    for i in range(30):
        goal.append(cx & 1)
        cx >>= 1
    goal.reverse()

    use = []
    nst = st
    for i in range(30):
        use.append(st & 1)
        st >>= 1
    use.reverse()

    re = 1

    for i in range(30):
        if use[i] > goal[i]:
            return re

        if use[i] == goal[i] and goal[i]:
            for j in range(n):
                arr[j] |= (1 << (29 - i))
            continue

        if use[i] < goal[i]:
            narr = [j >> (29 - i) for j in arr]
            nx = nst >> (29 - i)
            st = 0
            cur = 0
            for j in narr:
                st ^= j
                if st <= nx:
                    st = 0
                    cur += 1
            re = max(cur, re)

            for j in range(n):
                arr[j] |= (1 << (29 - i))
            nst |= (1 << (29 - i))

    narr = arr
    st = 0
    cur = 0
    for j in narr:
        st ^= j
        if st <= x:
            st = 0
            cur += 1

    re = max(cur, re)

    return re


for _ in range(t_num):
    r.append(solve())

for i in r:
    print(i)