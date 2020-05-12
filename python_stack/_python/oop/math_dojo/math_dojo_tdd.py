# import python testing framework
import unittest


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for num2 in nums:
            self.result += num2
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for num2 in nums:
            self.result -= num2
        return self


class math_dojo_tests(unittest.TestCase):
    # each method in this class is a test to be run

    def setUp(self):
        self.md = MathDojo()

    def test1(self):
        # md = MathDojo()
        self.assertIsInstance(self.md, MathDojo)

    def test2(self):
        self.assertEqual(self.md.add(2).add(3).add(4).result, 9)

    def test3(self):
        self.assertEqual(self.md.subtract(
            3).subtract(3).subtract(10).result, -16)

    def test4(self):
        self.assertEqual(self.md.add(5).add(
            10).subtract(5).subtract(5).result, 5)

    def test5(self):
        self.assertEqual(self.md.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).result, 55)

    def test6(self):
        self.assertEqual(self.md.add(1, 2, 3).subtract(2, 3).result, 1)


if __name__ == '__main__':
    unittest.main()  # This runs our tests.
