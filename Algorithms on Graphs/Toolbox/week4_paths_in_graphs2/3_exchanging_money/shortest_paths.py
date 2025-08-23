#Uses python3

import sys
import queue
from collections import deque


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    edges = []
    for u in range(n):
        for v, w in zip(adj[u], cost[u]):
            edges.append((u, v, w))

    distance[s] = 0
    reachable[s] = 1
    q = deque()
    for i in range(n):
        updated = False
        for u, v, w in edges:
            new_dist = distance[u] + w
            if distance[u] != 10**19 and new_dist < distance[v]:
                if i == n-1:
                    q.append(v)
                    continue
                distance[v] = new_dist
                reachable[v] = 1
                updated = True

        if not updated:
            break

    #vertices that can be reached from a negative cycle
    while q:
        u = q.popleft()
        if shortest[u]:
            shortest[u] = 0
            for v in adj[u]:
                if shortest[v]:
                    q.append(v)

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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

