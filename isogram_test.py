import unittest

import test_isogram
from main import isogram_check


class TestIsIsogram(unittest.TestCase):
    def test_isogram_check(self):
        # Test case with an empty string when the input is null
        self.assertTrue(isogram_check(""))

        # Test case with a single character
        self.assertTrue(isogram_check("a"))

        # Test case with all unique characters
        self.assertTrue(isogram_check("isogram"))

        # Test case with duplicate characters
        self.assertFalse(isogram_check("helloworld"))

        # Test case with mixed case characters
        self.assertFalse(isogram_check("AbCdefG"))

        # Test case with spaces
        self.assertTrue(isogram_check("nice day"))

        # Test case with numbers and symbols
        self.assertTrue(isogram_check("123!@#qwerty???"))


if __name__ == '__main__':
    unittest.main()
