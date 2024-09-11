import sys
"""
This module contains the functions to translate the input string to the either english or braille.
"""

# Constants for the input types
BRAILLE = "braille"
ENGLISH = "english"

# Dictionary for both english to braille and braille to english
# Note, numbers are represented by the letters a-j in braille; so no need to add
BRAILLE_TO_ENGLISH = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",  
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.OOOO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " "
}

# Reverse the dictionary for english to braille
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# Braille special symbols
CAPITAL_FOLLOWS_SYMBOL = ".....O"
NUMBER_FOLLOWS_SYMBOL = ".O.OOO"

def input_type(input_str : str) -> str:
    """
    Function to check the type of input string and returns the type of input string.

    :param input_str: input string that is to be checked.
    :type input_str: str
    :return: The type of input string. 
    :rtype: str
    """
    # check if the string is divivisble by 6, and only contains '.' and 'O'
    if len(input_str) % 6 == 0 and all(char in ['.', 'O'] for char in input_str):
        return BRAILLE
    
    # otherwise it's an english string
    return ENGLISH

def english_to_braille(english_input : str) -> str:
    """
    Function to convert the english string to braille string.

    :param english_str: English string that is to be converted to braille.
    :type english_str: str
    :return: The braille translation of the english string.
    :rtype: str
    """
    braille_translation = ""

    # flags for cheking when to end the number
    number = False
    for char in english_input:

        # checking for capital or number to add the special symbols
        if char.isupper():
            braille_translation += CAPITAL_FOLLOWS_SYMBOL
            char = char.lower()
        
        if char.isdigit() and not number:
            braille_translation += NUMBER_FOLLOWS_SYMBOL
            number = True
        
        if char == " ":
            number = False
        
        if number and char.isnumeric():
            if char == '0':
                char = 'j'
            else:
                char = chr(ord('a') + (ord(char) - ord('0')) - 1)

        braille_translation += ENGLISH_TO_BRAILLE[char]
    
    return braille_translation
       

def braille_to_english(braille_input : str) -> str:
    """
    Function to convert the braille string to english string.

    :param braille_input: Braille string that is to be converted to english.
    :type braille_input: str
    :return: The english translation of the braille string.
    :rtype: str
    """

    english_translation = ""

    # flags for cheking if the next braille char is a number or a capital letter
    capital, number = False, False

    # for loop that goes through multiples of 6 and then translate it character-wise to english
    for index in range(0, len(braille_input), 6):
        braille_char = braille_input[index:index+6]

        # check if the braille char is a special symbol
        if braille_char == CAPITAL_FOLLOWS_SYMBOL:
            capital = True
            continue

        if braille_char == NUMBER_FOLLOWS_SYMBOL:
            number = True
            continue
        
        english_char = BRAILLE_TO_ENGLISH[braille_char]

        if english_char == " ": # if it's a space, reset the flags
            capital, number = False, False
            
        # translate the braille char to english, with regard to the special symbols
        if capital:
            english_char = BRAILLE_TO_ENGLISH[braille_char].capitalize()
            capital = False
        
        # if it's a number, translate it to the number and check for it's range
        elif number and 'a' <= english_char <= 'j':            
            number_translation = ord(english_char) - ord('a') + 1 

            # base 10; j goes to zero so we mod 10 to ensure this
            number_translation %= 10 
            english_char = str(number_translation)
        
        english_translation += english_char
    
    return english_translation

def main():
    """
    Main function that reads the input from the command line and prints the translated string.
    """
    input_str = ' '.join(sys.argv[1:])
    input_type_str = input_type(input_str)
    translation = ""

    if input_type_str == BRAILLE:
        translation = braille_to_english(input_str)
    else:
        translation = english_to_braille(input_str)
    
    print(translation)

if __name__ == "__main__":
    main()
