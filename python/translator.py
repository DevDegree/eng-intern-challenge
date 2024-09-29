import sys

class Translator:
    # Braille to English Mapping
    BRAILLE_TO_ENGLISH = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' '
    }

    # Reverse mapping for English to Braille
    ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

    # Braille representation for numbers (j to i in Braille represent numbers)
    LETTER_TO_NUMBER = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    }

    # Translate input string based on whether it's Braille or English
    def translate(self, input_str):
        if self.is_braille(input_str):
            return self.braille_to_english(input_str)
        else:
            return self.english_to_braille(input_str)

    # Check if input string is Braille
    def is_braille(self, input_str):
        return all(c in "O." for c in input_str) and len(input_str) % 6 == 0

    # Translate Braille to English
    def braille_to_english(self, braille_str):
        chunks = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
        result = ""
        is_capital = False
        is_number = False

        for chunk in chunks:
            if chunk == '.....O':  # Capital letter indicator
                is_capital = True
            elif chunk == '.O.OOO':  # Number indicator
                is_number = True
            elif chunk in self.BRAILLE_TO_ENGLISH:
                letter = self.BRAILLE_TO_ENGLISH[chunk]
                
                if letter == ' ':  # Handle spaces
                    result += ' '
                    is_number = False
                elif is_number:
                    result += self.LETTER_TO_NUMBER.get(letter, '?')
                elif is_capital:
                    result += letter.upper()
                    is_capital = False
                else:
                    result += letter
            else:
                result += '?'  # Handle unrecognized sequences

        return result

    # Translate English to Braille
    def english_to_braille(self, english_str):
        result = ""
        is_number = False

        for char in english_str:
            if char.isupper():  # Handle capital letters
                result += self.ENGLISH_TO_BRAILLE['capital']
                char = char.lower()

            if char.isdigit():  # Handle numbers
                if not is_number:
                    result += self.ENGLISH_TO_BRAILLE['number']
                    is_number = True
                letter = list(self.LETTER_TO_NUMBER.keys())[int(char)]
                result += self.ENGLISH_TO_BRAILLE[letter]
            elif char == ' ':  # Handle spaces
                result += self.ENGLISH_TO_BRAILLE[' ']
                is_number = False
            else:  # Handle regular letters
                result += self.ENGLISH_TO_BRAILLE.get(char, '......')

        return result


if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:])
    translator = Translator()
    print(translator.translate(input_str))
