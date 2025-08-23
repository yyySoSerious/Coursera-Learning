#Uses python3

import sys

def reach(adj, x, y):
    if x == y:
        return 1

    visited = [False] * len(adj)
    visited[x] = True

    stack = [x]
    while stack :
        v = stack.pop()
        for neigh in adj[v]:
            if neigh == y:
                return 1
            if not visited[neigh]:
                visited[neigh] = True
                stack.append(neigh)

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
