import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output_mixed_case(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    
    def test_output_all_lowercase(self):
        command = ["python3", "translator.py", "abc", "xyz"]
        
        expected_output = "0......0.0...00..........00..0000.0000..000"
        
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
        
        
    def test_empty_input(self):
        command = ["python3", "translator.py", ""]
        
        expected_output = ""
        
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_special_characters(self):
        # Command to run translator.py script with special characters
        command = ["python3", "translator.py", "!?>"]
        
        expected_output = "..000...0.000..00."
        
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)
        
        
    def test_output_numbers(self):
        command = ["python3", "translator.py", "123"]
        
        expected_output = ".000..0.0...00...."
        
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
