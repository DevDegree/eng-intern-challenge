# translator.py
# Name: Jerry Hou

import sys

# Letter braille mapping
BRAILLE_LETTERS = {
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
    ' ': '......'
}

# Numbers braille mapping
BRAILLE_NUMBERS = {
    '1': BRAILLE_LETTERS['a'],
    '2': BRAILLE_LETTERS['b'],
    '3': BRAILLE_LETTERS['c'],
    '4': BRAILLE_LETTERS['d'],
    '5': BRAILLE_LETTERS['e'],
    '6': BRAILLE_LETTERS['f'],
    '7': BRAILLE_LETTERS['g'],
    '8': BRAILLE_LETTERS['h'],
    '9': BRAILLE_LETTERS['i'],
    '0': BRAILLE_LETTERS['j']
}

# Special indicators
CAPITAL_INDICATOR = '.....O'  
NUMBER_INDICATOR = '.O.OOO'   

# Reverse mappings for translation from Braille to English
ENGLISH_LETTERS = {v : k for k, v in BRAILLE_LETTERS.items()}
ENGLISH_NUMBERS = {v : k for k, v in BRAILLE_NUMBERS.items()}

def is_braille(input_str):
    """
    Determine if the input string is Braille.
    """
    if all (c in ('O', '.') for c in input_str) and len(input_str) % 6 == 0:
        return True
    else:
        return False

def english_to_braille(text):
    """
    Translate English text to Braille.
    """
    braille = ''
    number_mode = False

    for char in text:
        if char.isupper():
            # Add capital indicator
            braille += CAPITAL_INDICATOR
            # Map the lowercase letter
            braille_char = BRAILLE_LETTERS.get(char.lower(), '......')
            braille += braille_char
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                # Add number indicator
                braille += NUMBER_INDICATOR
                number_mode = True
            # Map the digit to Braille
            braille_char = BRAILLE_NUMBERS.get(char, '......')
            braille += braille_char
        elif char == ' ':
            # Space resets number mode
            braille += BRAILLE_LETTERS[' ']
            number_mode = False
        else:
            braille_char = BRAILLE_LETTERS.get(char, '......')
            braille += braille_char
            number_mode = False

    return braille

def braille_to_english(braille):
    """
    Translate Braille to English text.
    """
    english = ''
    chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    i = 0
    number_mode = False

    while i < len(chars):
        chunk = chars[i]

        if chunk == CAPITAL_INDICATOR:
            # Next character should be capitalized
            i += 1
            if i < len(chars):
                next_chunk = chars[i]
                letter = ENGLISH_LETTERS.get(next_chunk, '')
                english += letter.upper() if letter else ''
        elif chunk == NUMBER_INDICATOR:
            # Enter number mode
            number_mode = True
        else:
            if number_mode:
                # Check if chunk corresponds to a number
                if chunk in ENGLISH_NUMBERS:
                    english += ENGLISH_NUMBERS[chunk]
                elif chunk == BRAILLE_LETTERS[' ']:
                    # Exit number mode if chunk is a space
                    number_mode = False
                    letter = ENGLISH_LETTERS.get(chunk, ' ')
                    english += letter
            else:
                # Regular letter
                letter = ENGLISH_LETTERS.get(chunk, ' ')
                english += letter
        i += 1

    return english

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    # Join all arguments to handle multi-word inputs
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        output = braille_to_english(input_str)
    else:
        output = english_to_braille(input_str)

    print(output)

if __name__ == "__main__":
    main()
