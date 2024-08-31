import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_translation_capital_letters(self):
        command = ["python3", "translator.py", ".....OO.OO.."]
        expected_output = "H"
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_translation_numbers(self):
        command = ["python3", "translator.py", ".O.OOO" + "O....." + "O.O..." + "OO...."]
        expected_output = "123"
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_hello_world(self):
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        expected_output = "Hello world"
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_42(self):
        command = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]
        expected_output = "42"
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_braille_translation(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        expected_output = "Abc 123"
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_error_handling(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "123", "Abc"]
        expected_output = "Error: Unable to translate input text. Note that only basic Braille/English are supported."
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_error_handling_unsported_english_char(self):
        command = ["python3", "translator.py", "here!"]
        expected_output = "Error: Unable to translate input text. Note that only basic Braille/English are supported."
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_error_handling_invalid_braille_char(self):
        command = ["python3", "translator.py", "....OOO"]
        expected_output = "Error: Unable to translate input text. Note that only basic Braille/English are supported."
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
