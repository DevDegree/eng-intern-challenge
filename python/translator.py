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
    i = 0
    while i < len(text):
        char = text[i]
        if char.isupper():
            braille_output.append(CAPITAL_SYMBOL)
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                braille_output.append(NUMBER_SYMBOL)
                number_mode = True
            braille_output.append(BRAILLE_MAP[char])
        elif char == '.':
            if number_mode and i + 1 < len(text) and text[i+1].isdigit():
                # It's a decimal point
                braille_output.append(DECIMAL_SYMBOL)
            else:
                # It's a period (end of sentence or standalone)
                braille_output.append(BRAILLE_MAP['.'])
                number_mode = False
        elif char == ' ':
            braille_output.append(BRAILLE_MAP[' '])
            number_mode = False
        elif char.lower() in BRAILLE_MAP:
            if number_mode:
                number_mode = False
            braille_output.append(BRAILLE_MAP[char.lower()])
        else:
            # Unsupported character
            pass
        i += 1
    return ''.join(braille_output)

def braille_to_english(braille):
    """Translate Braille to English text."""
    english_output = []
    blocks = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capital_next = False
    number_mode = False

    i = 0
    while i < len(blocks):
        block = blocks[i]
        if block == CAPITAL_SYMBOL:
            capital_next = True
        elif block == NUMBER_SYMBOL:
            number_mode = True
        elif block == BRAILLE_MAP[' ']:
            english_output.append(' ')
            number_mode = False
        elif number_mode:
            if block == DECIMAL_SYMBOL:
                if i + 1 < len(blocks) and blocks[i+1] in DIGIT_MAP:
                    # It's a decimal point
                    english_output.append('.')
                else:
                    # It's likely the end of a sentence
                    english_output.append('.')
                    number_mode = False
            elif block in DIGIT_MAP:
                english_output.append(DIGIT_MAP[block])
            else:
                # If the block isn't a digit, exit number mode and interpret as letter
                number_mode = False
                if block in ENGLISH_MAP:
                    mapped_char = ENGLISH_MAP[block]
                    english_output.append(mapped_char.upper() if capital_next else mapped_char)
                    capital_next = False
        else:
            if block in ENGLISH_MAP:
                mapped_char = ENGLISH_MAP[block]
                english_output.append(mapped_char.upper() if capital_next else mapped_char)
                capital_next = False
            elif block in BRAILLE_MAP.values():
                # Handle punctuation and other symbols
                for char, braille_code in BRAILLE_MAP.items():
                    if braille_code == block:
                        english_output.append(char)
                        break
            else:
                # Unsupported Braille block
                pass
        i += 1

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
