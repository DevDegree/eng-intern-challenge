import unittest
import subprocess

class DetailedTestTranslator(unittest.TestCase):

    def run_translator(self, input_string):
        # Command to run translator.py script
        command = ["python3", "translator.py", input_string]
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        # Return the stripped output for comparison
        return result.stdout.strip()

    def test_lowercase_letters(self):
        # Test all lowercase letters
        expected_braille = {
            "a": "O.....",
            "b": "O.O...",
            "c": "OO....",
            "d": "OO.O..",
            "e": "O..O..",
            "f": "OOO...",
            "g": "OOOO..",
            "h": "O.OO..",
            "i": ".OO...",
            "j": ".OOO..",
            "k": "O...O.",
            "l": "O.O.O.",
            "m": "OO..O.",
            "n": "OO.OO.",
            "o": "O..OO.",
            "p": "OOO.O.",
            "q": "OOOOO.",
            "r": "O.OOO.",
            "s": ".OO.O.",
            "t": ".OOOO.",
            "u": "O...OO",
            "v": "O.O.OO",
            "w": ".OOO.O",
            "x": "OO..OO",
            "y": "OO.OOO",
            "z": "O..OOO"
        }
        for letter, braille in expected_braille.items():
            with self.subTest(letter=letter):
                self.assertEqual(self.run_translator(letter), braille)

    def test_uppercase_letters(self):
        # Test all uppercase letters with correct universal application of "Capital follows"
        letter_to_braille = {
            "A": "O.....",  # Braille for 'A', same as 'a' with "Capital follows"
            "B": "O.O...",  # Braille for 'B', same as 'b' with "Capital follows"
            "C": "OO....",  # Braille for 'C', same as 'c' with "Capital follows"
            "D": "OO.O..",  # Braille for 'D', same as 'd' with "Capital follows"
            "E": "O..O..",  # Braille for 'E', same as 'e' with "Capital follows"
            "F": "OOO...",  # Braille for 'F', same as 'f' with "Capital follows"
            "G": "OOOO..",  # Braille for 'G', same as 'g' with "Capital follows"
            "H": "O.OO..",  # Braille for 'H', same as 'h' with "Capital follows"
            "I": ".OO...",  # Braille for 'I', same as 'i' with "Capital follows"
            "J": ".OOO..",  # Braille for 'J', same as 'j' with "Capital follows"
            "K": "O...O.",  # Braille for 'K', same as 'k' with "Capital follows"
            "L": "O.O.O.",  # Braille for 'L', same as 'l' with "Capital follows"
            "M": "OO..O.",  # Braille for 'M', same as 'm' with "Capital follows"
            "N": "OO.OO.",  # Braille for 'N', same as 'n' with "Capital follows"
            "P": "OOO.O.",  # Braille for 'P', same as 'p' with "Capital follows"
            "Q": "OOOOO.",  # Braille for 'Q', same as 'q' with "Capital follows"
            "R": "O.OOO.",  # Braille for 'R', same as 'r' with "Capital follows"
            "S": ".OO.O.",  # Braille for 'S', same as 's' with "Capital follows"
            "T": ".OOOO.",  # Braille for 'T', same as 't' with "Capital follows"
            "U": "O...OO",  # Braille for 'U', same as 'u' with "Capital follows"
            "V": "O.O.OO",  # Braille for 'V', same as 'v' with "Capital follows"
            "W": ".OOO.O",  # Braille for 'W', same as 'w' with "Capital follows"
            "X": "OO..OO",  # Braille for 'X', same as 'x' with "Capital follows"
            "Y": "OO.OOO",  # Braille for 'Y', same as 'y' with "Capital follows"
            "Z": "O..OOO"  # Braille for 'Z', same as 'z' with "Capital follows"
        }

        # Expected Braille output with "Capital follows" symbol prepended
        for letter, braille in letter_to_braille.items():
            expected_output = ".....O" + braille  # Add "Capital follows" + Braille letter
            with self.subTest(letter=letter):
                self.assertEqual(self.run_translator(letter), expected_output)

    def test_numbers(self):
        # Test all numbers with correct universal application of "Number follows"
        number_to_braille = {
            "1": "O.....",  # Braille for 1, same as 'a'
            "2": "O.O...",  # Braille for 2, same as 'b'
            "3": "OO....",  # Braille for 3, same as 'c'
            "4": "OO.O..",  # Braille for 4, same as 'd'
            "5": "O..O..",  # Braille for 5, same as 'e'
            "6": "OOO...",  # Braille for 6, same as 'f'
            "7": "OOOO..",  # Braille for 7, same as 'g'
            "8": "O.OO..",  # Braille for 8, same as 'h'
            "9": ".OO...",  # Braille for 9, same as 'i'
            "0": ".OOO.."  # Braille for 0, same as 'j'
        }

        # Expected Braille output with "Number follows" symbol prepended
        for number, braille in number_to_braille.items():
            expected_output = ".O.OOO" + braille  # Add "Number follows" + Braille digit
            with self.subTest(number=number):
                self.assertEqual(self.run_translator(number), expected_output)

    def test_special_characters(self):
        # Test special characters
        expected_braille = {
            ",": "..O...",  # Comma
            "?": "..O.OO",  # Question Mark
            "!": "..OOO.",  # Exclamation Mark
            ":": "..OO..",  # Colon
            ";": "..O.O.",  # Semicolon
            "-": "....OO",  # Hyphen
            "/": ".O..O.",  # Slash
            "<": ".OO..O",  # Less than
            "(": "O.O..O",  # Open parenthesis
            ")": ".O.OO.",  # Close parenthesis
            " ": "......"  # Space
        }
        for char, braille in expected_braille.items():
            with self.subTest(char=char):
                self.assertEqual(self.run_translator(char), braille)

if __name__ == '__main__':
    unittest.main()
