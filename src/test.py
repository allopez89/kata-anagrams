import unittest
from AnagramApp import Anagrams

class TestAnagrams(unittest.TestCase):
    def test_empty_list_returns_0_anagrams(self):
        self.assertEqual(Anagrams([]), 0)

    def test_int_list_returns_warning(self):
        self.assertEqual(Anagrams([11, 11, 12, 21, 13, 31]), "The list must contain strings!")

unittest.main()