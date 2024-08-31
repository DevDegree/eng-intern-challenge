import sys
from enum import Enum
from typing import List, Dict

class BrailleSpecialChar(Enum):
    """Special Braille characters."""
    CAPITAL = '.....O'
    NUMBER = '.O.OOO'
    SPACE = '......'

class BrailleMapping:
    """Mappings between Braille and text characters."""
    ALPHABET: Dict[str, str] = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z'
    }
    NUMBERS: Dict[str, str] = {str(i): v for i, v in enumerate(ALPHABET.keys(), 1)}
    NUMBERS['0'] = ALPHABET['.OO...']  # '0' uses the same pattern as 'j'

    REVERSE_ALPHABET: Dict[str, str] = {v: k for k, v in ALPHABET.items()}
    REVERSE_NUMBERS: Dict[str, str] = {v: k for k, v in NUMBERS.items()}

class BrailleChar:
    """Represents a Braille character and its conversion to text."""
    def __init__(self, braille: str):
        self.braille = braille

    def to_text(self, number_mode: bool = False) -> str:
        """Convert Braille to text."""
        if self.braille == BrailleSpecialChar.SPACE.value:
            return ' '
        if number_mode:
            return BrailleMapping.REVERSE_NUMBERS.get(self.braille, '')
        return BrailleMapping.ALPHABET.get(self.braille, '')

class TextChar:
    """Represents a text character and its conversion to Braille."""
    def __init__(self, char: str):
        self.char = char

    def to_braille(self, number_mode: bool = False) -> str:
        """Convert text to Braille."""
        if number_mode and self.char.isdigit():
            return BrailleMapping.NUMBERS[self.char]
        if self.char.isalpha():
            return BrailleMapping.REVERSE_ALPHABET[self.char.lower()]
        if self.char.isspace():
            return BrailleSpecialChar.SPACE.value
        raise ValueError(f"Unsupported character: {self.char}")

class Validator:
    """Validates input for Braille and text."""
    @staticmethod
    def is_valid_braille(braille: str) -> bool:
        """Check if the input is valid Braille."""
        return all(c in 'O.' for c in braille) and len(braille) % 6 == 0

    @staticmethod
    def is_valid_text(text: str) -> bool:
        """Check if the input is valid text."""
        return all(c.isalnum() or c.isspace() for c in text)

    @staticmethod
    def validate(input_string: str, is_braille: bool) -> None:
        """Validate the input string."""
        if is_braille and not Validator.is_valid_braille(input_string):
            raise ValueError("Invalid Braille input")
        elif not is_braille and not Validator.is_valid_text(input_string):
            invalid_chars = [c for c in input_string if not (c.isalnum() or c.isspace())]
            raise ValueError(f"Unsupported character(s): {''.join(invalid_chars)}")

class Translator:
    """Translates between Braille and text."""
    @staticmethod
    def split_braille(braille: str) -> List[str]:
        """Split Braille string into individual characters."""
        return [braille[i:i+6] for i in range(0, len(braille), 6)]

    def braille_to_text(self, braille: str) -> str:
        """Convert Braille to text."""
        Validator.validate(braille, is_braille=True)
        result = []
        number_mode = capitalize_next = False

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
        """Convert text to Braille."""
        Validator.validate(text, is_braille=False)
        result = []
        number_mode = False

        for char in text:
            text_char = TextChar(char)
            if char.isdigit():
                if not number_mode:
                    result.append(BrailleSpecialChar.NUMBER.value)
                    number_mode = True
            elif number_mode:
                number_mode = False
            
            if char.isupper():
                result.append(BrailleSpecialChar.CAPITAL.value)
            
            result.append(text_char.to_braille(number_mode))

        return ''.join(result)
    
    def translate(self, input_string: str) -> str:
        """Translate between Braille and text."""
        if not input_string:
            return ""
        if Validator.is_valid_braille(input_string):
            return self.braille_to_text(input_string)
        return self.text_to_braille(input_string)

def main() -> None:
    """Main function to run the translator."""
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