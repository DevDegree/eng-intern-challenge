import sys
#!/usr/bin/env python3
from typing import List

class BrailleTranslator:
    # Constants for special indicators
    CAPITAL = '.....O'
    NUMBER = '.O.OOO'
    SPACE = '......'
    DECIMAL = '.O...O'
    
    # Mappings for translations
    ENGLISH_TO_BRAILLE = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': SPACE
    }

    NUM_TO_BRAILLE = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }
    
    PUNCTUATION_TO_BRAILLE = {
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
        ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
        '(': 'O.O..O', ')': '.O.OO.'
    }

    # Reverse mappings for Braille to English
    BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
    BRAILLE_TO_NUM = {v: k for k, v in NUM_TO_BRAILLE.items()}
    BRAILLE_TO_PUNCTUATION = {v: k for k, v in PUNCTUATION_TO_BRAILLE.items()}

    def __init__(self, input_text: str):
        self.input_text = input_text

    def is_braille(self) -> bool:
        # Determine if the input is Braille by checking characters
        return all(c in {'O', '.'} for c in self.input_text) and len(self.input_text) % 6 == 0

    def translate_to_braille(self, text: str) -> str:
        # Convert English text to Braille
        output = []
        is_number = False

        for char in text:
            if char.isdigit():
                if not is_number:
                    output.append(self.NUMBER)  # Enter number mode
                    is_number = True
                output.append(self.NUM_TO_BRAILLE[char])
            elif char.isalpha():
                if char.isupper():
                    output.append(self.CAPITAL)  # Capitalization
                output.append(self.ENGLISH_TO_BRAILLE[char.lower()])
                is_number = False  # Exit number mode after letter
            elif char in self.PUNCTUATION_TO_BRAILLE:
                output.append(self.PUNCTUATION_TO_BRAILLE[char])
                is_number = False
            elif char == ' ':
                output.append(self.SPACE)
                is_number = False

        return ''.join(output)

    def translate_to_english(self, braille: str) -> str:
        # Convert Braille text to English
        output = []
        is_capital = False
        is_number = False

        for i in range(0, len(braille), 6):
            symbol = braille[i:i + 6]

            if symbol == self.CAPITAL:
                is_capital = True
            elif symbol == self.NUMBER:
                is_number = True
            elif symbol == self.SPACE:
                output.append(' ')
                is_number = False  # Reset number mode on space
            elif is_number and symbol in self.BRAILLE_TO_NUM:
                output.append(self.BRAILLE_TO_NUM[symbol])
            elif is_capital and symbol in self.BRAILLE_TO_ENGLISH:
                output.append(self.BRAILLE_TO_ENGLISH[symbol].upper())
                is_capital = False  # Reset capitalization after use
            elif symbol in self.BRAILLE_TO_ENGLISH:
                output.append(self.BRAILLE_TO_ENGLISH[symbol])
            elif symbol in self.BRAILLE_TO_PUNCTUATION:
                output.append(self.BRAILLE_TO_PUNCTUATION[symbol])

        return ''.join(output)

    def translate(self) -> str:
        # Determine input type and perform the corresponding translation
        if self.is_braille():
            return self.translate_to_english(self.input_text)
        else:
            return self.translate_to_braille(self.input_text)


def main():
    # Capture input from command line
    input_text = ' '.join(sys.argv[1:])

    # Create translator object
    translator = BrailleTranslator(input_text)
    
    # Translate input and print the result
    try:
        result = translator.translate()
        print(result)
    except Exception as e:
        print(f"Error during translation: {e}")


if __name__ == "__main__":
    main()
