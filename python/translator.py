import sys

# Braille Indicators
BRAILLE_CAPITAL_INDICATOR = 'capital_follows'
BRAILLE_DECIMAL_INDICATOR = 'decimal_follows'
BRAILLE_NUMBER_INDICATOR = 'number_follows'

# Braille encoding for English Characters
BRAILLE_TO_ENGLISH_CHARACTER = {
    # Alphabets
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    # Punctuations
    '......': ' ', '..OO.O': ',', '..O...': '.', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
    # Special Cases
    '.....O': BRAILLE_CAPITAL_INDICATOR, '.O...O': BRAILLE_DECIMAL_INDICATOR, '.O.OOO': BRAILLE_NUMBER_INDICATOR,
}

# Braille encoding for Digits
BRAILLE_TO_DIGIT = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

# Reverse the character and digit Braille mappings
ENGLISH_CHARACTER_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH_CHARACTER.items()}
DIGIT_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_DIGIT.items()}
# Combine reversed character and digit Braille mappings into one english mapping as each key is unique
ENGLISH_TO_BRAILLE = {**ENGLISH_CHARACTER_TO_BRAILLE, **DIGIT_TO_BRAILLE}

def english_to_braille(english_text):
    """Convert English to Braille format."""
    braille_text = []
    number_mode = False
    for c in english_text:
        if c == ' ':
            braille_text.append(ENGLISH_TO_BRAILLE[c])
            number_mode = False
        elif c.isupper():
            braille_text.append(ENGLISH_TO_BRAILLE[BRAILLE_CAPITAL_INDICATOR])
            braille_text.append(ENGLISH_TO_BRAILLE[c.lower()])
        elif c == '.':
            braille_text.append(ENGLISH_TO_BRAILLE[BRAILLE_DECIMAL_INDICATOR])
            braille_text.append(ENGLISH_TO_BRAILLE[c])
        elif number_mode:
            braille_text.append(ENGLISH_TO_BRAILLE[c])
        elif c.isdigit():
            number_mode = True
            braille_text.append(ENGLISH_TO_BRAILLE[BRAILLE_NUMBER_INDICATOR])
            braille_text.append(ENGLISH_TO_BRAILLE[c])
        else:
            braille_text.append(ENGLISH_TO_BRAILLE[c])

    return ''.join(braille_text)
    
def braille_to_english(braille_text):
    """Convert Braille to English format."""
    english_text = []
    capital_mode = False
    decimal_mode = False
    number_mode = False
    for i in range(0, len(braille_text), 6):
        braille_cell = braille_text[i:i+6]
        if braille_cell == ENGLISH_TO_BRAILLE[' ']:
            english_text.append(BRAILLE_TO_ENGLISH_CHARACTER[braille_cell])
            number_mode = False
        elif capital_mode:
            english_text.append(BRAILLE_TO_ENGLISH_CHARACTER[braille_cell].upper())
            capital_mode = False
        elif decimal_mode:
            english_text.append(BRAILLE_TO_ENGLISH_CHARACTER['.'])
            decimal_mode = False
        elif number_mode:
            english_text.append(BRAILLE_TO_DIGIT[braille_cell])
        elif braille_cell == ENGLISH_TO_BRAILLE[BRAILLE_CAPITAL_INDICATOR]:
            capital_mode = True
        elif braille_cell == ENGLISH_TO_BRAILLE[BRAILLE_DECIMAL_INDICATOR]:
            decimal_mode = True
        elif braille_cell == ENGLISH_TO_BRAILLE[BRAILLE_NUMBER_INDICATOR]:
            number_mode = True
        else:
            english_text.append(BRAILLE_TO_ENGLISH_CHARACTER[braille_cell])
    
    return ''.join(english_text)
    
def is_braille_format(text):
    """Check if the string is in Braille representation."""
    
    # Check if the length of the string is divisible by 6
    if len(text) % 6 != 0:
        return False
        
    # Check if all characters in the string are either 'O' or '.'
    for character in text:
        if character not in ['O','.']:
            return False
                
    return True

def is_english_format(text):
    """Check if the string is in English representation."""
    for character in text:
        # Check if the character is alphanumeric, a space, or defined symbol
        if not (character.isalnum() or character.isspace() or character in ".,?!:;-/<>()"):
            return False
    return True

def main():
    if (len(sys.argv) < 2):
        print("File or arguments missing.")
    
    argList = sys.argv[1:]
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille_format(input_text):
        print(braille_to_english(input_text))
    elif is_english_format(input_text):
        print(english_to_braille(input_text))
    else:
        print("Unable to convert: Format is neither english nor braille.")

if __name__ == "__main__":    
    main()