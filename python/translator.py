
import sys
from typing import Dict, List

class BrailleTranslator:

    LETTER_TO_BRAILLE: Dict[str, str] = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO'
    }

    NUMBER_TO_BRAILLE: Dict[str, str] = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

    PUNCTUATION_TO_BRAILLE: Dict[str, str] = {
        ' ': '......', '.': '..O...', ',': '..O...', '?': '..O.O.', '!': '..OO..', 
        ':': '..OO.', ';': '...O..', '-': '..O..O', '/': '...O.O', '<': 'O....O', 
        '>': '.O..OO', '(': 'O.O...', ')': '.O..O.'
    }

    BRAILLE_TO_LETTER: Dict[str, str] = {v: k for k, v in LETTER_TO_BRAILLE.items()}
    BRAILLE_TO_NUMBER: Dict[str, str] = {v: k for k, v in NUMBER_TO_BRAILLE.items()}
    BRAILLE_TO_PUNCTUATION: Dict[str, str] = {v: k for k, v in PUNCTUATION_TO_BRAILLE.items()}


    SPECIAL_INDICATORS: Dict[str, str] = {
        #For capitals, numbers and decimals
        'CAPITAL': '.....O',
        'NUMBER': '.O.OOO',
        'DECIMAL': '.O...O'
    }

    @classmethod
    def is_braille(cls, text: str) -> bool:
        #Check if the given text is valid Braille
        return set(text).issubset({'O', '.'}) and len(text) % 6 == 0

    @classmethod
    def braille_to_text(cls, braille: str) -> str:
       #Function to convert Braille to text.
        if not cls.is_braille(braille):
            raise ValueError("Invalid Braille input")

        result = []
        capitalize_next = number_mode = False

        i = 0
        while i < len(braille):
            char = braille[i:i+6]

            if char == cls.SPECIAL_INDICATORS['CAPITAL']:
                capitalize_next = True
            elif char == cls.SPECIAL_INDICATORS['NUMBER']:
                number_mode = True
            else:
                if number_mode:
                    if char in cls.BRAILLE_TO_NUMBER:
                        result.append(cls.BRAILLE_TO_NUMBER[char])
                    elif char == cls.PUNCTUATION_TO_BRAILLE['.']:
                        result.append('.')
                    else:
                        number_mode = False
                        if char in cls.BRAILLE_TO_LETTER:
                            letter = cls.BRAILLE_TO_LETTER[char]
                            if capitalize_next:
                                letter = letter.upper()
                                capitalize_next = False
                            result.append(letter)
                        elif char in cls.BRAILLE_TO_PUNCTUATION:
                            result.append(cls.BRAILLE_TO_PUNCTUATION[char])
                        else:
                            raise ValueError(f"Invalid Braille character: {char}")
                else:
                    if char in cls.BRAILLE_TO_LETTER:
                        letter = cls.BRAILLE_TO_LETTER[char]
                        if capitalize_next:
                            letter = letter.upper()
                            capitalize_next = False
                        result.append(letter)
                    elif char in cls.BRAILLE_TO_PUNCTUATION:
                        result.append(cls.BRAILLE_TO_PUNCTUATION[char])
                    else:
                        raise ValueError(f"Invalid Braille character: {char}")

            i += 6

        return ''.join(result)

    @classmethod
    def text_to_braille(cls, text: str) -> str:
       #Function to convert text to Braille.
        if cls.is_braille(text):
            raise ValueError("Invalid text input")

        result: List[str] = []
        number_mode = False

        for char in text:
            if char.isdigit():
                if not number_mode:
                    result.append(cls.SPECIAL_INDICATORS['NUMBER'])
                    number_mode = True
                result.append(cls.NUMBER_TO_BRAILLE[char])
            elif char == '.':
                if number_mode:
                    result.append(cls.SPECIAL_INDICATORS['DECIMAL'])
                else:
                    result.append(cls.PUNCTUATION_TO_BRAILLE[char])
                number_mode = False
            elif char.isalpha():
                if number_mode:
                    number_mode = False
                    result.append(cls.PUNCTUATION_TO_BRAILLE[' '])
                if char.isupper():
                    result.append(cls.SPECIAL_INDICATORS['CAPITAL'])
                    char = char.lower()
                result.append(cls.LETTER_TO_BRAILLE[char])
            elif char in cls.PUNCTUATION_TO_BRAILLE:
                result.append(cls.PUNCTUATION_TO_BRAILLE[char])
                number_mode = False
            else:
                raise ValueError(f"Untranslatable character: {char}")

        return ''.join(result)

    @classmethod
    def translate(cls, text: str) -> str:
        #Translate between Braille and text.
        if cls.is_braille(text):
            return cls.braille_to_text(text)
        else:
            return cls.text_to_braille(text)

def main() -> None:
    #Command-line interface for the Braille Translator.
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()

    try:
        result = translator.translate(input_text)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()