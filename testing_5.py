from punto_5 import consecutive
import unittest

class Test(unittest.TestCase):
    def test1(self):
        list = [3,7]
        s_list = [1,3,5,7]
        self.assertEqual(consecutive(list,s_list), "False")

    def test2(self):
        list = [2,3]
        s_list = []
        self.assertEqual(consecutive(list,s_list), "True")

    def test3(self):
        list = [-3,-4]
        s_list = [1,6,9,-3,-4,78,0]
        self.assertEqual(consecutive(list,s_list), "True")