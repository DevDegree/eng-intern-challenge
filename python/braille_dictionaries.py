# braille_dictionaries.py

# English to Braille Dictionary
english_to_braille = {
    # Letters a-z
    'a': 'O.....',  # Dot 1
    'b': 'O.O...',  # Dots 1,2
    'c': 'OO....',  # Dots 1,4
    'd': 'OO.O..',  # Dots 1,4,5
    'e': 'O..O..',  # Dots 1,5
    'f': 'OOO...',  # Dots 1,2,4
    'g': 'OOOO..',  # Dots 1,2,4,5
    'h': 'O.OO..',  # Dots 1,2,5
    'i': '.OO...',  # Dots 2,4
    'j': '.OOO..',  # Dots 2,4,5
    'k': 'O...O.',  # Dots 1,3
    'l': 'O.O.O.',  # Dots 1,2,3
    'm': 'OO..O.',  # Dots 1,3,4
    'n': 'OO.OO.',  # Dots 1,3,4,5
    'o': 'O..OO.',  # Dots 1,3,5
    'p': 'OOO.O.',  # Dots 1,2,3,4
    'q': 'OOOOO.',  # Dots 1,2,3,4,5
    'r': 'O.OOO.',  # Dots 1,2,3,5
    's': '.OO.O.',  # Dots 2,3,4
    't': '.OOOO.',  # Dots 2,3,4,5
    'u': 'O...OO',  # Dots 1,3,6
    'v': 'O.O.OO',  # Dots 1,2,3,6
    'w': '.OOO.O',  # Dots 2,4,5,6
    'x': 'OO..OO',  # Dots 1,3,4,6
    'y': 'OO.OOO',  # Dots 1,3,4,5,6
    'z': 'O..OOO',  # Dots 1,3,5,6

    # Capitalization sign (Dot 6)
    'capital': '.....O',

    # Decimal sign (Dot 4,6)
    'decimal': '.0...0',

    # Number sign (Dots 3,4,5,6)
    'number': '.O.OOO',

    
    # Space
    ' ': '......',

    # Punctuation
    ',': '..O...',    # Dot 2
    ';': '..O.O.',    # Dots 2,3
    ':': '..OO..',    # Dots 2,4
    '.': '..00.0',    # Dots 2,5,6
    '!': '..OO.O',    # Dots 2,4,6
    '(': '0.0..0',    # Dots 1,2,6 (opening)
    ')': '.0.00.',    # Dots 3,4,5 (closing)
    '?': '..0.00',    # Dots 2,3,6
    '-': '....O0',    # Dot 5, 6
    '/': '.0..0.',    # Dot 3, 4
    '<': '.00..0',    # Dot 2, 4, 6
    '>': '0..00.',    # Dot 1, 3, 5

}

# Number Map (for digits 0-9)
number_map = {
    '1': 'a',  # Represents digit 1
    '2': 'b',  # Represents digit 2
    '3': 'c',  # Represents digit 3
    '4': 'd',  # Represents digit 4
    '5': 'e',  # Represents digit 5
    '6': 'f',  # Represents digit 6
    '7': 'g',  # Represents digit 7
    '8': 'h',  # Represents digit 8
    '9': 'i',  # Represents digit 9
    '0': 'j',  # Represents digit 0
}

# Braille to English Dictionary (reverse mapping) using dict comprehension
braille_to_english = {v: k for k, v in english_to_braille.items()}

# Reverse Number Map (for numbers mode)
number_map_reversed = {v: k for k, v in number_map.items()}
