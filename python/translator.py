import sys

# Braille patterns for letters, numbers, and special symbols
BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_SPECIALS = {
    'space': '......',
    'capital_follows': '.....O',
    'number_follows': '.O.OOO'
}

# Reverse mappings for Braille to English translation
ENGLISH_LETTERS = {v: k for k, v in BRAILLE_LETTERS.items()}
ENGLISH_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

def is_braille(input_str):
    """Check if the input string consists only of Braille characters."""
    return all(char in 'O.' for char in input_str)

def english_to_braille(text):
    """Translate English text to Braille."""
    result = []
    number_mode = False

    for char in text:
        # Handle letters
        if char.isalpha():
            if number_mode:
                result.append(BRAILLE_SPECIALS['space']) # Exit number mode with space
                number_mode = False
            # Handle capital letters
            if char.isupper():
                result.append(BRAILLE_SPECIALS['capital_follows'])
                char = char.lower()
            result.append(BRAILLE_LETTERS[char])
        # Handle numbers
        elif char.isdigit():
            if not number_mode:
                result.append(BRAILLE_SPECIALS['number_follows'])
                number_mode = True
            result.append(BRAILLE_NUMBERS[char])
        # Handle spaces
        elif char == ' ':
            result.append(BRAILLE_SPECIALS['space'])
            number_mode = False # Space resets number mode

    return ''.join(result)

def braille_to_english(braille):
    """Translate Braille text to English."""
    result = []
    i = 0
    number_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]

        # Handle capital letters
        if symbol == BRAILLE_SPECIALS['capital_follows']:
            next_symbol = braille[i+6:i+12]
            result.append(ENGLISH_LETTERS.get(next_symbol, '?').upper())
            i += 6
        # Handle number mode
        elif symbol == BRAILLE_SPECIALS['number_follows']:
            number_mode = True
        # Handle spaces
        elif symbol == BRAILLE_SPECIALS['space']:
            result.append(' ')
            number_mode = False
        # Handle letters/numbers
        else:
            if number_mode:
                result.append(ENGLISH_NUMBERS.get(symbol, '?'))
            else:
                result.append(ENGLISH_LETTERS.get(symbol, '?'))
        i += 6

    return ''.join(result)

def translator(input_str):
    """Determine if the input is Braille or English and translate accordingly."""
    if is_braille(input_str):
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        output = translator(input_str)
        print(output)
    else:
        print("No input provided.")