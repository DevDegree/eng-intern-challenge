import sys

# Braille mappings for lowercase letters, numbers, and space
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}
# "12.34 5.678"
# .O.OOOOO....OO.O.........O.OOOO..O....OO.O.O.OOOOOO...OOOO..O.OO..

# Reverse mapping from Braille to English letters
ENGLISH_MAP = {v: k for k, v in BRAILLE_MAP.items() if k.isalpha() or k == ' '}

# Reverse mapping from Braille to digits (1-0)
DIGIT_MAP = {v: k for k, v in BRAILLE_MAP.items() if k.isdigit()}

# Special symbols
CAPITAL_SYMBOL = '.....O' 
NUMBER_SYMBOL = '.O.OOO'   
DECIMAL_SYMBOL = '.O...O'  

def is_braille(input_string):
    """Determine if the input string is Braille."""
    return all(c in {'O', '.'} for c in input_string) and len(input_string) % 6 == 0

def english_to_braille(text):
    """Translate English text to Braille."""
    braille_output = []
    number_mode = False
    for char in text:
        if char.isupper():
            # Append capital symbol before the letter
            braille_output.append(CAPITAL_SYMBOL)
            char = char.lower()
            if char in BRAILLE_MAP:
                braille_output.append(BRAILLE_MAP[char])
            else:
                # Unsupported character
                pass
            number_mode = False  # Exiting number mode if previously in it
        elif char.isdigit():
            if not number_mode:
                # Enter number mode by appending number symbol
                braille_output.append(NUMBER_SYMBOL)
                number_mode = True
            if char in BRAILLE_MAP:
                braille_output.append(BRAILLE_MAP[char])
            else:
                # Unsupported digit
                pass
        elif char == ' ':
            # Append space and exit number mode
            braille_output.append(BRAILLE_MAP[' '])
            number_mode = False
        elif char.lower() in BRAILLE_MAP:
            if number_mode:
                # Exiting number mode upon encountering a letter
                number_mode = False
            braille_output.append(BRAILLE_MAP[char.lower()])
        else:
            # Unsupported character
            pass
    return ''.join(braille_output)

def braille_to_english(braille):
    """Translate Braille to English text."""
    english_output = []
    blocks = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capital_next = False
    number_mode = False

    for block in blocks:
        if block == CAPITAL_SYMBOL:
            capital_next = True
            continue
        if block == NUMBER_SYMBOL:
            number_mode = True
            continue
        if block == BRAILLE_MAP[' ']:
            english_output.append(' ')
            number_mode = False
            continue
        if number_mode:
            if block == DECIMAL_SYMBOL:
                english_output.append('.')
                continue
            if block in DIGIT_MAP:
                digit = DIGIT_MAP[block]
                english_output.append(digit)
            else:
                # If the block isn't a digit, exit number mode and interpret as letter
                number_mode = False
                if block in ENGLISH_MAP:
                    mapped_char = ENGLISH_MAP[block]
                    if capital_next:
                        english_output.append(mapped_char.upper())
                        capital_next = False
                    else:
                        english_output.append(mapped_char)
        else:
            if block in ENGLISH_MAP:
                mapped_char = ENGLISH_MAP[block]
                if capital_next:
                    english_output.append(mapped_char.upper())
                    capital_next = False
                else:
                    english_output.append(mapped_char)
            else:
                # Unsupported Braille block
                pass

    return ''.join(english_output)

def main():
    if len(sys.argv) < 2:
        # No input provided
        sys.exit(0)
    
    # Join all command-line arguments into a single string with spaces
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        translated = braille_to_english(input_string)
    else:
        translated = english_to_braille(input_string)
    
    print(translated)

if __name__ == "__main__":
    main()
