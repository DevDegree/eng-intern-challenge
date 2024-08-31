import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_original(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_alphabet_to_braille(self):
        command = ["python3", "translator.py", "abcdefghijklmnopqrstuvwxyz"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_alphabet_to_english(self):
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc 123 xYz"
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
