# Dictionary converting english alphabet characters to braille
character_to_braille = {
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
    'z': 'O..OOO'
}

# Dictionary converting digits to braille
digit_to_braille = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}

# Dictionary converting english punctuation to braille
punctuation_to_braille = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}

# Braille symbols for capitalization, decimal, and number follows
uppercase_follows = '.....O'
decimal_follows = '.O...O'
number_follows = '.O.OOO'

# Dictionaries containing braille to character, digit, punctuation
# Obtained by swapping key: values from the original dictionaries
braille_to_character = dict((reversed(item) for item in character_to_braille.items()))
braille_to_digit = dict((reversed(item) for item in digit_to_braille.items()))
braille_to_punctuation = dict((reversed(item) for item in punctuation_to_braille.items()))


"""
    Convert an English text to Braille
        param text: English text to convert
        returns: Braille representation of the text
"""
def english_to_braille(text):

    braille_text = ''
    is_number = False

    for char in text:

        if char.isalpha():
            if char.isupper():  # if the character is uppercase add the uppercase_follows
                braille_text += uppercase_follows
            braille_text += character_to_braille[char.lower()]

        elif char in digit_to_braille:
            if not is_number:  # if we are starting a number add the number_follows
                is_number = True
                braille_text += number_follows

            braille_text += digit_to_braille[char]

        elif char in punctuation_to_braille:
            if char == "." and is_number:  # if we are in a number and we find a decimal add the decimal_follows
                braille_text += decimal_follows
            elif char == " " and is_number:  # if we are in a number and we find a space, end the number
                is_number = False

            braille_text += punctuation_to_braille[char]

    return braille_text


"""
    Convert a Braille text to English
        param text: Braille text to convert
        returns: English representation of the text
"""
def braille_to_english(text):
    
    english_text = ''
    is_uppercase = False
    is_number = False

    for i in range(0, len(text), 6):
        braille = text[i: i+6] # get the next braille item (6 characters)

        if braille == uppercase_follows:
            is_uppercase = True

        elif braille == number_follows:
            is_number = True
        
        elif is_number:
            if braille == punctuation_to_braille['.']:  # if we find a decimal, add it to the english text
                english_text += '.'
            elif braille == punctuation_to_braille[' ']: # if we find a space, end the number and add the space character
                is_number = False
                english_text += ' '
            elif braille == decimal_follows:
                continue
            else:
                english_text += braille_to_digit[braille]

        elif braille in braille_to_character:
            if is_uppercase:
                english_text += braille_to_character[braille].upper() # if the character is uppercase, convert to uppercase
                is_uppercase = False
            else:
                english_text += braille_to_character[braille]
        else:
            english_text += braille_to_punctuation[braille]
    
    return english_text


if __name__ == '__main__':
    import sys
    args = sys.argv
    args.pop(0)

    # Get the input text as a string
    text = ' '.join(args)
    # Get the unique characters in the input
    characters = set(text)

    braille_chars = {"O", "."}

    # Check if the input is in braille or english and print the appropriate translation
    # We also handle the case of a string of dots that is a multiple of 6 which represent spaces in braille
    if characters == braille_chars or (characters == {"."} and len(text) % 6 == 0):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))
