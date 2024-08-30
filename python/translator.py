"""
Braille Translator Program

This Python script translates text between English and Braille, supporting both directions.
It uses a dictionary-based approach for mapping Braille symbols to English characters and vice versa.
Special cases such as capitalization, numeric symbols, and punctuation are also handled.

Author: Prithvi Seran
Date: August 30, 2024
"""

import sys

# Dictionary for mapping English letters, numbers, and punctuation to Braille representations and vice versa
ENGLISH_BRAILLE_TRANSLATIONS = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "capital follows": ".....O", "decimal follows": ".O...O",
    "number follows": ".O.OOO", ".": "..OO.O", ",": "..O...", "?": "..O.OO", 
    "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", "(": "O.O..O", ")": ".O.OO.", " ": "......",
    # Reverse mappings for Braille to English
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z", ".....O": "capital follows", ".O...O": "decimal follows",
    ".O.OOO": "number follows", "..OO.O": ".", "..O...": ",", "..O.OO": "?",
    "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", "......": " "
}

# Dictionary for mapping numbers to Braille representations and vice versa
NUMBER_BRAILLE_TRANSLATIONS = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    ".": "..OO.O", 
    # Reverse mappings for Braille to numbers
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "..OO.O": "."
}

def check_braille_or_english(input_words):
    """
    Determines whether the input is in Braille or English.
    
    Args:
        input_words (list): The list of input words (from command line arguments).
        
    Returns:
        list or None: Returns a list of Braille characters if input is Braille, otherwise returns None for English.
    """
    if len(input_words) > 2:  # More than two words suggest it's English
        return None
    
    input_text = input_words[1]
    
    if len(input_text) % 6 != 0:  # Non-divisible by 6 means it's English
        return None
    
    sorted_words = [input_text[i:i+6] for i in range(0, len(input_text), 6)]
    
    for element in sorted_words:
        if element not in ENGLISH_BRAILLE_TRANSLATIONS:
            return None
    
    return sorted_words

def translate_english_to_braille(input_words):
    """
    Translates English text to Braille.

    Args:
        input_words (list): The list of English words to translate.

    Returns:
        str: The Braille translation as a string.
    """
    braille = ""
    is_numeric = False
    
    for word in input_words:
        is_numeric = False
        for letter in word:
            if letter.isupper():
                braille += ENGLISH_BRAILLE_TRANSLATIONS["capital follows"]

            elif letter.isnumeric() and not is_numeric:
                is_numeric = True
                braille += ENGLISH_BRAILLE_TRANSLATIONS["number follows"]

            if is_numeric:
                if letter == ".":
                    braille += ENGLISH_BRAILLE_TRANSLATIONS["decimal follows"]
                    braille += ENGLISH_BRAILLE_TRANSLATIONS["."]

                elif letter == " ":
                    braille += ENGLISH_BRAILLE_TRANSLATIONS[" "]
                    is_numeric = False

                else:
                    braille += NUMBER_BRAILLE_TRANSLATIONS[letter]
            else:
                braille += ENGLISH_BRAILLE_TRANSLATIONS[letter.lower()]
        
        braille += ENGLISH_BRAILLE_TRANSLATIONS[" "]  # Add space between words

    return braille[:-6]  # Remove the trailing space Braille

def translate_braille_to_english(resulting_elements):
    """
    Translates Braille to English text.

    Args:
        resulting_elements (list): The list of Braille characters to translate.

    Returns:
        str: The English translation as a string.
    """
    english = ""
    is_numeric = False
    is_capital = False
    
    for i in range(len(resulting_elements)):
        if ENGLISH_BRAILLE_TRANSLATIONS[resulting_elements[i]] == "capital follows":
            is_capital = True

        elif ENGLISH_BRAILLE_TRANSLATIONS[resulting_elements[i]] == "number follows":
            is_numeric = True

        elif ENGLISH_BRAILLE_TRANSLATIONS[resulting_elements[i]] == " ":
            english += " "
            is_numeric = False

        elif ENGLISH_BRAILLE_TRANSLATIONS[resulting_elements[i]] == "decimal follows":
            continue  # Skip decimal follow marker

        else:
            if is_capital:
                english += ENGLISH_BRAILLE_TRANSLATIONS[resulting_elements[i]].upper()
                is_capital = False
            elif is_numeric:
                english += NUMBER_BRAILLE_TRANSLATIONS[resulting_elements[i]]
            else:
                english += ENGLISH_BRAILLE_TRANSLATIONS[resulting_elements[i]]

    return english

def main():
    """
    Main function to process input, check if it's Braille or English, 
    and translate accordingly.
    """
    input_words = sys.argv 

    resulting_elements = check_braille_or_english(input_words)

    if resulting_elements is None:
        output = translate_english_to_braille(input_words[1:])
    else:
        output = translate_braille_to_english(resulting_elements)

    print(output)

if __name__ == "__main__":
    main()

