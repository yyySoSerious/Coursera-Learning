#Uses python3

import sys


def negative_cycle(adj, cost):
    n = len(adj)
    edges = []
    for u in range(n):
        for v, w in zip(adj[u], cost[u]):
            edges.append((u, v, w))

    inf = float('inf')
    dist = [inf] * n
    def has_negative_cycle():
        for i in range(n):
            updated = False
            for u, v, w in edges:
                new_dist = dist[u] + w
                if new_dist < dist[v]:
                    if i == n - 1:
                        return 1
                    dist[v] = new_dist
                    updated = True

            if not updated:
                break
        return 0

    for start in range(n):
        if dist[start] == inf:
            dist[start] = 0
            if has_negative_cycle():
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
