import sys
from typing import Dict


BRAILLE_TO_CHAR: Dict[str, str] = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.O.OOO': '#', '.....O': 'capital',
}

CHAR_TO_BRAILLE: Dict[str, str] = {v: k for k, v in BRAILLE_TO_CHAR.items()}

NUM_TO_BRAILLE: Dict[str, str] = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_TO_NUM: Dict[str, str] = {v: k for k, v in NUM_TO_BRAILLE.items()}

def is_braille(input: str) -> bool:
    return True if all(c in 'O.' for c in input) else False

def translate_braille_to_english(input: str) -> str:
    translated = ""
    is_capital = False
    is_number = False

    for i in range(0, len(input), 6):
        braille_char = input[i:i+6]
        if braille_char == '.....O':
            is_capital = True
            continue
        if braille_char == '.O.OOO':
            is_number = True
            continue

        if is_number:
            if braille_char in NUM_TO_BRAILLE.values():
                translated += BRAILLE_TO_NUM[braille_char]
            elif braille_char in BRAILLE_TO_CHAR and BRAILLE_TO_CHAR[braille_char] == " ":
                is_number = False
                translated += " "
        else:
            char = BRAILLE_TO_CHAR[braille_char]
            if is_capital:
                char = char.upper()
                is_capital = False
            translated += char
    
    return translated

def translate_english_to_braille(input: str) -> str:
    translated = ""
    number_mode = False
    
    for char in input:
        if char.isdigit():
            if not number_mode:
                translated += CHAR_TO_BRAILLE['#']
                number_mode = True
            translated += NUM_TO_BRAILLE[char]
        elif char.isupper():
            translated += CHAR_TO_BRAILLE['capital']
            translated += CHAR_TO_BRAILLE[char.lower()]
            number_mode = False
        else:
            translated += CHAR_TO_BRAILLE.get(char, '......')
            number_mode = False
    
    return translated

def main():
    if len(sys.argv) < 2:
        sys.exit("Need to provide an argument")

    input_str = ' '.join(sys.argv[1:])

    try:
        if is_braille(input_str):
            return print(translate_braille_to_english(input_str))
        else:
            return print(translate_english_to_braille(input_str))
    except ValueError:
        sys.exit("Input is invalid.")
    except:
        sys.exit("Something went wrong.")

if __name__ == "__main__":
    main()