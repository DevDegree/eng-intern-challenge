import sys

# Braille mappings
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

braille_punc = {
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO', 'decimal': '.O...O',
    ',': 'O.....', '.': 'O..OO.', '?': 'O.O.OO', '!': 'O.OO.O', ':': 'O...OO',
    ';': 'O.O...', '-': 'OO....', '/': 'OO.O..', '<': 'O..O..', '>': 'OOO...',
    '(': 'OOOO..', ')': 'O.OO..', '.': '..OO.O'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Invert the dictionary for reverse lookup
english_to_braille = {**braille_alphabet, **braille_punc, **braille_numbers}
braille_to_alphabet = {v: k for k, v in braille_alphabet.items()}
braille_to_punc = {v: k for k, v in braille_punc.items()}
braille_to_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_str):
    """Determines if the input string is in Braille format."""
    return all(c in 'O.' for c in input_str) and len(input_str) % 6 == 0

def translate_to_braille(text):
    """Converts English text to Braille."""
    result = []
    num_mode = False
    decimal_mode = False
    for i, char in enumerate(text):
        if char.isdigit():
            if not num_mode:
                result.append(english_to_braille['num'])
                num_mode = True
            result.append(braille_numbers[char])
        elif char == '.':
            if i > 0 and i < len(text) - 1 and text[i - 1].isdigit() and text[i + 1].isdigit():
                result.append(english_to_braille['decimal'])  # Decimal point
                decimal_mode = True
            else:
                result.append(english_to_braille['.'])  # Regular period punctuation
        elif char.isalpha():
            if char.isupper():
                result.append(english_to_braille['cap'])
            result.append(braille_alphabet[char.lower()])
        elif char in braille_alphabet:
            result.append(braille_alphabet[char])
            num_mode = False
            decimal_mode = False
        elif char == ' ':
            result.append(braille_punc[' '])
            num_mode = False
            decimal_mode = False
    return ''.join(result)

def translate_to_english(braille):
    """Converts Braille to English text."""
    result = []
    num_mode = False
    decimal_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == english_to_braille['cap']:
            next_symbol = braille[i+6:i+12]
            result.append(braille_to_alphabet[next_symbol].upper())
            i += 12
        elif symbol == english_to_braille['num']:
            num_mode = True
            i += 6
        elif symbol == english_to_braille['decimal']:
            decimal_mode = True
            result.append('.')  # Add the decimal point in English
            i += 6
        elif symbol == english_to_braille[' ']:
            result.append(' ')
            i += 6
        else:
            if num_mode or decimal_mode:
                result.append(braille_to_numbers[symbol])
            elif symbol in braille_to_alphabet:
                result.append(braille_to_alphabet[symbol])
            else:
                result.append(braille_to_punc[symbol])
            i += 6
    return ''.join(result)

def main():
    # Read the input from the command line argument (there might ve more than one word; then the space will be ignored)
    input_str = ' '.join(sys.argv[1:])

    # Determine if the input is in Braille or English
    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()
