BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..OO.O', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', ' ': '......',
    'cap_follows': '.....O', 'decimal_follows': '.O...O', 'number_follows': '.O.OOO'
}

NUMBER_BRAILLE_DICT = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

ENGLISH_DICT = {v: k for k, v in BRAILLE_DICT.items() if k not in ['cap_follows', 'decimal_follows', 'number_follows']}

ENGLISH_NUMBER_DICT = {v: k for k, v in NUMBER_BRAILLE_DICT.items()}

def english_to_braille(text):
    result = ''
    number = False
    for char in text:
        if char.isupper():
            result += BRAILLE_DICT['cap_follows'] + BRAILLE_DICT[char.lower()]
        elif char.isdigit():
            if not number:
                result += BRAILLE_DICT['number_follows']
                number = True
            result += NUMBER_BRAILLE_DICT[char]
        elif char == ' ':
            number = False 
            result += BRAILLE_DICT[char]
        else:
            number = False
            result += BRAILLE_DICT.get(char, '......')
    return result

def braille_to_english(braille):
    result = ''
    i = 0
    is_capital = False
    is_number = False
    while i < len(braille):
        braille_char = braille[i:i+6]
        
        if braille_char == BRAILLE_DICT['cap_follows']:
            is_capital = True
        elif braille_char == BRAILLE_DICT['number_follows']:
            is_number = True
        elif braille_char == BRAILLE_DICT['decimal_follows']:
            result += '.'
        elif braille_char == '......':
            result += ' '
            is_number = False
        else:
            if braille_char in ENGLISH_DICT:
                if is_number:
                    result += ENGLISH_NUMBER_DICT.get(braille_char, '?')
                elif is_capital:
                    result += ENGLISH_DICT[braille_char].upper()
                    is_capital = False
                else:
                    result += ENGLISH_DICT.get(braille_char, '?')
            else:
                result += '?'
        i += 6
    return result

def main():
    import sys
    input_str = ' '.join(sys.argv[1:])

    if 'O' in input_str or '.' in input_str:
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == '__main__':
    main()
