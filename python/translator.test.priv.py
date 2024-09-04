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

    def test_english_to_braille(self):
        cases = [
            (
                "Hello world",
                ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..",
            ),
            ("42", ".O.OOOOO.O..O.O..."),
            (
                "Hello world 42",
                ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.........O.OOOOO.O..O.O...",
            ),
            (
                "Hello world42",
                ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O...O.OOOOO.O..O.O...",
            ),
        ]

        for input_str, expected in cases:

            with self.subTest(input_str=input_str, expected=expected):
                self.assertEqual(
                    self.translator.translate_eng_to_braille(input_str), expected
                )

    def test_back_n_forth(self):
        input_str = "The 12 quick 34 brown5 6 Fox 78 jumps 9 over 0 the lazy dog"

        in_braille = self.translator.translate(input_str)
        in_english = self.translator.translate(in_braille)

        with open("out.txt", "w") as f:
            f.write(f"{in_braille}\n\n{in_english}")

        # If encoding is correct, then applying them back to back should result in the same text
        self.assertEqual(in_english, input_str)


if __name__ == "__main__":
    unittest.main()
