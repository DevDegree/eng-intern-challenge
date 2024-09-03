import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_empty_input(self):
        # Command to run translator.py script with empty input
        command = ["python3", "translator.py", ""]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output for empty input
        expected_output = ""
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
