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
        
#         # Strip any leading/trailing whitespace from the output and compare
#         self.assertEqual(result.stdout.strip(), expected_output)

class TestTranslatorCustom(unittest.TestCase):
    def test_mix_O_period_english_number(self):
        command = ["python3", "translator.py", "O..OHello40"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO..OO...OO.O..OO.O.....OO..OO......OO.OO..O..O..O.O.O.O.O.O.O..OO..O.OOOOO.O...OOO.."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_all_caps(self):
        command = ["python3", "translator.py", "ABC"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO..........OO.O........OOO...."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_string_length_but_only_one_alphabet(self):
        command = ["python3", "translator.py", "OO.O.a"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO..OO......OO..OO...OO.O.....OO..OO...OO.OO....."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_string_length_but_only_one_number(self):
        command = ["python3", "translator.py", "OO.O.4"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO..OO......OO..OO...OO.O.....OO..OO...OO.O.O.OOOOO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_incorrect_braille_correct_length(self):
        command = ["python3", "translator.py", ".O.O.O"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "..OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_incorrect_braille_incorrect_length(self):
        command = ["python3", "translator.py", ".O.O.O."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "..OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O"
        self.assertEqual(result.stdout.strip(), expected_output)

    # def test_only_punctuation(self):
    #     command = ["python3", "translator.py", "!?;:-/><)("]
    #     result = subprocess.run(command, capture_output=True, text=True)
    #     expected_output = "..OOO...O.OO..O.O...OO......OO.O..O.O..OO..OO..O.O.OO.O.O..O"
    #     self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english(self):
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Hello world"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_number(self):
        command = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "42"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english_and_number(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc 123"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_blank_string(self):
        command = ["python3", "translator.py", ""]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ""
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
