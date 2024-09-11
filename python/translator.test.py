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

    def test_output_eng_to_braille_1(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Hello", "world"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_eng_to_braille_2(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "42"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".O.OOOOO.O..O.O..."

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_eng_to_braille_all_num(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "1234567890"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output ='.O.OOO' + 'O.....' + 'O.O...' + 'OO....' + 'OO.O..' + 'O..O..' + 'OOO...' + 'OOOO..' + 'O.OO..' + '.OO...' + '.OOO..'

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_eng_to_braille_all_char(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "abcdefghijklmnopqrstuvwxyz"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = 'O.....' + 'O.O...' + 'OO....' + 'OO.O..' + 'O..O..' + 'OOO...' + 'OOOO..' + 'O.OO..' + '.OO...' + '.OOO..' + 'O...O.' + 'O.O.O.' + 'OO..O.' + 'OO.OO.' + 'O..OO.' + 'OOO.O.' + 'OOOOO.' + 'O.OOO.' + '.OO.O.' + '.OOOO.' + 'O...OO' + 'O.O.OO' + '.OOO.O' + 'OO..OO' + 'OO.OOO'+ 'O..OOO'

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_eng_1(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "Hello world"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_eng_2(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", ".O.OOOOO.O..O.O..."]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "42"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_eng_all_num(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", '.O.OOO' + 'O.....' + 'O.O...' + 'OO....' + 'OO.O..' + 'O..O..' + 'OOO...' + 'OOOO..' + 'O.OO..' + '.OO...' + '.OOO..']

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = '1234567890'
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_invalid(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "!?!?!?!?!"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ""

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_output_braille_to_eng_all_char(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", 'O.....' + 'O.O...' + 'OO....' + 'OO.O..' + 'O..O..' + 'OOO...' + 'OOOO..' + 'O.OO..' + '.OO...' + '.OOO..' + 'O...O.' + 'O.O.O.' + 'OO..O.' + 'OO.OO.' + 'O..OO.' + 'OOO.O.' + 'OOOOO.' + 'O.OOO.' + '.OO.O.' + '.OOOO.' + 'O...OO' + 'O.O.OO' + '.OOO.O' + 'OO..OO' + 'OO.OOO'+ 'O..OOO']

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = "abcdefghijklmnopqrstuvwxyz"

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)
if __name__ == '__main__':
    unittest.main()
