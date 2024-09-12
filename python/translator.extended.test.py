import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_numbers_and_letters_to_braille(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_number_to_braille(self):
        command = ["python3", "translator.py", "42"] 
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOOOO.O..O.O..."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_letters_to_braille(self):
        command = ["python3", "translator.py", "Abc"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.....O.O...OO...."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_letters(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc"
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_braille_to_numbers(self):
        command = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "42"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_numbers_and_letters(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc 123"
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
