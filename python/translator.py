import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_specials = {
    '.': '.O.OO.',
    ',': 'O.....',
    '?': 'O.O...',
    '!': 'OO.O..',
    ':': 'O..O..',
    ';': 'O.O...',
    '-': 'O..O..',
    '/': '.O..O.',
    '(': 'O...O.',
    ')': 'O.O.O.',
    '<': 'O...O.',
    '>': 'O.O.O.',
    '\"': '......',
    '\'': '.O....'
}

CAP_MARKER = '.....O'
NUM_MARKER = '.O.OOO'
SPACE = '......'

english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_numbers = {v: k for k, v in braille_numbers.items()}
english_specials = {v: k for k, v in braille_specials.items()}

def translate_braille_to_english(braille):
    result = []
    is_capital = False
    number_mode = False
    i = 0

    while i < len(braille):
        segment = braille[i:i+6]
        i += 6

        if segment == CAP_MARKER:
            is_capital = True
            continue

        elif segment == NUM_MARKER:
            number_mode = True
            continue

        elif segment == SPACE:
            result.append(' ')
            number_mode = False
            continue

        if number_mode:
            char = english_numbers.get(segment, '')
            if char:
                result.append(char)
            else:
                number_mode = False
                char = english_alphabet.get(segment, '') or english_specials.get(segment, '')
                if is_capital:
                    char = char.upper()
                    is_capital = False
                result.append(char)
        else:
            char = english_alphabet.get(segment, '') or english_specials.get(segment, '')
            if is_capital:
                char = char.upper()
                is_capital = False
            result.append(char)

    return ''.join(result)

def translate_english_to_braille(text):
    result = []
    number_mode = False

    for i, char in enumerate(text):
        if char.isdigit():
            if not number_mode:
                result.append(NUM_MARKER)
                number_mode = True
            result.append(braille_numbers[char])
        else:
            if number_mode:
                number_mode = False
                if char.isalpha():
                    if char.isupper():
                        result.append(CAP_MARKER)
                    result.append(braille_alphabet[char.lower()])
                    continue

            if char == ' ':
                result.append(SPACE)
            elif char.isalpha():
                if char.isupper():
                    result.append(CAP_MARKER)
                result.append(braille_alphabet[char.lower()])
            elif char in braille_specials:
                result.append(braille_specials[char])

    return ''.join(result)


def detect_and_translate(input_string):
    if set(input_string).issubset({'O', '.'}):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)

if __name__ == "__main__":
    input_string = ''.join(sys.argv[1:])
    output = detect_and_translate(input_string)
    print(output)