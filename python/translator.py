"""
Command-line application that translates Braille to English and vice versa.
"""
import sys

# Symbol conversions
ALPHA_TO_BRAILLE = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
                    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
                    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
                    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
                    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
                    'z': 'O..OOO'}
NUMBER_TO_BRAILLE = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
                     '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}
BRAILLE_TO_ALPHA = dict((v,k) for k,v in ALPHA_TO_BRAILLE.items())  # flip key and value pairs of ALPHA_TO_BRAILLE
BRAILLE_TO_NUMBER = dict((v,k) for k,v in NUMBER_TO_BRAILLE.items())  # flip key and value pairs of NUMBER_TO_BRAILLE

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'
BRAILLE_SPACE = '......'


def isBraille(input_str):
    """
    Checks whether input string is Braille or not.
    Braille inputs only consist of 'O' and '.', and have a length divisible by 6 because each symbol is represented by
    a 6-character string.
    """
    if all([c in ['O', '.'] for c in input_str]) and len(input_str) % 6 == 0:
        return True
    return False


def translateBrailleToEnglish(input_str):
    """
    Converts Braille string to English by iterating through segments of 6 characters.
    input_str (str): string text in Braille
    """
    output_str = ''

    i = 0
    capital_follows = False  # applies to next symbol
    number_follows = False  # applies to all following symbols until next space
    while i < len(input_str):
        # get 6-character string for current symbol
        curr_symbol = input_str[i:i+6]

        if curr_symbol == BRAILLE_CAPITAL:
            capital_follows = True
            translated_symbol = ''
        elif curr_symbol == BRAILLE_NUMBER:
            number_follows = True
            translated_symbol = ''

        elif curr_symbol == BRAILLE_SPACE:
            translated_symbol = ' '
            number_follows = False

        elif number_follows and curr_symbol in BRAILLE_TO_NUMBER:
            # number
            translated_symbol = BRAILLE_TO_NUMBER[curr_symbol]

            if capital_follows:
                # only applies to next symbol, which does not affect numbers
                capital_follows = False
        else:
            # alphabet letter
            translated_symbol = BRAILLE_TO_ALPHA[curr_symbol]
            if capital_follows:
                translated_symbol = translated_symbol.capitalize()
                capital_follows = False

        output_str += translated_symbol
        i += 6
    return output_str


def translateEnglishToBraille(input_str):
    """
    Converts English string to Braille by iterating through characters.
    input_str (str): string text in English
    """
    output_str = ''

    is_number = False
    for curr_symbol in input_str:
        if curr_symbol == ' ':
            # space
            is_number = False
            output_str += BRAILLE_SPACE
        elif curr_symbol.isalpha():
            # alphabet letter
            if curr_symbol.isupper():
                output_str += BRAILLE_CAPITAL
            output_str += ALPHA_TO_BRAILLE[curr_symbol.lower()]
        else: 
            # number
            if not is_number:
                output_str += BRAILLE_NUMBER
                is_number = True
            output_str += NUMBER_TO_BRAILLE[curr_symbol]
    return output_str


def translate(input_str):
    if isBraille(input_str):
        output_str = translateBrailleToEnglish(input_str)
    else:
        output_str = translateEnglishToBraille(input_str)
        
    return output_str


if __name__ == "__main__":
    # Get input string from command line arguments
    input_str = sys.argv[1:]  # remove first item, which is the Python file name
    input_str = ' '.join(input_str)  # Words are loaded as separate arguments, so we need to combine into one string

    # Translate string and print output to the terminal
    translated_text = translate(input_str)
    print(translated_text)