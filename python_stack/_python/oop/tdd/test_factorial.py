# import python testing framework
import unittest


def factorial(n):

    if n >= 1:
        return n*factorial(n-1)
    else:
        return 1


class testFactorial(unittest.TestCase):
    # each method in this class is a test to be run

    def test1(self):
        self.assertEqual(factorial(4), 24)

    def test2(self):
        self.assertTrue(factorial(5), 120)

    def test3(self):
        self.assertNotEqual(factorial(5), 150)

    def test4(self):
        self.assertEqual(factorial(7), 5040)

    def test5(self):
        self.assertIsNot(factorial(7), 5020)

    def test6(self):
        self.assertFalse(factorial(7) == 5020)

    def test7(self):
        self.assertEqual(factorial(11), 39916800)


if __name__ == '__main__':
    unittest.main()  # This runs our tests.
