# python3

from sys import stdin
import copy
# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if not v:
    return
  v.sum = v.key + (v.left.sum if v.left else 0) + (v.right.sum if v.right else 0)
  if v.left:
    v.left.parent = v
  if v.right:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if not parent:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent:
    if grandparent.left == parent:
      grandparent.left = v
    else:
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  else:
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if not v:
    return None
  while v.parent:
    if not v.parent.parent:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
  v = root
  last = root
  next = None
  while v:
    if v.key >= key and (not next or v.key < next.key):
      next = v
    last = v
    if v.key == key:
      break
    if v.key < key:
      v = v.right
    else:
      v = v.left
  root = splay(last)
  return next, root

def split(root, key):
  (result, root) = find(root, key)
  if not result:
    return (root, None)
  right = splay(result)
  left = right.left
  right.left = None
  if left:
    left.parent = None
  update(left)
  update(right)
  return left, right


def merge(left, right):
  if not left:
    return right
  if not right:
    return left
  while right.left:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right


# Code that uses splay tree to solve the problem

root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if not right or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
  root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    if not root:
      return
    (left, right) = split(root, x)
    if right and right.key == x:
       right = right.right
       if right:
         right.parent = None
    root = merge(left, right)

def search(x):
    global root
    if not root:
      return False
    (left, right) = split(root, x)
    root = merge(left, right)
    return right.key == x if right else False

def sum(fr, to):
    global root
    if not root:
      return 0
    (left, middle) = split(root, int(fr))
    (middle, right) = split(middle, int(to) + 1)
    ans = middle.sum if middle else 0
    root = merge(left , merge(middle, right))

    return  ans

MODULO = 1000000001

if __name__ == '__main__':
  n = int(stdin.readline())
  last_sum_result = 0
  for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
      x = int(line[1])
      insert((((x + last_sum_result) % MODULO) + MODULO) % MODULO)
    elif line[0] == '-':
      x = int(line[1])
      erase((((x + last_sum_result) % MODULO) + MODULO) % MODULO)
    elif line[0] == '?':
      x = int(line[1])
      print('Found' if search((((x + last_sum_result) % MODULO) + MODULO) % MODULO) else 'Not found')
    elif line[0] == 's':
      l = int(line[1])
      r = int(line[2])
      res = sum(((((l + last_sum_result) % MODULO) + MODULO) % MODULO), ((((r + last_sum_result) % MODULO) + MODULO) % MODULO))
      print(str(res))
      last_sum_result = res % MODULO