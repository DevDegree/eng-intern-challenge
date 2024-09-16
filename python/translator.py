import sys
import re
import math


def is_braille(word):
    """ Checks if word is in Braille

    Valid braille words only contain O or . and are a length multiple of 6
    Keyword arguments:
    word - the string to check
    """
    
    return (bool(re.match('^[O\.]+$', word)) and len(word) % 6 == 0)

def braille_to_eng(word, lang_dict, num_dict):
    """Translates word from Braille to English

    Keyword arguments:
    word - a valid Braille string
    lang_dict - a dictionary that maps Braille characters to English characters
    num_dict - a dictionary that maps Braille numbers to English numbers
    """
    BRAILLE_UPPERCASE = '.....O'
    BRAILLE_DECIMAL = '.O...O'
    BRAILLE_NUMBER = '.O.OOO'
    BRAILLE_SPACE = '......'
    translated_string = ''
    isUppercase = False
    isDecimal = False
    isNumber = False
    # Loop through each Braille substring
    for i in range(0, len(word), 6):
        current_braille = word[i: i + 6]
        # Check if the current braille is any special modifiers
        if (current_braille == BRAILLE_SPACE):
            translated_string += ' '
            # Stops writing a special modifier once a space is hit
            isUppercase = False
            isDecimal = False
            isNumber = False
        elif (isUppercase):
            # Writes only the current character as uppercase
            translated_string += lang_dict.get(current_braille).upper()
            isUppercase = False
        elif (isDecimal or isNumber):
            # Writes the character as a number
            translated_string += num_dict.get(current_braille)
        else:
            # Check for special modifier characters
            isUppercase = current_braille == BRAILLE_UPPERCASE
            isDecimal = current_braille == BRAILLE_DECIMAL
            isNumber = current_braille == BRAILLE_NUMBER
            if (isDecimal):
                # Write a decimal character and all subsequent characters will be written as numbers
                translated_string += '.'
            elif(not isUppercase and not isNumber):
                # Write the current braille as a regular alphabet character
                translated_string += lang_dict.get(current_braille)
    return translated_string

def eng_to_braille(word, lang_dict, num_dict):
    """Translates word from English to Braille

    Key Arguments:
    word - an English string
    lang_dict - a dictionary that maps English characters to Braille characters
    num_dict - a dictionary that maps English numbers to Braille numbers
    """
    BRAILLE_UPPERCASE = '.....O'
    BRAILLE_DECIMAL = '.O...O'
    BRAILLE_NUMBER = '.O.OOO'
    BRAILLE_SPACE = '......'

    translated_string = ''

    # Check if the whole word is a decimal number and should lead with a number symbol
    isDecimal = word.isdecimal()
    if (isDecimal):
        translated_string += BRAILLE_NUMBER

    # Loop through each character of the word
    for current_char in word:
        if (current_char == ' '):
            # Add a space and stop writing characters as decimals
            translated_string += BRAILLE_SPACE
            isDecimal = False
        elif (current_char.isupper()):
            # Add an uppercase symbol before writing letter in
            translated_string += BRAILLE_UPPERCASE
            translated_string += lang_dict.get(current_char.lower())
        elif(isDecimal):
            # Add a decimal symbol if the decimal point is current character
            # Otherwise, write the braille number without the number symbol as it came before this character
            if (current_char == '.'):
                translated_string += BRAILLE_DECIMAL
            else:
                translated_string += num_dict.get(current_char)
        elif(current_char.isnumeric()):
            # Write the number symbol and the character as a braille number
            translated_string += BRAILLE_NUMBER
            translated_string += num_dict.get(current_char)
        else:
            # Write the character as an alphabet braille character
            translated_string += lang_dict.get(current_char)
    return translated_string

def braille_translator(words):
    """Translates a word to either English or Braille based on the detected language

    Key arguments:
    word - a string that is either in English or Braille
    """

    # Create dictionaries to map English characters to Braille
    braille_dict = {
        'a' : 'O.....',
        'b' : 'O.O...',
        'c' : 'OO....',
        'd' : 'OO.O..',
        'e' : 'O..O..',
        'f' : 'OOO...',
        'g' : 'OOOO..',
        'h' : 'O.OO..',
        'i' : '.OO...',
        'j' : '.OOO..',
        'k' : 'O...O.',
        'l' : 'O.O.O.',
        'm' : 'OO..O.',
        'n' : 'OO.OO.',
        'o' : 'O..OO.',
        'p' : 'OOO.O.',
        'q' : 'OOOOO.',
        'r' : 'O.OOO.',
        's' : '.OO.O.',
        't' : '.OOOO.',
        'u' : 'O...OO',
        'v' : 'O.O.OO',
        'w' : '.OOO.O',
        'x' : 'OO..OO',
        'y' : 'OO.OOO',
        'z' : 'O..OOO',
        '.' : '..OO.O',
        ',' : '..O...',
        '?' : '..O.OO',
        '!' : '..OOO.',
        ':' : '..OO..',
        ';' : '..O.O.',
        '-' : '....OO',
        '/' : '.O..O.',
        '<' : '.OO..O',
        '(' : 'O.O..O',
        ')' : '.O.OO.',
        ' ' : '......'
    }
    braille_num_dict = {
        '1' : braille_dict.get('a'),
        '2' : braille_dict.get('b'),
        '3' : braille_dict.get('c'),
        '4' : braille_dict.get('d'),
        '5' : braille_dict.get('e'),
        '6' : braille_dict.get('f'),
        '7' : braille_dict.get('g'),
        '8' : braille_dict.get('h'),
        '9' : braille_dict.get('i')
    }

    # Create dictionaries to map Braille characters to English
    eng_dict = {v: k for k, v in braille_dict.items()}
    eng_num_dict = {v: k for k, v in braille_num_dict.items()}



    translated_word = ""

    # Go through each word
    for i in range(0, len(words), 1):
        # Check whether the word is being translated to Braille or English
        if (is_braille(words[i])):
            # Add a space first if it is not the first word
            if (i > 0):
                translated_word += ' '
            translated_word += braille_to_eng(words[i], eng_dict, eng_num_dict)
        else:
            # Add a space if it is not the first word
            if (i > 0):
                translated_word += '......'
            translated_word += eng_to_braille(words[i], braille_dict, braille_num_dict)
    
    return translated_word


if __name__ == "__main__":
    sys.stdout.write(braille_translator(sys.argv[1:]))
