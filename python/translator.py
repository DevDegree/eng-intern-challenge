# Author: Zipeng Liang
# Description: Braille translation - Translator between Braille and English

import sys

# Dictionary for Braille to English
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b',
    'OO....': 'c', 'OO.O..': 'd', 
    'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', 
    '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 
    'O..OO.': 'o', 'OOO.O.': 'p', 
    'OOOOO.': 'q', 'O.OOO.': 'r', 
    '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', 
    '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z', 
    '......': ' ', '.': '..OO.O',
    ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO',
    '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O',
    ')': '.O.OO.', '.....O': 'capital', 
    '.O...O': 'decimal', '.O.OOO': 'number'
}

# Dictionary for English to Braille
ENGLISH_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_ENGLISH.items()}

# Dictionary betweeen digit and corresponding letter since they are the same Braille letter 
NUMBER_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def braille_to_english(braille):
    '''
    Converts a Braille-encoded string into its English equivalent.
    
    The input Braille string is processed in chunks of 6 characters, where each chunk represents a Braille character. 
    The function supports special Braille symbols for capitalization and number mode.
    
    Parameters:
    braille: A string of Braille characters

    Returns: The translated English string.
    '''
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        if char == ENGLISH_TO_BRAILLE['capital']:
            capitalize_next = True
        elif char == ENGLISH_TO_BRAILLE['number'] or char == ENGLISH_TO_BRAILLE['decimal']:
            number_mode = True
        else:
            letter = BRAILLE_TO_ENGLISH[char]
            if number_mode and letter in NUMBER_MAP:
                result.append(NUMBER_MAP[letter])
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
                number_mode = False
        i += 6

    return ''.join(result)

def english_to_braille(english):
    '''
    Converts an English string into its Braille equivalent.
    
    The function processes an English string, character by character, 
    and converts each character into its Braille representation using a predefined mapping. 
    It handles both letters and numbers, as well as capitalization.

    Parameters:
    english: A string of English characters

    Returns: The translated Braille string.
    '''
    result = []
    number_mode = False

    for char in english:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[list(NUMBER_MAP.keys())[list(NUMBER_MAP.values()).index(char)]])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital'])
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char.lower()])

    return ''.join(result)


def translate(input_string):
    '''
    Detect whether the input is Braille or English and translate accordingly

    Parameters:
    input_string: The input string

    Returns: The translated string.
    '''

    if set(input_string).issubset({'O', '.'}) and len(input_string) % 6 == 0:
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    # Check input length
    if len(sys.argv) < 1:
        print("Please provide valid input format")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    print(translate(input_string))