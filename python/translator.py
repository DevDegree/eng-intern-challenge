import sys 

ENG_TO_BRAILLE = { #maps English characters to Braille
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}
BRAILLE_TO_ENG_LET = {} #maps Braille characters to English numbers
BRAILLE_TO_ENG_NUM = {} #maps Braille characters to English lowercase letters; includes space character

for key, value in ENG_TO_BRAILLE.items(): #Fills Braille-to-English dictionaries
    if key.isalpha() or key == " ":
        BRAILLE_TO_ENG_LET[value] = key
    else:
        BRAILLE_TO_ENG_NUM[value] = key

def is_braille(text):
    """Returns True if the input text is braille, False otherwise"""
    for char in text:
        if char != "O" and char != ".":
            return False
    return True

def convert_e_to_b(text):
    """Converts input text in English to its corresponding Braille text 
    and returns the Braille"""
    braille = "" #Braille output
    wasnum = False #True when the current char is a number and the previous char wasn't, i.e. the char is the first number
    for char in text:
        if char.isupper():
            braille = braille + ".....O"
            braille_char = ENG_TO_BRAILLE[char.lower()]
        else:
            if char.isnumeric() and not wasnum:
                braille = braille + ".O.OOO"
                wasnum = True
            if char == " ":
                wasnum = False
            braille_char = ENG_TO_BRAILLE[char]
        braille = braille + braille_char
    return braille

def b_lookup (b_char, is_cap, is_num):
    """Returns the correct English translation of the inputted braille character b_char
    according to whether it is capitalised, numeric, or neither."""
    if is_num:
        return BRAILLE_TO_ENG_NUM[b_char]
   
    e_char = BRAILLE_TO_ENG_LET[b_char]
    if is_cap:
        return e_char.upper()
    return e_char

def convert_b_to_e(text):
    """Converts input text in Braille to its corresponding English text
    and returns the English text"""
    english = "" #English output
    is_cap = False #True if the next character is capitalised
    is_num = False #True if the next character is a number
    for i in range(0, len(text), 6):
        b_char = text[i:i+6] #current Braille character
        if b_char == ".....O":
            is_cap = True
        elif b_char == ".O.OOO":
            is_num = True
        else:
            if b_char == "......":
                is_num = False
            e_char = b_lookup(b_char, is_cap, is_num) #correct English char
            english = english + e_char
            is_cap = False
    return english

def main():
    """Reads console input and returns its translation"""
    text = " ".join(sys.argv[1:])
    if is_braille(text):
        return convert_b_to_e(text)
    return convert_e_to_b(text) 

sys.stdout.write(main())
