import unittest
import subprocess

class TestTranslator(unittest.TestCase):

    def check_english_to_braille(self, english_str, braille_str):
        command = ["python3", "translator.py", english_str]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), braille_str)

    def check_braille_to_english(self, english_str, braille_str):
        command = ["python3", "translator.py", braille_str]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), english_str)
    
    def test_example(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
   
    def test_translate_empty_strings(self):
        english_str = ''
        braille_str = ''
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_translate_only_space(self):
        english_str = ' '
        braille_str = '......'
        self.check_english_to_braille(english_str, braille_str)

        # Stdout can't read the single space?
        # self.check_braille_to_english(english_str, braille_str)

    def test_only_capital(self):
        english_str = "ABC"
        braille_str = ".....OO..........OO.O........OOO...."
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_only_lowercase(self):
        english_str = "abc"
        braille_str = "O.....O.O...OO...."
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_only_numbers(self):
        english_str = "42"
        braille_str = ".O.OOOOO.O..O.O..."
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_only_symbols(self):
        english_str = ".,!"
        braille_str = ".O...O..OO.O.O...O..O....O...O..OOO."
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_alpha_with_spaces(self):
        english_str = "Hello world"
        braille_str = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_alpha_and_numbers(self):
        english_str = "Abc 123"
        braille_str = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_alternating_alpha_and_numbers(self):
        english_str = '1a2b3c'
        braille_str = '.O.OOOO...........O......O.OOOO.O.........O.O....O.OOOOO..........OO....'
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_alpha_and_numbers_and_symbols(self):
        english_str = '<mNo>? 123!'
        braille_str = '.O...O.OO..OOO..O......OOO.OO.O..OO..O...OO..OO..O...O..O.OO.......O.OOOO.....O.O...OO...........O...O..OOO.'
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)

    def test_translate_invalid_braille(self):
        english_str = ''
        braille_str = 'OOOOOO'
        self.check_braille_to_english(english_str, braille_str)

    def test_should_translate_to_english(self):
        invalid_braille_str = 'O....'
        expected_braille_output = '.....OO..OO..O...O..OO.O.O...O..OO.O.O...O..OO.O.O...O..OO.O'
        self.check_english_to_braille(invalid_braille_str, expected_braille_output)

    def test_should_translates_to_braille(self):
        english_str = 'a'
        braille_str = 'O.....'
        self.check_english_to_braille(english_str, braille_str)
        self.check_braille_to_english(english_str, braille_str)


if __name__ == '__main__':
    unittest.main()
