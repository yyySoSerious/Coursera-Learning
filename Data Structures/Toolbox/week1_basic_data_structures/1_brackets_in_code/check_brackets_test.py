import unittest
from check_brackets import find_mismatch


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for text, answer in (
                ("([])[[", 5),
                ("((([timothey][()])))", "Success"),
                ("[]", "Success"),
                ("{}[]", "Success"),
                ("{", 1),
                ("[", 1),
                ("}}}", 1),
                ("foo(bar[i)", 10),
                ("{[}", 3),
                ("foo(bar)", "Success")):
            self.assertEqual(find_mismatch(text), answer, f'text:{text} answer:{answer}')  # add assertion here


if __name__ == '__main__':
    unittest.main()
