import sys

# Braille to English and English to Braille mappings
BRAILLE_ALPHABET = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', ' ': '......',  # Space
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Special markers in Braille
CAPITAL_PREFIX = '.....O'
NUMBER_PREFIX = '.O.OOO'

# Reverse mapping for Braille to English
REVERSE_BRAILLE = {v: k for k, v in BRAILLE_ALPHABET.items()}
REVERSE_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

def is_braille(input_string):
    """Determine if the input is Braille based on the character patterns."""
    return all(char in 'O.' for char in input_string)

def english_to_braille(text):
    """Translate English text to Braille."""
    braille = []
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            braille.append(NUMBER_PREFIX)
            number_mode = True
        elif not char.isdigit():
            number_mode = False
            
        if char.isupper():
            braille.append(CAPITAL_PREFIX)
            braille.append(BRAILLE_ALPHABET[char.upper()])
        elif char.isdigit():
            braille.append(BRAILLE_NUMBERS[char])
        else:
            braille.append(BRAILLE_ALPHABET[char.upper()])
    
    return ''.join(braille)

def braille_to_english(braille):
    """Translate Braille text to English."""
    english = []
    index = 0
    length = len(braille)
    capital_mode = False
    number_mode = False
    
    while index < length:
        chunk = braille[index:index+6]
        
        if chunk == CAPITAL_PREFIX:
            capital_mode = True
            index += 6
            continue
        elif chunk == NUMBER_PREFIX:
            number_mode = True
            index += 6
            continue
        elif chunk == '......':
            english.append(' ')
        elif number_mode:
            english.append(REVERSE_NUMBERS.get(chunk, '?'))
        else:
            letter = REVERSE_BRAILLE.get(chunk, '?')
            if capital_mode:
                letter = letter.upper()
                capital_mode = False
            english.append(letter)
        
        index += 6
    
    return ''.join(english)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)
    
    input_text = sys.argv[1]
    
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))
