#Uses python3
import sys
import math
import heapq

def clustering(x, y, k):
    n = len(x)
    edges = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            length = math.hypot(x[i] - x[j], y[i] - y[j])
            edges[i].append((j, length))

    inf = float('inf')
    dist = [inf] * n
    dist[0] = 0
    q = [(0, 0)]
    lengths = []
    done = [False] *  n
    while q:
        u_length, u = heapq.heappop(q)
        if done[u]:
            continue
        done[u] = True
        if u_length > 0:
            lengths.append(u_length)
        for v, length in edges[u]:
            if not done[v] and length < dist[v]:
                dist[v] = length
                heapq.heappush(q, (length, v))

    lengths = sorted(lengths)

    return lengths[n-k]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
