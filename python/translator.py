import sys


# Braille dictionary
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  'capital': '.....O', 'number': '.O.OOO',
    # '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    # '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

num_map = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j'
}

text_to_num = {i: j for j, i in num_map.items()}

braille_to_text = {i: j for j, i in braille_map.items()}

def eng_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isupper():
            result.append(braille_map['capital'])
            result.append(braille_map[char.lower()])
        elif char.isdigit():
            if not number_mode:
                result.append(braille_map['number'])
                number_mode = True
            result.append(braille_map[num_map[char]])
        else:
            if number_mode:
                number_mode = False
            result.append(braille_map[char])
    return ''.join(result)

def braille_to_eng(braille):
    result = []
    number_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_map['capital']:
            i += 6
            next_symbol = braille[i:i+6]
            result.append(braille_to_text[next_symbol].upper())
        elif symbol == braille_map['number']:
            number_mode = True
        elif symbol == braille_map[' ']:
            number_mode = False
            result.append(' ')
            
        else:
            char = braille_to_text[symbol]
            if number_mode:
                char = text_to_num[char]
            result.append(char)
            
        i += 6
    return ''.join(result)

# assumptions
# Supported english text does not contain punctuation, so we are able to use 
# the presence of a "." to determine whether an input string is Braille or not
#
#
def braille_translator(input_text):
    if '.' in input_text:
        return braille_to_eng(input_text)
    else:
        return eng_to_braille(input_text)



input_text = ' '.join(sys.argv[1:])
output = braille_translator(input_text)
print(output)

