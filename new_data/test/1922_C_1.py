def pas(direction, a):
    prev = 1e9
    sm = 0
    for i in range(n - 1):
        a_cur = a[i]
        a_next = a[i + 1]
        d = abs(a_cur - a_next)
        if d < prev:
            sm += 1
        else:
            sm += d
        direction[i + 1] = sm
        prev = d


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    forward = [0 for i in range(n)]
    back = [0 for i in range(n)]
    # forward pass
    pas(forward, a)
    # backward pass
    a = list(reversed(a))
    pas(back, a)
    back = list(reversed(back))

    m = int(input())
    anses = []
    for _ in range(m):
        q = list(map(int, input().split()))
        s = q[0] - 1
        e = q[1] - 1
        if e > s:
            ans = forward[e] - forward[s]
        else:
            ans = back[e] - back[s]
        anses.append(ans)
    for ans in anses:
        print(ans)
