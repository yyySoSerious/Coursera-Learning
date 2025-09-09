# python3

import sys

class Vertex:
	def __init__(self, index, chr, size, left, right, parent):
		self.index, self.chr, self.size, self.left, self.right, self.parent = index, chr, size, left, right, parent

	def update(self):
		self.size = 1
		if self.left:
			self.left.parent = self
			self.size += self.left.size
		if self.right:
			self.right.parent = self
			self.size += self.right.size

class Rope:
	def __init__(self, s):
		self.s = s
		self.root = None
		self._createTree(self.s)

	def _small_rotation(self, v):
		if not v:
			return
		parent = v.parent
		if parent:
			grand_parent = parent.parent
			if v.parent.right == v: #left rotate
				m = v.left
				v.left = parent
				parent.right = m
			else: #right rotate
				m = v.right
				v.right = parent
				parent.left = m
			v.parent = grand_parent
			parent.update()
			v.update()
			if grand_parent:
				if grand_parent.left == parent:
					grand_parent.left = v
				else:
					grand_parent.right = v

	def _bigRotation(self, v):
		if not v or not v.parent:
			return None
		if not v.parent.parent: #zig
			self._small_rotation(v)
		else:
			parent = v.parent
			grand_parent = v.parent.parent
			if ((parent.left == v and grand_parent.left == parent) or
				(parent.right == v and grand_parent.right == parent)): #zig zig
				self._small_rotation(parent)
				self._small_rotation(v)
			else: #zig zag
				self._small_rotation(v)
				self._small_rotation(v)

		return v

	def _splay(self, v):
		if not v:
			return None
		while v.parent:
			if v.parent.parent: #zig zig or zig zag
				self._bigRotation(v)
			else: #zig
				self._small_rotation(v)
		return v

	def _find(self, root:Vertex, index):
		last, next = None, None
		curr_vertex = root
		while curr_vertex:
			last = curr_vertex
			if curr_vertex.index >= index and (not next or curr_vertex.index < next.index):
				next = curr_vertex
			if curr_vertex.index == index:
				break
			elif curr_vertex.index > index:
				if curr_vertex.left:
					new_index = curr_vertex.index - 1
					if curr_vertex.left.right:
						new_index -= curr_vertex.left.right.size
					curr_vertex.left.index = new_index
				curr_vertex = curr_vertex.left
			else:
				if curr_vertex.right:
					new_index = curr_vertex.index + 1
					if curr_vertex.right.left:
						new_index += curr_vertex.right.left.size
					curr_vertex.right.index = new_index
				curr_vertex = curr_vertex.right

		new_root = self._splay(last)
		return next, new_root

	def _split(self, root:Vertex, index):
		found_vertex, new_root = self._find(root, index)
		if not found_vertex:
			return new_root, None

		right = self._splay(found_vertex)
		left = right.left
		right.left = None
		if left:
			left.parent = None
		right.index = 1
		right.update()

		return left, right

	def _merge(self, left:Vertex, right:Vertex):
		if not left:
			return right
		if not right:
			return left
		index = left.size
		largest_vertex, new_root = self._find(left, index)
		#right.index = (right.left.size if right.left else 0) + index + 1 #can comment out
		new_root.right = right
		new_root.update()

		return new_root

	def _insert(self, chr, idx):
		left, right = self._split(self.root, idx)
		new_vertex = None
		if not right or right.index != idx:
			new_vertex = Vertex(idx, chr, 1, None, None, None)
		self.root = self._merge(left, self._merge(new_vertex, right))

	def _createTree(self, s):
		str_len = len(s)
		for i in range(str_len):
			self._insert(s[i], i+1)

	def _cut_substring(self, root, i, j):
		left, middle = self._split(root, i + 1)
		middle, right = self._split(middle, j-i + 2)
		leftover  = self._merge(left, right)
		return middle, leftover

	def inOrder(self, v):
		self.s = ""
		result = []
		verbose = []
		stack = []
		while stack or v:
			while v:
				stack.append(v)
				v = v.left

			v = stack.pop()
			result.append(v.chr)
			verbose.append((v.chr, v.index, "root" if not v.parent else "none-root",
			             ("left: " + v.left.chr if v.left else None),
			             ("right: " + v.right.chr) if v.right else None))
			v = v.right

		return result, verbose

	def _print_tree(self, root):
		print(self.inOrder(root)[1])

	def result(self):
		self.s = ''.join(self.inOrder(self.root)[0])
		return self.s

	def process(self, i, j, k):
		removed_substring, leftover_substring = self._cut_substring(self.root, i, j)
		prefix = None
		if k > 0:
			prefix, leftover_substring = self._cut_substring(leftover_substring, 0, k - 1)
		self.root = self._merge(self._merge(prefix, removed_substring), leftover_substring)
                

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
