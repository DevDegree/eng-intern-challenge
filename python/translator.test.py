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

    # reverse of the test above
    def test_braille_to_english(self):
        braille_input = ".....OO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        command = ["python3", "translator.py", braille_input]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "123 xYz"
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
