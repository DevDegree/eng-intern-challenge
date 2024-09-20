import unittest
import subprocess

class TestTranslator(unittest.TestCase):

    def run_translator(self, input_str):
        # Command to run translator.py script
        command = ["python3", "translator.py", input_str]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        return result.stdout.strip()

    def test_english_to_braille_mixed_case_with_numbers(self):
        input_str = "Hello World 123"
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.........O.OOOO.....O.O...OO...."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_english_to_braille_uppercase_sequence_with_mixed_digits(self):
        input_str = "WOW 42 ZEBRA"
        expected_output = ".....O.OOO.O.....OO..OO......O.OOO.O.......O.OOOOO.O..O.O..............OO..OOO.....OO..O.......OO.O........OO.OOO......OO....."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_english_to_braille_multiple_spaces(self):
        input_str = "Go   big   or   go   home 1234"
        expected_output = ".....OOOOO..O..OO...................O.O....OO...OOOO....................O..OO.O.OOO...................OOOO..O..OO...................O.OO..O..OO.OO..O.O..O.........O.OOOO.....O.O...OO....OO.O.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_english_to_braille_single_character(self):
        input_str = "A"
        expected_output = ".....OO....."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_english_to_braille_empty_input(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_braille_to_english_mixed_case_with_numbers(self):
        input_str = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.........O.OOOO.....O.O...OO...."
        expected_output = "Hello World 123"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_braille_to_english_uppercase_sequence_with_mixed_digits(self):
        input_str = ".....O.OOO.O.....OO..OO......O.OOO.O.......O.OOOOO.O..O.O..............OO..OOO.....OO..O.......OO.O........OO.OOO......OO....."
        expected_output = "WOW 42 ZEBRA"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_braille_to_english_multiple_spaces(self):
        input_str = ".....OOOOO..O..OO...................O.O....OO...OOOO....................O..OO.O.OOO...................OOOO..O..OO...................O.OO..O..OO.OO..O.O..O.........O.OOOO.....O.O...OO....OO.O.."
        expected_output = "Go   big   or   go   home 1234"
        self.assertEqual(self.run_translator(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()
