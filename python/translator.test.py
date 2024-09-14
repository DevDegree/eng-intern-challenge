import unittest
import subprocess
from helpers import detect_language

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

    def test_braille_to_english(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc 123 xYz"
        self.assertEqual(result.stdout.strip(), expected_output)
        
        command = ["python3", "translator.py", "O.OO...OO..."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "hi"
        self.assertEqual(result.stdout.strip(), expected_output)

        command = ["python3", "translator.py", ".....OO......O.OOOO....."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "A1"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_examples(self):
        # Test case 1: Input: "Hello world"
        command = ["python3", "translator.py", "Hello", "world"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)

        # Test case 2: Input: "42"
        command = ["python3", "translator.py", "42"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOOOO.O..O.O..."
        self.assertEqual(result.stdout.strip(), expected_output)

        # Test case 3: Input: ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc 123"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_detect_language(self):
        self.assertEqual(detect_language("O.OO.OOOO"), "Braille")
        self.assertEqual(detect_language("Hello123"), "English")
        self.assertEqual(detect_language("HeLLoWORLD"), "English")
        self.assertEqual(detect_language("Hello World"), "English")
        self.assertEqual(detect_language("O.O OOO"), "Braille")
        self.assertEqual(detect_language("!@#$%^&*()"), "English")
        self.assertEqual(detect_language("....."), "Braille")
        self.assertEqual(detect_language("OOOOOO"), "Braille")


if __name__ == '__main__':
    unittest.main()
