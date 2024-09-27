import unittest
import subprocess


class TestTranslatorCustom(unittest.TestCase):
    def test_hello_world(self):
        command = ["python3", "translator.py", "Hello", "world"]
        result = subprocess.run(command, capture_output=True, text=True)

        self.assertEqual(result.stdout.strip(), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        result = subprocess.run(command, capture_output=True, text=True)

        self.assertEqual(result.stdout.strip(), "Hello world")

    def test_Abc_123_xYz(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_42(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "42"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".O.OOOOO.O..O.O..."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_Abc_123(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "Abc 123"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_decimal(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "1.3"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".O.OOO" + "O....." + ".O...O" + "OO...."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
