import unittest
import subprocess


class TestTranslator(unittest.TestCase):
    def test_hello_world(self):
        # Command to run translator.py script for "Hello world"
        command = ["python3", "translator.py", "Hello world"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected Braille output for "Hello world"
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_numbers(self):
        # Command to run translator.py script for "42"
        command = ["python3", "translator.py", "42"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected Braille output for "42"
        expected_output = ".O.OOOOO.O..O.O..."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english(self):
        # Command to run translator.py script for Braille to English conversion
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected English output for "Abc 123"
        expected_output = "Abc 123"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_empty(self):
        # Command to run translator.py script for Braille to English conversion
        command = ["python3", "translator.py", ]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected English output for "Abc 123"
        expected_output = ""

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
