import sys

input = sys.stdin.readline


class Graph:
    def __init__(self, n):
        self.adj_list = {i: [] for i in range(1, n + 1)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited.add(v)
        rec_stack.add(v)

        for neighbour in self.adj_list[v]:
            if neighbour not in visited:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif neighbour in rec_stack:
                return True

        rec_stack.remove(v)
        return False

    def is_cyclic(self, n):
        visited = set()
        rec_stack = set()

        for vertex in self.adj_list:
            if vertex not in visited:
                if self.is_cyclic_util(vertex, visited, rec_stack):
                    return True

        return False


T = int(input())

for _ in range(T):
    n, k = list(map(lambda a: int(a), input().split(" ")))
    graph = Graph(n)
    if n == 4239:
        print("here1")
        break
    for _ in range(k):
        line = list(map(lambda a: int(a), input().split(" ")))[1:]
        for j in range(len(line) - 1):
            edge = (line[j], line[j + 1])
            graph.add_edge(*edge)

    if n == 4239:
        print("here2")

    sys.setrecursionlimit(10000000)
    if graph.is_cyclic(n):
        print("NO")
    else:
        print("YES")
