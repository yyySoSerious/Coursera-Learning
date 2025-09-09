#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def is_binary_search_tree_recursive(tree, node_idx, min_val, max_val):
  if node_idx == -1:
    return True

  node = tree[node_idx][0]
  if min_val <= node < max_val:
    left_child_idx = tree[node_idx][1]
    right_child_idx = tree[node_idx][2]
    return (is_binary_search_tree_recursive(tree, left_child_idx, min_val, node) and
            is_binary_search_tree_recursive(tree, right_child_idx, node, max_val))

  return False


def IsBinarySearchTree(tree):
  if not tree:
    return True
  return is_binary_search_tree_recursive(tree, 0, float('-inf'), float('inf'))


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
