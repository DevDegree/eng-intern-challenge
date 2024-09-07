import sys

# Braille dictionary for letters, numbers, and special symbols
braille_dict = {
    'a': 'O.....', 
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..', 
    'f': 'OOO...', 
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..',
    'k': 'O...O.', 
    'l': 'O.O.O.', 
    'm': 'OO..O.', 
    'n': 'OO.OO.', 
    'o': 'O..OO.', 
    'p': 'OOO.O.', 
    'q': 'OOOOO.', 
    'r': 'O.OOO.', 
    's': '.OO.O.', 
    't': '.OOOO.',
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO', 
    'z': 'O..OOO',
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..',
    ' ': '......', 
    'capital': '.....O', 
    'number': '.O.OOO',
    '.': '.O.O..',
    ',': 'O.....',
    '?': '.OO.O.',
    '!': 'O.OO.O', 
    ';': 'O.O...', 
    ':': 'OO....', 
    '-': 'O..O..', 
    '/': 'O.OO..', 
    '<': 'OO.O..', 
    '>': 'O..OO.',

}

# Reverse dictionary for Braille to English conversion
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(s):
    # Check if the input string consists only of 'O' and '.'
    return all(c in 'O.' for c in s)

def translate_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            # Add the capital symbol and the lowercase equivalent of the character
            result.append(braille_dict['capital'])
            result.append(braille_dict[char.lower()])
        elif char.isdigit():
            # Add the number symbol and the digit
            result.append(braille_dict['number'])
            result.append(braille_dict[char])
        else:
            # Add the Braille representation of the character
            result.append(braille_dict[char])
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_dict['capital']:
            # Handle capitalization
            i += 6
            symbol = braille[i:i+6]
            result.append(reverse_braille_dict[symbol].upper())
        elif symbol == braille_dict['number']:
            # Handle numbers
            i += 6
            while i < len(braille) and braille[i:i+6] != '......':
                symbol = braille[i:i+6]
                result.append(reverse_braille_dict[symbol])
                i += 6
            continue
        else:
            # Add the English representation of the Braille symbol
            result.append(reverse_braille_dict[symbol])
        i += 6
    return ''.join(result)

def main():
    if len(sys.argv) != 2:
        # Exit if the number of arguments is not equal to 2
        return

    input_string = sys.argv[1]
    if is_braille(input_string):
        # Translate Braille to English
        print(translate_to_english(input_string))
    else:
        # Translate English to Braille
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()

