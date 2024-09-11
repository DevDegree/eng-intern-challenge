# Test suite to rigorously test the translator.py file

import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def run_translator(self, input_str):
        '''
        Function to run the translator.py script with the given input string
        '''
        # Split the input string into a list of arguments
        command = ['python3', 'translator.py'] + input_str.split()
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
        input_str = "HELLO WORLD"
        expected_output = ".....OO.OO.......OO..O.......OO.O.O......OO.O.O......OO..OO............O.OOO.O.....OO..OO......OO.OOO......OO.O.O......OOO.O.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_only_numbers(self):
        input_str = "1231232024"
        expected_output = ".O.OOOO.....O.O...OO....O.....O.O...OO....O.O....OOO..O.O...OO.O.."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_braille_to_english(self):
        input_str = "O.OO..O..O..O.O.O.O.O.O.O..OO."
        expected_output = "hello"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_braille_to_english_with_numbers(self):
        input_str = ".O.OOOO.....O.O...OO...............OO.OO..O..O..O.O.O.O.O.O.O..OO........O.OOOO.....O.O...OO...."
        expected_output = "123 Hello 123"
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_number_letter_edge_case(self):
        '''
        This case should return a space in between number and letter due to behaviour of "number follows" mode
        '''
        input_str = "2t"
        expected_output = ".O.OOOO.O..........OOOO."
        self.assertEqual(self.run_translator(input_str), expected_output)

    def test_translate_back(self):
        '''
        The test should return the original string when translating from english to braille and back
        '''
        input_str = "Hello World"
        # Gets braille
        output_str = self.run_translator(input_str)
        # Translates back
        self.assertEqual(self.run_translator(output_str), input_str)

    def test_empty_input(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(self.run_translator(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()