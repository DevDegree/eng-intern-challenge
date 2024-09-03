import subprocess
import unittest

from translator import Translator


class TestTranslator(unittest.TestCase):
    translator = Translator()

    def test_braille_to_english(self):

        cases = [
            (".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "Abc 123"),
            (".....OOO..OO.....OOO.OOO.....OO..OOO", "XYZ"),
            (".O.OOOO.....O.O...OO...............OO.....O.O...OO....", "123 Abc"),
        ]

        for input_str, expected in cases:

            with self.subTest(input_str=input_str, expected=expected):
                self.assertEqual(
                    self.translator.translate_braille_to_eng(input_str), expected
                )


if __name__ == "__main__":
    unittest.main()
