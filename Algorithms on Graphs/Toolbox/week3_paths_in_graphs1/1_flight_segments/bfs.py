#Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    if s == t:
        return 0
    n = len(adj)
    inf = float('inf')
    dist = [inf] * n
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        d_v = dist[v]
        for w in adj[v]:
            if w == t:
                return d_v + 1
            if dist[w] == inf:
                q.append(w)
                dist[w] = d_v + 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
