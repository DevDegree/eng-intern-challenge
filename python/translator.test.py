import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        command = ["python", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille(self):
        # Command to run translator.py script
        command_braille = ["python", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        
        # Run the command and capture output
        result_braille = subprocess.run(command_braille, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output_braille = "Abc 123"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result_braille.stdout.strip(), expected_output_braille)

if __name__ == '__main__':
    unittest.main()
