import sys
from typing import List, Dict

ENGLISH_TO_BRAILLE: Dict[str, str] = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'CAPITAL': '.....O', 'NUMBER': '.O.OOO', 'SPACE': '......'
}

BRAILLE_TO_ENGLISH: Dict[str, str] = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if not k.isdigit()}
BRAILLE_TO_NUMBER: Dict[str, str] = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k.isdigit()}

def is_braille(input_string: str) -> bool:
    return all(char in ('O', '.') for char in input_string)

def braille_to_english_translator(braille: str) -> str:
    translated: List[str] = []
    number_follows: bool = False
    capital_follows: bool = False

    for i in range(0, len(braille), 6):
        braille_char: str = braille[i:i+6]
        if braille_char == ENGLISH_TO_BRAILLE['CAPITAL']:
            capital_follows = True
        elif braille_char == ENGLISH_TO_BRAILLE['SPACE']:
            translated.append(' ')
            number_follows = False # reset after space
        elif braille_char == ENGLISH_TO_BRAILLE['NUMBER']:
            number_follows = True
        else:
            if number_follows and braille_char in BRAILLE_TO_NUMBER:
                char = BRAILLE_TO_NUMBER[braille_char]
            else:
                char = BRAILLE_TO_ENGLISH[braille_char]
                if capital_follows:
                    char = char.upper()
                    capital_follows = False
            translated.append(char)

    return ''.join(translated)

def english_to_braille_translator(text: str) -> str:
    translated: List[str] = []
    number_follows: bool = False

    for char in text:
        if char.isalpha():
            if char.isupper():
                translated.append(ENGLISH_TO_BRAILLE['CAPITAL'])
            translated.append(ENGLISH_TO_BRAILLE[char.lower()])
            number_follows = False
        elif char.isdigit():
            if not number_follows:
                translated.append(ENGLISH_TO_BRAILLE['NUMBER'])
                number_follows = True
            translated.append(ENGLISH_TO_BRAILLE[char])
        elif char == ' ':
            translated.append(ENGLISH_TO_BRAILLE['SPACE'])
            number_follows = False
        else:
            translated.append(ENGLISH_TO_BRAILLE[char])
            number_follows = False

    return ''.join(translated)

def main():
    input: List[str] = sys.argv[1:]
    input_string: str = ' '.join(input)

    if is_braille(input_string):
        translated: str = braille_to_english_translator(input_string)
        print(translated)
    else:
        translated: str = english_to_braille_translator(input_string)
        print(translated)


if __name__ == "__main__":
    main()
