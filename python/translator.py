import sys

# Braille character mappings
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

reverse_braille_map = {v: k for k, v in braille_map.items()}

def is_braille(input_str):
    return all(c in ['O', '.'] for c in input_str)

def translate_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_map['number'])
                number_mode = True
            result.append(braille_map[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False  
            if char.isupper():
                result.append(braille_map['capital'])
            result.append(braille_map[char.lower()])
        elif char == ' ':
            result.append(braille_map[' '])
            number_mode = False  
    return ''.join(result)

def translate_to_english(braille):
    result = []
    number_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i + 6]
        if symbol == braille_map['number']:
            number_mode = True
            i += 6
            continue
        if symbol == braille_map['capital']:
            i += 6
            symbol = braille[i:i + 6]
            char = reverse_braille_map.get(symbol, '?')
            result.append(char.upper())
            i += 6
        else:
            char = reverse_braille_map.get(symbol, '?')
            if number_mode and char in 'abcdefghijklmnopqrstuvwxyz':
                result.append(char)
            else:
                result.append(char)
            number_mode = False  
            i += 6
    return ''.join(result)

def main():
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if _name_ == "_main_":
    main()
