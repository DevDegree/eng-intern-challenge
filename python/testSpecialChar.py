import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_special_characters(self):
        # Command to run translator.py script with special characters
        command = ["python3", "translator.py", "Hey! $%^&*("]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output for special characters (example output, adjust as needed)
        expected_output = ".....O...O....O..O.O...O...O..O..O"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
