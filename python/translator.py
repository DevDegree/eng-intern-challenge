import sys

class BrailleConverter:
    def __init__(self):
        # Braille mappings
        self.english_to_braille = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
            'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
            '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
            '0': '.OOO..', 'capital': '.....O', 'number': '.O.OOO', ' ': '......'
        }

        # Reverse mapping for Braille to English
        self.braille_to_english = {v: k for k, v in self.english_to_braille.items() if k not in '1234567890'}

        # Number mode translation (braille to numbers)
        self.number_translation = {
            'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
            'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0', '......': ' '
        }

    # Check if the input string consists only of Braille characters (O and .)
    def is_braille(self, input_string):
        return all(char in 'O.' for char in input_string)

    # Validate that the Braille string has a length that is a multiple of 6
    def validate_braille(self, input_string):
        if len(input_string) % 6 != 0:
            raise ValueError("Braille input is malformed: each character should be 6 dots.")

    # Validate that the English string contains only supported characters
    def validate_english(self, input_string):
        valid_chars = set(self.english_to_braille.keys()).union(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '))
        invalid_chars = set(input_string) - valid_chars
        if invalid_chars:
            raise ValueError(f"Invalid characters found: {', '.join(invalid_chars)}")

    # Convert a Braille string to English
    def convert_braille_to_english(self, input_string):
        try:
            self.validate_braille(input_string)  # Ensure the Braille string is valid
        except ValueError as e:
            return str(e)

        result, number_mode, next_capital = '', False, False

        for i in range(0, len(input_string), 6):
            current_braille = input_string[i:i + 6]

            if number_mode:
                symbol = self.number_translation[current_braille]
                if symbol == ' ':
                    number_mode = False
                result += symbol
            else:
                symbol = self.braille_to_english[current_braille]
                if symbol == 'number':
                    number_mode = True
                    next_capital = False
                elif symbol == 'capital':
                    next_capital = True
                elif next_capital:
                    result += symbol.upper()
                    next_capital = False
                else:
                    result += symbol

        return result

    # Convert an English string to Braille
    def convert_english_to_braille(self, input_string):
        try:
            self.validate_english(input_string)  # Ensure valid English input
        except ValueError as e:
            return str(e)

        result, number_mode = '', False

        for char in input_string:
            if not char.isdigit():
                number_mode = False
            if char.isdigit() and not number_mode:
                result += self.english_to_braille['number']
                number_mode = True
            elif char.isupper():
                result += self.english_to_braille['capital']
            result += self.english_to_braille[char.lower()]

        return result

    # Determine whether the input is Braille or English, and convert accordingly
    def process_input(self, input_string):
        if self.is_braille(input_string):
            return self.convert_braille_to_english(input_string)
        else:
            return self.convert_english_to_braille(input_string)


def main():
    try:
        input_string = ' '.join(sys.argv[1:])
        converter = BrailleConverter()
        print(converter.process_input(input_string))
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

