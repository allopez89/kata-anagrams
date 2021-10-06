import unittest
from AnagramApp import Anagrams, ReadFile, Timer

class TestAnagrams(unittest.TestCase):
    def test_empty_list_returns_0_anagrams(self):
        self.assertEqual(Anagrams([]), 0)

    def test_int_list_returns_warning(self):
        self.assertEqual(Anagrams([11, 11, 12, 21, 13, 31]), "The list must contain strings!")

    def test_wordlist_file_returns_30404_anagrams(self):
        self.assertEqual(Anagrams(ReadFile("src\wordlist.txt")), 30404)

    def test_algorithm_timer_returs_less_than_68s(self):
        self.assertLessEqual(Timer(), 1.8)

unittest.main()