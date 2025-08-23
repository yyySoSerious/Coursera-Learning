#Uses python3
import sys
import math
import heapq

def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)

    return parent[i]

def union(i, j, parent, rank):
    i_id = find(i, parent)
    j_id = find(j, parent)

    if i_id == j_id:
        return False

    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1

    return True

def minimum_distance(x, y):
    result = 0.
    n = len(x)

    parent = [i for i in range(n)]
    rank = [0] * n
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            length = math.hypot(x[i] - x[j], y[i] - y[j])
            edges.append((length, i, j))

    edges = sorted(edges)
    for edge_length, i, j in edges:
        if union(i, j, parent, rank):
            result += edge_length

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
