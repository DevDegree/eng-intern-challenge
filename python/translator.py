# Braille to English letter mapping
BRAILLE_LETTER_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
}

# Braille to Number letter mapping
BRAILLE_NUMBER_MAP = {
    '0': '.O.OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Braille to Symbol letter mapping
BRAILLE_SYMBOL_MAP = {
    ',': '..O...', ';': '..O.O.', ':': '..OO..', '.': '..OOO.', '!': '..OO.O', '?': '..O.OO',
    '-': '....O.', '(': '...OO.', ')': '...OOO', '/': '...O.O', '<': '...OOO', '>': '...OOO'
}

# Special markers
CAPITAL_MARKER = '.....O'
NUMBER_MARKER = '.O.OOO'
DECIMAL_MARKER = '.O...O'
SPACE = '......'

# Reverse the Braille Letter mapping
ENGLISH_LETTER_MAP = {braille: char for char, braille in BRAILLE_LETTER_MAP.items()}

# Reverse the Braille Number mapping
ENGLISH_NUMBER_MAP = {braille: char for char, braille in BRAILLE_NUMBER_MAP.items()}

# Reverse the Braille Symbol mapping
ENGLISH_SYMBOL_MAP = {braille: char for char, braille in BRAILLE_SYMBOL_MAP.items()}

# Checks if the input string is a valid Braille representation.
def is_braille(input_string):
    return all(char in 'O.' for char in input_string) and len(input_string) % 6 == 0

# Translate English to Braille.
def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_MARKER)
                number_mode = True
            result.append(BRAILLE_NUMBER_MAP[char])
        elif char == ' ':
            result.append(SPACE)
            number_mode = False
        elif char.isupper():
            result.append(CAPITAL_MARKER)
            result.append(BRAILLE_LETTER_MAP[char.lower()])
            number_mode = False
        else:
            braille_char = BRAILLE_LETTER_MAP.get(char, BRAILLE_SYMBOL_MAP.get(char, ''))
            result.append(braille_char)
            number_mode = False
            
    return ''.join(result)

# Translate Braille to English.
def braille_to_english(braille):
    result = []
    number_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        # Check current symbol being processed

        # Capitalize the next character
        if symbol == CAPITAL_MARKER:  
            i += 6  
            if i + 6 <= len(braille): 
                next_symbol = braille[i:i+6]
                capitalized_char = ENGLISH_LETTER_MAP.get(next_symbol, '').upper()
                result.append(capitalized_char)
                i += 6  
            else:
                break

        # Number mode starts here
        elif symbol == NUMBER_MARKER:  
            number_mode = True
            i += 6

        # Handle space   
        elif symbol == SPACE:  
            result.append(' ')
            number_mode = False
            i += 6
            
        else:
            char = ENGLISH_LETTER_MAP.get(symbol, ENGLISH_NUMBER_MAP.get(symbol, ENGLISH_SYMBOL_MAP.get(symbol, '')))
            if number_mode:
                if char.isdigit():
                    result.append(char)  
                else:
                    result.append('') 
            else:
                result.append(char)  
            i += 6

    return ''.join(result)


# Translate the input text between Braille and English.
def translator(input_text):
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

# Get input from command-line arguments
if __name__ == '__main__':
    import sys
    input_text = ' '.join(sys.argv[1:])
    translator(input_text)