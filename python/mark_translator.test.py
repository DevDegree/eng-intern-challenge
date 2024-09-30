import unittest
import subprocess

from constants import *

class TestTranslator(unittest.TestCase):
    # Convert a string to Braille and back to the original string
    def perform_bijection_test(self, input: str):
        # Command to run translator.py script
        command = ["python3", "translator.py", input.strip()]
        result = subprocess.run(command, capture_output=True, text=True)

        reverse_command = ["python3", "translator.py", result.stdout.strip()]
        result = subprocess.run(reverse_command, capture_output=True, text=True)
        
        # Strip any leading/trailing whitespace from the output and ensure it matches the initial input
        self.assertEqual(result.stdout.strip(), input)

    def test_valid_bijections(self):
        test_strings = [
            "Abc",
            "123",
            "xYz",
            "HAHAHAAA",
            "abcdefghijklmnopqrstuvwxyz",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "1234567890",
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
            "a b c d e f g h i j k l m n o p q r s t u v w x y z",
            "1 2 3 4 5 6 7 8 9 0",
            "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",
            "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0",
            "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",
            "a123 b456 c789 d0 e1 f2 g3 h4 i5 j6 k7 l8 m9 n0 o1 p2 q3 r4 s5 t6 u7 v8 w9 x0 y1 z2",
        ]

        for test_string in test_strings:
            self.perform_bijection_test(test_string)

    def test_invalid_input(self):
        invalid_inputs = [
            "abc!",
            "@",
            "123.456",
            "O.OOOA",
            "A4C",
            "2A",
            "OOOOOOOOOOO.",
            ".O...O",
            "O.O.O",
            BRAILLE_CAPITAL_MODIFIER,
            BRAILLE_NUMBER_MODIFIER,
            BRAILLE_NUMBER_MODIFIER + BRAILLE_CAPITAL_MODIFIER + ENGLISH_TO_BRAILLE["k"],
            BRAILLE_CAPITAL_MODIFIER + BRAILLE_NUMBER_MODIFIER + ENGLISH_TO_BRAILLE["a"],
            BRAILLE_CAPITAL_MODIFIER + " ",
            BRAILLE_NUMBER_MODIFIER + ENGLISH_TO_BRAILLE["k"],
            BRAILLE_NUMBER_MODIFIER + ENGLISH_TO_BRAILLE[" "],
            BRAILLE_CAPITAL_MODIFIER + ENGLISH_TO_BRAILLE[" "],
        ]

        for invalid_input in invalid_inputs:
            result = subprocess.run(["python3", "translator.py", invalid_input], capture_output=True, text=True)
            self.assertFalse(result.returncode == 0, f"Invalid input '{invalid_input}' was accepted.")

    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
