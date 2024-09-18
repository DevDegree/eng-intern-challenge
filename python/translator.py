
# Dict for English to Braille conversion
english_to_braille = {
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
    'capital': '.....O',
    'number': '.O.OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

# Separate dicts for Braille to English conversion due to duplicate mappings
braille_to_letter = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c', 
    'OO.O..': 'd', 
    'O..O..': 'e', 
    'OOO...': 'f', 
    'OOOO..': 'g',
    'O.OO..': 'h', 
    '.OO...': 'i', 
    '.OOO..': 'j', 
    'O...O.': 'k', 
    'O.O.O.': 'l', 
    'OO..O.': 'm', 
    'OO.OO.': 'n',
    'O..OO.': 'o', 
    'OOO.O.': 'p', 
    'OOOOO.': 'q', 
    'O.OOO.': 'r', 
    '.OO.O.': 's', 
    '.OOOO.': 't', 
    'O...OO': 'u',
    'O.O.OO': 'v', 
    '.OOO.O': 'w', 
    'OO..OO': 'x', 
    'OO.OOO': 'y', 
    'O..OOO': 'z',
}

braille_to_number = {
    'O.....': '1', 
    'O.O...': '2', 
    'OO....': '3', 
    'OO.O..': '4', 
    'O..O..': '5', 
    'OOO...': '6', 
    'OOOO..': '7',
    'O.OO..': '8', 
    '.OO...': '9',
    '.OOO..': '0'
}

def is_braille(input_string):
    """
    Determines if the input string is Braille or English
    :param input_string: A string of characters
    :return: True if the input string is Braille, False otherwise
    """

    return all(char in ['O', '.'] for char in input_string)


def translate_braille_to_english(braille_string):
    """
    Translates a string of Braille characters to English.
    :param braille_string: A string of Braille characters (O and .)
    :return: A string of English characters
    """

    # If braille input is not a multiple of 6, exit early
    str_len = len(braille_string)
    if str_len % 6 != 0:
        print("Invalid input: Braille input length is not a multiple of 6")
        sys.exit(2)

    # Break the input into chunks of 6 characters
    letters = [braille_string[i:i+6] for i in range(0, str_len, 6)]
    translated = []
    number_mode = False
    capitalize_next = False 
    
    for letter in letters:
        if letter == '......':
            translated.append(' ')
            number_mode = False
        elif letter == '.....O':
            capitalize_next = True
        elif letter == '.O.OOO':
            number_mode = True
        elif number_mode and letter in braille_to_number: 
            translated.append(braille_to_number[letter])
        elif letter in braille_to_letter:
            char = braille_to_letter[letter]
            if capitalize_next:
                translated.append(char.upper())
                capitalize_next = False
            else:
                translated.append(char)
            number_mode = False  # Exit number mode after translating letters
        else:
            continue  # Skip unrecognized Braille patterns

    return ''.join(translated).strip()


def translate_english_to_braille(english_string):
    """
    Translates a string of English characters to Braille.
    :param english_string: A string of English characters
    :return: A string of Braille characters
    """

    # As per the requirements, only letters, numbers, and spaces are allowed
    valid_english = bool(re.fullmatch(r'[a-zA-Z0-9 ]+', english_string))
    if not valid_english:
        print("Invalid input: English input contains invalid characters")
        sys.exit(2)

    translated = []
    number_mode = False
    for char in english_string:
        if char.isdigit():
            if not number_mode:
                translated.append(english_to_braille['number'])
                number_mode = True
            translated.append(english_to_braille[char])
        elif char.isalpha():
            if char.isupper():
                translated.append(english_to_braille['capital'])
                translated.append(english_to_braille[char.lower()])
            else:
                translated.append(english_to_braille[char])
            number_mode = False
        elif char == ' ':
            translated.append(english_to_braille[' '])
            number_mode = False
    return ''.join(translated)


if __name__ == "__main__":
    import sys
    import re

    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(2)

    input_string = ' '.join(sys.argv[1:])
    is_braile = bool(re.fullmatch(r'[O.]+', input_string))

    if is_braile:
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))
