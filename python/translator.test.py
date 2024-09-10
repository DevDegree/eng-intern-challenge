import unittest
import subprocess

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

    def test_output_ASCII_to_braille_0(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Hello", "world"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_ASCII_to_braille_1(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "42"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".O.OOOOO.O..O.O..."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_ASCII_to_braille_2(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_ASCII_to_braille_3(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "abc", "123"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "O.....O.O...OO...........O.OOOO.....O.O...OO...."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_ASCII(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Abc 123 xYz"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_ASCII_0(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Hello world"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_ASCII_1(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "42"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_ASCII_2(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Abc 123"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_ASCII_3(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "O.....O.O...OO...........O.OOOO.....O.O...OO...."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "abc 123"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
