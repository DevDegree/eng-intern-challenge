# @CelinZiad
# Celine Ziade
# celine.ziade@outlook.com
# shopify github challenge

# import system specific parameters and functions like command-line arguments
import sys

# Create the braille alphabet array to be used as translation
# Each element is a 6 digit combination of O and .
braille_alphabet_letter = {

    # letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # punctuation
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    '-': '....OO', ' ': '......'
}

# create the braille alphabet array when number_follows to be used as translation
# each element is a 6 digit combination of O and .
braille_alphabet_number = {

    # numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# create variables for grammar indication
capital_follows = '.....O'
number_follows = '.O.OOO'
decimal_follows = '.O...O'

# inverse each element of the braille_alphabet array when input_braille-to-English is required
# english translation is obtained by swapping the roles of each key-value pair in the braille_alphabet
inverse_braille_alphabet_letter = {v: k for k, v in braille_alphabet_letter.items()}
inverse_braille_alphabet_number = {v: k for k, v in braille_alphabet_number.items()}

# function to translate english to braille
def translate_to_braille(input_english):
    translation = []
    isnumber = False  # indicates if letter or number alphabet is needed

    for char in input_english:

        if char.isupper():  # function in sys to detect capital letters
            translation.append(capital_follows)
            translation.append(braille_alphabet_letter[char.lower()])

        elif char.isdigit() and not isnumber:  # function in sys to detect numbers
            translation.append(number_follows)
            translation.append(braille_alphabet_number[char])
            isnumber = True  # number alphabet is needed

        elif char.isdigit():  # numbers have succeeded before
            translation.append(braille_alphabet_number[char])

        else:
            translation.append(braille_alphabet_letter.get(char, ''))
            isnumber = False  # reset number mode when a letter or punctuation is encountered

    return ''.join(translation)  # combine all elements in an array

# function to translate braille to english
def translate_to_english(input_braille):
    translation = []
    i = 0
    isnumber = False # indicates if letter or number alphabet is needed
    iscapital = False # indicates if the next letter should be capitalized

    while i < len(input_braille):

        char_braille = input_braille[i:i + 6]  # input comes in a long string. every 6th element is a character

        if char_braille == capital_follows:
            iscapital = True  # set iscapital flag to capitalize the next letter

        elif char_braille == number_follows:
            isnumber = True

        elif char_braille==decimal_follows:
            isnumber==True
            translation.append("..OO.O")

        else:
            letter = inverse_braille_alphabet_letter.get(char_braille, '')
            number = inverse_braille_alphabet_number.get(char_braille, '')

            if iscapital:
                isnumber = False   # make sure that number is false with a capital
                translation.append(letter.upper())
                iscapital = False  # reset capital flag after processing

            elif isnumber:
                translation.append(number)
    
            else: # lower case letter
                translation.append(letter)
        i += 6

    return ''.join(translation)

# function to check if input is braille or not (if composed in only . and O)
def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

if __name__ == "__main__":

    # if no additional arguments were provided by the user
    if len(sys.argv) == 1:
        sys.exit("No argumens to translate were given, please provide an argument in python.")

    input_string = " ".join(sys.argv[1:])

    # verify which translation function to use
    if is_braille(input_string):
        print(translate_to_english(input_string))

    else:
        print(translate_to_braille(input_string))