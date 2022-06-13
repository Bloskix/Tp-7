from punto_3 import *
import unittest

class Test(unittest.TestCase):

    def test1(self):
        nums = list(range(0, 101))
        nums.remove(5)
        self.assertEquals(check_missing_number(nums), 5)

    def test2(self):
        nums = list(range(0, 101))
        nums.remove(10)
        self.assertEquals(check_missing_number(nums), 10)