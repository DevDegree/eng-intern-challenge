import re
import sys
from enum import Enum

# Enum for alphabets and special characters in Braille
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

# Enum for numbers in Braille
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

# Convert English special characters to their corresponding enum key
def english_special_char_to_enum(char):
    if char == '.':
        return "period"
    elif char == ',':
        return "comma"
    elif char == '?':
        return "question"
    elif char == '!':
        return "exclaim"
    elif char == ':':
        return "colon"
    elif char == ';':
        return "sColon"
    elif char == '-':
        return "hyphen"
    elif char == '/':
        return "slash"
    elif char == '>':
        return "great"
    elif char == '<':
        return "less"
    elif char == '(':
        return "open"
    elif char == ')':
        return "close"
    else:
        return None

# Convert enum key of special characters back to the actual character
def enum_to_special_char(enum_key):
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

# Determine if the input is in Braille or English based on its pattern
def identify_input_language(input_text):
    braille_pattern = r'^[oO.]+$'
    # Check if the length is a multiple of 6, not just spaces, and matches Braille pattern
    if (len(input_text) % 6 == 0) and not input_text.isspace() and re.match(braille_pattern, input_text):
        return "Braille"
    else:
        return "English"

# Translate English text to Braille representation
def english_to_braille(english_text):
    braille_translation = ""
    index = 0
    while index < len(english_text):
        char = english_text[index]
        
        # Handle alphabetic characters
        if char.isalpha():
            # Prefix with capital indicator if the character is uppercase
            if char.isupper():
                braille_translation += BrailleAlphabetAndSpecialChars.capital.value
            # Add the Braille representation of the lowercase character
            braille_translation += BrailleAlphabetAndSpecialChars[char.lower()].value

        # Handle numeric characters
        elif char.isdigit():
            # If the previous character is not a digit, prefix with number indicator
            if index == 0 or not english_text[index - 1].isdigit():
                braille_translation += BrailleAlphabetAndSpecialChars.number.value
                braille_translation += BrailleNumbers["N" + char].value
            else:
                braille_translation += BrailleNumbers["N" + char].value

        # Handle spaces
        elif char.isspace():
            braille_translation += BrailleAlphabetAndSpecialChars.space.value

        # Handle special characters
        elif not char.isalnum():
            special_enum = english_special_char_to_enum(char)
            if special_enum:
                braille_translation += BrailleAlphabetAndSpecialChars[special_enum].value

        # Handle unrecognized characters
        else:
            braille_translation += "$$$$$$"

        index += 1

    return braille_translation

# Translate Braille representation back to English text
def braille_to_english(braille_text):
    english_translation = ""
    is_capital = False
    is_number = False

    index = 0
    while index < len(braille_text):
        # Extract a chunk of 6 characters representing one Braille cell
        braille_chunk = braille_text[index:index+6]

        if len(braille_chunk) < 6:
            break  # Incomplete Braille chunk

        # Check for number indicator
        if braille_chunk == BrailleAlphabetAndSpecialChars['number'].value:
            is_number = True

        # Check for capital indicator
        elif braille_chunk == BrailleAlphabetAndSpecialChars['capital'].value:
            is_capital = True

        # Check for space
        elif braille_chunk == BrailleAlphabetAndSpecialChars['space'].value:
            english_translation += enum_to_special_char("space")
            if is_number:
                is_number = False

        # Check if the chunk represents an alphabet character
        elif (not is_number and not is_capital and 
              BrailleAlphabetAndSpecialChars(braille_chunk).name.isalpha() and
              len(BrailleAlphabetAndSpecialChars(braille_chunk).name) == 1):
            english_char = BrailleAlphabetAndSpecialChars(braille_chunk).name
            if is_capital:
                english_char = english_char.upper()
                is_capital = False
            english_translation += english_char

        # Check if the chunk represents a special character
        elif (not is_number and not is_capital and
              enum_to_special_char(BrailleAlphabetAndSpecialChars(braille_chunk).name)):
            english_translation += enum_to_special_char(BrailleAlphabetAndSpecialChars(braille_chunk).name)

        # Check if the chunk represents a number
        elif is_number:
            english_translation += BrailleNumbers(braille_chunk).name[1]
        
        # Handle capital letters
        elif is_capital:
            english_char = BrailleAlphabetAndSpecialChars(braille_chunk).name.upper()
            english_translation += english_char
            is_capital = False

        # Handle unrecognized chunks
        else:
            english_translation += "$"

        index += 6

    return english_translation

if __name__ == '__main__':
    # Collect all command-line arguments as the input text
    arguments = sys.argv[1:]
    input_text = " ".join(arguments).strip()

    # Detect the language of the input (Braille or English)
    language = identify_input_language(input_text)

    # Perform translation based on the detected language
    if language == "English":
        output = english_to_braille(input_text)
    else:
        output = braille_to_english(input_text)

    # Output the translated text
    print(output)

