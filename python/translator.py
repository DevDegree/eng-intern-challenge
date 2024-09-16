import sys

CAPITAL = '.....O'
NUMBER = '.O.OOO'

alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'}

numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

}

'''
For '>' and 'o', both are represented as 'O..OO.', and no clear instruction was provided, so I assigned 'OOOOOO' for '>'.
'''

symbols = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'OOOOOO',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}
    

def english_to_braille(txt):
    braille = []
    in_number = False
    
    for char in txt:
        if char.isupper():
            braille.append(CAPITAL)
            braille.append(alphabet[char.lower()])
            in_number = False
        elif char.isdigit():
            if not in_number:
                braille.append(NUMBER)
                in_number = True
            braille.append(numbers[char])

        elif char in symbols:
            braille.append(symbols[char])
            in_number = False

        else:
            if char in alphabet:
                braille.append(alphabet[char])
                in_number = False
            else:
                braille.append('?')
    return ''.join(braille)

def braille_to_english(braille):
    to_alphabet = {v: k for k, v in alphabet.items()}
    to_numbers = {v: k for k, v in numbers.items()}
    to_symbols = {v: k for k, v in symbols.items()}

    english = []
    capital_mode = False
    number_mode = False
    
    i = 0
    while i < len(braille):
        braille_char = braille[i:i+6]
        
        if braille_char == CAPITAL:
            capital_mode = True
            i += 6
            continue
        if braille_char == NUMBER:
            number_mode = True
            i += 6
            continue
        
        if number_mode and braille_char in to_numbers:
            char = to_numbers[braille_char]
            english.append(char)
        elif braille_char in to_alphabet:
            char = to_alphabet[braille_char]
            if capital_mode:
                english.append(char.upper())
                capital_mode = False
            else:
                english.append(char)
            
        elif braille_char in to_symbols:
            char = to_symbols[braille_char]
            english.append(char)

        else:
            english.append('?')
        
        i += 6
    
    return ''.join(english)

if __name__ == "__main__":
    user_input = sys.argv[1:]

    if all(char in 'O.' for char in user_input):
        print(braille_to_english(user_input))
    else:
        print(english_to_braille(user_input))
