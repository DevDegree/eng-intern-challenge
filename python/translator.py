
import sys

# Define Braille mappings
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO',
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Reverse mapping for Braille to English
ENGLISH_BRAILLE = {v: k for k, v in {**BRAILLE_ALPHABET, **BRAILLE_NUMBERS}.items()}


def is_braille(text):
    """Determine if input is Braille based on whether it contains 'O' and '.' characters only."""
    return all(c in 'O.' for c in text)


def translate_to_braille(text):
    """Convert English to Braille."""
    result = []
    is_number = False

    for char in text:
        if char.isdigit():
            if not is_number:
                result.append(BRAILLE_ALPHABET['number'])
                is_number = True
            result.append(BRAILLE_NUMBERS[char])
        elif char.isalpha():
            if is_number:
                is_number = False
            if char.isupper():
                result.append(BRAILLE_ALPHABET['capital'])
            result.append(BRAILLE_ALPHABET[char.lower()])
        elif char == ' ':
            result.append(BRAILLE_ALPHABET[' '])

    return ''.join(result)


def translate_to_english(braille):
    """Convert Braille to English."""
    result = []
    is_capital = False
    is_number = False

    # Split braille into 6-character chunks
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == BRAILLE_ALPHABET['capital']:
            is_capital = True
            continue
        elif symbol == BRAILLE_ALPHABET['number']:
            is_number = True
            continue

        char = ENGLISH_BRAILLE.get(symbol, '')
        if char:
            if is_capital:
                char = char.upper()
                is_capital = False
            if is_number:
                # Numbers only map to digits 0-9, not letters.
                if char.isdigit():
                    result.append(char)
                is_number = False
            else:
                result.append(char)

    return ''.join(result)


if __name__ == "__main__":
    # Get input from command line
    input_text = ' '.join(sys.argv[1:])

    # Determine if the input is Braille or English
    if is_braille(input_text):
        # Input is Braille, translate to English
        output = translate_to_english(input_text)
    else:
        # Input is English, translate to Braille
        output = translate_to_braille(input_text)

    # Output the translated result
    print(output)