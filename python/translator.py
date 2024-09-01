import sys

# Braille to English translation dictionary
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

REVERSE_BRAILLE_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}
REVERSE_BRAILLE_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

def translate_to_english(braille_string):
    """
    Translates a braille string to English.

    Args:
        braille_string (str): The braille string to be translated.

    Returns:
        str: The translated English string.
    """
    english_string = ''
    is_capital = False
    is_number = False
    # Split the braille_string into chunks of 6 characters each
    letters = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    for letter in letters:
        if letter == BRAILLE_ALPHABET['cap']:
            is_capital = True
        elif letter == BRAILLE_ALPHABET['num']:
            is_number = True
        elif letter == BRAILLE_ALPHABET[' ']:
            is_number = False 
            english_string += ' '
        elif is_number and letter in REVERSE_BRAILLE_NUMBERS:
            english_string += REVERSE_BRAILLE_NUMBERS[letter]
        elif letter in REVERSE_BRAILLE_ALPHABET:
            if is_capital:
                english_string += REVERSE_BRAILLE_ALPHABET[letter].upper()
                is_capital = False
            else:
                english_string += REVERSE_BRAILLE_ALPHABET[letter]
    return english_string

def translate_to_braille(english_string):
    """
    Translates an English string to braille.

    Args:
        english_string (str): The English string to be translated.

    Returns:
        str: The translated braille string.
    """
    braille_string = ''
    is_number = False
    for char in english_string:
        if char.isupper():
            braille_string += BRAILLE_ALPHABET['cap']
            char = char.lower()
        if char.isdigit():
            if not is_number:
                braille_string += BRAILLE_ALPHABET['num']
                is_number = True
            braille_string += BRAILLE_NUMBERS[char]
        else:
            is_number = False
            braille_string += BRAILLE_ALPHABET[char]
    return braille_string

def main():
    """
    Main function that handles command line arguments and calls the appropriate translation function.
    """
    # Concatenate all arguments with spaces in between
    input_string = ' '.join(sys.argv[1:])
    if '.' in input_string:
        translated_string = translate_to_english(input_string)
    else:
        translated_string = translate_to_braille(input_string)
    print(translated_string)

if __name__ == '__main__':
    main()