#Uses python3

import sys


def acyclic2(adj):
    n = len(adj)
    visited = [0] * n 

    for start in range(n):
        if visited[start] != 0:
            continue
        stack = [(start, 0)]
        visited[start] = 1

        while stack:
            v, i = stack[-1]
            if i < len(adj[v]):
                u = adj[v][i]
                stack[-1] = (v, i + 1)
                if visited[u] == 1:
                    return 1
                if visited[u] == 0:
                    visited[u] = 1
                    stack.append((u, 0))
            else:
                visited[v] = 2
                stack.pop()

    return 0

def acyclic(adj):
    n = len(adj)
    visited = [0] * n
    for start in range(n):
        if visited[start] == 0:
            stack = [start]
            visited[start] = 1
            while stack:
                v = stack[-1]
                print(f'visited: {v+1}')
                for neigh in adj[v]:
                    if visited[neigh] == 1:
                        return 1
                    if visited[neigh] == 0:
                        visited[neigh] = 1
                        stack.append(neigh)
                if v == stack[-1]:
                    visited[v] = 2
                    stack.pop()

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
