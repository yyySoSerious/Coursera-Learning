#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass

def toposort3(adj):
    n = len(adj)
    state = [0] * n
    idx = [0] * n
    order = []
    for start in range(n):
        if state[start] != 0:
            continue
        stack = [start]
        state[start] = 1

        while stack:
            v = stack[-1]
            i = idx[v]
            if i < len(adj[v]):
                u = adj[v][i]
                idx[v] = i + 1
                if state[u] == 1:
                    print("no topo")
                    return []
                if state[u] == 0:
                    state[u] = 1
                    stack.append(u)
            else:
                order.append(v)
                state[v] = 2
                stack.pop()

    order.reverse()
    return order

def toposort(adj):
    n = len(adj)
    used = [0] * n
    order = [0] * n
    curr_idx = n-1
    for start in range(n):
        if not used[start]:
            stack = [start]
            used[start] = 1
            while stack:
                curr_v = stack[-1]
                for neigh in adj[curr_v]:
                    if not used[neigh]:
                        used[neigh] = 1
                        stack.append(neigh)
                        break

                if curr_v == stack[-1]:
                    order[curr_idx] = stack.pop()
                    curr_idx -= 1


    return order

def toposort2(adj):
    n = len(adj)
    visited = [0] * n
    order = []
    for start in range(n):
        if visited[start] == 0:
            stack = [start]
            while stack:
                v = stack[-1] #stack.pop()
                if visited[v] != 1:
                    visited[start] = 1
                    for neigh in adj[v]:
                        if visited[neigh] == 1:
                            print("no topo")
                            return []
                        if visited[neigh] == 0:
                            visited[neigh] = 2
                            stack.append(neigh)
                if v == stack[-1]:
                    order.append(v)
                    visited[v] = 2
                    stack.pop()
    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

