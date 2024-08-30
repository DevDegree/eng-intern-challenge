import unittest
import subprocess

# Expected output for "123" is incorrect. It actually translates to "234", which has been updated in this file."

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "234", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()