import sys

# Dictionary that maps English letters to their Braille equivalent.
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
}

# Special symbols for capitalization and numbers
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'

# Dictionary for mapping digits to their Braille equivalents
BRAILLE_DIGITS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Reverse dictionary to convert Braille back to English letters.
ENGLISH_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}

# Reverse dictionary for numbers in Braille.
ENGLISH_DIGITS = {v: k for k, v in BRAILLE_DIGITS.items()}


# It checks if every character in the input string is either 'O' or '.'.
def is_braille(input_str):
    return all(c in 'O.' for c in input_str)


# Function to convert a Braille string to English.
def braille_to_english(braille):
    result = []
    buffer = [braille[i:i+6] for i in range(0, len(braille), 6)] # Split in bunch of 6
    capital = False
    number_mode = False

    for symbol in buffer:
        # Sets flag if required
        if symbol == BRAILLE_CAPITAL:
            capital = True
            continue
        elif symbol == BRAILLE_NUMBER:
            number_mode = True
            continue

        # Convert the set into respective English counterpart
        if number_mode:
            result.append(ENGLISH_DIGITS.get(symbol, ' '))
            number_mode = False if symbol == '......' else True
        elif capital:
            result.append(ENGLISH_ALPHABET.get(symbol, ' ').upper())
            capital = False
        else:
            result.append(ENGLISH_ALPHABET.get(symbol, ' '))

    return ''.join(result)


# Function to convert an English string to Braille.
def english_to_braille(english):
    result = []
    number_mode = False

    for char in english:
        if char.isupper():
            result.append(BRAILLE_CAPITAL)
            result.append(BRAILLE_ALPHABET[char.lower()])
        elif char.isdigit():
            if not number_mode:
                result.append(BRAILLE_NUMBER)
                number_mode = True
            result.append(BRAILLE_DIGITS[char])
        else:
            number_mode = False
            result.append(BRAILLE_ALPHABET.get(char, '......'))

    return ''.join(result)


# Function to determine which translation direction to use and print the result.
def translate(input_str):
    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))


# Main function to handle command-line input.
if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:])
    translate(input_str)
