import unittest
from translator import english_to_braille, braille_to_english

class TestBrailleConverter(unittest.TestCase):
    def test_english_to_braille_letters(self):
        self.assertEqual(english_to_braille("hello"), "O.O.O.O.O....OO.O.O..O")
        self.assertEqual(english_to_braille("WORLD"), ".....OO.O.OO.O.....OO..OO.O.....OO.O.O..O....OOO..O.O.")

    def test_english_to_braille_numbers(self):
        self.assertEqual(english_to_braille("123"), ".O.OOOO....OO.O...OO....")
        self.assertEqual(english_to_braille("2024"), ".O.OOOO.O....OO..O...OO.O..")

    def test_english_to_braille_mixed(self):
        self.assertEqual(english_to_braille("Hello 2024"), ".....OO.O.O.O.O.O....OO.O.O..O......O.OOOO.O....OO..O...OO.O..")

    def test_english_to_braille_decimals(self):
        self.assertEqual(english_to_braille("3.14"), ".O.OOOO.....O...OO....O....O.....")
        self.assertEqual(english_to_braille("$19.99"), ".O.OOOO....O....O.O...O......O.OO...O.O...")
        self.assertEqual(braille_to_english(".O.OOOO....O....O.O...O......O.OO...O.O..."), "19.99")

if __name__ == '__main__':
    unittest.main()