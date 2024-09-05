import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',

    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.O..O.',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.'
}

NUMBERS_TO_BRAILLE = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

# Inverted Maps for converting braille to string
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

CAPITAL_FLAG = '.....O'
NUMBER_FLAG = '.O.OOO'
SPACE = '......'

def translate_braille(input_string):
    result = ""
    is_upper_case = False
    is_number = False

    index = 0

    while index < len(input_string)/6:
        start_idx = 6 * index
        next_char = input_string[start_idx:start_idx + 6]

        if next_char == CAPITAL_FLAG:
            is_upper_case = True
        elif next_char == NUMBER_FLAG:
            is_number = True
        elif next_char == SPACE:
            is_number = False
            result += ' '
        else:
            if is_number:
                result += BRAILLE_TO_NUMBERS[next_char]
            elif is_upper_case:
                result += BRAILLE_TO_ENGLISH[next_char].upper()
                is_upper_case = False
            else:
                result += BRAILLE_TO_ENGLISH[next_char]

        index += 1

    return result

def translate_english(input_string):
    result = ""
    is_number = False

    for char in input_string:
        if char == ' ':
            is_number = False
            result += SPACE

        elif char.isdigit():
            if not is_number:
                is_number = True
                result += NUMBER_FLAG
            result += NUMBERS_TO_BRAILLE[char]

        else:
            if char.isupper():
                result += CAPITAL_FLAG
                char = char.lower()

            result += ENGLISH_TO_BRAILLE[char]

    return result

# check if the input string is provided in braille
def is_braille(input_string):
    if len(input_string) % 6 != 0:
        return False

    return all(char in ['.', 'O'] for char in input_string)

if __name__ == "__main__":
    input_string = ""

    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
    else:
        print("No string was provided as an argument.")
        sys.exit(1)

    result = ""
    if is_braille(input_string):
        result = translate_braille(input_string)
    else:
        result = translate_english(input_string)

    print(result)