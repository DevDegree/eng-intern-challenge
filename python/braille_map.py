# braille_map.py

# Braille map for letters, digits, and punctuation
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',   # Space

    # Numbers 0-9
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Punctuation
    '.': '..OO.O',  
    ',': '..O...',  
    '?': '...OOO',  
    '!': '..OOO.',  
    ':': '..OO..',  
    ';': '..O.O.',  
    '-': '....OO',  
    '/': '.O..O.',  
    '<': '.OO..O',  
    '>': 'O..OO.',  
    '(': 'O.O..O',  
    ')': '.O.OO.',   
    ' ': '......'
}

braille_follows_symbols = {
    'capitalSign': '.....O',  # Capitalization follows
    'numberSign': '.O.OOO',   # Numbers follows
    'decimalSign': '.O...O'  # Decimal follows
}

reverse_braille_map = {}

special_symbols = set('<>?!:;,./()')

# Populate reverse_braille_map with both letters and digits
for key, value in braille_map.items():
    if value not in reverse_braille_map:
        reverse_braille_map[value] = {}

    if key.isdigit():
        reverse_braille_map[value]['digit'] = key  # Store the digit for the Braille symbol
    elif key in special_symbols:
        reverse_braille_map[value]['symbol'] = key
    else:
        # Otherwise, store it as a letter
        reverse_braille_map[value]['letter'] = key