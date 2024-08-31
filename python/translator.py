SPACE = "......"
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
# DEFAULT, CAPITAL, or NUMBER - indicates if we are translating lowercase letters, capital letters, or numbers
mode = "DEFAULT"

# map from lowercase English letters + space to Braille translation - used when in DEFAULT or CAPITAL mode
LETTER_TO_BRAILLE = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": SPACE
}
# inverse mapping of the above
BRAILLE_TO_LETTER = {v: k for k, v in LETTER_TO_BRAILLE.items()}

# map from numbers + space to Braille translation - used when in NUMBER mode
NUMBER_TO_BRAILLE = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    " ": SPACE
}
# inverse mapping of the above
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

'''
    determines if input_string is Braille
    assumes that Braille string is any input consisting only of O's and .'s with length divisible by 6
    Braille strings must also have at least 1 "." since no given Braille cells consist of only raised dots
'''
def is_braille(input_string):
    return all(char in "O." for char in input_string) and len(input_string) % 6 == 0 and "." in input_string

'''
translates a single Braille cell to English - including potentially changing the mode
returns the translated English character (empty string if mode-changing)
'''
def braille_to_english_single(cell):
    global mode

    # if capital or number follows, does not add any characters to output - just changes mode
    if cell == CAPITAL_FOLLOWS:
        mode = "CAPITAL"
        return ""
    if cell == NUMBER_FOLLOWS:
        mode = "NUMBER"
        return ""

    if mode == "CAPITAL":
        english = BRAILLE_TO_LETTER[cell].upper()
        mode = "DEFAULT" # capital follows only affects next cell
    elif mode == "NUMBER":
        english = BRAILLE_TO_NUMBER[cell]
        if cell == SPACE: # number follows takes effect until next space
            mode = "DEFAULT"
    else:
        english = BRAILLE_TO_LETTER[cell]
    return english

'''
translates a single English character to Braille cell - including potentially adding capital/number follows
'''
def english_to_braille_single(character):
    global mode

    if character == " ":
        mode = "DEFAULT" # number follows takes effect until next space
        return SPACE
    if character in NUMBER_TO_BRAILLE.keys():
        braille = ""
        if mode != "NUMBER": # do not need to add another number follows if one is already in effect
            mode = "NUMBER"
            braille += NUMBER_FOLLOWS
        braille += NUMBER_TO_BRAILLE[character]
    elif character in LETTER_TO_BRAILLE.keys(): # lowercase letter
        braille = LETTER_TO_BRAILLE[character]
    else: # uppercase letter
        braille = CAPITAL_FOLLOWS + LETTER_TO_BRAILLE[character.lower()]
    return braille

def braille_to_english(input_string):
    translations = []
    # each Braille cell consists of 6 consecutive characters in input
    cells = [input_string[i: i + 6] for i in range(0, len(input_string), 6)]
    for cell in cells:
        translations.append(braille_to_english_single(cell))
    return "".join(translations)

def english_to_braille(input_string):
    translations = []
    for character in input_string:
        translations.append(english_to_braille_single(character))
    return "".join(translations)

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    to_translate = " ".join(sys.argv[1:])
    if is_braille(to_translate):
        print(braille_to_english(to_translate))
    else:
        print(english_to_braille(to_translate))
