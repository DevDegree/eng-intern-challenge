import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_english_to_braille(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = "Abc 123 xYz"

        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_to_brail_decimal(self):
        command = ["python3", "translator.py", "3.1"]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = ".O.OOOOO.....O...OO....."

        self.assertEqual(result.stdout.strip(), expected_output)

    def translate_braille_to_english_decimal(self):
        command = ["python3", "translator.py", ".O.OOOOO.....O...OO....."]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = "3.1"

        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_to_braille_period(self):
        command = ["python3", "translator.py", "3. 3"]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = ".O.OOOOO......OO.O.......O.OOOOO...."

        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english_period(self):
        command = ["python3", "translator.py", ".O.OOOOO......OO.O.......O.OOOOO...."]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = "3. 3"

        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()