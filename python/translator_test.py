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
        
    def test_Hello_world(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Hello", "world"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_Abc_123(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_42(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "42"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".O.OOOOO.O..O.O..."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_Braille_1(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output =  "Abc 123 xYz"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_Braille_2(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Hello world"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_Braille_3(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Abc 123"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_Braille_4(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "42"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_Braille_5(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "..OO.O"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_punc_1(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "..."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "..OO.O..OO.O..OO.O"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_punc_2(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "...OO"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "..OO.O..OO.O..OO.O.....OO..OO......OO..OO."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_punc_3(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "...OO)"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "..OO.O..OO.O..OO.O.....OO..OO......OO..OO..O.OO."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_punc_4(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "..OO.O."]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "..OO.O..OO.O.....OO..OO......OO..OO...OO.O.....OO..OO...OO.O"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_punc_5(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "..OO.O..OO.O.....OO..OO......OO..OO...OO.O.....OO..OO...OO.O"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "..OO.O."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_dec_1(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "1.2"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".O.OOOO......O...OO.O..."
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        
    def test_dec_2(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".O.OOOOO.....O...OO.......OO.O"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "3.1"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
