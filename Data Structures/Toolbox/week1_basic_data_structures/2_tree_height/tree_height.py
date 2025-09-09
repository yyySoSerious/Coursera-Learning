# python3

import sys
import threading
from collections import deque


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def compute_height_recursive(tree, curr_node):
    if curr_node not in tree:
        return 1
    max_height = float("-inf")
    for node in tree[curr_node]:
        max_height = max(max_height, 1 + compute_height_recursive(tree, node))

    return max_height

def compute_height_fast(n, parents):
    tree = {}# {i:[] for i in range(n)}
    root = -1
    for i, node in enumerate(parents):
        if node == -1:
            root = i
        else:
            tree[node]= tree.get(node, []) + [i]
    return compute_height_recursive(tree, root)

def compute_height_faster(n, parents):
    if n == 0:
        return 0

    tree = {i:[] for i in range(n)}
    root = -1
    for i in range(n):
        node = parents[i]
        if node == -1:
            root = i
        else:
            tree[node] += [i]

    queue = deque([(root, 1)])
    max_height = 0
    while queue:
        node, height = queue.popleft()
        max_height = max(max_height, height)
        for child_node in tree[node]:
            queue.append((child_node, height + 1))

    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_faster(n, parents))

if __name__ == "__main__":
    main()
# In Python, the default limit on recursion depth is rather low,
# # so raise it here for this problem. Note that to take advantage
# # of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
