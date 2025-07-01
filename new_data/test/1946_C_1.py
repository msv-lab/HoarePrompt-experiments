def load_data():
    with open('problem_4/1.in') as f:
        t = int(f.readline().strip())
        n, k = map(int, f.readline().strip().split())
        edges = []
        for i in range(n - 1):
            u, v = map(int, f.readline().strip().split())
            edges.append((u, v))
    return t, n, k, edges


def check(tree, mid, node, visited):
    # count: 能额外切分出几个子树，remain: 切分后连到父节点还剩多少节点
    remain, count = 1, 0
    for v in tree[node]:
        if v not in visited:
            visited.add(v)
            _remain, _count = check(tree, mid, v, visited)
            if _remain >= mid:
                count += 1
            else:
                remain += _remain
            count += _count
    return remain, count


def main():
    # t, n, k, edges = load_data()
    t = int(input())
    for _ in range(t):
        try:
            n, k = map(int, input().strip().split())
            tree = {i: [] for i in range(1, n + 1)}
            for i in range(n - 1):
                u, v = map(int, input().strip().split())
                # u, v = edges[i]
                tree[u].append(v)
                tree[v].append(u)

            min_, max_ = 1, n // (k + 1) + 1
            while max_ - min_ > 1:
                mid = (min_ + max_) // 2
                visited = {n // 2, }
                remain, count = check(tree, mid, n // 2, visited)
                if remain >= mid:
                    count += 1
                if count >= k + 1:
                    min_ = mid
                else:
                    max_ = mid
            print(min_)
        except Exception as e:
            print(e)


main()
