#Uses python3

import sys
import queue
import heapq


def distance(adj, cost, s, t):
    n = len(adj)
    inf = float('inf')
    dist = [inf] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        v_cost, v = heapq.heappop(q)
        if v == t:
            return v_cost
        if v_cost > dist[v]:
            continue
        for w_cost, w in zip(cost[v], adj[v]):
            new_cost = v_cost + w_cost
            if new_cost < dist[w]:
                dist[w] = new_cost
                heapq.heappush(q, (new_cost, w))

    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
