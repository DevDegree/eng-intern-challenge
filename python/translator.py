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
    'capital_follows': '.....O', 
    'decimal_follows': '.O...O', 
    'number_follows': '.O.OOO',
    ' ': '......'
}

NUMBER_TO_BRAILLE = {
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

BRAILLE_TO_ENGLISH = dict(zip(ENGLISH_TO_BRAILLE.values(), ENGLISH_TO_BRAILLE.keys()))
BRAILLE_TO_NUMBER = dict(zip(NUMBER_TO_BRAILLE.values(), NUMBER_TO_BRAILLE.keys()))

# Braille if char is multiple of 6 and only contains . or O
def is_braille(str):
    if len(str) % 6:
        return False

    for c in str:
        if c != '.' and c != 'O':
            return False
    return True

def braille_to_english(text):
    english_res = ""
    is_numbers_follows = False
    is_capital_follows = False
    size = 6

    for i in range(0, len(text), size):
        text_to_convert = text[i: i + size]
        char = BRAILLE_TO_ENGLISH[text_to_convert]
        if char == 'capital_follows':
            is_capital_follows = True
            continue
        elif char == 'number_follows':
            is_numbers_follows = True
            continue
        elif char == ' ':
            is_numbers_follows = False
    
        if is_numbers_follows:
            char = BRAILLE_TO_NUMBER[text_to_convert]
            english_res += char
        elif is_capital_follows:
            char = char.upper()
            is_capital_follows = False
            english_res += char

    return english_res


def english_to_braille(text):
    braille_res = ""
    is_numbers_follows = False
    for char in text:
        if char.isdigit():
            if not is_numbers_follows:
                braille_res += ENGLISH_TO_BRAILLE['number_follows']
                is_numbers_follows = True
            braille_res += NUMBER_TO_BRAILLE[char]
            continue

        if char.isupper():
            braille_res += ENGLISH_TO_BRAILLE['capital_follows']
            char = char.lower()
        is_numbers_follows = False

        braille_res += ENGLISH_TO_BRAILLE[char]

    return braille_res


if len(sys.argv) < 2:
    print('Error: Not sufficient argument to translate')

text = ' '.join(sys.argv[1:])
if is_braille(text):
    print(braille_to_english(text))
else:
    print(english_to_braille(text))
