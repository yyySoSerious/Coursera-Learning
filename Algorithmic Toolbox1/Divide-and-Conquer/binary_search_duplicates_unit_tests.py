import unittest
from binary_search_duplicates import binary_search_duplicate


class TestBinarySearch(unittest.TestCase):
    def test_small(self):
        for (keys, query, answer) in [
            ([2, 4, 4, 4, 7, 7, 9], 9, 6),
            ([4, 5, 6], 7, -1),
            ([2, 4, 4, 4, 7, 7, 9], 4, 1),
            ([2, 4, 4, 4, 7, 7, 9], 5, -1),
            ([2, 4, 4, 4, 7, 7, 9], 2, 0)

        ]:
            self.assertEqual(
                binary_search_duplicate(keys, query),
                answer,
                f'query:{query}'
            )



if __name__ == '__main__':
    unittest.main()
