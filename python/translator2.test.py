import unittest
import subprocess
import sys

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Use sys.executable to ensure we're using the same Python interpreter
        command = [sys.executable, "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Print debug information
        print("Command:", ' '.join(command))
        print("Stdout:", repr(result.stdout))
        print("Stderr:", repr(result.stderr))
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()