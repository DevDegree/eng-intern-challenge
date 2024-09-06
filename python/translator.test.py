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
        command = ["python3", "python/translator.py", "Kai1.5 xyz"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO...O.O......OO....O.OOOO......O...OO..O........OO..OOOO.OOOO..OOO"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
   
    def test_output5(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ".5"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".O.OOO..OO.OO..O.."
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_output6(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ">Hello"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "O..OO......OO.OO..O..O..O.O.O.O.O.O.O..OO."
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)


    def test_output7(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "kai .5"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "O...O.O......OO..........O.OOO..OO.OO..O.."
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    # Braille to English Tests


    def test_output8(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Abc 123 xYz"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output9(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Hello world"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output10(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ".O.OOOOO.O..O.O..."]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "42"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output11(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ".....OO...O.O......OO....O.OOOO......O...OO..O........OO..OOOO.OOOO..OOO"]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Kai1.5 xyz"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)    

    def test_output12(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ".O.OOO..OO.OO..O.."]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".5"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_output13(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........O.OOOO..O..O..OO.O....."]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "Hello 5>1"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output14(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "O...O.O......OO..........O.OOO..OO.OO..O.."]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = "kai .5"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
    

    def test_output15(self):
        # Command to run translator.py script
        command = ["python3", "python/translator.py", "Kai", "12 x",".OO.O..OOOO.O..OO.OOO.O...O.OO" ]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO...O.O......OO..........O.OOOO.....O.O.........OO..OO......stop?"
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
