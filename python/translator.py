"""
Kristi Dodaj: Braille Translator Solution
"""

import sys

BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

REVERSE_BRAILLE_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}
REVERSE_BRAILLE_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

def translate_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.extend([BRAILLE_ALPHABET['cap'], BRAILLE_ALPHABET[char.lower()]])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                result.append(BRAILLE_ALPHABET['num'])
                number_mode = True
            result.append(BRAILLE_NUMBERS[char])
        elif char == ' ':
            result.append(BRAILLE_ALPHABET[' '])
            number_mode = False
        else:
            result.append(BRAILLE_ALPHABET.get(char, '......'))
            number_mode = False
    
    return ''.join(result)

def translate_to_english(braille):
    result = []
    is_capital = is_number = False
    
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == BRAILLE_ALPHABET['cap']:
            is_capital = True
        elif symbol == BRAILLE_ALPHABET['num']:
            is_number = True
        elif symbol == BRAILLE_ALPHABET[' ']:
            result.append(' ')
            is_number = False
        else:
            if is_number:
                result.append(REVERSE_BRAILLE_NUMBERS.get(symbol, ''))
            else:
                char = REVERSE_BRAILLE_ALPHABET.get(symbol, '')
                if is_capital:
                    char = char.upper()
                    is_capital = False
                result.append(char)
    
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        return

    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()