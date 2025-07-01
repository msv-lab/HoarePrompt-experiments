
import sys
from collections import deque

def compute_distances(n, adj):
    # Compute distances from each vertex to all other vertices
    distances = [ [ [] for _ in range(n) ] for _ in range(n) ]
    for u in range(n):
        q = deque()
        q.append(u)
        dist = [ -1 ] * n
        dist[u] = 0
        distances[u][0].append(u)
        while q:
            current = q.popleft()
            for neighbor in adj[current]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[current] + 1
                    if dist[neighbor] < n:
                        distances[u][dist[neighbor]].append(neighbor)
                    q.append(neighbor)
    return distances

def solve_test_case(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    distances = compute_distances(n, adj)
    covered = [ False ] * n
    result = []
    uncovered_count = n
    while uncovered_count > 0:
        max_count = -1
        best_op = (-1, -1)
        for u in range(n):
            for d in range(n):
                if distances[u][d]:
                    count = 0
                    for v in distances[u][d]:
                        if not covered[v]:
                            count += 1
                    if count > max_count:
                        max_count = count
                        best_op = (u, d)
        if max_count > 0:
            u, d = best_op
            result.append( (u + 1, d) )
            for v in distances[u][d]:
                if not covered[v]:
                    covered[v] = True
                    uncovered_count -= 1
        else:
            break
    return len(result), result

def main():
    input = sys.stdin.read().splitlines()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        edges = []
        for _ in range(n-1):
            u, v = map(int, input[idx].split())
            edges.append( (u-1, v-1) )
            idx += 1
        op_count, ops = solve_test_case(n, edges)
        print(op_count)
        for u, d in ops:
            print(u, d)

if __name__ == '__main__':
    main()
