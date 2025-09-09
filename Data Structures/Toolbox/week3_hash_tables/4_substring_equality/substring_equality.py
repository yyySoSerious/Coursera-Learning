# python3

import sys
import random


class Solver:
	def __init__(self, s):
		self.s = s
		self.m1 = 10 ** 9 + 7
		self.m2 = 10 ** 9 + 9
		self.x = random.randint(1, self.m1-1)
		self.y1_powers = self.precompute_y_powers(self.x, self.m1)
		self.y2_powers = self.precompute_y_powers(self.x, self.m2)
		self.h1 = self.precompute_hashes(self.s, self.m1, self.x)
		self.h2 = self.precompute_hashes(self.s, self.m2, self.x)

	def precompute_hashes(self, input_str, p, x):
		str_len = len(input_str)
		h = [0] * (str_len + 1)
		for i in range(1, str_len + 1):
			h[i] = (x * h[i - 1] + ord(input_str[i - 1])) % p

		return h

	def precompute_y_powers(self, x, p):
		y_powers = [1] * (len(self.s) + 1)
		for i in range(1, len(y_powers)):
			y_powers[i] = (y_powers[i-1] * x) % p

		return y_powers

	def ask(self, a, b, l):
		a_hash1 = (self.h1[a + l] - self.y1_powers[l] * self.h1[a] + self.m1) % self.m1
		b_hash1 = (self.h1[b + l] - self.y1_powers[l] * self.h1[b] + self.m1) % self.m1
		a_hash2 = (self.h2[a + l] - self.y2_powers[l] * self.h2[a] + self.m2) % self.m2
		b_hash2 = (self.h2[b + l] - self.y2_powers[l] * self.h2[b] + self.m2) % self.m2

		return a_hash1 == b_hash1 and a_hash2 == b_hash2

if __name__ == '__main__':
	s = sys.stdin.readline()
	q = int(sys.stdin.readline())
	solver = Solver(s)
	for i in range(q):
		a, b, l = map(int, sys.stdin.readline().split())
		print("Yes" if solver.ask(a, b, l) else "No")
