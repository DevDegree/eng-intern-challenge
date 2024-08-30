import unittest
from translator import BrailleTranslator


class TestBrailleTranslator(unittest.TestCase):

    def setUp(self):
        self.translator = BrailleTranslator()

    def test_english_to_braille(self):
        # Test basic conversion
        self.assertEqual(
            self.translator.english_to_braille("Hello world"),
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..",
        )
        self.assertEqual(self.translator.english_to_braille("42"), ".O.OOOOO.O..O.O...")
        self.assertEqual(
            self.translator.english_to_braille("Abc 123"),
            ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..",
        )

    def test_braille_to_english(self):
        # Test basic conversion
        self.assertEqual(
            self.translator.braille_to_english(
                ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
            ),
            "Hello world",
        )
        self.assertEqual(self.translator.braille_to_english(".O.OOOOO.O..O.O..."), "42")
        self.assertEqual(
            self.translator.braille_to_english(
                ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O.."
            ),
            "Abc 123",
        )


if __name__ == "__main__":
    unittest.main()
