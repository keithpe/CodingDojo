# import python testing framework.
import unittest


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


if __name__ == '__main__':
    unittest.main()  # this runs our tests.
