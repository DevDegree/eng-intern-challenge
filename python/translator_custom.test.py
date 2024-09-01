import unittest
import subprocess

class TestTranslator(unittest.TestCase):

    def run_translator(self, input_args, expected_output):
        """Helper method to run the translator with given input and check output."""
        command = ["python3", "translator.py"] + input_args
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Compare the output with the expected output
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_to_braille_brackets(self):
        self.run_translator(["()<>"], "O.O..O.O.OO..OO..OO..OO.")
        
    def test_english_to_braille_single_word(self):
        self.run_translator(["Hello"], ".....OO.OO..O..O..O.O.O.O.O.O.O..OO.")

    def test_english_to_braille_sentence(self):
        self.run_translator(["Hello", "World"], ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..")

    def test_english_to_braille_numbers(self):
        self.run_translator(["42"], ".O.OOOOO.O..O.O...")
    
    def test_english_to_braille_mixed(self):
        self.run_translator(["Abc", "123", "xYz"], ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")

    def test_english_to_braille_all_lowercase(self):
        self.run_translator(["hello"], "O.OO..O..O..O.O.O.O.O.O.O..OO.")

    def test_english_to_braille_all_uppercase(self):
        self.run_translator(["HELLO"], ".....OO.OO.......OO..O.......OO.O.O......OO.O.O......OO..OO.")

    def test_english_to_braille_mixed_case_and_numbers(self):
        self.run_translator(["Hello123"], ".....OO.OO..O..O..O.O.O.O.O.O.O..OO..O.OOOO.....O.O...OO....")

    def test_english_to_braille_sentence_with_punctuation(self):
        self.run_translator(["Hello,", "world!"], ".....OO.OO..O..O..O.O.O.O.O.O.O..OO...O..........OOO.OO..OO.O.OOO.O.O.O.OO.O....OOO.")

    def test_braille_to_english_single_word(self):
        self.run_translator([".....OO.OO..O..O..O.O.O.O.O.O.O..OO."], "Hello")

    def test_braille_to_english_sentence(self):
        self.run_translator([".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."], "Hello world")

    def test_braille_to_english_numbers(self):
        self.run_translator([".O.OOOOO.O..O.O..."], "42")
    
    def test_braille_to_english_mixed(self):
        self.run_translator([".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"], "Abc 123 xYz")

    def test_braille_to_english_with_decimal(self):
        self.run_translator([".O.OOOOO.O..O.O....O...OO.O..."], "42.2")

    def test_braille_to_english_all_lowercase(self):
        self.run_translator(["O.OO..O..O..O.O.O.O.O.O.O..OO."], "hello")

    def test_braille_to_english_all_uppercase(self):
        self.run_translator([".....OO.OO.......OO..O.......OO.O.O......OO.O.O......OO..OO."], "HELLO")

    def test_braille_to_english_mixed_case_and_numbers(self):
        self.run_translator([".....OO.OO..O..O..O.O.O.O.O.O.O..OO..O.OOOO.....O.O...OO...."], "Hello123")

    def test_braille_to_english_sentence_with_punctuation(self):
        self.run_translator([".....OO.OO..O..O..O.O.O.O.O.O.O..OO...O..........OOO.OO..OO.O.OOO.O.O.O.OO.O....OOO."], "Hello, world!")

if __name__ == '__main__':
    unittest.main()
