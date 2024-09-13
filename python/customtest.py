import unittest
import subprocess

class TestEnglishToBraille(unittest.TestCase):
    def test_english_to_braille_all_letters_no_capital_letter_with_space(self):
        command = ["python3", "translator.py", "ab", "ef"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "O.....O.O.........O..O..OOO..."
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_english_to_braille_capital_letters_without_space(self):
        command = ["python3", "translator.py", "CA"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OOO.........OO....."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_english_to_braille_all_numbers_with_space(self):
        command = ["python3", "translator.py", "23", "4"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOOO.O...OO...........O.OOOOO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_english_to_braille_mixed_capital_letters_with_spaces_and_numbers(self):
        command = ["python3", "translator.py", "A", "2", "c", "4"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO............O.OOOO.O.........OO...........O.OOOOO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_english_to_braille_invalid_input(self):
        command = ["python3", "translator.py", "A", "Bcd", "2", "."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Special characters are not supported in this tool"
        self.assertEqual(result.stdout.strip(), expected_output)

class TestBrailleToEnglish(unittest.TestCase):
    def test_braille_to_english_all_letters_no_capital_letter_with_space(self):
        command = ["python3", "translator.py", "O.....O.O.........O..O..OOO..."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "ab ef"
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_braille_to_english_capital_letters_without_space(self):
        command = ["python3", "translator.py", ".....OOO.........OO....."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "CA"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english_all_numbers_with_space(self):
        command = ["python3", "translator.py", ".O.OOOO.O...OO...........O.OOOOO.O.."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "23 4"
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_braille_to_english_mixed_capital_letters_with_spaces_and_numbers(self):
        command = ["python3", "translator.py", ".....OO............O.OOOO.O.........OO...........O.OOOOO.O.."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "A 2 c 4"
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english_invalid_input(self):
        command = ["python3", "translator.py", ".....OO............O.OOOO.O.........OO...........O.OOOOO.O..O"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Special characters are not supported in this tool"
        self.assertEqual(result.stdout.strip(), expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
