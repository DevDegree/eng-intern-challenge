import re
import sys
from enum import Enum


# Enum for Braille representation of alphabets and special characters
class BrailleAlphabetAndSpecialChars(Enum):
    a = "O....."
    b = "O.O..."
    c = "OO...."
    d = "OO.O.."
    e = "O..O.."
    f = "OOO..."
    g = "OOOO.."
    h = "O.OO.."
    i = ".OO..."
    j = ".OOO.."
    k = "O...O."
    l = "O.O.O."
    m = "OO..O."
    n = "OO.OO."
    o = "O..OO."
    p = "OOO.O."
    q = "OOOOO."
    r = "O.OOO."
    s = ".OO.O."
    t = ".OOOO."
    u = "O...OO"
    v = "O.O.OO"
    w = ".OOO.O"
    x = "OO..OO"
    y = "OO.OOO"
    z = "O..OOO"
    period = "..OO.O"
    comma = "..O..."
    question = "..O.OO"
    exclaim = "..OOO."
    colon = "..OO.."
    sColon = "..O.O."
    hyphen = "....OO"
    slash = ".O..O."
    great = "O..OO."
    less = ".OO..O"
    open = "O.O..O"
    close = ".O.OO."
    space = "......"
    capital = ".....O"
    decimal = ".O...O"
    number = ".O.OOO"


# Enum for Braille representation of numbers
class BrailleNumbers(Enum):
    N1 = "O....."
    N2 = "O.O..."
    N3 = "OO...."
    N4 = "OO.O.."
    N5 = "O..O.."
    N6 = "OOO..."
    N7 = "OOOO.."
    N8 = "O.OO.."
    N9 = ".OO..."
    N0 = ".OOO.."


# Function to map special characters to their enum keys during English to Braille conversion
def mapSpecialCharToEnumKey(ch):
    if ch == '.':
        return "period"
    elif ch == ',':
        return "comma"
    elif ch == '?':
        return "question"
    elif ch == '!':
        return "exclaim"
    elif ch == ':':
        return "colon"
    elif ch == ';':
        return "sColon"
    elif ch == '-':
        return "hyphen"
    elif ch == '/':
        return "slash"
    elif ch == '>':
        return "great"
    elif ch == '<':
        return "less"
    elif ch == '(':
        return "open"
    elif ch == ')':
        return "close"
    else:
        return None


# Function to map Braille enum keys back to special characters during Braille to English conversion
def mapEnumKeyToSpecialChar(enum_key):
    if enum_key == "period":
        return '.'
    elif enum_key == "comma":
        return ','
    elif enum_key == "question":
        return '?'
    elif enum_key == "exclaim":
        return '!'
    elif enum_key == "colon":
        return ':'
    elif enum_key == "sColon":
        return ';'
    elif enum_key == "hyphen":
        return '-'
    elif enum_key == "slash":
        return '/'
    elif enum_key == "great":
        return '>'
    elif enum_key == "less":
        return '<'
    elif enum_key == "open":
        return '('
    elif enum_key == "close":
        return ')'
    elif enum_key == "space":
        return ' '
    elif enum_key == "decimal":
        return '.'
    else:
        return None


# Function to detect whether the input is in Braille or English
def detectInputLanguage(input_string):
    # Regex pattern to detect if input consists of 'O' or '.' in lengths divisible by 6
    regex_pattern = r'^[o.]+$'
    if ((len(input_string) % 6 == 0) and not input_string.isspace() and re.match(regex_pattern, input_string)):
        detected_lang = "Braille"
    else:
        detected_lang = "English"
    return detected_lang


# Function to convert English text to Braille representation
def englishToBraille(english_string):
    translated_braille = ""
    i = 0
    while i < len(english_string):
        c = english_string[i]
        # Handling alphabets
        if c.isalpha():
            # Handling uppercase letters
            if c.isupper():
                translated_braille += BrailleAlphabetAndSpecialChars.capital.value
            translated_braille += BrailleAlphabetAndSpecialChars[c.lower()].value

        # Handling numbers
        elif c.isnumeric():
            # Insert number indicator if it's the first numeric character
            if i - 1 < 0 or not english_string[i - 1].isnumeric():
                translated_braille += BrailleAlphabetAndSpecialChars.number.value
            translated_braille += BrailleNumbers["N" + c].value

        # Handling spaces
        elif c.isspace():
            translated_braille += BrailleAlphabetAndSpecialChars.space.value

        # Handling special characters
        elif not c.isalnum():
            enum_key = mapSpecialCharToEnumKey(c)
            if enum_key:
                translated_braille += BrailleAlphabetAndSpecialChars[enum_key].value

        # Fallback for unknown characters
        else:
            translated_braille += "$$$$$$"

        i += 1

    return translated_braille


# Function to convert Braille representation to English text
def brailleToEnglish(braille_string):
    translated_english = ""
    caps_braille = False
    numbers_braille = False

    i = 0
    while i < len(braille_string):
        braille_chunk = braille_string[i:i + 6]

        if len(braille_chunk) < 6:
            break
        # Check for number indicator
        if braille_chunk == BrailleAlphabetAndSpecialChars['number'].value:
            numbers_braille = True
        # Check for capital letter indicator
        elif braille_chunk == BrailleAlphabetAndSpecialChars['capital'].value:
            caps_braille = True
        # Check for space character
        elif braille_chunk == BrailleAlphabetAndSpecialChars['space'].value:
            translated_english += mapEnumKeyToSpecialChar("space")
            if numbers_braille:
                numbers_braille = False

        # Handling regular alphabet characters
        elif not numbers_braille and not caps_braille and BrailleAlphabetAndSpecialChars(braille_chunk).name.isalpha():
            translated_english += BrailleAlphabetAndSpecialChars(braille_chunk).name

        # Handling special characters
        elif not numbers_braille and not caps_braille and mapEnumKeyToSpecialChar(BrailleAlphabetAndSpecialChars(braille_chunk).name):
            translated_english += mapEnumKeyToSpecialChar(BrailleAlphabetAndSpecialChars(braille_chunk).name)

        # Handling numbers
        elif numbers_braille:
            translated_english += BrailleNumbers(braille_chunk).name[1]
            numbers_braille = False

        # Handling capital letters
        elif caps_braille:
            translated_english += BrailleAlphabetAndSpecialChars(braille_chunk).name.upper()
            caps_braille = False

        else:
            translated_english += "$"

        i += 6

    return translated_english


if __name__ == '__main__':

    arguments = sys.argv[1:]
    input_language = " ".join(arguments)

    found_lang = detectInputLanguage(input_language)

    if found_lang == "English":
        translated_string = englishToBraille(input_language)
    else:
        translated_string = brailleToEnglish(input_language)

    print(translated_string)

