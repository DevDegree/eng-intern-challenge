import sys

# Dict for characters to braille
ALPHABET_TO_BRAILLE = {
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
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

CAPTIAL_SYMBOL = '.....O'
NUMBER_SYBMOL = '.O.OOO'
SPACE_SYMBOL = '......'

# Reverse dict for braille to characters
BRAILLE_TO_ALPHABET = {value: key for key, value in ALPHABET_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {value: key for key, value in NUMBER_TO_BRAILLE.items()}

# Function to translate English to Braille
def eng_to_braille(string):
    result = []
    number_follows = False

    for char in string:
        # Check for alphabets
        if char.isalpha() and not number_follows:
            # Check for captial
            if char.isupper():
                result.append(CAPTIAL_SYMBOL)
            result.append(ALPHABET_TO_BRAILLE[char.lower()])
        # Check for numbers
        elif char.isdigit():
            if not number_follows:
                result.append(NUMBER_SYBMOL)
                number_follows = True
            result.append(NUMBER_TO_BRAILLE[char])
        # Check for spaces
        elif char == ' ':
            result.append(SPACE_SYMBOL)
            number_follows = False
        # Invalid character
        else:
            return ''

    return ''.join(result)

# Function to tranlate Braille to English
def braille_to_eng(string):
    result = []
    i=0
    capital_follows = False
    number_follows = False

    # Check for invalid input
    if (len(string) % 6 != 0):
        return ""

    while i < len(string):
        symbol = string[i:i+6]

        # Check for number follows symbol
        if symbol == NUMBER_SYBMOL:
            number_follows = True
        # Check for captial follows symbol
        elif symbol == CAPTIAL_SYMBOL:
            capital_follows = True
        # Check for space symbol
        elif symbol == SPACE_SYMBOL:
            result.append(' ')
            number_follows = False
        # Translation
        elif number_follows and symbol in BRAILLE_TO_NUMBER:
            result.append(BRAILLE_TO_NUMBER[symbol])
        elif not number_follows and symbol in BRAILLE_TO_ALPHABET:
            if capital_follows:
                result.append(BRAILLE_TO_ALPHABET[symbol].upper())
                capital_follows = False
            else:
                result.append(BRAILLE_TO_ALPHABET[symbol])
        # Invalid Symbol
        else:
            return ""

        i+=6

    return ''.join(result)
    

# Main driver code
input_text = ' '.join(sys.argv[1:])
result = ""
if all(c in 'O.' for c in input_text):
    result = braille_to_eng(input_text)
else:
    result = eng_to_braille(input_text)

print(result)