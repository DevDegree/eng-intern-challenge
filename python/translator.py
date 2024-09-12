from typing import Dict, List
from enum import Enum, auto
import sys
class CharacterType(Enum):
    LETTER = auto()
    NUMBER = auto()
    SPECIAL = auto()

class BrailleTranslator:
    # Braille mappings
    BRAILLE_MAP: Dict[str, str] = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
        'z': 'O..OOO',
        
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        
        ' ': '......',
        'capital': '.....O',  # Capitalization indicator
        'number': '.O.OOO',   # Number indicator
    }
    
    # Reverse maps for easy lookup from Braille to English
    REVERSE_MAP: Dict[CharacterType, Dict[str, str]] = {
        CharacterType.LETTER: {v: k for k, v in BRAILLE_MAP.items() if k.isalpha()},
        CharacterType.NUMBER: {v: k for k, v in BRAILLE_MAP.items() if k.isdigit()},
        CharacterType.SPECIAL: {v: k for k, v in BRAILLE_MAP.items() if k in ['capital', 'number']}
    }

    def __init__(self):
        pass
    
    @staticmethod
    def is_braille(text: str) -> bool:
        """Determines if the given text is in Braille format."""
        return set(text).issubset({'O', '.'})
    
    def translate_to_braille(self, text: str) -> str:
        """Translates English text to Braille."""
        braille_output: List[str] = []
        in_number_mode: bool = False

        for char in text:
            if char.isdigit():
                if not in_number_mode:
                    braille_output.append(self.BRAILLE_MAP['number'])
                    in_number_mode = True
                braille_output.append(self.BRAILLE_MAP[char])
            else:
                if in_number_mode and char != '.':
                    in_number_mode = False
                if char.isupper():
                    braille_output.append(self.BRAILLE_MAP['capital'])
                    braille_output.append(self.BRAILLE_MAP[char.lower()])
                elif char.lower() in self.BRAILLE_MAP:
                    braille_output.append(self.BRAILLE_MAP[char.lower()])
                else:
                    raise ValueError(f"Unrecognized character in English text: '{char}'")
        
        return ''.join(braille_output)
    
    def translate_to_english(self, braille_text: str) -> str:
        """Translates Braille text to English."""
        english_output: List[str] = []
        i: int = 0
        capital_next: bool = False
        in_number_mode: bool = False

        while i < len(braille_text):
            braille_char: str = braille_text[i:i+6]  # Get the next 6 characters (a Braille character)

            # Handle special cases: capital and number indicators
            if braille_char == self.BRAILLE_MAP['capital']:
                capital_next = True
            elif braille_char == self.BRAILLE_MAP['number']:
                in_number_mode = True

            # Handle spaces to exit number mode if needed
            elif braille_char == self.BRAILLE_MAP[' ']:
                english_output.append(' ')
                in_number_mode = False

            # Handle number characters
            elif in_number_mode and braille_char in self.REVERSE_MAP[CharacterType.NUMBER]:
                char = self.REVERSE_MAP[CharacterType.NUMBER][braille_char]
                english_output.append(char)

            # Handle letters
            elif braille_char in self.REVERSE_MAP[CharacterType.LETTER]:
                char = self.REVERSE_MAP[CharacterType.LETTER][braille_char]
                if capital_next:
                    char = char.upper()
                    capital_next = False
                english_output.append(char)
                in_number_mode = False  # Reset number mode after a letter

            else:
                raise ValueError(f"Unrecognized Braille character: '{braille_char}'")

            i += 6

        return ''.join(english_output)

    def translate(self, input_text: str) -> str:
        """Determines the type of input and translates accordingly."""
        if self.is_braille(input_text):
            return self.translate_to_english(input_text)
        else:
            return self.translate_to_braille(input_text)


if __name__ == "__main__":    
    translator = BrailleTranslator()
    
    if len(sys.argv) > 1:
        input_text: str = ' '.join(sys.argv[1:])
        print(translator.translate(input_text))
    else:
        print("Please provide text to translate as command-line arguments.")
