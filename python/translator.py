import sys
from typing import Dict

# Mapping for Braille to text
BRAILLE_TO_TEXT: Dict[str, str] = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.O.OOO': 'number_start', '.....O': 'uppercase',
}

TEXT_TO_BRAILLE: Dict[str, str] = {char: code for code, char in BRAILLE_TO_TEXT.items()}

NUM_TO_BRAILLE: Dict[str, str] = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_TO_NUM: Dict[str, str] = {code: num for num, code in NUM_TO_BRAILLE.items()}

def convert_braille_to_text(braille_input: str) -> str:
    result: str = []
    is_uppercase: bool = False
    is_number: bool = False

    for i in range(0, len(braille_input), 6):
        braille_char: str = braille_input[i:i+6]

        if braille_char == '.....O':
            is_uppercase = True
        elif braille_char == '.O.OOO':
            is_number = True
        elif is_number:
            if braille_char in BRAILLE_TO_NUM:
                result.append(BRAILLE_TO_NUM[braille_char])
            elif braille_char == '......':
                result.append(' ')
                is_number = False
            else:
                is_number = False
        else:
            char: str = BRAILLE_TO_TEXT.get(braille_char, '')
            if is_uppercase:
                char = char.upper()
                is_uppercase = False
            result.append(char)

    return ''.join(result)

def convert_text_to_braille(text_input: str) -> str:
    result: str = []
    is_number_mode: bool = False

    for char in text_input:
        if char.isdigit():
            if not is_number_mode:
                result.append(TEXT_TO_BRAILLE['number_start'])
                is_number_mode = True
            result.append(NUM_TO_BRAILLE[char])
        elif char.isupper():
            result.append(TEXT_TO_BRAILLE['uppercase'])
            result.append(TEXT_TO_BRAILLE[char.lower()])
            is_number_mode = False
        else:
            result.append(TEXT_TO_BRAILLE.get(char, '......'))
            is_number_mode = False

    return ''.join(result)

def translate(input_str: str) -> str:
    if input_str[0] in 'O.':
        return convert_braille_to_text(input_str)
    return convert_text_to_braille(input_str)

def main() -> None:
    input_data: str = ' '.join(sys.argv[1:])
    output_data: str = translate(input_data)
    print(output_data)

if __name__ == "__main__":
    main()
