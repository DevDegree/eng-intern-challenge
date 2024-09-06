#!/usr/bin/env python3

import sys

ALPHA_TO_BRAILLE_DICT = {
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
}

NUMBER_TO_BRAILLE_DICT = {
    ".": "..OO.O",
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

SIGN_TO_BRAILLE_DICT = {
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
}

BRAILLE_TO_ALPHA_DICT = {braille: alpha for alpha, braille in ALPHA_TO_BRAILLE_DICT.items()}
BRAILLE_TO_NUMBER_DICT = {braille: number for number, braille in NUMBER_TO_BRAILLE_DICT.items()}
BRAILLE_TO_SIGN_DICT = {braille: sign for sign, braille in SIGN_TO_BRAILLE_DICT.items()}

CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"
BRAILLE_CHARS = {"O", "."}
SPACE = "......"
BRAILLE_CODE_LENGTH = 6

# determine if the given string should be translated to English or Braille
def is_braille(input):
    # check if the string contains only {"O", "."}
    # check if the string length is a multiple of 6
    if set(input) == BRAILLE_CHARS and len(input) % BRAILLE_CODE_LENGTH == 0:
        return True
    return False

def capital_follows(input):
    if input == CAPITAL_FOLLOWS:
        return True
    return False

def decimal_follows(input):
    if input == DECIMAL_FOLLOWS:
        return True
    return False

def number_follows(input):
    if input == NUMBER_FOLLOWS:
        return True
    return False

def translate_to_english(input):
    output = ""
    # divide the input string into a list of 6-character string for processing
    chars = [input[i:i+6] for i in range(0, len(input), BRAILLE_CODE_LENGTH)]
    is_capital, is_number = False, False
    
    for char in chars:
        if capital_follows(char):
            is_capital = True
        elif number_follows(char) or decimal_follows(char):
            is_number = True
        elif is_capital:
            output += BRAILLE_TO_ALPHA_DICT[char].upper()
            is_capital = False
        elif is_number:
            if char == SPACE:
                output += " "
                is_number = False
            else:
                output += BRAILLE_TO_NUMBER_DICT[char]
        elif char == SPACE:
            output += " "
        else:
            # since 'o' and '>' share the same braille cell pattern,
            # we translate to alphabet for such cases by default without a specific context
            if BRAILLE_TO_ALPHA_DICT.get(char) and BRAILLE_TO_SIGN_DICT.get(char):
                output += BRAILLE_TO_ALPHA_DICT[char]
            elif BRAILLE_TO_ALPHA_DICT.get(char):
                output += BRAILLE_TO_ALPHA_DICT[char]
            else:
                output += BRAILLE_TO_SIGN_DICT[char]
                
    return output
            
def main():
    # retrieve the input
    if len(sys.argv) >= 2:
        input = ' '.join(sys.argv[1:])
        if is_braille(input):
            print(translate_to_english(input))
    else:
        print("Please provide your input.")
        
if __name__ == '__main__':
    main()