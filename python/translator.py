import sys
from enum import Enum

# Special braille characters that don't visually appear but have special meanings
braille_uppercase = '.....O'
braille_number_symbol = '.O.OOO'

# Lookup for english to braille translation
# These symbols could also be programmatically generated beyond the first 10 using their pattern if desired
# I elected to keep everything within one file for simplicity given that an automated test will be run on it
english_to_braille_lookup = {
    ' ': '......',
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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}


# These lookups are generated using the english to braille lookup. This is currently done at runtime, although could
# easily be instead done beforehand and saved in a similar format to above
braille_to_english_lookup_alpha = {}
braille_to_english_lookup_numeric = {}


# Store the state when reading in braille
class BrailleState(Enum):
    LOWERCASE = 0
    NUMBER = 1
    UPPERCASE = 2


# Take the english to braille lookup and create lookups from braille to english by reversing the key value pairs.
# Split into alphabet characters and numeric characters since they share symbols
def generate_braille_to_english_lookup():
    for english, braille in english_to_braille_lookup.items():
        if english.isnumeric():
            braille_to_english_lookup_numeric[braille] = english
        else:
            braille_to_english_lookup_alpha[braille] = english


# Returns a string built using the command line arguments
def get_argument_input():
    arg_input = ""

    # Iterate over the arguments and add them to the input string
    for arg in sys.argv[1:]:
        # If not the first argument, insert a space between the words
        if arg_input != "":
            arg_input += " "
        arg_input += arg

    return arg_input


# Takes english text and returns that text in braille
def english_to_braille(english_text):
    braille_text = ""
    outputting_numbers = False  # Tracks if a "is a number" braille symbol was already written

    for c in english_text:
        if c.isupper():  # If the character that is being added is uppercase, add the symbol that specified that the next is uppercase
            braille_text += braille_uppercase
        elif c.isnumeric() and not outputting_numbers:  # If it is numeric and there isn't already a symbol specifying such, add it and change the flag
            outputting_numbers = True
            braille_text += braille_number_symbol
        elif c == ' ':  # If it is a space, remove the flag that tracks if there is a corresponding numeric symbol
            outputting_numbers = False

        # Add the character from the lookup
        braille_text += english_to_braille_lookup[c.lower()]

    return braille_text


# Takes braille text and returns that text in english
def braille_to_english(braille_text):
    english_text = ""

    # Start in the lowercase state, since no symbol has yet been read to require switching
    state = BrailleState.LOWERCASE

    # Look through the text in increments of 6, retrieving the corresponding block of braille
    for i in range(0, len(braille_text), 6):
        braille_character = braille_text[i:i+6]

        # If reading a braille capital or number follows symbol, switch to the corresponding state
        # Otherwise run the logic to add an english character
        if braille_character == braille_uppercase:
            state = BrailleState.UPPERCASE
        elif braille_character == braille_number_symbol:
            state = BrailleState.NUMBER
        else:
            # If outputting a space, switch back to the lowercase state so that this and future characters are letters
            if braille_character == english_to_braille_lookup[' ']:
                state = BrailleState.LOWERCASE

            # If within the influence of a number follows character, add from the list of number characters
            # Otherwise add from the list of alphabet characters, converting to uppercase if necessary
            if state == BrailleState.NUMBER:
                english_text += braille_to_english_lookup_numeric[braille_character]
            else:
                english_character = braille_to_english_lookup_alpha[braille_character]

                # If the preceding character was an uppercase follows character, switch to uppercase and reset the state
                if state == BrailleState.UPPERCASE:
                    english_character = english_character.upper()
                    state = BrailleState.LOWERCASE

                # Add the character to the text
                english_text += english_character

    return english_text


def main():
    # Generate the english to braille lookup
    generate_braille_to_english_lookup()

    # Retrieve the input from the arguments
    original_text = get_argument_input()

    translated_text = braille_to_english(original_text)
    # translated_text = english_to_braille(original_text)

    print(translated_text)


main()