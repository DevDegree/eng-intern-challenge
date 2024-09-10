import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'
}

capital_follows = '.....O'
number_follows = '.O.OOO'

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


english_braille_map = {v: k for k, v in braille_alphabet.items()}
english_number_map = {v: k for k, v in braille_numbers.items()}

def translate_to_braille(text: str) -> str:
    out = []
    is_number_mode = False
    for char in text:
        if char.isdigit():
            if not is_number_mode:
                out.append(number_follows) 
                is_number_mode = True
            out.append(braille_numbers[char])
            continue
        elif is_number_mode:
            out.append("......")
            is_number_mode = False
        if char.isupper():
            out.append(capital_follows)
            out.append(braille_alphabet[char.lower()])
        else:
            out.append(braille_alphabet[char])
    return ''.join(out)


def translate_to_english(braille: str) -> str:
    out = []
    i = 0
    is_number_mode = False
    
    while i < len(braille):
        chunk = braille[i:i+6]
        if is_number_mode and chunk == "......":
            is_number_mode = False
        elif is_number_mode:
            out.append(english_number_map[chunk])
        elif chunk == capital_follows:
            i += 6
            chunk = braille[i:i+6]
            out.append(english_braille_map[chunk].upper())
        elif chunk == number_follows:
            is_number_mode = True
        else:
            out.append(english_braille_map[chunk])
        i += 6
    return ''.join(out)
        

inp = " ".join(sys.argv[1:])

isBraille = True
if len(inp) % 6 != 0:
    isBraille = False
else:
    for char in inp:
        if char not in ['O', '.']:
            isBraille = False

if isBraille:
    print(translate_to_english(inp))
else:
    print(translate_to_braille(inp))
