import unittest
from tree_height import compute_height_fast, compute_height_faster


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for parents, answer in (
                ([4, -1, 4, 1, 1], 3),
                ([-1, 0, 4, 0, 3], 4)
        ):
            self.assertEqual(compute_height_faster(5, parents), answer, f'text:{parents} answer:{answer}')\


if __name__ == '__main__':
    unittest.main()
