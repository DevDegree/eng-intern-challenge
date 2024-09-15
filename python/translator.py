import sys

BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
}

BRAILLE_NUMBERS = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...'
}

BRAILLE_CONSTANTS = {
    'capital': '.....O',
    'number': '.O.OOO',
    'decimal': '.OOO.O',
    'space': '......',
}

BRAILLE_SYMBOLS = {
    '.': '..OO.O',
    ',': '..O...',
    ';': '..OO..',
    ':': '..OO..',
    '?': '..O.OO',
    '!': '..OOO.',
    '-': '....OO',
    '/': '.O..O.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    '>': 'O..OO.',
    '<': '.OO..O',
}

def is_braille(translation_input: str) -> bool:
    return all([char in ['.', 'O'] for char in translation_input]) and len(translation_input) % 6 == 0

def is_english(translation_input: str) -> bool:
    return all([char.isalnum() or char.isspace() for char in translation_input])

def english_to_braille(translation_input: str) -> str:
    translated_string = ''
    is_number = False
    is_capital = False

    for char in translation_input:
        if char.isnumeric():
            if not is_number:
                translated_string += BRAILLE_CONSTANTS['number']
                is_number = True
            translated_string += BRAILLE_NUMBERS[char]
        elif char.isalnum():
            if is_number:
                print(f'Invalid character: number and alphabet in the same word: {char}')
                sys.exit(1)
            if char.isupper():
                if not is_capital:
                    translated_string += BRAILLE_CONSTANTS['capital']
                    is_capital = True
                char = char.lower()
            translated_string += BRAILLE_ALPHABET[char]
        elif char == ' ':
            translated_string += BRAILLE_CONSTANTS['space']
            is_number = False
            is_capital = False
        elif char in BRAILLE_SYMBOLS:
            translated_string += BRAILLE_SYMBOLS[char]
        else:
            print(f'Invalid character: {char}')
            sys.exit(1)
    return translated_string


def braille_to_english(translation_input: str) -> str:
    translated_string = ''
    is_capital = False
    is_number = False
    process_numbers = False

    for i in range(0, len(translation_input), 6):
        char = translation_input[i:i + 6]
        if char == BRAILLE_CONSTANTS['capital']:
            is_capital = True
        elif char == BRAILLE_CONSTANTS['space']:
            translated_string += ' '
            is_number = False
            process_numbers = False
        elif char == BRAILLE_CONSTANTS['number']:
            is_number = True
            process_numbers = True
        elif char in BRAILLE_ALPHABET.values() and not process_numbers:
            if is_capital:
                translated_string += list(BRAILLE_ALPHABET.keys())[list(BRAILLE_ALPHABET.values()).index(char)].upper()
                is_capital = False
            else:
                translated_string += list(BRAILLE_ALPHABET.keys())[list(BRAILLE_ALPHABET.values()).index(char)]
        elif char in BRAILLE_NUMBERS.values():
            if is_number:
                translated_string += list(BRAILLE_NUMBERS.keys())[list(BRAILLE_NUMBERS.values()).index(char)]
                is_number = False
            elif process_numbers:
                translated_string += list(BRAILLE_NUMBERS.keys())[list(BRAILLE_NUMBERS.values()).index(char)]
            else:
                translated_string += list(BRAILLE_SYMBOLS.keys())[list(BRAILLE_SYMBOLS.values()).index(char)]
        else:
            print(f'Invalid character: {char}')
            sys.exit(1)

    return translated_string

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: Invalid number of arguments')
        sys.exit(1)

    input_string = sys.argv[1:]
    output = ''
    if is_braille(input_string[0]):
        output = braille_to_english(input_string[0])
    elif is_english(' '.join(input_string)):
        output = english_to_braille(' '.join(input_string))
    else:
        print('Invalid input')
        sys.exit(1)

    print(output)
    sys.exit(0)
