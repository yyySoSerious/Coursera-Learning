# python3

import sys
from collections import namedtuple
import random

Answer = namedtuple('answer_type', 'i j len')


class longest_common_substring_solver:
	_m1 = 1000000007
	_m2 = 1000000009
	def __init__(self, s, t):
		self.s_str_len = len(s)
		self.t_str_len = len(t)
		self.max_length = min(self.s_str_len, self.t_str_len)
		self.hash_table_size = 200007
		self.hash_table_size = 2 * self.max_length
		self._x = random.randint(1, self._m1 - 1)
		self._a = random.randint(1, self._m1 - 1)
		self._b = random.randint(0, self._m1 - 1)
		self.s_hashes1 = self.precompute_hashes(s, self._m1, self._x)
		self.s_hashes2 = self.precompute_hashes(s, self._m2, self._x)
		self.t_hashes1 = self.precompute_hashes(t, self._m1, self._x)
		self.t_hashes2 = self.precompute_hashes(t, self._m2, self._x)
		self.x_powers1 = self._precompute_powers_of_x(self._x, self._m1)
		self.x_powers2 = self._precompute_powers_of_x(self._x, self._m2)

	def precompute_hashes(self, input_str, p, x):
		input_str_len = len(input_str)
		h = [0] * (input_str_len + 1)
		for i in range(1, input_str_len+1):
			h[i] = (h[i-1]*x + ord(input_str[i-1])) % p

		return h

	def _precompute_powers_of_x(self, x, p):
		powers = [1] * (self.max_length + 1)
		for i in range(1, self.max_length + 1):
			powers[i] = (powers[i-1] * x) % p

		return powers

	def get_substring_hash(self, hashes, powers, start_idx, length, p):
		return (hashes[start_idx + length] - (powers[length]*hashes[start_idx]) + p) % p

	def secondary_hash(self, primary_hash):
		return (primary_hash * self._a + self._b) % self._m1

	def has_common_substring_of_length_k(self, length_k):
		if length_k == 0:
			return 0, 0

		num_s_substrings = self.s_str_len - length_k + 1
		num_t_substrings = self.t_str_len - length_k + 1
		s_hash_table = [[] for _ in range(self.hash_table_size)]
		for s_idx in range(num_s_substrings):
			s_sub_hash1 = self.get_substring_hash(self.s_hashes1, self.x_powers1, s_idx, length_k, self._m1)
			s_sub_hash2 = self.get_substring_hash(self.s_hashes2, self.x_powers2, s_idx, length_k, self._m2)

			secondary_hash1 = self.secondary_hash(s_sub_hash1)
			secondary_hash2 = self.secondary_hash(s_sub_hash2)
			bucket_idx = secondary_hash1 % self.hash_table_size

			s_hash_table[bucket_idx].append((secondary_hash1, secondary_hash2, s_idx))
		for t_idx in range(num_t_substrings):
			t_sub_hash1 = self.get_substring_hash(self.t_hashes1, self.x_powers1, t_idx, length_k, self._m1)
			t_sub_hash2 = self.get_substring_hash(self.t_hashes2, self.x_powers2, t_idx, length_k, self._m2)

			t_secondary_hash1 = self.secondary_hash(t_sub_hash1)
			t_secondary_hash2 = self.secondary_hash(t_sub_hash2)
			bucket_idx = t_secondary_hash1 % self.hash_table_size
			for s_secondary_hash1, s_secondary_hash2, s_idx in s_hash_table[bucket_idx]:
				if s_secondary_hash1 == t_secondary_hash1 and s_secondary_hash2 == t_secondary_hash2:
					return s_idx, t_idx

		return -1, -1

	def longest_common_substring(self):
		left, right = 0, self.max_length
		result = Answer(0, 0, 0)
		while left <= right:
			mid = (left + right)//2
			s_idx, t_idx =  self.has_common_substring_of_length_k(mid)
			if s_idx != -1:
				result = Answer(s_idx, t_idx, mid)
				left = mid + 1
			else:
				right = mid - 1

		return result

if __name__ == '__main__':
	for line in sys.stdin.readlines():
		s, t = line.split()
		solver = longest_common_substring_solver(s, t)
		ans = solver.longest_common_substring()
		print(ans.i, ans.j, ans.len)
