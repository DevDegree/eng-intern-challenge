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

    def test_hello_world(self):
        command = ["python3", "translator.py", "Hello", "world"]
        
        result = subprocess.run(command, capture_output=True, text=True)
             
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."

        self.assertEqual(result.stdout.strip(), expected_output)

    def test_empty_input(self):
        command = ["python3", "translator.py"]
        
        result = subprocess.run(command, capture_output=True, text=True)
             
        expected_output = ""

        self.assertEqual(result.stdout.strip(), expected_output)

    def test_numbers(self):
        command = ["python3", "translator.py", "42"]
        
        result = subprocess.run(command, capture_output=True, text=True)
             
        expected_output = ".O.OOOOO.O..O.O..."

        self.assertEqual(result.stdout.strip(), expected_output)


    def test_single_letter_and_decimal(self):
        command = ["python3", "translator.py", "A", "1.2"]

        result = subprocess.run(command, capture_output=True, text=True)
        
        expected_output = ".....O" + "O....." + "......" + ".O.OOO" + "O....." + ".O...O" + "O.O..."

        self.assertEqual(result.stdout.strip(), expected_output)

    def test_special_characters(self):
        command = ["python3", "translator.py", "<", "a", "!"]

        result = subprocess.run(command, capture_output=True, text=True)

        expected_output =   ".OO..O" + "......" + "O....." + "......" + "..OOO."


        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()