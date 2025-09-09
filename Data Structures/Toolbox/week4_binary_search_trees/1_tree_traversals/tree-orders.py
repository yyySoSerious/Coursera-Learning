# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def __init__(self):
      self.result = None

  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
      result = []
      stack = []
      current_index = 0

      while stack or current_index != -1:
          while current_index != -1:
              stack.append(current_index)
              current_index = self.left[current_index]

          current_index = stack.pop()
          result.append(self.key[current_index])

          current_index = self.right[current_index]

      return result

  def preOrder(self):
      result = []
      stack = []
      current_index = 0

      while stack or current_index != -1:
          while current_index != -1:
              result.append(self.key[current_index])
              stack.append(current_index)
              current_index = self.left[current_index]

          current_index = stack.pop()
          current_index = self.right[current_index]

      return result

  def postOrder(self):
      result = []
      stack = []
      current_index = 0  # Start with the root node
      last_visited_index = None

      while stack or current_index != -1:
          while current_index != -1:
              stack.append(current_index)
              current_index = self.left[current_index]

          current_index = stack[-1]

          if self.right[current_index] == -1 or  self.right[current_index] == last_visited_index:
              result.append(self.key[current_index])
              last_visited_index = stack.pop()
              current_index = -1
          else:
              current_index = self.right[current_index]


      return result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
