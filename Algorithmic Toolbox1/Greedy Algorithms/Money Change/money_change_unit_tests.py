import unittest
from money_change import money_change, money_change2


class TestSumOfTwoDigits(unittest.TestCase):
    def test(self):
        for (money, number_of_coins) in [(1, 1), (2, 2), (28, 6), ]:
            self.assertEqual(money_change2(money), number_of_coins,
                             f'money: {money}')


if __name__ == '__main__':
    unittest.main()
