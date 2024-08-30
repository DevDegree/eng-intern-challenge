import unittest
from python.translator import (
    is_braille,
    Translator,
    EnglishToBrailleStrategy,
    BrailleToEnglishStrategy,
)


class TestBrailleTranslation(unittest.TestCase):

    def test_is_braille_true(self):
        # Test valid Braille input
        self.assertTrue(is_braille(['O.....O.O...', 'OO....', '......']))
        self.assertTrue(is_braille(['......']))  # Braille space

    def test_is_braille_false(self):
        # Test invalid Braille input
        self.assertFalse(is_braille(['O.....O.O..']))  # Invalid length
        self.assertFalse(is_braille(['O.....X.O...']))  # Invalid character
        self.assertFalse(is_braille(['abcdef']))  # Not Braille characters

    def test_english_to_braille_translation(self):
        # Test simple English to Braille translation
        translator = Translator(EnglishToBrailleStrategy())
        result = translator.translate(['Abc 123'])
        expected = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'
        self.assertEqual(result, expected)

        result = translator.translate(['Hello world'])
        expected = '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'
        self.assertEqual(result, expected)

    def test_braille_to_english_translation(self):
        # Test simple Braille to English translation
        translator = Translator(BrailleToEnglishStrategy())
        result = translator.translate(['.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'])
        expected = 'Abc 123'
        self.assertEqual(result, expected)

        result = translator.translate(['.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'])
        expected = 'Hello world'
        self.assertEqual(result, expected)

    def test_english_to_braille_with_numbers(self):
        # Test English to Braille translation with numbers
        translator = Translator(EnglishToBrailleStrategy())
        result = translator.translate(['a1', 'B2'])
        expected = 'O......O.OOOO................OO.O....O.OOOO.O...'
        self.assertEqual(result, expected)

    def test_braille_to_english_with_numbers(self):
        # Test Braille to English translation with numbers
        translator = Translator(BrailleToEnglishStrategy())
        result = translator.translate(['O......O.OOOO................OO.O....O.OOOO.O...'])
        expected = 'a1 B2'
        self.assertEqual(result, expected)

    def test_english_to_braille_sentence_with_numbers(self):
        # Test sentence with numbers and uppercase
        translator = Translator(EnglishToBrailleStrategy())
        result = translator.translate(['Abc 123 Fox'])
        expected = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO...............OOOO...O..OO.OO..OO'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
