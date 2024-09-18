import sys

BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOOO.',
    ' ': '......', 'CAPITAL': '.....O', 'NUMBER': '.O.OOO',
}

BRAILLE_LOOKUP = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ',
}

LETTER_TO_NUMBER = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0',
}

# Define sets
UPPERCASE_SET = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
DIGIT_SET = set('0123456789')

# Define states
NORMAL, CAPITAL, NUMBER = 0, 1, 2

# Checks if the input string only contains Braille chars
def is_braille(input_str):
    return all(c in {'O', '.'} for c in input_str)

def braille_to_english(braille_str):
    """
    Converts a string of Braille characters to its English equivalent.
    Handles capitalization and numbers based on special Braille patterns.
    """

    result = []
    state = NORMAL
    n = len(braille_str)

    for i in range(0, n, 6):
        braille_char = braille_str[i:i+6]

        if braille_char == BRAILLE_DICT['CAPITAL']:
            state = CAPITAL
            continue
        elif braille_char == BRAILLE_DICT['NUMBER']:
            state = NUMBER
            continue

        char = BRAILLE_LOOKUP.get(braille_char, '')

        if not char:
            continue

        if state == NUMBER:
            num = LETTER_TO_NUMBER.get(char, '')
            if num:
                result.append(num)
            else:
                state = NORMAL
                if 'a' <= char <= 'z':
                    result.append(char.upper())
                else:
                    result.append(char)
        elif state == CAPITAL:
            result.append(char.upper())
            state = NORMAL
        else:
            result.append(char)

    return ''.join(result)

def english_to_braille(english_str):
    """
    Converts an English string to its Braille equivalent.
    Handles capitalization and numbers by inserting appropriate Braille patterns.
    """

    result = []
    state = NORMAL

    for char in english_str:
        if char in UPPERCASE_SET:
            result.append(BRAILLE_DICT['CAPITAL'])
            char = chr(ord(char) + 32)

        if char in DIGIT_SET:
            if state != NUMBER:
                result.append(BRAILLE_DICT['NUMBER'])
                state = NUMBER
            braille_char = BRAILLE_DICT.get(char, BRAILLE_DICT[' '])
            result.append(braille_char)
        else:
            if state == NUMBER:
                state = NORMAL
            if char == ' ':
                braille_char = BRAILLE_DICT[' ']
            else:
                braille_char = BRAILLE_DICT.get(char, BRAILLE_DICT[' '])
            result.append(braille_char)

    return ''.join(result)

def main():
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        translated = braille_to_english(input_str)
    else:
        translated = english_to_braille(input_str)

    print(translated)

if __name__ == "__main__":
    main()
