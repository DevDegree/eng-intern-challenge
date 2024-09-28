
"""
Author: Ray Wang
Date: 09/27/2024
Purpose: Command line English/Braille Translator for the Shopify Eng Intern Challenge
"""

import sys

#Below dictionary contains mappings for english to braille and braille to english.
#Mappings for the digits 1-9 correspond with the mappings of the letters a-i, with 0 corresponding with j

ENG_BRAILLE_DICT = {
    #English to Braille
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",

    "capital_follows": ".....O", "decimal_follows": ".O...O", "number_follows": ".O.OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",  ";": "..O.O.",
    "-": "....OO", "/": ".O..O.", "<": ".OO..O", "(": "O.O..O",  ")": ".O.OO.", " ": "......",
    #__________________________________________________________________________
    #Braille to English
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",

    ".....O": "capital_follows", ".O...O": "decimal_follows", ".O.OOO": "number_follows",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";",
    "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", "......": " "
}

#number to add to ascii value of any digit (besides 0) to convert it to its corresponding letter
#with the same braille translation
NUMBER_TO_ALPHA_CONST = 48

#character length of a single braille symbol
BRAILLE_SYMBOL_LENGTH = 6


"""
Converts a string of english text into a string of braille symbols
    params: text (string), assumed to be valid english text containing only characters defined in
            the braille alphabet, otherwise defaulted to a space if not found
    returns: a string with text translated into braille symbols
"""
def translate_eng_to_braille(text):
    translated_text = []
    number_mode_flag = False
    for i, char in enumerate(text):
        if char.isupper():
            translated_text.append(ENG_BRAILLE_DICT["capital_follows"])
            translated_text.append(ENG_BRAILLE_DICT[char.lower()])

        elif char == " " and number_mode_flag:
            number_mode_flag = False
            translated_text.append(ENG_BRAILLE_DICT[char])

        elif char == ".":
            #check if the period is actually a decimal point in a number
            if i < len(text)-1 and text[i+1].isnumeric():
                translated_text.append(ENG_BRAILLE_DICT["decimal_follows"])
                translated_text.append(ENG_BRAILLE_DICT["."])

            else:
                translated_text.append(ENG_BRAILLE_DICT["."])

        elif char.isnumeric():
            if not number_mode_flag:
                translated_text.append(ENG_BRAILLE_DICT["number_follows"])
                number_mode_flag = True

            if char == '0':
                #convert the digit into the corresponding letter with the same braille translation
                translated_text.append(ENG_BRAILLE_DICT["j"])

            else:
                #convert the digit into the corresponding letter with the same braille translation
                translated_text.append(ENG_BRAILLE_DICT[chr((ord(char)+NUMBER_TO_ALPHA_CONST))])

        else:
            #default to space symbol if text not found in braille alphabet
            translated_text.append(ENG_BRAILLE_DICT.get(char, "......"))

    return ''.join(translated_text)


"""
Converts a string of braille text into a string of english text
    params: text (string), assumed to be valid braille text containing only symbols defined in
            the braille alphabet, otherwise defaulted to a space if not found
    returns: a string with text translated into english
"""
def translate_braille_to_eng(text):
    translated_text = []

    #split the braille text into symbols
    split_text = [text[i:i + BRAILLE_SYMBOL_LENGTH] for i in range(0, len(text), BRAILLE_SYMBOL_LENGTH)]

    number_mode_flag = False
    capital_mode_flag = False

    for symbol in split_text:
        #get translated symbol, default to space if otherwise not found
        translated_symbol = ENG_BRAILLE_DICT.get(symbol, " ")
        if translated_symbol == "capital_follows":
            capital_mode_flag = True

        elif translated_symbol == "number_follows":
            number_mode_flag = True

        elif translated_symbol == "decimal_follows":
            continue

        elif number_mode_flag and translated_symbol == " ":
            translated_text.append(" ")
            number_mode_flag = False

        elif number_mode_flag and 'a' <= translated_symbol <= 'j':
            if translated_symbol == 'j':
                # convert the letter into the corresponding digit with the same braille translation
                translated_text.append("0")

            else:
                # convert the letter into the corresponding digit with the same braille translation
                translated_text.append(chr((ord(translated_symbol) - NUMBER_TO_ALPHA_CONST)))

        elif capital_mode_flag:
            translated_text.append(translated_symbol.upper())
            capital_mode_flag = False

        else:
            translated_text.append(translated_symbol)

    return ''.join(translated_text)

"""
Checks if a given string of text is in braille or english
    params: text (string), can have any characters
    returns: a bool denoting whether the text is a braille representation or english
"""
def is_braille_text(text):

    #check if the provided text can be split into chunks of braille symbols
    #and if the symbols only consist of "." or "O"
    if len(text) % BRAILLE_SYMBOL_LENGTH == 0:
        unique_chars = set(text)
        if len(unique_chars) == 2 and "." in unique_chars and "O" in unique_chars:
            return True
        else:
            return False
    else:
        return False

"""
Main entry point of the program
"""
def main():
    input_text = " ".join(sys.argv[1:])
    if is_braille_text(input_text):
        print(translate_braille_to_eng(input_text))
    else:
        print(translate_eng_to_braille(input_text))

if __name__ == "__main__":
    main()

