import logging
import argparse
from enum import Enum
from collections import Counter

# Enums
class SpecialChar(Enum):
    CAPITAL = "CAPITAL"
    NUMBER = "NUMBER"
    SPACE = " "

# Constants
english_to_braille_dict = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",
    
    SpecialChar.CAPITAL.value: ".....O", SpecialChar.NUMBER.value: ".O.OOO",
    SpecialChar.SPACE.value: "......"
}

english_numbers_braille_dict = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}

braille_to_english_dict = {value : key for key, value in english_to_braille_dict.items()}
braille_to_english_numbers = {value : key for key, value in english_numbers_braille_dict.items()}
validBrailleChar = {'.', 'O'}

def isInputStringContainValidChar(string, language_chars):
    for letter in string:
        if not(letter.isdigit() or letter.lower() in language_chars):
            print(f"invalid english letter {letter}")
            return False
    
    return True

def isInputStringBaraille(string):
    if not (len(string) % 6 == 0):
        return False

    letters = Counter(string)
    
    if len(letters) > 2:
        return False

    for letter, count in letters.items():
        if letter not in validBrailleChar:
            return False
    
    return True
    

def parse_braille_string_to_language(braille_text, braille_to_language, braille_to_numbers):
    pass


def parse_language_to_braille(text, language_to_braille, number_to_braille):
    pass
    
        
    

def main():
    parser = argparse.ArgumentParser(
        prog="Braille Translator",
        description="CLI tool that will translate english to braille and vice versa",
        epilog="Thanks for using my tool. Made with love for the Shopify Eng Intern Challenge. :)"
    )
    
    parser.add_argument('input_text_to_translate', nargs='+', help="String that we want translated. Input string can be either Braille/English and the program will translate it automatically.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")
    
    arguments = parser.parse_args()
    
    # should be defined with a valid string
    if not arguments.input_text_to_translate:
        return
    
    text = ' '.join(arguments.input_text_to_translate).strip()
    translated_text = ""
    if isInputStringBaraille(text):
        translated_text = parse_braille_string_to_language(text, braille_to_english_dict, braille_to_english_numbers)
    elif isInputStringContainValidChar(text, english_to_braille_dict):
        translated_text = parse_language_to_braille(text, english_to_braille_dict, english_numbers_braille_dict)
    else:
        # Throw error
        print("Error: Unable to currently translate text")
    
    
    print(f"{translated_text}")
    

if __name__ == "__main__":
    main()
