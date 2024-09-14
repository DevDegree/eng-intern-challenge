import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    
    def run_command(self, input_text):
        command = ["python3", "translator.py", input_text]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def test_translator_mixed_input(self):
        result = self.run_command("Hello World! 123")
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O....OOO........O.OOOO.....O.O...OO...."
        self.assertEqual(result, expected_output)

    def test_translator_special_chars(self):
        result = self.run_command("2024 Shopify Intern Challenge - Vraj Bhavsar!")
        expected_output = ".O.OOOO.O....OOO..O.O...OO.O.............O.OO.O.O.OO..O..OO.OOO.O..OO...OOO...OO.OOO...........O.OO...OO.OO..OOOO.O..O..O.OOO.OO.OO............OOO....O.OO..O.....O.O.O.O.O.O.O..O..OO.OO.OOOO..O..O............OO...........OO.O.OOO.OOO.O......OOO.............OO.O...O.OO..O.....O.O.OO.OO.O.O.....O.OOO...OOO."
        self.assertEqual(result, expected_output)

    # Test Case for Braille to English
    def test_translator_flipped_input(self):
        test_string = "2024 Shopify Intern Challenge - Vraj Bhavsar!"
        result_braille = self.run_command(test_string)
        output_string = self.run_command(result_braille)
        self.assertEqual(output_string, test_string)

    def test_translator_invalid_char(self):
        result = self.run_command("~")
        expected_output = "Error: Character '~' not valid"
        self.assertEqual(result, expected_output)

    def test_translator_long_string(self):
        long_string = "The quick brown fox jumps over the lazy dog 1234567890"
        result = self.run_command(long_string)
        expected_output = ".....O.OOOO.O.OO..O..O........OOOOO.O...OO.OO...OO....O...O.......O.O...O.OOO.O..OO..OOO.OOO.OO.......OOO...O..OO.OO..OO.......OOO..O...OOOO..O.OOO.O..OO.O.......O..OO.O.O.OOO..O..O.OOO........OOOO.O.OO..O..O........O.O.O.O.....O..OOOOO.OOO......OO.O..O..OO.OOOO.........O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO...OO....O.O...OOO.."
        self.assertEqual(result, expected_output)

    def test_translator_consecutive_spaces(self):
        result = self.run_command("Hello   World")
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........................O.OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result, expected_output)

    def test_translator_numbers_symbols(self):
        result = self.run_command("123! 456-")
        expected_output = ".O.OOOO.....O.O...OO......OOO........O.OOOOO.O..O..O..OOO.......OO" 
        self.assertEqual(result, expected_output)

    def test_translator_braille_to_english(self):
        result = self.run_command(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
        expected_output = "Abc 123" 
        self.assertEqual(result, expected_output)

    def test_translator_space(self):
        result = self.run_command(" ")
        expected_output = "......"
        self.assertEqual(result, expected_output)

    def test_translator_invalid_mixed(self):
        result = self.run_command("Hello World ! !")
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..........OOO.........OOO."
        self.assertEqual(expected_output, result)
        
    def test_translator_braille_special(self):
        result = self.run_command("!.,<")
        expected_output = "..OOO...OO.O..O....OO..O"
        self.assertEqual(expected_output, result)

if __name__ == "__main__":
    unittest.main()
