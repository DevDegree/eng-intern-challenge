import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output_english(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        command_1 = ["python3", "translator.py", "Hello", "world"]
        command_2 = ["python3", "translator.py", "42"]
        command_3 = ["python3", "translator.py", "Abc", "123"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        result_1 = subprocess.run(command_1, capture_output=True, text=True)
        result_2 = subprocess.run(command_2, capture_output=True, text=True)
        result_3 = subprocess.run(command_3, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        expected_output_1 = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        expected_output_2 = ".O.OOOOO.O..O.O..."
        expected_output_3 = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        self.assertEqual(result_1.stdout.strip(), expected_output_1)
        self.assertEqual(result_2.stdout.strip(), expected_output_2)
        self.assertEqual(result_3.stdout.strip(), expected_output_3)

    def test_output_braille(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        command_1 = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        command_2 = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]
        command_3 = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        result_1 = subprocess.run(command_1, capture_output=True, text=True)
        result_2 = subprocess.run(command_2, capture_output=True, text=True)
        result_3 = subprocess.run(command_3, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "Abc 123 xYz"
        expected_output_1 = "Hello world"
        expected_output_2 = "42"
        expected_output_3 = "Abc 123"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
        self.assertEqual(result_1.stdout.strip(), expected_output_1)
        self.assertEqual(result_2.stdout.strip(), expected_output_2)
        self.assertEqual(result_3.stdout.strip(), expected_output_3)

if __name__ == '__main__':
    unittest.main()
