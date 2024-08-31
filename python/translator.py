import sys


class BrailleTranslator:

    CAPITAL = ".....O"
    SPACE = "......"
    DECIMAL = ".O...O"
    NUMBER = ".O.OOO"

    BRAILLE_TRANSLATIONS = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO',
    }

    ENGLISH_TRANSLATIONS = {v: k for k, v in BRAILLE_TRANSLATIONS.items()}

    BRAILLE_SPECIAL_CHARACTERS = {
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
        ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
        '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    }

    ENGLISH_SPECIAL_CHARACTERS = {v: k for k, v in BRAILLE_SPECIAL_CHARACTERS.items()}

    BRAILLE_NUMBERS = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
        '9': '.OO...', '0': '.OOO..',
    }

    ENGLISH_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

    def is_braille(self, input: str):
        """
        Determines if text is in Braille or English.

        input: a string containing the text in question.

        Return: a bool where True means the text is in Braille and False means it is in English.

        """
        return all(c in 'O.' for c in input)

    def english_to_braille(self, input: str):
        """
        Converts a text in the English alphabet to its equivalent in Braille.

        input: a string containing the english text to convert.

        Return: a list containing the converted text in Braille.
        """
        braille_text = []
        is_number = False
        is_decimal = False

        for char in input:
            if char.isupper():
                braille_text.append(self.CAPITAL)
                char = char.lower()
                braille_text.append(self.BRAILLE_TRANSLATIONS[char])
            elif char.islower():
                braille_text.append(self.BRAILLE_TRANSLATIONS[char])
            elif char.isspace():
                braille_text.append(self.SPACE)
                is_number = False
                is_decimal = False
            elif char.isdigit():
                if not is_number:
                    braille_text.append(self.NUMBER)
                    is_number = True
                braille_text.append(self.BRAILLE_NUMBERS[char])
            elif char == '.':
                if not is_decimal:
                    braille_text.append(self.DECIMAL)
                    is_decimal = True
            elif char in self.BRAILLE_SPECIAL_CHARACTERS:
                braille_text.append(self.BRAILLE_SPECIAL_CHARACTERS[char])
            else:
                raise ValueError("This character does not exist in this system definition for Braille") 
                # there are a few undefined special characters that are not implemented
                

        return ''.join(braille_text)

    def braille_to_english(self, input: str):
        """
        Converts a text Braille to its equivalent in the English alphabet.

        input: a string containing the Braille text to convert.

        Return: a list containing the converted text in English.
        """
        english_text = []
        next_num = False
        next_dec = False
        next_cap = False
        i = 0

        if len(input) % 6 != 0:
            raise ValueError("Incorrect Braille Message")

        while i < len(input):
            char = input[i : i + 6]

            if char == self.CAPITAL:
                next_cap = True
            elif char == self.DECIMAL:
                next_dec = True
            elif char == self.NUMBER:
                next_num = True
            elif char == self.SPACE:
                english_text.append(' ')
                next_num = False
                next_dec = False
            else:
                if next_num and char in self.ENGLISH_NUMBERS:
                    symbol = self.ENGLISH_NUMBERS[char]
                elif char in self.ENGLISH_TRANSLATIONS:
                    symbol = self.ENGLISH_TRANSLATIONS[char]
                elif char in self.ENGLISH_SPECIAL_CHARACTERS:
                    symbol = self.ENGLISH_SPECIAL_CHARACTERS[char]
                else:
                    raise ValueError("Incorrect Braille message")

                if symbol.isalpha() and next_cap:
                    symbol = symbol.upper()
                    next_cap = False
                elif next_dec:
                    english_text.append('.')
                    next_dec = False

                english_text.append(symbol)

            i += 6

        return "".join(english_text)


def main():

    if len(sys.argv) < 2:
        print("Incorrect usage")

    input = ' '.join(sys.argv[1:])

    braille_translator = BrailleTranslator()

    if braille_translator.is_braille(input):
        result = braille_translator.braille_to_english(input)
    else:
        result = braille_translator.english_to_braille(input)

    print(result)


if __name__ == "__main__":
    main()
