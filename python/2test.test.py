import subprocess
import unittest

class TestBrailleTranslator(unittest.TestCase):

    # Path to the translator program
    TRANSLATOR = "python3 translator.py"

    # Function to run a test case
    def run_translator(self, input_text):
        # Command to run the translator program
        result = subprocess.run([self.TRANSLATOR, input_text], capture_output=True, text=True)
        # Return the stripped output (remove leading/trailing whitespaces)
        return result.stdout.strip()

    # Simple Test Cases
    def test_empty_input(self):
        self.assertEqual(self.run_translator(""), "")

    def test_single_lowercase_letter(self):
        self.assertEqual(self.run_translator("a"), "O.....")

    def test_single_uppercase_letter(self):
        self.assertEqual(self.run_translator("A"), ".....OO")

    def test_single_digit_number(self):
        self.assertEqual(self.run_translator("5"), ".O.OOOO..")

    def test_space_character(self):
        self.assertEqual(self.run_translator(" "), "......")

    def test_simple_word(self):
        self.assertEqual(self.run_translator("cat"), "OO....O.....OO....")

    def test_braille_to_english_single_letter(self):
        self.assertEqual(self.run_translator("O....."), "a")

    # Intermediate Test Cases
    def test_mixed_case_word(self):
        self.assertEqual(self.run_translator("HeLLo"), ".....OO.OO..O..O..O.O.")

    def test_number_sequence(self):
        self.assertEqual(self.run_translator("123"), ".O.OOOO.....O.O...OO....")

    def test_sentence_with_space(self):
        self.assertEqual(self.run_translator("hi there"), "O.OO...OO.... ......O..O..O.OO..O..O.O...")

    # Complex Test Cases
    def test_sentence_with_capitals_and_numbers(self):
        input_text = "Hello World 42"
        expected_output = ".....OO.OO..O..O..O.O.O......OOOOO.O.OO..O...OOO.O...O.OOO...O......O.OOOOO.O..O.O..."
        self.assertEqual(self.run_translator(input_text), expected_output)

    def test_braille_to_english_complex(self):
        input_text = ".....OO.OO..O..O..O.O.O......OOOOO.O.OO..O...OOO.O...O.OOO...O......O.OOOOO.O..O.O..."
        expected_output = "Hello World 42"
        self.assertEqual(self.run_translator(input_text), expected_output)

    def test_braille_input_with_capital_and_number_indicators(self):
        input_text = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        expected_output = "Abc 123"
        self.assertEqual(self.run_translator(input_text), expected_output)

    def test_input_with_unsupported_characters(self):
        input_text = "Hello, World!"
        expected_output = ".....OO.OO..O..O..O.O.O......OOOOO.O.OO..O...OOO.O..."
        self.assertEqual(self.run_translator(input_text), expected_output)

    def test_long_text_input(self):
        input_text = "The quick brown fox jumps over the lazy dog 9876543210"
        expected_output = ".....O.O...OOOO...O.OO...O..OOO......OOO...OO....OOOOO...OO....O.OO...OO.OO......OO....OO.OO.O.OO..O......O..OOO.OO.O...OOO...O.OO...OO......O.O.OO.O..OO...O.OOOO.O......O..OOO...O.OO..OO.OO..O.OO...OO....O.OOO......O.OO...O...OO....O..O..OO.OOOO.....O.O...OO....OOO...OOO...OOO...OOOOO...OOOOO...OOOOO..."
        self.assertEqual(self.run_translator(input_text), expected_output)

if __name__ == '__main__':
    print("Starting Tests for Braille Translator")
    print("======================================")
    unittest.main()
