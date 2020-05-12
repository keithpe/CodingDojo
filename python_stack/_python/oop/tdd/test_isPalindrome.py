# import the python testing framework
import unittest


def isPalindrome(word):
    print("word", word)
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


if __name__ == '__main__':
    unittest.main()  # this runs our tests
