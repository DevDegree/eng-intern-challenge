import sys

BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Special Braille symbols
CAPITAL_BRAILLE = '.....O'
NUMBER_BRAILLE = '.O.OOO'
SPACE_BRAILLE = '......'


class Translator:

    def __init__(self):
        self.number_mode = False
        self.capital_mode = False

    def english_to_braille(self, english_text):
        braille_output = []  # List to store Braille output

        for char in english_text:

            # For digits
            if char.isdigit():
                if not self.number_mode:
                    braille_output.append(NUMBER_BRAILLE)
                    self.number_mode = True

                braille_output.append(BRAILLE_NUMBERS[char])

            elif char.isalpha():
                # For uppercase letters
                if char.isupper():
                    braille_output.append(CAPITAL_BRAILLE)

                braille_output.append(BRAILLE_ALPHABET[char.lower()])
                self.number_mode = False  # Exit number mode after letters
            
            # Handle spaces or any unknown symbols as spaces
            else:
                braille_output.append(BRAILLE_ALPHABET.get(char, SPACE_BRAILLE))
                self.number_mode = False  # Exit number mode for spaces or unknowns
        
        return ''.join(braille_output)

    def braille_to_english(self, braille_text):
        # Split Braille text into 6-character chunks
        braille_chars = [braille_text[i:i + 6] for i in range(0, len(braille_text), 6)]
        english_output = []  # List to store English output

        for braille_char in braille_chars:
            if braille_char == CAPITAL_BRAILLE:
                self.capital_mode = True

            elif braille_char == NUMBER_BRAILLE:
                self.number_mode = True

            elif braille_char == SPACE_BRAILLE:
                english_output.append(' ')
                self.number_mode = False
            else:
                # If in number mode, map Braille to a digit
                if self.number_mode:
                    digit = list(BRAILLE_NUMBERS.keys())[list(BRAILLE_NUMBERS.values()).index(braille_char)]
                    english_output.append(digit)

                else:
                    # If not, then map Braille to a letter
                    letter = list(BRAILLE_ALPHABET.keys())[list(BRAILLE_ALPHABET.values()).index(braille_char)]
                    if self.capital_mode:
                        english_output.append(letter.upper())
                        self.capital_mode = False

                    else:
                        english_output.append(letter)

                # Exit number mode after encountering a letter
                if braille_char in BRAILLE_ALPHABET.values() and braille_char not in BRAILLE_NUMBERS.values():
                    self.number_mode = False

        return ''.join(english_output)


if __name__ == "__main__":
    input_args = sys.argv[1:] # Get input arguments from command line
    input_string = ' '.join(input_args) # Join all input arguments into a single string
    translator = Translator()

    # For Braille input
    if all(c in '.O' for c in input_string):
        print(translator.braille_to_english(input_string))
    # For English input
    else:
        print(translator.english_to_braille(input_string))
