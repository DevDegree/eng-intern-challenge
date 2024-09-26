import sys

# Mapping from English letters to Braille
ENGLISH_TO_BRAILLE = {
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

# Braille prefixes
CAPITAL_PREFIX = '.....O'
NUMBER_PREFIX = '..OOOO'

# Mapping digits to Braille using letters 'a' to 'j'
DIGIT_TO_BRAILLE = {
    '1': ENGLISH_TO_BRAILLE['a'],
    '2': ENGLISH_TO_BRAILLE['b'],
    '3': ENGLISH_TO_BRAILLE['c'],
    '4': ENGLISH_TO_BRAILLE['d'],
    '5': ENGLISH_TO_BRAILLE['e'],
    '6': ENGLISH_TO_BRAILLE['f'],
    '7': ENGLISH_TO_BRAILLE['g'],
    '8': ENGLISH_TO_BRAILLE['h'],
    '9': ENGLISH_TO_BRAILLE['i'],
    '0': ENGLISH_TO_BRAILLE['j'],
}

# Reverse mapping for letters
BRAILLE_TO_ENGLISH_LETTER = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

# Reverse mapping for digits
BRAILLE_TO_ENGLISH_DIGIT = {v: k for k, v in DIGIT_TO_BRAILLE.items()}

def is_braille(input_str):
    """Determine if the input string is in Braille format."""
    return all(c in {'O', '.'} for c in input_str)

def english_to_braille(text):
    """Translate English text to Braille."""
    braille_output = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(NUMBER_PREFIX)
                number_mode = True
            braille_output.append(DIGIT_TO_BRAILLE.get(char, '......'))
        else:
            if number_mode:
                # Terminate number mode by inserting space
                braille_output.append(ENGLISH_TO_BRAILLE[' '])
                number_mode = False
            if char.isupper():
                braille_output.append(CAPITAL_PREFIX)
                braille_output.append(ENGLISH_TO_BRAILLE.get(char.lower(), '......'))
            else:
                braille_output.append(ENGLISH_TO_BRAILLE.get(char, '......'))

    # Optionally, terminate number mode if still active
    if number_mode:
        braille_output.append(ENGLISH_TO_BRAILLE[' '])

    return ''.join(braille_output)

def braille_to_english(braille_text):
    """Translate Braille to English text."""
    english_output = []
    i = 0
    number_mode = False
    capitalize_next = False

    while i < len(braille_text):
        # Each Braille character is 6 characters long
        chunk = braille_text[i:i+6]
        if len(chunk) < 6:
            # Invalid Braille character length
            break

        if chunk == CAPITAL_PREFIX:
            capitalize_next = True
            i += 6
            continue
        elif chunk == NUMBER_PREFIX:
            number_mode = True
            i += 6
            continue
        elif chunk == ENGLISH_TO_BRAILLE[' ']:  # '......'
            if number_mode:
                # Terminate number mode without appending a space
                number_mode = False
            else:
                # Actual space in input
                english_output.append(' ')
            i += 6
            continue
        else:
            if number_mode:
                # Should be digit
                char = BRAILLE_TO_ENGLISH_DIGIT.get(chunk, '?')
                if char != '?':
                    english_output.append(char)
                else:
                    # Not a digit, terminate number mode
                    number_mode = False
                    # Try to get as letter
                    char = BRAILLE_TO_ENGLISH_LETTER.get(chunk, '?')
                    if capitalize_next and char.isalpha():
                        char = char.upper()
                        capitalize_next = False
                    english_output.append(char)
            else:
                # Should be letter
                char = BRAILLE_TO_ENGLISH_LETTER.get(chunk, '?')
                if char != '?':
                    if capitalize_next and char.isalpha():
                        char = char.upper()
                        capitalize_next = False
                    english_output.append(char)
                else:
                    # Unknown character
                    english_output.append('?')
        i += 6

    return ''.join(english_output)

def main():
    """Main function to handle input and translation."""
    # Check if input is provided via command-line arguments
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
    else:
        # Interactive prompt
        input_str = input("Enter the string to translate: ").strip()
    if is_braille(input_str):
        translated = braille_to_english(input_str)
    else:
        translated = english_to_braille(input_str)
    print(translated)

if __name__ == "__main__":
    main()
