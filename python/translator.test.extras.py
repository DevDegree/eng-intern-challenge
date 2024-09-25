import unittest
import subprocess
from braille_to_char import CHAR_TO_BRAILLE as char2braille
from braille_to_char import NUM_TO_BRAILLE as num2braille
from functools import reduce

braille2char = {v: k for k, v in char2braille.items()}
braille2num = {v: k for k, v in num2braille.items()}

tok2char = braille2char | braille2num


class TestTranslator(unittest.TestCase):
    def run_translator(self, input_str):
        command = ["python3", "translator.py"] + input_str.split()
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    # def test_mixed_case_and_punctuation(self):
    #     input_str = "Hello, World!"
    #     result = self.run_translator(input_str)
    #     expected_output = ".....OO.OO..O..O..O..O....O.......O..OO.O.O.OO..O..OOO."
    #
    def test_numbers_and_decimal(self):
        input_str = "3.14 > 2.71"
        expected_output = (
            ".O.OOOOO........O.OO.....O.O..O..OO.......O.OOOO.O....OO.O.....O....O"
        )
        result = self.run_translator(input_str)
        chunked_expected = "\n".join(
            [expected_output[i : i + 6] for i in range(0, len(expected_output), 6)]
        )
        chunked_result = "\n".join(
            [result[i : i + 6] for i in range(0, len(result), 6)]
        )
        for expected, res in zip(chunked_expected.split(), chunked_result.split()):
            print(
                expected,
                braille2char.get(expected, "&"),
                res,
                braille2char.get(res, "&"),
            )

        self.assertEqual(self.run_translator(input_str), expected_output)

    # def test_special_characters_and_missing(self):
    #     input_str = "<braille@example.com>"
    #     expected_output = ".OO..OO.O.OO...O....O.O..O.O.O......0.00...O..OO....OO..O.OO..O..OO..O.O...O..OO."
    #     self.assertEqual(self.run_translator(input_str), expected_output)


if __name__ == "__main__":
    unittest.main()
