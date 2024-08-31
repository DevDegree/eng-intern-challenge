import sys
from enum import Enum
from typing import List, Dict

class BrailleSpecialChar(Enum):
    CAPITAL = '.....O'
    NUMBER = '.O.OOO'
    SPACE = '......'

class BrailleMapping:
    ALPHABET: Dict[str, str] = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z'
    }
    NUMBERS: Dict[str, str] = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

class BrailleChar:
    def __init__(self, braille: str):
        self.braille = braille

    def to_text(self, number_mode: bool = False) -> str:
        if self.braille == BrailleSpecialChar.SPACE.value:
            return ' '
        if number_mode:
            for num, braille in BrailleMapping.NUMBERS.items():
                if braille == self.braille:
                    return num
        return BrailleMapping.ALPHABET.get(self.braille, '')

class TextChar:
    def __init__(self, char: str):
        self.char = char

    def to_braille(self, number_mode: bool = False) -> str:
        if number_mode and self.char.isdigit():
            return BrailleMapping.NUMBERS[self.char]
        if self.char.isalpha():
            braille = {v: k for k, v in BrailleMapping.ALPHABET.items()}
            return braille[self.char.lower()]
        if self.char.isspace():
            return BrailleSpecialChar.SPACE.value
        raise ValueError(f"Unsupported character: {self.char}")

class BrailleValidator:
    @staticmethod
    def is_valid(braille: str) -> bool:
        return all(c in 'O.' for c in braille) and len(braille) % 6 == 0

    @staticmethod
    def validate(braille: str) -> None:
        if not BrailleValidator.is_valid(braille):
            raise ValueError("Invalid Braille input")

class TextValidator:
    @staticmethod
    def is_valid(text: str) -> bool:
        return all(c.isalnum() or c.isspace() for c in text)

    @staticmethod
    def validate(text: str) -> None:
        invalid_chars = [c for c in text if not (c.isalnum() or c.isspace())]
        if invalid_chars:
            raise ValueError(f"Unsupported character(s): {''.join(invalid_chars)}")

class Translator:
    @staticmethod
    def split_braille(braille: str) -> List[str]:
        return [braille[i:i+6] for i in range(0, len(braille), 6)]

    def braille_to_text(self, braille: str) -> str:
        BrailleValidator.validate(braille)
        result = []
        number_mode = False
        capitalize_next = False

        for char in self.split_braille(braille):
            braille_char = BrailleChar(char)
            if char == BrailleSpecialChar.NUMBER.value:
                number_mode = True
            elif char == BrailleSpecialChar.CAPITAL.value:
                capitalize_next = True
            elif char == BrailleSpecialChar.SPACE.value:
                result.append(' ')
                number_mode = False
            else:
                text = braille_char.to_text(number_mode)
                if text:
                    if capitalize_next:
                        text = text.upper()
                        capitalize_next = False
                    result.append(text)
                    if not text.isdigit():
                        number_mode = False

        return ''.join(result)

    def text_to_braille(self, text: str) -> str:
        TextValidator.validate(text)
        result = []
        number_mode = False

        for i, char in enumerate(text):
            text_char = TextChar(char)
            if char.isdigit():
                if not number_mode:
                    result.append(BrailleSpecialChar.NUMBER.value)
                    number_mode = True
            elif number_mode:
                # If we're in number mode and encounter a non-digit, exit number mode
                number_mode = False
            
            if char.isupper():
                result.append(BrailleSpecialChar.CAPITAL.value)
            
            result.append(text_char.to_braille(number_mode))

        return ''.join(result)
    
    def translate(self, input_string: str) -> str:
        if not input_string:
            return ""
        if BrailleValidator.is_valid(input_string):
            return self.braille_to_text(input_string)
        return self.text_to_braille(input_string)

def main() -> None:
    translator = Translator()
    try:
        if len(sys.argv) < 2:
            raise ValueError("No input string provided. Please provide a string to translate.")

        input_string = ' '.join(sys.argv[1:])
        output = translator.translate(input_string)
        print(output, end='')
        
    except ValueError as e:
        print(f"ValueError: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()