import unittest
import subprocess

class EnglishBraillePair:
    def __init__(self, english_text: str, braille_text: str):
        self.english_text = english_text
        self.braille_text = braille_text

class TestTranslator(unittest.TestCase):
    english_braille_pairs = [
        EnglishBraillePair(
            "Abc 123 xYz",
            ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        ),
        EnglishBraillePair(
            "Hello world",
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
        ),
        EnglishBraillePair("42", ".O.OOOOO.O..O.O..."),
        EnglishBraillePair("Abc 123", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."),
    ]

    def test_english_to_braille(self):
        for english_braille_pair in self.english_braille_pairs:
            # Split English text into list of arguments to pass to command
            english_text = english_braille_pair.english_text
            english_text_args = english_text.split(" ")

            # Command to run translator.py script
            command = ["python3", "translator.py"] + english_text_args

            expected_braille_text = english_braille_pair.braille_text
            
            # Run the command and capture output
            result = subprocess.run(command, capture_output=True, text=True)

            # Strip any leading/trailing whitespace from the output and compare
            self.assertEqual(result.stdout.strip(), expected_braille_text)

    def test_braille_to_english(self):
        for english_braille_pair in self.english_braille_pairs:
            # Command to run translator.py script
            command = ["python3", "translator.py", english_braille_pair.braille_text]

            expected_english_text = english_braille_pair.english_text

            # Run the command and capture output
            result = subprocess.run(command, capture_output=True, text=True)

            # Strip any leading/trailing whitespace from the output and compare
            self.assertEqual(result.stdout.strip(), expected_english_text)

if __name__ == '__main__':
    unittest.main()
