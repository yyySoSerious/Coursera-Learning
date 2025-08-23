import unittest
from organizing_lottery import points_cover, points_cover_naive
from random import randint

class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),

        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        for n in (10, 100):
            for max_value in (1, 2, 10, 10 ** 5):
                points = [randint(0, max_value) for _ in range(n)]
                starts = [randint(0, 30) for _ in range(n)]
                ends =  [randint(30, 50) for _ in range(n)]
                self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                                 points_cover_naive(starts, ends, points),
                                 f'points:{points}, starts:{starts}, ends:{ends}')

    def test_large(self):
        pass


if __name__ == '__main__':
    unittest.main()
