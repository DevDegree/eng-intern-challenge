import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'capital_follows': '.....O', 'decimal_follows': '.O...O', 'number_follows': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
    '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}

def is_english(input_str):
    return not (len(input_str) % 6 == 0 and all(c in 'O.' for c in input_str))

def convert_to_braille(text):
    braille_output = []
    is_number_context = False
    
    for char in text:
        if char.isdigit() and not is_number_context:
            braille_output.append(braille_alphabet['number_follows'])
            is_number_context = True
        elif not char.isdigit():
            is_number_context = False
        
        if char.isupper():
            braille_output.append(braille_alphabet['capital_follows'])
            char = char.lower()
        
        braille_output.append(braille_alphabet.get(char, ''))
    
    return ''.join(braille_output)

def convert_to_english(braille):
    english_output = []
    is_number_context = False
    is_capital_context = False
    
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        
        if braille_char == braille_alphabet['number_follows']:
            is_number_context = True
            continue
        elif braille_char == braille_alphabet['capital_follows']:
            is_capital_context = True
            continue
        
        char = reverse_braille_alphabet.get(braille_char, '')
        if is_number_context:
            char = char if char.isdigit() else ''
        if is_capital_context:
            char = char.upper()
            is_capital_context = False
        
        english_output.append(char)
    
    return ''.join(english_output)

def main():
    input = ' '.join(sys.argv[1:])
    
    if is_english(input):
        print(convert_to_braille(input), end='')
    else:
        braille_characters = [input[i:i+6] for i in range(0, len(input), 6)]
        print(convert_to_english(braille_characters), end='')

if __name__ == '__main__':
    main()