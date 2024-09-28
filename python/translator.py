import sys

# Map english characters to braille
ENGLISH_TO_BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
}

NUMS_TO_BRAILLE_DICT = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

SYMBOLS_TO_BRAILLE_DICT = {
    ' ': '......', 'capital_follows': '.....0', 'number_follows': '.O.OOO'
}

# Map braille to english characters
BRAILLE_TO_ENGLISH_DICT = {value: key for key, value in ENGLISH_TO_BRAILLE_DICT.items()}
BRAILLE_TO_NUMS_DICT = {value: key for key, value in NUMS_TO_BRAILLE_DICT.items()}
BRAILLE_TO_SYMBOLS = {value: key for key, value in SYMBOLS_TO_BRAILLE_DICT.items()}

# convert english text to braille
def convert_english_to_braille(text):
    braille = ''
    for i, character in enumerate(text):
        # if the character is a capital letter
        if character.isupper():
            braille += SYMBOLS_TO_BRAILLE_DICT['capital_follows']
            braille += ENGLISH_TO_BRAILLE_DICT[character.lower()]
        # if the character is a number
        elif character.isdigit():
            # if the number is the first number in a sequence of numbers or the first character
            if i == 0 or text[i - 1].isdigit():
                braille += SYMBOLS_TO_BRAILLE_DICT['number_follows']
                braille += NUMS_TO_BRAILLE_DICT[character]
            # if the character isn't the first number
            else:
                braille += NUMS_TO_BRAILLE_DICT[character]
        # all other characters (lower case letters and space)
        else:
            if character == ' ':
                braille += SYMBOLS_TO_BRAILLE_DICT[character]
            else:
                braille += ENGLISH_TO_BRAILLE_DICT[character]

    return braille

# convert braille text to english
def convert_braille_to_english(text):
    english = ''
    capital = False
    digit = False
    for i in range(0, len(text), 6):
        character = text[i: i + 6]
        if character in BRAILLE_TO_SYMBOLS:
            if BRAILLE_TO_SYMBOLS[character] == 'capital_follows':
                capital = True
            elif BRAILLE_TO_SYMBOLS[character] == 'number_follows':
                digit = True
            else:
                english += BRAILLE_TO_SYMBOLS[character]
                digit = False
        elif capital:
            english += BRAILLE_TO_ENGLISH_DICT[character].upper()
            capital = False
        elif digit:
            english += BRAILLE_TO_NUMS_DICT[character]
        else:
            english += BRAILLE_TO_ENGLISH_DICT[character]

    return english

# check if the string is english or braille
def is_braille(text):
    for character in text:
        if character not in ['.', 'O']:
            return False
    return True

# Getting the command line arguments
input_string = ' '.join(sys.argv[1:])

# Output
if is_braille(input_string):
    print(convert_braille_to_english(input_string))
else:
    print(convert_english_to_braille(input_string))