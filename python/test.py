import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_translator(self):
        # Test case 1: Mixed input
        command_mixed = ["python3", "translator.py", "Hello World! 123"]
        result_mixed = subprocess.run(command_mixed, capture_output=True, text=True)
        expected_output_mixed = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O....000........O.OOOO.....O.O...OO...."
        self.assertEqual(result_mixed.stdout.strip(), expected_output_mixed)

        # Test case 2: Long String Mix Input
        command_special_chars = ["python3", "translator.py", "2024 Shopify Intern Challenge - Vraj Bhavsar!"]
        result_special_chars = subprocess.run(command_special_chars, capture_output=True, text=True)
        expected_output_special_chars = ".O.OOOO.O....OOO..O.O...OO.O.............O.OO.O.O.OO..O..OO.OOO.O..O.O..OOO...OO.OOO...........O.O.O..OO.OO..OOOO.O..O..O.OOO.OO.OO............OOO....O.OO..O.....O.O.O.O.O.O.O..O..OO.OO.OOOO..O..O............OO...........OO.O.OOO.OOO.O......OOO.............OO.O...O.OO..O.....O.O.OO.OO.O.O.....O.OOO...000."
        self.assertEqual(result_special_chars.stdout.strip(), expected_output_special_chars)

        # Test case 3: Invalid character input
        command_invalid_char = ["python3", "translator.py", "~"]
        result_invalid_char = subprocess.run(command_invalid_char, capture_output=True, text=True)
        expected_output_invalid_char = "Error: Character '~' not valid"
        self.assertEqual(result_invalid_char.stdout.strip(), expected_output_invalid_char)

        # Test case 4: Long string input 2
        long_string = "The quick brown fox jumps over the lazy dog 1234567890"
        command_long_string = ["python3", "translator.py", long_string]
        result_long_string = subprocess.run(command_long_string, capture_output=True, text=True)
        expected_output_long_string = ".....O.OOOO.O.OO..O..O........OOOOO.O...OO.O.O..OO....O...O.......O.O...O.OOO.O..OO..OOO.OOO.OO.......OOO...O..OO.OO..OO.......OOO..O...OOOO..O.OOO.O..OO.O.......O..OO.O.O.OOO..O..O.OOO........OOOO.O.OO..O..O........O.O.O.O.....O..OOOOO.OOO......OO.O..O..OO.OOOO.........O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...O.O...OOO.."
        self.assertEqual(result_long_string.stdout.strip(), expected_output_long_string)

        # Test case 5: Input with consecutive spaces
        command_consecutive_spaces = ["python3", "translator.py", "Hello   World"]
        result_consecutive_spaces = subprocess.run(command_consecutive_spaces, capture_output=True, text=True)
        expected_output_consecutive_spaces = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result_consecutive_spaces.stdout.strip(), expected_output_consecutive_spaces)

        # Test case 6: Input with numbers and symbols mixed
        command_numbers_symbols = ["python3", "translator.py", "123! 456-"]
        result_numbers_symbols = subprocess.run(command_numbers_symbols, capture_output=True, text=True)
        expected_output_numbers_symbols = ".O.OOOO.....O.O...OO......000........O.OOOOO.O..O..O..OOO.......OO" 
        self.assertEqual(result_numbers_symbols.stdout.strip(), expected_output_numbers_symbols)

        # Test case 7: Edge case with capital letters and special characters
        command_capital_special = ["python3", "translator.py", "HELLO!!!"]
        result_capital_special = subprocess.run(command_capital_special, capture_output=True, text=True)
        expected_output_capital_special = ".....O.....O.....O.....O.....O.....OOO"
        self.assertEqual(result_capital_special.stdout.strip(), expected_output_capital_special)

        # Test case 8: Empty string input
        command_empty = ["python3", "translator.py", " "]
        result_empty = subprocess.run(command_empty, capture_output=True, text=True)
        expected_output_empty = "Usage: python3 translator.py <text>"
        self.assertEqual(result_empty.stdout.strip(), expected_output_empty)

        # Test case 9: Input with invalid characters mixed with valid ones
        command_invalid_mixed = ["python3", "translator.py", "Hello World ! !"]
        result_invalid_mixed = subprocess.run(command_invalid_mixed, capture_output=True, text=True)
        expected_output_invalid_mixed = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..........000.........000."
        self.assertIn(expected_output_invalid_mixed, result_invalid_mixed.stdout)

        # Test case 10: Edge case with symbols only
        command_symbols_only = ["python3", "translator.py", ".,?!:;-/<>"]
        result_symbols_only = subprocess.run(command_symbols_only, capture_output=True, text=True)
        expected_output_symbols_only = ".....O....000...000."
        self.assertEqual(result_symbols_only.stdout.strip(), expected_output_symbols_only)

if __name__ == "__main__":
    unittest.main()
