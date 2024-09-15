import unittest
from translator import BrailleTranslator
from constants import (
    NUMBER_FOLLOWS,
    CAPITAL_FOLLOWS,
    ALPHABETS_TO_BRAILLE,
    NUMBERS_TO_BRAILLE,
    BRAILLE_TO_ALPHABETS,
    BRAILLE_TO_NUMBERS,
)


class TestBrailleTranslator(unittest.TestCase):
    """
    Unit tests for the BrailleTranslator class.
    """

    def test_english_to_braille(self):
        """
        Test the translation from English to Braille.
        """
        translator = BrailleTranslator("Hello world")
        self.assertEqual(
            translator.english_to_braille(),
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..",
        )

        translator = BrailleTranslator("42")
        self.assertEqual(translator.english_to_braille(), ".O.OOOOO.O..O.O...")

        translator = BrailleTranslator("Abc 123")
        self.assertEqual(
            translator.english_to_braille(),
            ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....",
        )

    def test_braille_to_english(self):
        """
        Test the translation from Braille to English.
        """
        translator = BrailleTranslator(
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        )
        self.assertEqual(
            translator.braille_to_english(),
            "Hello world",
        )

        translator = BrailleTranslator(".O.OOOOO.O..O.O...")
        self.assertEqual(translator.braille_to_english(), "42")

        translator = BrailleTranslator(
            ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        )
        self.assertEqual(
            translator.braille_to_english(),
            "Abc 123",
        )

    def test_is_braille(self):
        """
        Test the identification of Braille input.
        """
        translator = BrailleTranslator(
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        )
        self.assertTrue(translator.is_braille())

        translator = BrailleTranslator(".O.OOOOO.O..O.O...")
        self.assertTrue(translator.is_braille())

        translator = BrailleTranslator(
            ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        )
        self.assertTrue(translator.is_braille())

        translator = BrailleTranslator("Hello world")
        self.assertFalse(translator.is_braille())

        translator = BrailleTranslator("42")
        self.assertFalse(translator.is_braille())

        translator = BrailleTranslator("Abc 123")
        self.assertFalse(translator.is_braille())

    def test_alphabets_and_numbers_to_braille(self):
        """
        Test every single alphabet-to-Braille and number-to-Braille mapping.
        """
        for char, braille in ALPHABETS_TO_BRAILLE.items():
            translator = BrailleTranslator(char)
            self.assertEqual(translator.english_to_braille(), braille)

        for number, braille in NUMBERS_TO_BRAILLE.items():
            translator = BrailleTranslator(number)
            result = translator.english_to_braille()
            expected = NUMBER_FOLLOWS + braille
            self.assertEqual(result, expected)

    def test_braille_to_alphabets_and_numbers(self):
        """
        Test every single Braille-to-alphabet and Braille-to-number mapping.
        """
        for braille, char in BRAILLE_TO_ALPHABETS.items():
            translator = BrailleTranslator(braille)
            self.assertEqual(translator.braille_to_english(), char)

        for braille, number in BRAILLE_TO_NUMBERS.items():
            translator = BrailleTranslator(NUMBER_FOLLOWS + braille)
            result = translator.braille_to_english()
            expected = number
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
