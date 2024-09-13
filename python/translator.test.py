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
