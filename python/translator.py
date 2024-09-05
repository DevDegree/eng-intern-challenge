import argparse
from typing import Dict

BRAILLE_TO_ENGLISH : Dict[str, str] = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O....O': 'u', 'O.O..O': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.O.O': 'y',
    'O..O.O': 'z', '......': 'SPACE',
    '.....O': 'CAPITAL',
    '.O.OOO': 'NUMBER'
}

BRAILLE_TO_NUMBER : Dict[str, str] = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

ENGLISH_TO_BRAILLE: Dict[str, str] = { v: k for k, v in BRAILLE_TO_ENGLISH.items() if not k.isdigit() }
NUMBER_TO_BRAILLE: Dict[str, str] = { v: k for k, v in BRAILLE_TO_NUMBER.items() if not k.isdigit() }

for k, v in BRAILLE_TO_ENGLISH.items():
    if v.islower():
        ENGLISH_TO_BRAILLE[v] = k

# Adding mapping for capital letters
for letter in 'abcdefghijklmnopqrstuvwxyz':
    ENGLISH_TO_BRAILLE[letter.upper()] = '.....O' + ENGLISH_TO_BRAILLE[letter]

# Map numbers since they have the same braille representations as chars a-j
for number, letter in zip('1234567890', 'abcdefghij'):
    ENGLISH_TO_BRAILLE[number] = '.O.OOO' + ENGLISH_TO_BRAILLE[letter]

def braille_to_english_translator(braille: str) -> str:
    translated = ''
    capital_follows = False
    number_follows = False
    i = 0

    while i < len(braille):
        braille_char = braille[i:i+6]
        if braille_char == '.....O':
            capital_follows = True
        elif braille_char == '.O.OOO':
            number_follows = True
        elif braille_char == '......':
            translated += ' '
            number_follows = False  # reset on space
        else:
            if number_follows:
                char = BRAILLE_TO_NUMBER.get(braille_char, '?')
            else:
                char = BRAILLE_TO_ENGLISH.get(braille_char, '?')
                if capital_follows:
                    char = char.upper()
                    capital_follows = False
            translated += char
        i += 6
    return translated.strip()

def english_to_braille_translator(english: str) -> str:
    #translated = ''
    translated: List[str] = []
    number_follows = False

    for char in english:
        if char == ' ':
            translated.append(ENGLISH_TO_BRAILLE['SPACE'])
            #translated += '......'
            number_follows = False
        elif char.isdigit():
            if not number_follows:
                translated.append(ENGLISH_TO_BRAILLE['NUMBER'])
                #translated += '.O.OOO'
                number_follows = True
            #translated += ENGLISH_TO_BRAILLE.get(char, '......')
            translated.append(NUMBER_TO_BRAILLE[char])
        else:
            number_follows = False
            #translated += ENGLISH_TO_BRAILLE.get(char, '......')
            translated.append(ENGLISH_TO_BRAILLE[char])
    return ''.join(translated)

def detect_input_type(input_string):
    braille_chars = {'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..',
                     'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..',
                     'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.',
                     'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.',
                     'O....O', 'O.O..O', '.OOO.O', 'OO...O', 'OO.O.O',
                     'O..O.O', '......', '.....O', '.O.OOO'
                     }

    if any(braille_char in input_string for braille_char in braille_chars):
        return 'braille'
    else:
        return 'english'

def main():
    parser = argparse.ArgumentParser(description="Translate between English and Braille")
    parser.add_argument('input_string', type=str)
    args = parser.parse_args()

    input_type = detect_input_type(args.input_string)

    if input_type == 'braille':
        print(braille_to_english_translator(args.input_string))
    else:
        print(english_to_braille_translator(args.input_string))

if __name__ == "__main__":
    main()
