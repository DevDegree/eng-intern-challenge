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

    def test_all_english_to_braille(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234567890", "abcdefghijklmnopqrstuvwxyz"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".....OO..........OO.O........OOO.........OOO.O.......OO..O.......OOOO........OOOOO.......OO.OO.......O.OO........O.OOO.......OO...O......OO.O.O......OOO..O......OOO.OO......OO..OO......OOOO.O......OOOOOO......OO.OOO......O.OO.O......O.OOOO......OO...OO.....OO.O.OO.....O.OOO.O.....OOO..OO.....OOO.OOO.....OO..OOO.......O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO........O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_all_braille_to_english(self):
        # Command to run translator.py script
        command = [
            "python3",
            "translator.py",
            ".....OO..........OO.O........OOO.........OOO.O.......OO..O.......OOOO........OOOOO.......OO.OO.......O.OO........O.OOO.......OO...O......OO.O.O......OOO..O......OOO.OO......OO..OO......OOOO.O......OOOOOO......OO.OOO......O.OO.O......O.OOOO......OO...OO.....OO.O.OO.....O.OOO.O.....OOO..OO.....OOO.OOO.....OO..OOO.......O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO........O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO"
        ]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 abcdefghijklmnopqrstuvwxyz"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
