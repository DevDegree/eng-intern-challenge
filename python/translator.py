# O = black dot
# . = white dot
import sys

input_message = ' '.join(sys.argv[1:])

# Constants

CAPITAL_FOLLOWS_BRAILLE = '.....O'
NUMBER_FOLLOWS_BRAILLE = '.O.OOO'

BRAILLE_ALPHABET = {
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
    ' ': '......',
}

BRAILLE_NUMBERS = {
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
}

def is_braille(message):
    if len(set(message)) == 2 and '.' in message and 'O' in message:
        return True 

def braille_to_english(message):
    idx = 0
    capital_follows = False 
    number_follows = False
    english = ''

    # Iterate through each substring (6 chars)
    while (idx < len(message)):
        # Get substring
        braille = message[idx:idx+6]

        # Set number follows
        if NUMBER_FOLLOWS_BRAILLE == braille:
            number_follows = True 

        # Set capital follows
        elif CAPITAL_FOLLOWS_BRAILLE == braille:
            capital_follows = True 

        # Substring is not a "follows indicator"
        else:

            if number_follows:
                if braille == '......':
                    english += ' '
                    # Number follows becomes false after space char
                    number_follows = False
                else:
                    # Find english number (key) based on braille symbol (value)
                    english_number = list(BRAILLE_NUMBERS.keys())[list(BRAILLE_NUMBERS.values()).index(braille)]
                    english += english_number
            else:
                # Space character
                if braille == '......':
                    english += ' '
                # Alphabetical character
                else:
                    # Find english letter (key) based on braille symbol (value)
                    english_letter = list(BRAILLE_ALPHABET.keys())[list(BRAILLE_ALPHABET.values()).index(braille)]

                    # Capital letter
                    if capital_follows:
                        english += english_letter.upper()
                        # Set capital to false
                        capital_follows = False
                    else:
                        # Non-capital english letter
                        english += english_letter
        # Increment
        idx += 6 
    
    return english

def english_to_braille(message):
    braille = ''
    is_number = False

    # Loop through each char
    for char in message:
        # Check if number 
        if char in BRAILLE_NUMBERS.keys():
            # Add "number follows" symbol
            if not is_number:
                braille += NUMBER_FOLLOWS_BRAILLE 
            braille += BRAILLE_NUMBERS[char]
            is_number = True
        # Letter or space
        else:
            if char == ' ':
                braille += '......'
                # Is number becomes false after space char
                is_number = False
            else:
                # Check if capital letter
                if char.isupper():
                    # Add "capital follows" symbol
                    braille += CAPITAL_FOLLOWS_BRAILLE

                braille += BRAILLE_ALPHABET[char.lower()]

    return braille
    
# Determine if braille and translate accordingly
if is_braille(input_message):
    print(braille_to_english(input_message))
else:
    print(english_to_braille(input_message))

