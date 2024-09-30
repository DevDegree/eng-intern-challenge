
import sys

class BrailleTranslator:
    # Static mappings for Braille to English and vice versa
    braille_to_text = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '.....O': 'capital_marker', '.O...O': 'decimal_marker',
        '.O.OOO': 'number_marker', '..OO.O': '.', '..O...': ',', '..O.OO': '?',
        '..OOO.': '!', '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
        '.OO..O': '<', 'O..OOO': '>', 'O.O..O': '(', '.O.OO.': ')', '......': ' '
    }

    text_to_braille = {v: k for k, v in braille_to_text.items()}

    digits_to_braille = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

    special_chars = {
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
        ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OOO',
        '(': 'O.O..O', ')': '.O.OO.'
    }

    def __init__(self, input_text):
        self.input_text = input_text
        self.translation_result = []

    @staticmethod
    def is_braille_input(text):
        # Check if text only contains Braille valid chars and length is multiple of 6
        characters = text.replace(' ', '')
        return all(ch in ['O', '.'] for ch in characters) and len(characters) % 6 == 0

    @staticmethod
    def remove_spaces(string):
        return string.replace(" ", "")

    def convert_braille_to_text(self):
        """Convert Braille to English"""
        words = self.input_text.split(' ')
        capitalize_next = False
        is_number_mode = False

        for word in words:
            for index in range(0, len(word), 6):
                braille_char = word[index:index + 6]

                if braille_char == '.....O':  # Capital letter marker
                    capitalize_next = True
                    continue
                elif braille_char == '.O.OOO':  # Number marker
                    is_number_mode = True
                    continue

                if is_number_mode:
                    # Convert Braille number
                    self.translation_result.append(
                        list(self.digits_to_braille.keys())[list(self.digits_to_braille.values()).index(braille_char)]
                    )
                    continue  # Remain in number mode
                elif capitalize_next:
                    # Capitalize next letter
                    self.translation_result.append(self.braille_to_text[braille_char].upper())
                    capitalize_next = False
                else:
                    self.translation_result.append(self.braille_to_text.get(braille_char, ' '))

            self.translation_result.append(' ')  # Space between words
            is_number_mode = False  # Reset number mode at the end of each word

        return self.remove_spaces(''.join(self.translation_result).strip())

    def convert_text_to_braille(self):
        """Convert English text to Braille"""
        number_mode = False

        for char in self.input_text:
            if char.isdigit():
                if not number_mode:
                    self.translation_result.append('.O.OOO')  # Start number mode
                    number_mode = True
                self.translation_result.append(self.digits_to_braille[char])
            elif char.isupper():
                number_mode = False  # Exit number mode
                self.translation_result.append('.....O')  # Capital letter marker
                self.translation_result.append(self.text_to_braille[char.lower()])
            elif char == ' ':
                number_mode = False  # Exit number mode
                self.translation_result.append('......')  # Space marker
            elif char in self.text_to_braille:
                number_mode = False  # Exit number mode
                self.translation_result.append(self.text_to_braille[char])
            elif char in self.special_chars:
                self.translation_result.append(self.special_chars[char])
            else:
                continue  # Ignore unrecognized characters

        return self.remove_spaces(' '.join(self.translation_result).strip())

    def translate(self):
        """Determine whether to translate Braille to English or English to Braille"""
        if self.is_braille_input(self.input_text):
            return self.convert_braille_to_text()
        else:
            return self.convert_text_to_braille()


class TranslatorApp:
    def __init__(self):
        if len(sys.argv) < 2:
            print("Usage: python translator.py <input_text>")
            sys.exit(1)
        self.input_text = ' '.join(sys.argv[1:])

    def run(self):
        translator = BrailleTranslator(self.input_text)
        translation_result = translator.translate()
        print(translation_result)


if __name__ == "__main__":
    app = TranslatorApp()
    app.run()
