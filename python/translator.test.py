import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_1(self):
        # Test with mixed input of letters and numbers
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_2(self):
        # Test with mixed input of letters and numbers
        command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output =  "Abc 123 xYz"
        self.assertEqual(result.stdout.strip(), expected_output)

    
    def test_mixed_case_and_numbers(self):
        # Test with mixed uppercase and lowercase letters and numbers
        command = ["python3", "translator.py", "Hi123"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.OO...OO....O.OOOO.....O.O...OO...."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_mixed_case_and_numbers_reverse(self):
        # Test with mixed uppercase and lowercase letters and numbers
        command = ["python3", "translator.py", ".....OO.OO...OO....O.OOOO.....O.O...OO...."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Hi123"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_mixed_case_and_numbers_2(self):
        # Test with mixed uppercase and lowercase letters and numbers
        command = ["python3", "translator.py", "123Hi"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOOO.....O.O...OO.........OO.OO...OO..."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_mixed_case_and_numbers_2_reverse(self):
        # Test with mixed uppercase and lowercase letters and numbers
        command = ["python3", "translator.py", ".O.OOOO.....O.O...OO.........OO.OO...OO..."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "123Hi"
        self.assertEqual(result.stdout.strip(), expected_output)


    def test_spaces(self):
        # Test with multiple spaces
        command = ["python3", "translator.py", "     "]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "......" * 5  # Braille output should handle spaces
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_spaces_reverse(self):
        # Test with multiple spaces
        command = ["python3", "translator.py", "......"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = " "
        self.assertEqual(result.stdout.strip('\n'), expected_output)

    def test_one_letter_reverse(self):
        # Test with multiple spaces
        command = ["python3", "translator.py", "O....."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "a" # Braille output should handle spaces
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_one_letter(self):
        # Test with multiple spaces
        command = ["python3", "translator.py", "a"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "O....." # Braille output should handle spaces
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
