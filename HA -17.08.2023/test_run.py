import unittest

from run import multi


class TestSub(unittest.TestCase):

    def test_multi_function(self):
        self.assertEqual(multi(3, 7), 21)
        self.assertEqual(multi(4, 6), 24)

    def test_multi_function_with_floats(self):
        self.assertAlmostEqual(multi(7.5, 7.5), 56.25)


if __name__ == "__main__":
    unittest.main()