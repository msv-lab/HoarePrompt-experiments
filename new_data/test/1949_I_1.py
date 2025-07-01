def main():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef0 = [None] * n
    coef1 = [None] * n
    nodes = []
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())

    def dfs(i):
        if not visited[i]:
            visited[i] = True
            nodes.append(i)
            for j in range(n):
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                if not visited[j] and (r[i] + r[j]) ** 2 == dx ** 2 + dy ** 2:
                    coef0[j] = r[i] + r[j] - coef0[i]
                    coef1[j] = -coef1[i]
                    dfs(j)

    ok = False
    for i in range(n):
        if not visited[i]:
            coef0[i] = 0
            coef1[i] = 1
            nodes = []
            dfs(i)
            c0 = 0
            c1 = 0
            for j in nodes:
                c0 += coef0[j]
                c1 += coef1[j]
            ok = ok or c1 != 0;
    if ok:
        print("YES")
    else:
        print("NO")

main()
