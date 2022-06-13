from punto_4 import *
import unittest

class Test(unittest.TestCase):
    def test1(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bingo_numbers = [2, 9, 7, 14, 16]
        self.assertEqual(bingo_check(bingo_numbers,list), "Loser")

    def test2(self):
        list = [20, 12, 23, 14, 6, 22, 12, 17, 2, 26]
        bingo_numbers = [2, 9, 7, 14, 16]
        self.assertEqual(bingo_check(bingo_numbers,list), "Loser")

    def test3(self):
        list = [1, 2, 3, 7, 5, 14, 7, 15, 9, 10]
        bingo_numbers = [2, 9, 7, 14, 15]
        self.assertEqual(bingo_check(bingo_numbers,list), "Winner")

    def test4(self):
        list = [5, 2, 13, 7, 5, 14, 17, 15, 9, 10]
        bingo_numbers = [2, 9, 7, 14, 15]
        self.assertEqual(bingo_check(bingo_numbers,list), "Winner")