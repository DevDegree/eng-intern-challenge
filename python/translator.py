<<<<<<< HEAD
"""
Author: Shidrath Rahman Haider
email: shidrathrahman365@gmail.com

Create a command line translator to convert A string
from English to Braille and visa versa

is_braille() : checks if the input is a braille input or not
translate_braille_to_english(): translate braille to english
translate_english_to_braille() : translate english to braille
translate() : determine the input type and translate accordingly
"""
import sys


class BrailleTranslator:
    def __init__(self):
        try:
            # Define the Braille mappings
            self.braille_to_english = {
                'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
                'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
                'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
                'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
                'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
                'O..OOO': 'z'
            }

            # Mapping for digits when preceded by number sign
            self.number_map = {
                'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
                'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0',
                'O': '>'
            }

            # Adding special characters English to Braille mapping
            self.special_chars = {
                '..OO.O': '.',   # Period
                '..O...': ',',   # Comma
                '..O.OO': '?',   # Question mark
                '..OOO.': '!',   # Exclamation mark
                '..OO..': ':',   # Colon
                '..O.O.': ';',   # Semicolon
                '....OO': '-',   # Dash
                '.O..O.': '/',   # Slash
                '.OO..O': '<',   # Less than
                'O..OO.': '>',   # Greater than
                'O.O..O': '(',   # Opening parenthesis
                '.O.OO.': ')',   # Closing parenthesis
                '......': ' ',  # Space
            }

            # Mapping for English to Braille including letters,digits, and special characters
            self.english_to_braille = {
                value: key for key, value in self.braille_to_english.items()
            }
            self.capital_sign = '.....O'
            self.number_sign = '.O.OOO'
            self.decimal_sign = '.O...O'

        except Exception as e:
            print(f"Error during initialization: {e}")

    def is_braille(self, text):
        """Check if the input text is in Braille."""
        try:
            return all(char in 'O.' for char in text.replace(' ', ''))
        except Exception as e:
            print(f"Error checking if the text is Braille: {e}")
            return False

    def translate_braille_to_english(self, braille_text):
        """Translate Braille text to English."""
        try:
            # Split the input into Braille words, assuming words are separated by spaces
            words = braille_text.split(' ')
            translated_words = []
            is_capital = False
            is_number = False

            for word in words:
                braille_chars = [word[i:i + 6] for i in range(0, len(word), 6)]
                translated_word = ''

                for braille_char in braille_chars:
                    if braille_char == self.capital_sign:
                        is_capital = True
                        continue

                    if braille_char == self.number_sign:
                        is_number = True
                        continue

                    # Translate Braille character to English
                    translated_char = self.braille_to_english.get(braille_char, '')

                    # Handle number mode
                    if is_number:
                        translated_char = self.number_map.get(translated_char.upper(), translated_char)

                    # Handle capitalization
                    if is_capital:
                        translated_char = translated_char.upper()
                        is_capital = False  # Reset after applying capitalization

                    translated_word += translated_char

                # Append the translated word with space for the next word
                translated_words.append(translated_word)

            # Join words with space
            return ' '.join(translated_words)
        except Exception as e:
            print(f"Error translating Braille to English: {e}")
            return ""

    def translate_english_to_braille(self, english_text):
        """Translate English text to Braille."""
        try:
            braille_output = []
            in_number_mode = False #Flag to track if we are in number
            for char in english_text:
                if char.isupper():
                    braille_output.append(self.capital_sign)
                    braille_output.append(
                        self.english_to_braille.get(char.lower(),''))
                    in_number_mode = False
                elif char.isdigit():
                    if not in_number_mode:
                        braille_output.append(self.number_sign)
                        in_number_mode = True # Set flag for number mode
                    # Translate digit to corresponding Braille character using self.number_map
                    braille_letter = chr(
                        ord('A') + int(char) - 1)  # Convert digit to corresponding letter (1 -> A, 2 -> B, etc.)
                    braille_output.append(self.english_to_braille.get(braille_letter.lower(), ''))
                elif char in self.special_chars:
                    braille_output.append(
                        self.special_chars.get(char,''))
                    in_number_mode = False
                elif char == ' ':
                    braille_output.append(' ')
                    in_number_mode = False
                else:
                    braille_output.append(self.english_to_braille.get(char, ''))
                    in_number_mode = False

            return ' '.join(braille_output)
        except Exception as e:
            print(f"Error translating English to Braille: {e}")
            return ""

    def translate(self, input_text):
        """Determine the input type and translate accordingly."""
        try:
            if self.is_braille(input_text):
                return self.translate_braille_to_english(input_text)
            else:
                return self.translate_english_to_braille(input_text)
        except Exception as e:
            print(f"Error during translation: {e}")
            return ""


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Usage: python braille_translator.py <word1> <word2> ...")
            sys.exit(1)

        input_text = ' '.join(sys.argv[1:])
        translator = BrailleTranslator()
        translation = translator.translate(input_text)
        print(translation)
    except Exception as e:
        print(f"Error in main execution: {e}")
=======

>>>>>>> upstream/main
