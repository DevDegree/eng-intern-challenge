import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script with example arguments
        command = ["python3", "translator.py", "Abc 123 xYz"]
        
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Adjust expected_output to match the new mappings
        expected_output = "O..... O..... O.O... OO.... ...... O.OO.O O.....O.O.O. O.....O..OO. O.....OO.OOO"
        
        # Check if the actual output matches the expected output
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()