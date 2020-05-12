# import python testing framework
import unittest


def reverseList(arr):

    for i in range(0, int(len(arr)/2), 1):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr


class ReverseListTests(unittest.TestCase):
    # each method in this class is a test to be run
    def test1(self):
        self.assertEqual(reverseList([1, 2, 3]), [3, 2, 1])

    def test2(self):
        self.assertTrue(reverseList([3, 5, 6, 7]), [7, 6, 5, 3])

    def test3(self):
        self.assertEqual(reverseList(["one", "two", "three", "four", "five"]), [
                         "five", "four", "three", "two", "one"])

    def test4(self):
        self.assertEqual(reverseList([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()  # This runs our tests.
