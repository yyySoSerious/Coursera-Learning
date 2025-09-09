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
  v.sum = v.key
  if v.left:
    v.left.parent = v
    v.sum += v.left.sum
  if v.right:
    v.right.parent = v
    v.sum += v.right.sum

def smallRotation(v):
  parent = v.parent
  if not parent:
    return
  grandparent = parent.parent

  if parent.left is v:
    # Right rotation
    parent.left = v.right
    if v.right:
      v.right.parent = parent
    v.right = parent
  else:
    # Left rotation
    parent.right = v.left
    if v.left:
      v.left.parent = parent
    v.left = parent

  parent.parent = v
  v.parent = grandparent

  if grandparent:
    if grandparent.left is parent:
      grandparent.left = v
    else:
      grandparent.right = v

  update(parent)
  update(v)

def bigRotation(v):
  if not v.parent or not v.parent.parent:
    return

  parent = v.parent
  grand = parent.parent

  # Zig-zig
  if (grand.left is parent and parent.left is v) or \
          (grand.right is parent and parent.right is v):
    smallRotation(parent)
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
    else:
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
  v = left
  while v.right:
    v = v.right
  left = splay(v)
  left.right = right
  right.parent = left
  update(left)
  return left


# Code that uses splay tree to solve the problem

root = None

def insert(x):
  global root

  left, right = split(root, x)
  # Avoid inserting duplicate
  if right and right.key == x:
    root = merge(left, right)
    return

  new_vertex = Vertex(x, x, None, None, None)
  new_vertex.left = left
  new_vertex.right = right
  if left:
    left.parent = new_vertex
  if right:
    right.parent = new_vertex
  update(new_vertex)
  root = new_vertex


def erase(x):
    global root
    if not root:
      return

    left, right = split(root, x)
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