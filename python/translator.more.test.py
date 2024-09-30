import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        command = ["python", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_hello_world(self):
        command = ["python", "translator.py", "Hello", "world"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_number_42(self):
        command = ["python", "translator.py", "42"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".O.OOOOO.O..O.O..."
        self.assertEqual(result.stdout.strip(), expected_output)

    def test_braille_to_english(self):
        command = ["python", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc 123"
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_braille_to_english_for_first_case(self):
        command = ["python", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Abc 123 xYz"
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_braille_to_english_for_hello_world(self):
        command = ["python", "translator.py", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "Hello world"
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_braille_to_english_for_42(self):
        command = ["python", "translator.py", ".O.OOOOO.O..O.O..."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "42"
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_english_to_braille_where_number_and_words_alternate_but_no_space(self):
        command = ["python", "translator.py", "Hello42world"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO..O.OOOOO.O..O.O....OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_english_to_braille_where_number_and_letters_alternate_with_space(self):
        command = ["python", "translator.py", "Hello 4 2world"]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........O.OOOOO.O.........O.OOOO.O....OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        self.assertEqual(result.stdout.strip(), expected_output)
    
    def test_braille_to_english_where_number_and_capital_letters_alternate_but_no_space(self):
        command = ["python", "translator.py", ".....OO......O.OOOO..........OO.O...O.O..."]
        result = subprocess.run(command, capture_output=True, text=True)
        expected_output = "A1B2"
        self.assertEqual(result.stdout.strip(), expected_output)
    

if __name__ == '__main__':
    unittest.main()