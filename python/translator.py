import sys

# Braille dictionary
braille_dict = {
    'capital': '.....O', 
    'decimal': '.O...O',
    'number': '.O.OOO',
    ' ': '......',
    '.': '..OO.O', 
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...'
}

# Reverse dictionary for Braille to English translation
reverse_braille_dict = {}
for k, v in braille_dict.items():
    # Exclude numbers from reverse dict
    if k not in '0123456789':
        reverse_braille_dict[v] = k

# Separate dictionary for number translations
number_dict = {braille_dict[str(i)]: str(i) for i in range(10)}

'''
    When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
    When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
'''
def english_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char.isupper():
            result.append(braille_dict['capital'])
            char = char.lower()
        if char.isdigit() and not is_number:
            result.append(braille_dict['number'])
            is_number = True
        elif not char.isdigit():
            is_number = False
        result.append(braille_dict[char])
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    is_capital = False
    is_number = False
    while i < len(braille):
        code = braille[i:i+6]
        if code == braille_dict['capital']:
            is_capital = True
        elif code == braille_dict['number']:
            is_number = True
        else:
            if is_number and code in number_dict:
                char = number_dict[code]
            else:
                char = reverse_braille_dict.get(code, '')
                is_number = False  # Exit number mode if not a valid number code
            if is_capital:
                char = char.upper()
                is_capital = False
            result.append(char)
        i += 6
    return ''.join(result)

def is_valid_braille(input_string):
    '''Check if input is Braille (contains only '.' and 'O' and length is multiple of 6)
    '''
    return set(input_string) <= set('.O') and len(input_string) % 6 == 0

def translate(input_string):
    if is_valid_braille(input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == '__main__':
    input_string = ' '.join(sys.argv[1:])
    print(translate(input_string))