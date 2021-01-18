import unittest
from base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")


    def test_base17(self):
        self.assertEqual(convert(315,16),"13B")


    def test_base18(self):
        self.assertEqual(convert(314,16),"13A")


    def test_base19(self):
        self.assertEqual(convert(317,16),"13D")


    def test_base20(self):
        self.assertEqual(convert(318,16),"13E")


    def test_base21(self):
        self.assertEqual(convert(319,16),"13F")

if __name__ == "__main__":
        unittest.main()