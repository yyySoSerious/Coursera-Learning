#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj, order, visited, v):
    visited[v] = 1
    for w in adj[v]:
        if visited[w] == 0:
            dfs(adj, order, visited, w)
    order.append(v)

def number_of_strongly_connected_components(adj):
    n = len(adj)

    #build reverse graph
    rev_adj = [[] for _ in range(n)]
    for v, neighbors in enumerate(adj):
        for w in neighbors:
            rev_adj[w].append(v)

    #sort vertices in the reverse graph by their reverse post-order
    visited = [0] * n
    order = []
    for v in range(n):
        if visited[v] == 0:
            dfs(rev_adj, order, visited, v)
    order.reverse()

    #count number of sccs starting from a sink scc
    visited = [0] * n
    count = 0
    for v in order:
        if visited[v] == 0:
            dfs(adj, [], visited, v)
            count += 1

    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
