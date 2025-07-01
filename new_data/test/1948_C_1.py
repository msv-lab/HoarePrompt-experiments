def BFS():
    return


def solve(n, row, arr):
    des = (1, n - 1)
    queue = []
    for i in range(len(row)):
        for j in range(len(row[i])):
            if row[i][j] == ">":
                queue.append((i, j))
    ok = [des]
    status = 0
    # print(queue)
    while (ok != []):
        x, y = ok.pop(0)
        # print(x,y)
        if (x, y) == (0, 0) or (x, y) == (1, 2):
            return "YES"
        if (x, y - 1) in queue:
            status = 1
            ok.append((x, y - 1))
        if (x - 1, y) in queue:
            status = 1
            ok.append((x - 1, y))
        if status == 0:
            return "NO"
        # print(ok)
    return "NO"


n = int(input())
for _ in range(n):
    arrow = int(input())
    tam = [[False] * arrow, [False] * arrow]
    row = []
    row.append([i for i in input()])
    row.append([i for i in input()])
    print(solve(arrow, row, tam))
