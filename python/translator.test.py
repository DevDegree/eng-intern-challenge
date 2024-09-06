import unittest
import subprocess

class TestTranslator(unittest.TestCase):

    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "Abc", "123", "xYz"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output1(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "Hello world"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output2(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "42"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".O.OOOOO.O..O.O..."
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output3(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "Kai1.5"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO...O.O......OO....O.OOOO......O...OO..O.."
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_output4(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "Kai1.5 xyz",]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO...O.O......OO....O.OOOO......O...OO..O........OO..OOOO.OOOO..OOO"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
