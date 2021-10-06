import unittest
from AnagramApp import Anagrams

class TestAnagrams(unittest.TestCase):
    def test_empty_list_returns_0_anagrams(self):
        self.assertEqual(Anagrams([]), 0)

unittest.main()