from collections import deque

def sol():
    n = int(input())

    rad = []
    cn = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        cn.append((x, y))
        rad.append(r)

    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            dx = cn[i][0] - cn[j][0]
            dy = cn[i][1] - cn[j][1]
            dt = dx * dx + dy * dy
            dr = rad[i] + rad[j]
            if dr * dr == dt:
                g[i].append(j)
                g[j].append(i)

    vis = [False] * n

    for i in range(n):
        if vis[i]:
            continue

        vis[i] = True
        q = deque([(i, 0)])
        od, ev = set(), set()
        ev.add(i)
        pos = True

        while q and pos:
            c, p = q.popleft()
            p = 1 - p
            for ch in g[c]:
                if vis[ch]:
                    if p:
                        if ch in ev:
                            pos = False
                    else:
                        if ch in od:
                            pos = False
                    continue
                vis[ch] = True
                if p:
                    od.add(ch)
                else:
                    ev.add(ch)
                q.append((ch, p))

        if pos:
            if len(od) != len(ev):
                print("YES")
                return

    print("NO")

sol()
