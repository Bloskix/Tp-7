from punto_2 import validate_pin
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(validate_pin("12345"), False)

    def test2(self):
        self.assertEqual(validate_pin("9765"), True)

    def test3(self):
        self.assertEqual(validate_pin("a345"), False)
