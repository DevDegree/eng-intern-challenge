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
    BRAILLE_UPPERCASE = '.....O'
    BRAILLE_DECIMAL = '.O...O'
    BRAILLE_NUMBER = '.O.OOO'
    BRAILLE_SPACE = '......'
    translated_string = ''
    isUppercase = False
    isDecimal = False
    isNumber = False
    for i in range(0, len(word), 6):
        current_braille = word[i: i + 6]
        if (current_braille == BRAILLE_SPACE):
            translated_string += ' '
            isUppercase = False
            isDecimal = False
            isNumber = False
        elif (isUppercase):
            translated_string += lang_dict.get(current_braille).upper()
            isUppercase = False
        elif (isDecimal or isNumber):
            translated_string += num_dict.get(current_braille)
        else:
            isUppercase = current_braille == BRAILLE_UPPERCASE
            isDecimal = current_braille == BRAILLE_DECIMAL
            isNumber = current_braille == BRAILLE_NUMBER
            if (isDecimal):
                translated_string += '.'
            elif(not isUppercase and not isNumber):
                translated_string += lang_dict.get(current_braille)
    return translated_string

def eng_to_braille(word, lang_dict, num_dict):
    BRAILLE_UPPERCASE = '.....O'
    BRAILLE_DECIMAL = '.O...O'
    BRAILLE_NUMBER = '.O.OOO'
    BRAILLE_SPACE = '......'
    translated_string = ''
    isDecimal = word.isdecimal()
    if (isDecimal):
        translated_string += BRAILLE_NUMBER

    for current_char in word:
        if (current_char == ' '):
            translated_string += BRAILLE_SPACE
            isDecimal = False
        elif (current_char.isupper()):
            translated_string += BRAILLE_UPPERCASE
            translated_string += lang_dict.get(current_char.lower())
        elif(isDecimal):
            if (current_char == '.'):
                translated_string += BRAILLE_DECIMAL
            else:
                translated_string += num_dict.get(current_char)
        elif(current_char.isnumeric()):
            translated_string += BRAILLE_NUMBER
            translated_string += num_dict.get(current_char)
        else:
            translated_string += lang_dict.get(current_char)
    return translated_string

def braille_translator(words):
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

    eng_dict = {v: k for k, v in braille_dict.items()}
    eng_num_dict = {v: k for k, v in braille_num_dict.items()}



    translated_word = ""

    for i in range(0, len(words), 1):
        if (is_braille(words[i])):
            if (i > 0):
                translated_word += ' '
            translated_word += braille_to_eng(words[i], eng_dict, eng_num_dict)
        else:
            if (i > 0):
                translated_word += '......'
            translated_word += eng_to_braille(words[i], braille_dict, braille_num_dict)
    
    return translated_word


if __name__ == "__main__":
    sys.stdout.write(braille_translator(sys.argv[1:]))
