import unittest
import subprocess

# Additional unit tests

class TestTranslator(unittest.TestCase):
    def run_translator(self, input_str):
        command = ["python3", "python/translator.py"] + input_str.split()
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def test_mixed_case_and_numbers(self):
        input_str = "Abc 123 xYz"
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_all_lowercase(self):
        input_str = "hello world"
        expected_output = "O.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_all_uppercase(self):
        input_str = "BRAILLE"
        expected_output = ".....OO.O........OO.OOO......OO..........O.OO........OO.O.O......OO.O.O......OO..O.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_numbers_only(self):
        input_str = "2023"
        expected_output = ".O.OOOO.O....OOO..O.O...OO...."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_braille_to_english(self):
        input_str = "O.OO..O..O..O.O.O.O.O.O.O..OO."
        expected_output = "hello"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_braille_to_english_with_numbers(self):
        input_str = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........O.OOOO.....O.O...OO...."
        expected_output = "Hello 123"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_empty_input(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(self.run_translator(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()