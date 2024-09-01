import unittest
from translator import translate_to_braille

class TestBrailleTranslator(unittest.TestCase):

    def test_english_to_braille(self):
        self.assertEqual(
            translate_to_braille("42"),
            ".O.OOOOO.O..O.O..."
        )
        self.assertEqual(
            translate_to_braille("Abc 123"),
            ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        )
        self.assertEqual(
            translate_to_braille("Hello world"),
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        )

if __name__ == "__main__":
    unittest.main()
