import unittest
import subprocess


# class TestTranslator(unittest.TestCase):
#     def test_output(self):
#         # Command to run translator.py script
#         command = ["python3", "translator.py", "Abc", "123", "xYz"]

#         # Run the command and capture output
#         result = subprocess.run(command, capture_output=True, text=True)

#         # Expected output without the newline at the end
#         expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"

#         # DEBUGGING
#         # chunked_expected = "\n".join(
#         #     [expected_output[i : i + 6] for i in range(0, len(expected_output), 6)]
#         # )
#         # chunked_result = "\n".join(
#         #     [
#         #         result.stdout.strip()[i : i + 6]
#         #         for i in range(0, len(result.stdout.strip()), 6)
#         #     ]
#         # )
#         # for expected, res in zip(chunked_expected.split(), chunked_result.split()):
#         #     print(expected, res)

#         # Strip any leading/trailing whitespace from the output and compare
#         self.assertEqual(result.stdout.strip(), expected_output)


# if __name__ == "__main__":
#     unittest.main()


import unittest
import subprocess


class TestTranslator(unittest.TestCase):
    def run_translator(self, input_str):
        command = ["python3", "translator.py"] + input_str.split()
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def test_mixed_case_and_punctuation(self):
        input_str = "Hello, World!"
        result = self.run_translator(input_str)
        expected_output = ".....OO.OO..O..O..O..O....O.......O..OO.O.O.OO..O..OOO."
        # DEBUGGING
        chunked_expected = "\n".join(
            [expected_output[i : i + 6] for i in range(0, len(expected_output), 6)]
        )
        chunked_result = "\n".join(
            [result[i : i + 6] for i in range(0, len(result), 6)]
        )
        for expected, res in zip(chunked_expected.split(), chunked_result.split()):
            print(expected, res)

        self.assertEqual(self.run_translator(input_str), expected_output)

    # def test_numbers_and_decimal(self):
    #     input_str = "3.14 > 2.71"
    #     expected_output = (
    #         ".O.OOOOO........O.OO.....O.O..O..OO.......O.OOOO.O....OO.O.....O....O"
    #     )
    #     self.assertEqual(self.run_translator(input_str), expected_output)

    # def test_special_characters_and_missing(self):
    #     input_str = "<braille@example.com>"
    #     expected_output = ".OO..OO.O.OO...O....O.O..O.O.O......0.00...O..OO....OO..O.OO..O..OO..O.O...O..OO."
    #     self.assertEqual(self.run_translator(input_str), expected_output)


if __name__ == "__main__":
    unittest.main()
