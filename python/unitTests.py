import unittest
from translator import Translator  # Assuming your code is in a file named translator.py

class TestBrailleTranslator(unittest.TestCase):
    
    def setUp(self):
        self.translator = Translator()

    # Test English to Braille translation for lowercase letters
    def test_english_to_braille_lowercase(self):
        self.assertEqual(self.translator.translate("abc"), "O.....O.O...OO....")

    # Test Braille to English translation for lowercase letters
    def test_braille_to_english_lowercase(self):
        self.assertEqual(self.translator.translate("O.....O.O...OO...."), "abc")

    # Test English to Braille translation with capitalization
    def test_english_to_braille_capitalization(self):
        self.assertEqual(self.translator.translate("Abc"), ".....OO.....O.O...OO....")

    # Test Braille to English translation with capitalization
    def test_braille_to_english_capitalization(self):
        self.assertEqual(self.translator.translate(".....OO.....O.O...OO...."), "Abc")

    # Test translation of a single space in English to Braille
    def test_english_to_braille_single_space(self):
        self.assertEqual(self.translator.translate(" "), "......")

    # Test translation of a single space in Braille to English
    def test_braille_to_english_single_space(self):
        self.assertEqual(self.translator.translate("......"), " ")


if __name__ == "__main__":
    unittest.main()
