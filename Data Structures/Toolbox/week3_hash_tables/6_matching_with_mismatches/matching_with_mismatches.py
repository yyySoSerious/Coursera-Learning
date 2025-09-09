# python3

import sys
import random
class MismatchesSolver:
	_m1 = 10**9 + 7
	_m2 = 10**9 + 9
	def __init__(self, k, t, p):
		self._x = random.randint(1, self._m1-1)
		self._k = int(k)
		self._t = t
		self._p = p
		self._t_str_len = len(t)
		self._p_str_len = len(p)
		self._pattern_length = self._p_str_len
		self._t_hashes1 = self._precompute_hashes(t, self._m1)
		self._t_hashes2 = self._precompute_hashes(t, self._m2)
		self._p_hashes1 = self._precompute_hashes(p, self._m1)
		self._p_hashes2 = self._precompute_hashes(p, self._m2)
		self._x_powers1 = self._precompute_powers_of_x(self._m1)
		self._x_powers2 = self._precompute_powers_of_x(self._m2)

	def _precompute_hashes(self, input_str, p):
		str_len = len(input_str)
		h = [0] * (str_len + 1)
		for i in range(1, str_len+1):
			h[i] = (h[i-1] * self._x + ord(input_str[i-1])) % p

		return h

	def _precompute_powers_of_x(self, p):
		powers = [1] * (self._pattern_length + 1)
		for i in range(1, self._pattern_length + 1):
			powers[i] = (powers[i-1] * self._x) % p

		return powers

	def _compute_substring_hash(self, hashes, start_idx, length, x_powers, p):
		return (hashes[start_idx + length] - x_powers[length]*hashes[start_idx] + p) % p

	def _find_first_mismatch(self, t_start_idx, p_start_idx, length):
		if length == 0:
			return -1

		left_offset, right_offset = 0, length -1
		mismatch_offset = -1
		while left_offset <= right_offset:
			mid_offset = (left_offset + right_offset) // 2
			current_length = mid_offset + 1
			t_substring_hash1 = self._compute_substring_hash(self._t_hashes1, t_start_idx, current_length,
															 self._x_powers1, self._m1)
			t_substring_hash2 = self._compute_substring_hash(self._t_hashes2, t_start_idx, current_length,
															 self._x_powers2, self._m2)
			p_substring_hash1 = self._compute_substring_hash(self._p_hashes1, p_start_idx, current_length,
															 self._x_powers1, self._m1)
			p_substring_hash2 = self._compute_substring_hash(self._p_hashes2, p_start_idx, current_length,
															 self._x_powers2, self._m2)
			if t_substring_hash1 == p_substring_hash1 and t_substring_hash2 == p_substring_hash2:
				left_offset = mid_offset + 1
			else:
				mismatch_offset = mid_offset
				right_offset = mid_offset -1

		return mismatch_offset

	def find_at_most_k_mismatches(self):
		result = []
		num_substrings = self._t_str_len - self._p_str_len + 1
		for i in range(num_substrings):
			num_mismatches = 0
			t_start_index = i
			p_start_index = 0
			remaining_length = self._pattern_length
			while num_mismatches <= self._k and remaining_length > 0:
				mismatch_offset = self._find_first_mismatch(t_start_index, p_start_index, remaining_length)
				if mismatch_offset == -1:
					break
				t_start_index += mismatch_offset + 1
				p_start_index += mismatch_offset + 1
				remaining_length -= (mismatch_offset + 1)
				num_mismatches += 1

			if num_mismatches <= self._k:
				result.append(i)

		return result

# 0 ababab baaa
# 1 ababab baaa
# 1 xabcabc ccc
# 2 xabcabc ccc
# 3 aaa xxx
if __name__ == '__main__':
	for line in sys.stdin.readlines():
		k, t, p = line.split()
		solver = MismatchesSolver(k, t, p)
		ans = solver.find_at_most_k_mismatches()
		print(len(ans), *ans)
