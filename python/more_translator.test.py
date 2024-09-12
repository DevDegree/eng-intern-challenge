import unittest
from translator import translate


class TestTranslator(unittest.TestCase):
    def test_blank(self):
        self.assertEqual("", translate(""))

    def test_adj_mod(self):
        self.assertRaises(AssertionError, translate, ".....O.....O")
        self.assertRaises(KeyError, translate, ".O.OOO.....O")

    def test_invalid_num(self):
        self.assertRaises(AssertionError, translate, "45a")
        self.assertRaises(KeyError, translate, ".O.OOOOOOOO.")

    def test_invalid_braille(self):
        self.assertRaises(AssertionError, translate, ".")


if __name__ == "__main__":
    unittest.main()
