import sys

# Braille mapping for letters (lowercase and capital) and numbers
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  # Space
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

BRAILLE_CAPITAL = '.....O'  # Braille capital symbol
BRAILLE_NUMBER = '.O.OOO'   # Braille number symbol

# Reverse map to look up Braille strings from English characters
ENGLISH_MAP = {v: k for k, v in BRAILLE_MAP.items()}

def is_braille(input_str):
    return all(c in "O." for c in input_str)

def translate_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(BRAILLE_CAPITAL)
            char = char.lower()
        if char.isdigit() and not number_mode:
            result.append(BRAILLE_NUMBER)
            number_mode = True
        if not char.isdigit() and number_mode:
            number_mode = False
        result.append(BRAILLE_MAP.get(char, '......'))
    
    return ''.join(result)

def translate_to_english(braille):
    result = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capital_mode = False
    number_mode = False

    for symbol in braille_chars:
        if symbol == BRAILLE_CAPITAL:
            capital_mode = True
            continue
        if symbol == BRAILLE_NUMBER:
            number_mode = True
            continue
        char = ENGLISH_MAP.get(symbol, ' ')
        if capital_mode:
            char = char.upper()
            capital_mode = False
        if number_mode and char.isdigit():
            number_mode = False
        result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])  # Join arguments into a single string

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

