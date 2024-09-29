import sys

# Braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', 
    '......': ' ', 
    '.....O': 'capital follows', '.O.OOO': 'number follows', '.O...O': 'decimal follows'
}

# Reverse mapping
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

NUMBER_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

BRAILLE_DECIMAL = {
    '..OO.O':'.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';',
    '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', ".O.OO.": ')'
}

# reverse mapping
ENGLISH_DECIMAL = {v: k for k, v in BRAILLE_DECIMAL.items()}

def braille_to_english(braille):
    '''
    Convert braille to english

    Args:
        braille (str): Braille text to convert

    Returns:
        str: English text
    '''

    result = []
    capitalize_next = False # Flag to capitalize next letter
    number_mode = False # Flag to indicate number mode
    decimal_mode = False # Flag to indicate decimal mode
    i = 0

    while i < len(braille):
        char = braille[i:i+6] # Get the next 6 characters : a single braille character
        if char == ENGLISH_TO_BRAILLE['capital follows']: # Check if the character is a flag to capitalize next letter
            capitalize_next = True
        elif char == ENGLISH_TO_BRAILLE['number follows']: # Check if the character is a flag to indicate number next letter
            number_mode = True
        elif char == ENGLISH_TO_BRAILLE['decimal follows']: # Check if the character is a flag to indicate decimal mode
            decimal_mode = True
        elif char in BRAILLE_DECIMAL and decimal_mode:
            result.append(BRAILLE_DECIMAL[char])
        elif char in BRAILLE_TO_ENGLISH:
            letter = BRAILLE_TO_ENGLISH[char]
            if number_mode and letter in NUMBER_MAP:
                result.append(NUMBER_MAP[letter])
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                if decimal_mode:
                    decimal_mode = False
                result.append(letter)
                number_mode = False
        i += 6
    return ''.join(result)

def english_to_braille(english):
    '''
    Convert english to braille

    Args:
        english (str): English text to convert

    Returns:
        str: Braille text
    '''

    result = []
    number_mode = False # Flag to indicate number mode
    decimal_mode = False # Flag to indicate decimal mode
    
    for char in english:
        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE['capital follows'])
            char = char.lower()
        elif char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number follows'])
                number_mode = True
            char = list(NUMBER_MAP.keys())[list(NUMBER_MAP.values()).index(char)] # Get the corresponding letter
        else:
            number_mode = False

        if char in ENGLISH_DECIMAL:
            result.append(ENGLISH_TO_BRAILLE['decimal follows'])
            decimal_mode = True
        else:
            decimal_mode = False

        
        if not decimal_mode:
            result.append(ENGLISH_TO_BRAILLE[char])
        else:
            result.append(ENGLISH_DECIMAL[char])
    return ''.join(result)

def is_braille(text):
    '''
    Check if the input text is braille

    Args:
        text (str): Input text

    Returns:
        bool: True if the input text is braille, False otherwise
    '''

    return all(c in 'O.' for c in text)

def translate(text):
    '''
    Translate the input text

    Args:
        text (str): Input text to translate 

    Returns:
        str: Translated text
    '''

    if is_braille(text):
        if len(text) % 6 != 0: # Braille input must be a multiple of 6 characters
            return "Invalid Braille Input"
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py {{ text/braille to translate }}")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))