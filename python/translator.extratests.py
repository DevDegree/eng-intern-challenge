import unittest
import subprocess


class TestTranslator(unittest.TestCase):
    def test_capitals_w_numbers(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_just_numbers(self):
        command = ["python3", "translator.py",
                   "42"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOOOO.O..O.O..."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_words_w_capitalization(self):
        command = ["python3", "translator.py",
                   "Hello world"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_numbers_w_space(self):
        command = ["python3", "translator.py", "0123", "0123"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOO.OOO..O.....O.O...OO...........O.OOO.OOO..O.....O.O...OO...."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_world(self):
        command = ["python3", "translator.py",
                   ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Hello world"
        self.assertEqual(result.stdout.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
