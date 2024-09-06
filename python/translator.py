# Define Braille alphabet mapping
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # Numbers (same as letters a-j, but prefixed by the number indicator)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Special symbols
    ' ': '......', '.': '..O.OO', ',': '..O...', '?': '..OO.O', '!': '..OOO.',
    ':': 'OO..O.', ';': 'OO.OO.', '-': '......', '/': '.O.O..', '(': '.OO.O.',
    ')': '.OO.O.', '<': 'O.....', '>': 'O.....',

    # Special markers
    'CAPITAL': '.....O', 'NUMBER': '.O.OO.'
}

BRAILLE_TO_ENGLISH = {v: k for k, v in BRAILLE_ALPHABET.items()}

# Function to convert English to Braille
def english_to_braille(input_str):
    braille = ""
    number_mode = False  # Track when we are in number mode
    
    for char in input_str:
        if char.isupper():
            # Add the CAPITAL marker before the uppercase letter
            braille += BRAILLE_ALPHABET['CAPITAL'] + BRAILLE_ALPHABET[char.lower()]
            number_mode = False  # Exit number mode on encountering letters
        elif char.isdigit():
            if not number_mode:
                # Add the NUMBER marker before digits
                braille += BRAILLE_ALPHABET['NUMBER']
                number_mode = True
            braille += BRAILLE_ALPHABET[char]
        elif char == ' ':
            # Add a space and reset modes
            braille += BRAILLE_ALPHABET[' ']
            number_mode = False  # Exit number mode after space
        else:
            braille += BRAILLE_ALPHABET[char]
            number_mode = False  # Exit number mode on encountering letters or punctuation
    
    return braille


# Function to convert Braille to English
def braille_to_english(input_str):
    english = ""
    capitalize_next = False
    number_mode = False
    i = 0
    while i < len(input_str):
        braille_char = input_str[i:i+6]
        if braille_char == BRAILLE_ALPHABET['CAPITAL']:
            capitalize_next = True
        elif braille_char == BRAILLE_ALPHABET['NUMBER']:
            number_mode = True
        elif braille_char == '......':
            english += ' '
        else:
            char = BRAILLE_TO_ENGLISH.get(braille_char, '')
            if number_mode and char in 'abcdefghij':
                english += str(ord(char) - ord('a') + 1)
                number_mode = False
            elif capitalize_next:
                english += char.upper()
                capitalize_next = False
            else:
                english += char
        i += 6
    return english

# Determine if the input is Braille or English
def detect_input_type(input_str):
    return all(char in ['O', '.'] for char in input_str)

if __name__ == "__main__":
    import sys
    input_data = ''.join(sys.argv[1:])
    
    if detect_input_type(input_data):
        # Convert Braille to English
        print(braille_to_english(input_data))
    else:
        # Convert English to Braille
        print(english_to_braille(input_data))
