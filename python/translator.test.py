import unittest
import subprocess

"""
Individual test cases for the translator.py script

Contains some failing cases, I wish to demonstrate by ability to write tests. Have to submit it as is because of the time constraint.
"""

class TestTranslator(unittest.TestCase):
    def test_english_to_braille(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz", "Hello", "world1", "42", ":)"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO...........OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O...O.OOOO............O.OOOOO.O..O.O...........OO...O.OO."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english(self):
        # Command to run translator.py script
        braille_input = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO...........OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O...O.OOOO............O.OOOOO.O..O.O...........OO...O.OO."
        command = ["python3", "translator.py", braille_input]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "Abc 123 xYz Hello world1 42 :)"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    # > and o are same in braille, made the assumption > will only come after an opening
    def test_braille_to_english_edge_case_tribracket(self):
        # Command to run translator.py script
        braille_input = ".OO..OO..OO.O..OO."
        command = ["python3", "translator.py", braille_input]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "<>o"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    # case where braille input are given in multple arguments
    def test_braille_to_english_edge_case_diff_args(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO.", ".OOO.OO..OO.O.OOO.O.O.O.OO.O.."]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "Helloworld"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    # mostly braille but includes other char than . and O
    # just becomes a code
    def test_braille_to_english_edge_case_diff_args(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO.a"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "..OO.O..OO.O..OO.O..OO.O..OO.O.....OO..OO......OO..OO...OO.O.....OO..OO......OO..OO...OO.O..OO.O.....OO..OO...OO.O..OO.O.....OO..OO...OO.O..OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O..OO.O.....OO..OO......OO..OO...OO.OO....."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    # mostly braille but missing a dot, resulting in %6 != 0
    def test_braille_to_english_edge_case_diff_args(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".OOO.OO..OO.O.OOO.O.O.O.OO.O."]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "..OO.O.....OO..OO......OO..OO......OO..OO...OO.O.....OO..OO......OO..OO...OO.O..OO.O.....OO..OO......OO..OO...OO.O.....OO..OO...OO.O.....OO..OO......OO..OO......OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO......OO..OO...OO.O.....OO..OO...OO.O"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
