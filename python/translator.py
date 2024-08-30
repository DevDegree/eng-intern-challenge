SPACE = "......"
# map from lowercase English letters + space to Braille translation
LETTER_TO_BRAILLE = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    # todo: finish this
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": SPACE
}
# inverse mapping of the above
BRAILLE_TO_LETTER = {v: k for k, v in LETTER_TO_BRAILLE.items()}

# map from numbers + space to Braille translation
NUMBER_TO_BRAILLE = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    # todo: finish this
    " ": SPACE
}
# inverse mapping of the above
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
# DEFAULT, CAPITAL, or NUMBER - indicates the translation mode, based on capital/number follows characters
mode = "DEFAULT"

# determines if input string is Braille
# assumes that any input consisting of only 0's and with at least 1 "." with length divisible by 6 is Braille - no Braille cells consist only of raised dots (O)
def is_braille(input_string):
    return all(char in "O." for char in input_string) and len(input_string) % 6 == 0 and "." in input_string

'''
translates a single Braille cell to English - including potentially changing the mode
returns the translated English character (empty string if mode-changing)
'''
def braille_to_english_single(cell):
    global mode  # todo: change this

    # if capital or number follows, does not add any characters to output - just changes mode
    if cell == CAPITAL_FOLLOWS:
        mode = "CAPITAL"
        return ""
    if cell == NUMBER_FOLLOWS:
        mode = "NUMBER"
        return ""

    if mode == "CAPITAL":
        english = BRAILLE_TO_LETTER[cell].capitalize()
        # capital follows only affects next cell
        mode = "DEFAULT"
    elif mode == "NUMBER":
        english = BRAILLE_TO_NUMBER[cell]
        if cell == SPACE:
            mode = "DEFAULT"  # number follows takes effect until next space
    else:
        english = BRAILLE_TO_LETTER[cell]
    return english

'''
translates a single English character to Braille cell - including potentially changing the mode
'''
def english_to_braille_single(character):
    global mode
    if character == " ":
        mode = "DEFAULT"
        return SPACE
    if character in NUMBER_TO_BRAILLE.keys():
        braille = ""
        if mode != "NUMBER":
            mode = "NUMBER"
            braille += NUMBER_FOLLOWS
        braille += NUMBER_TO_BRAILLE[character]
    elif character in LETTER_TO_BRAILLE.keys(): # checks for lowercase letter
        braille = LETTER_TO_BRAILLE[character]
    else: # uppercase letter
        braille = CAPITAL_FOLLOWS + LETTER_TO_BRAILLE[character.lower()]
    return braille

def braille_to_english(word):
    translations = []
    cells = [word[i: i + 6] for i in range(0, len(word), 6)]
    for cell in cells:
        translations.append(braille_to_english_single(cell))
    return ''.join(translations)

def english_to_braille(word):
    translations = []
    for character in word:
        translations.append(english_to_braille_single(character))
    return ''.join(translations)

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    word = " ".join(sys.argv[1:])
    #print(word)
    if is_braille(word):
        #print("word is Braille")
        print(braille_to_english(word))
    else:
        #print("word is English")
        print(english_to_braille(word))
    #print(braille_to_english(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"))
