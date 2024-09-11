# Assumption:
# No invalid inputs are given to the program; based on the assumptions in technical requirements

import sys
import re

# CONSTANTS FOR ENGLISH -> BRAILLE and BRAILLE -> ENGLISH
BRAILLE_TO_LETTER_MAP = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
  'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
  'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
  'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
  'O..OOO': 'z'
}
BRAILLE_TO_NUMBER_MAP = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
  'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
BRAILLE_NUMBER_FOLLOWS = '.O.OOO'
BRAILLE_CAPITAL_FOLLOWS = '.....O'
BRAILLE_SPACE_FOLLOW = '......'
LETTER_TO_BRAILLE_MAP = {v: k for k, v in BRAILLE_TO_LETTER_MAP.items()}
NUMBER_TO_BRAILLE_MAP = {v: k for k, v in BRAILLE_TO_NUMBER_MAP.items()}

# Regular Expression to check if input is braille or english
PATTERN = r'^[.O]+$'

# Converts Braille input to English text
def braille_to_english(braille: str) -> str:
    english_text = []
    counter = 0
    isCapital = False
    isNumber = False
    while counter < len(braille):
        curr_braille = braille[counter:counter + 6]
        if curr_braille == BRAILLE_CAPITAL_FOLLOWS:
            isCapital = True
            counter += 6
        elif curr_braille == BRAILLE_NUMBER_FOLLOWS:
            isNumber = True
            counter += 6
        elif curr_braille == BRAILLE_SPACE_FOLLOW:
            isNumber = False
            english_text.append(" ")
            counter += 6
        else:
            if isCapital == True:
                isCapital = False
                english_text.append(BRAILLE_TO_LETTER_MAP[curr_braille].upper())
            elif isNumber == True:
                english_text.append(BRAILLE_TO_NUMBER_MAP[curr_braille])
            else:
                english_text.append(BRAILLE_TO_LETTER_MAP[curr_braille])
            
            counter += 6
    
    return ''.join(english_text)

# Converts English input to Braille text
def english_to_braille(english: str) -> str:
    braille_text = []
    isNumber = False

    for c in english:
        if c.isalpha():
            if c.isupper():
                braille_text.append(BRAILLE_CAPITAL_FOLLOWS)
                braille_text.append(LETTER_TO_BRAILLE_MAP[c.lower()])
            else:
                braille_text.append(LETTER_TO_BRAILLE_MAP[c])
        elif c.isdigit():
            if isNumber:
                braille_text.append(NUMBER_TO_BRAILLE_MAP[c])
            else:
                isNumber = True
                braille_text.append(BRAILLE_NUMBER_FOLLOWS)
                braille_text.append(NUMBER_TO_BRAILLE_MAP[c])
        elif c == ' ':
            isNumber = False
            braille_text.append(BRAILLE_SPACE_FOLLOW)

    return ''.join(braille_text)


# determines whether braille or english input was given by the user
def check_input_type(input: str) -> str:
    if re.match(PATTERN, input):
        return "braille"
    else:
        return "english"

# Parses English/Braille text from the command line
def get_input() -> str:
    if len(sys.argv) < 2:
        raise ValueError("Text not provided")
    return " ".join(sys.argv[1:])

if __name__ == "__main__":
    input = get_input()
    input_type = check_input_type(input)
    result = braille_to_english(input) if input_type == "braille" else english_to_braille(input)
    print(result)
    

