#small note, the input in the github for '.....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..' actually returns Abc 234, not Abc 123 like its stated in the github. Thank you.
#By Omar Al-Dulaimi
import sys
from typing import Dict

ENG_TO_BRAILLE: Dict[str, str] = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'CAP': '.....O', 'NUM': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_TO_ENG: Dict[str, str] = {v: k for k, v in ENG_TO_BRAILLE.items()}

NUMBER_TO_LETTER: Dict[str, str] = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

LETTER_TO_NUMBER: Dict[str, str] = {v: k for k, v in NUMBER_TO_LETTER.items()}

def text_to_braille(text: str) -> str:

    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(ENG_TO_BRAILLE['NUM'])
                number_mode = True
            result.append(ENG_TO_BRAILLE[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(ENG_TO_BRAILLE['CAP'])
            result.append(ENG_TO_BRAILLE[char.lower()])
        elif char == ' ':
            number_mode = False
            result.append(ENG_TO_BRAILLE[char])
        else:
            result.append('......') 

    return ''.join(result)

def braille_to_text(braille: str) -> str:

    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        chunk = braille[i:i+6]
        
        if chunk == ENG_TO_BRAILLE['CAP']:
            capitalize_next = True
        elif chunk == ENG_TO_BRAILLE['NUM']:
            number_mode = True
        elif chunk in BRAILLE_TO_ENG:
            char = BRAILLE_TO_ENG[chunk]
            if number_mode and char in NUMBER_TO_LETTER:
                result.append(LETTER_TO_NUMBER[char])
            else:
                if char == ' ' or char not in NUMBER_TO_LETTER:
                    number_mode = False
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)
        else:
            result.append('?') 
        
        i += 6

    return ''.join(result)

def is_braille(input_string: str) -> bool:

    return all(char in 'O.' for char in input_string)

def main() -> None:

    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate>")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        print(braille_to_text(input_string))
    else:
        print(text_to_braille(input_string))

if __name__ == "__main__":
    main()
