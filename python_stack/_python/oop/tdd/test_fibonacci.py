# import python testing framework
import unittest


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


class testFibonacci(unittest.TestCase):
    # each method in this class is a test to be run

    def test1(self):
        self.assertEqual(fibonacci(3), 2)

    def test2(self):
        self.assertEqual(fibonacci(5), 5)

    def test3(self):
        self.assertEqual(fibonacci(8), 21)

    def test4(self):
        self.assertIs(fibonacci(9), 34)

    def test5(self):
        self.assertNotEqual(fibonacci(11), 27)

    def test6(self):
        self.assertEqual(fibonacci(14), 377)


if __name__ == '__main__':
    unittest.main()  # This runs our tests.
