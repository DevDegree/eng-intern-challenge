import unittest
from translator import english_to_braille, braille_to_english, is_braille


class TestBrailleTranslator(unittest.TestCase):

    def test_english_to_braille(self):
        # Test basic basic english to braille
        self.assertEqual(
            english_to_braille("Hello world"),
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..",
        )
        self.assertEqual(english_to_braille("42"), ".O.OOOOO.O..O.O...")
        self.assertEqual(
            english_to_braille("Abc 123"),
            ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....",
        )

    def test_braille_to_english(self):
        # Test basic braille to english
        self.assertEqual(
            braille_to_english(
                ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
            ),
            "Hello world",
        )
        self.assertEqual(braille_to_english(".O.OOOOO.O..O.O..."), "42")
        self.assertEqual(
            braille_to_english(
                ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
            ),
            "Abc 123",
        )

    def test_is_braille(self):
        # Test basic braille indentification
        self.assertTrue(
            is_braille(
                ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
            )
        )
        self.assertTrue(is_braille(".O.OOOOO.O..O.O..."))
        self.assertTrue(
            is_braille(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
        )
        self.assertFalse(is_braille("Hello world"))
        self.assertFalse(is_braille("42"))
        self.assertFalse(is_braille("Abc 123"))


if __name__ == "__main__":
    unittest.main()
