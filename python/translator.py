import sys

braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'cap': '.....O', 'decimal': '.0...0', 'num': '.O.OOO',
    '.': 'O..O.O', ',': 'O.....', '?': '.0O.O.', '!': '.O.O.O', ':': 'O..OOO', 
    ';': 'O.O.O.', '-': 'O.....', '/': 'O..O.O', '<': '.00..0', '>': '0..00.',
    '(': '.0.O..', ')': '.0.O..', ' ': '......', 
}

english_map = {v: k for k,  v in braille_map.items()}

def translate_to_braille(text):
    res = []
    num_mode = False

    for c in text:
        if c.isupper():
            res.append(braille_map['cap'])
            res.append(braille_map[c.lower()])
        elif c.isdigit():
            if not num_mode:
                res.append(braille_map['num'])
                num_mode = True
            res.append(braille_map[c])
        elif c in braille_map:
            res.append(braille_map[c])
            if num_mode:
                num_mode = False
        else:
            res.append(braille_map[' '])
    return ''.join(res)

def translate_to_english(text):
    res = []
    i = 0
    number_mode = False

    while i < len(text):
        braille_char = text[i:i+6]
        if braille_char == braille_map['cap']:
            next_char = text[i+6:i+12]
            res.append(english_map.get(next_char, '?').upper())
            i += 12
        elif braille_char == braille_map['num']:
            number_mode = True
            i += 6
        else:
            char = english_map.get(braille_char, '?')
            if number_mode and char.isalpha():
                res.append(str(ord(char) - ord('a') + 1))
                number_mode = False
            else:
                res.append(char)
            i += 6
    
    return ''.join(res)

def main():
    if len(sys.argv) < 2:
        return

    text = ' '.join(sys.argv[1:])

    if all(c in ['O', '.'] for c in text):
        print(translate_to_english(text))
    else:
        print(translate_to_braille(text))

if __name__ == "__main__":
    main()