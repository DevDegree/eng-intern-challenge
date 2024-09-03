import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_mixed_input(self):
        # Command to run translator.py script with mixed input
        command = ["python3", "translator.py", "Hello World! 123"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output for mixed input (example output, adjust as needed)
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O....000........O.OOOO.....O.O...OO...."
            
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
