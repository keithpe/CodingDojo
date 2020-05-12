# import python testing framework
import unittest


def reverseList(arr):
    for i in range(0, int(len(arr)/2), 1):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr


class reverseListTests(unittest.TestCase):

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


def isPalindrome(word):
    for i in range(0, int(len(word)/2), 1):
        if word[i] != word[len(word)-i-1]:
            return False

    return True


class isPalindromeTests(unittest.TestCase):
    # each method in this class is a test to be run
    def test1(self):
        self.assertEqual(isPalindrome('racecar'), True)

    def test2(self):
        self.assertTrue(isPalindrome('barab'), True)

    def test3(self):
        self.assertFalse(isPalindrome('keith'))

    def test4(self):
        self.assertIs(isPalindrome('kkkk'), True)

    def test5(self):
        self.assertIsNot(isPalindrome('keith'), True)

    def test6(self):
        self.assertNotEqual(isPalindrome('abba'), False)


def coins(amt):

    quarters = int(amt / 25)
    amt -= quarters * 25

    dimes = int(amt / 10)
    amt -= dimes * 10

    nickels = int(amt / 5)
    amt -= nickels * 5

    pennies = int(amt / 1)
    amt -= pennies * 1

    # print("quarters", quarters)
    # print("dimes", dimes)
    # print("nickels", nickels)
    # print("pennies", pennies)
    # print("amt", amt)

    return [quarters, dimes, nickels, pennies]


class CoinsTests(unittest.TestCase):
    # each method in this class is a test to be run
    def test1(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])

    def test2(self):
        self.assertTrue(coins(87), [3, 1, 0, 2])

    def test3(self):
        self.assertNotEqual(coins(87), [2, 0, 1, 3])

    def test4(self):
        self.assertEqual(coins(255), [10, 0, 1, 0])

    def test5(self):
        self.assertTrue(coins(255), [10, 0, 1, 0])

    def test6(self):
        self.assertNotEqual(coins(255), [0, 1, 0, 10])


def factorial(n):

    if n >= 1:
        return n*factorial(n-1)
    else:
        return 1


class FactorialTests(unittest.TestCase):
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


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


class FibonacciTests(unittest.TestCase):
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
