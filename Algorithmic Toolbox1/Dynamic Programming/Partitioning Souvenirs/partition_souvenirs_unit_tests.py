import unittest
from partition_souvenirs import partition3, partition3_naive, partition3_faster


class PartitionSouvenirs(unittest.TestCase):
    def test_small(self):
        for values in (
            (20,),
            (1, 2, 3),
            (3, 3, 3),
            (3, 3, 3, 3),
            (3, 4, 3, 4, 3, 4),
        ):
            self.assertEqual(partition3_faster(values), partition3_naive(values))

    def test_medium(self):
        for values, answer in (
            ((3, 4, 5, 3, 4, 5, 3, 4, 5), 1),

        ):
            self.assertEqual(partition3_faster(values), answer)


if __name__ == '__main__':
    unittest.main()
