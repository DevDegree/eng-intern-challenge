import re
import sys

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
}

BRAILLE_TO_NUMBERS = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

BRAILLE_TO_INSTRUCTIONS = {
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number'
}

BRAILLE_TO_SYMBOLS = {
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': "/",
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
NUMBERS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMBERS.items()}
INSTRUCTIONS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_INSTRUCTIONS.items()}
SYMBOLS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_SYMBOLS.items()}

def english_to_braille(text):
    braille_text = ''
    number_mode = False
    
    for c in text:
        if c.isupper():
            braille_text += INSTRUCTIONS_TO_BRAILLE['capital']
            braille_text += ENGLISH_TO_BRAILLE[c.lower()]
            number_mode = False
        elif c.isdigit():
            if not number_mode:
                braille_text += INSTRUCTIONS_TO_BRAILLE['number']
                number_mode = True
            braille_text += NUMBERS_TO_BRAILLE[c]
        elif c == ' ':
            braille_text += SYMBOLS_TO_BRAILLE[' ']
            number_mode = False
        elif c in SYMBOLS_TO_BRAILLE:
            braille_text += SYMBOLS_TO_BRAILLE[c]
            number_mode = False
        else:
            braille_text += ENGLISH_TO_BRAILLE.get(c, '')
            number_mode = False

    return braille_text

def braille_to_english(braille_text):
    english_text = ''
    i = 0
    number_mode = False
    length = len(braille_text)

    while i < length:
        braille_char = braille_text[i:i+6]

        if braille_char == INSTRUCTIONS_TO_BRAILLE['capital']:
            next_char = braille_text[i+6:i+12]
            english_text += BRAILLE_TO_ENGLISH.get(next_char, '').upper()
            i += 12
        elif braille_char == INSTRUCTIONS_TO_BRAILLE['number']:
            number_mode = True
            i += 6
        elif braille_char in BRAILLE_TO_SYMBOLS:
            english_text += BRAILLE_TO_SYMBOLS.get(braille_char, '')
            i += 6
            number_mode = False
        elif number_mode:
            english_text += BRAILLE_TO_NUMBERS.get(braille_char, '')
            i += 6
        else:
            english_text += BRAILLE_TO_ENGLISH.get(braille_char, '')
            i += 6

    return english_text

def english_or_braille(text):
    braille_regex = re.compile(r'^[O. ]+$')

    if braille_regex.match(text):
        return 'Braille'
    
    return 'English'

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    text_type = english_or_braille(input_text)

    if text_type == 'Braille':
        translated_text = braille_to_english(input_text)
    else:
        translated_text = english_to_braille(input_text)

    print(translated_text)
