import sys

# Braille
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'
}

braille_c = '.....O'
braille_num = '.O.OOO'
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_to_eng = {v: k for k, v in braille_letters.items()}
braille_to_num = {v: k for k, v in braille_numbers.items()}

def convert_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_num)
                number_mode = True
            result.append(braille_numbers[char])
        elif char.isupper():
            result.append(braille_c)
            result.append(braille_letters[char.lower()])
            number_mode = False 
        else:
            result.append(braille_letters.get(char, ''))
            number_mode = False  
    return ''.join(result)


def convert_to_english(braille):
    output = []
    i = 0
    capital = False
    number_mode = False
    while i < len(braille):
        sym = braille[i:i+6]
        if sym == braille_c:
            capital = True
            i += 6
            continue
        elif sym == braille_num:
            number_mode = True
            i += 6
            continue
        elif number_mode:
            output.append(braille_to_num.get(sym, ''))
            i += 6
            continue
        char = braille_to_eng.get(sym, '')
        if capital:
            output.append(char.upper())
            capital = False
        else:
            output.append(char)
        i += 6
    return ''.join(output)

def braille_translator(input_text):
    if all(c in ['O', '.'] for c in input_text):  
        return convert_to_english(input_text)
    else: 
        return convert_to_braille(input_text)

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    print(braille_translator(input_text))
