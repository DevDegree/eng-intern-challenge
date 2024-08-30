import sys

# Braille dictionary for letters, numbers, and symbols
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

braille_symbols = {
    '.': '.O.O.O', ',': 'O.....', '!': 'OOO...', '?': '.O.OO.', 
    '-': 'O....O', ':': 'OO.O..', ';': 'O.O...', "'": 'O....O',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Reverse lookups
reverse_letters_lookup = {v: k for k, v in braille_letters.items()}
reverse_numbers_lookup = {v: k for k, v in braille_numbers.items()}
reverse_symbols_lookup = {v: k for k, v in braille_symbols.items()}

# Translate English to Braille
def text_to_braille(text):
    braille = ''
    last_was_number = False  # To track if we are in number mode

    for char in text:
        if char.isupper():
            braille += braille_symbols['capital'] + braille_letters[char.lower()]
            last_was_number = False  # Reset number mode
        elif char.isdigit():
            if not last_was_number:
                braille += braille_symbols['number']
                last_was_number = True
            braille += braille_numbers[char]
        else:
            braille += braille_letters.get(char, braille_symbols.get(char, '......'))
            last_was_number = False  # Reset number mode
    return braille

# Translate Braille to English
def braille_to_text(braille):
    text = ''
    i = 0
    capital = False
    number = False

    while i < len(braille):
        code = braille[i:i+6]

        if code == braille_symbols['capital']:
            capital = True
            i += 6
            continue
        elif code == braille_symbols['number']:
            number = True
            i += 6
            continue

        if number:
            char = reverse_numbers_lookup.get(code, '')
        else:
            char = reverse_letters_lookup.get(code, reverse_symbols_lookup.get(code, ''))

        if capital:
            char = char.upper()
            capital = False

        text += char

        if char == ' ':
            number = False 

        i += 6

    return text

# Main function
if len(sys.argv) > 1:
    input_text = ' '.join(sys.argv[1:])  # Join all arguments as a single string
    
    # Determine whether the input is in English or Braille
    if all(c in 'O.' for c in input_text):
        # Input is Braille, translate to English
        print(braille_to_text(input_text))
    else:
        # Input is English, translate to Braille
        print(text_to_braille(input_text))
else:
    print("No input provided. Please pass the text to translate as a command-line argument.")
