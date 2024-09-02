import re
import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
}

SYMBOL_TO_BRAILLE = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    ' ': '......'
}

INSTRUCTION_TO_BRAILLE = {
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

NUMBER_TO_BRAILLE = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...',
}


def reverse_mapping(dictionary):
    return {value: key for key, value in dictionary.items()}


BRAILLE_TO_ENGLISH = reverse_mapping(ENGLISH_TO_BRAILLE)
BRAILLE_TO_NUMBER = reverse_mapping(NUMBER_TO_BRAILLE)
BRAILLE_TO_INSTRUCTION = reverse_mapping(INSTRUCTION_TO_BRAILLE)
BRAILLE_TO_SYMBOL = reverse_mapping(SYMBOL_TO_BRAILLE)


def braille_to_english(sequence):
    translated = ""
    index = 0
    capitalize = False
    num_flag = False

    while index < len(sequence):
        braille = sequence[index:index + 6]
        if braille == INSTRUCTION_TO_BRAILLE['decimal']:
            translated += "."
            index += 12  # Consumes instruction and decimal braille chars
            continue
        elif braille == INSTRUCTION_TO_BRAILLE['number']:
            num_flag = True
        elif braille == INSTRUCTION_TO_BRAILLE['capital']:
            capitalize = True
        elif braille in BRAILLE_TO_SYMBOL:
            translated += BRAILLE_TO_SYMBOL[braille]
            if BRAILLE_TO_SYMBOL[braille] == ' ':
                num_flag = False
        elif num_flag is True:
            translated += BRAILLE_TO_NUMBER[braille]
        else:  # Alphabet
            if capitalize:
                translated += BRAILLE_TO_ENGLISH[braille].upper()
                capitalize = False
            else:
                translated += BRAILLE_TO_ENGLISH[braille]
        index += 6

    return translated


def english_to_braille(sequence):
    translated = ""
    num_flag = False

    for char in sequence:
        if char.isdigit():
            if not num_flag:  # First number in sequence
                num_flag = True
                translated += INSTRUCTION_TO_BRAILLE['number']  # number follows
            translated += NUMBER_TO_BRAILLE[char]
            continue

        if char in SYMBOL_TO_BRAILLE:
            if num_flag and char == '.':
                translated += INSTRUCTION_TO_BRAILLE['decimal']
            elif char == ' ':  # broke out of number sequence, so reset the flag
                num_flag = False
            translated += SYMBOL_TO_BRAILLE[char]
        else:
            if char.isupper():
                translated += INSTRUCTION_TO_BRAILLE['capital']
            translated += ENGLISH_TO_BRAILLE[char.lower()]

    return translated


def english_or_braille(sequence):
    regex = re.compile(r'^[.O]+$')

    if len(sequence) % 6 == 0 and regex.match(sequence):
        return "Braille"

    return "English"


if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])

    system = english_or_braille(input_text)

    if system == "Braille":
        result = braille_to_english(input_text)
    else:
        result = english_to_braille(input_text)

    print(result)
