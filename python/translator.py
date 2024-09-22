
"""
Author: Nolawi Teklehaimanot
Date: 09/22/2024
"""

import sys

ENG_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "capital": ".....O", "decimal": ".O...O", "number": ".O.OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", 
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", "(": "O.O..O", 
    ")": ".O.OO.", " ": "......",
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z", ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(",
    ".O.OO.": ")", "......": " "
}

NUM_TO_BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    ".": "..OO.O", 
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "..OO.O": "."
}

"""
Split the input text into chunks of six characters, each representing a single Braille character.

Parameters: text (str): The string of Braille characters to be split.

Returns: list of str: A list where each element is a six-character string representing a Braille character.
"""
def split_braille_chars(text):
    return [text[i:i+6] for i in range(0, len(text), 6)]

"""
Determine whether the input provided is in Braille or English by analyzing its structure and characters.

Parameters: words (list of str): The list of command-line arguments passed to the script.

Returns: list of str or None: Returns a list of Braille character chunks if the input is valid Braille;
                            otherwise, returns None indicating the input is likely English text.
"""
def detect_input_type(words):
    if len(words) > 2:
        return None

    text = words[1]
    if len(text) % 6 != 0:
        return None

    braille_chars = split_braille_chars(text)
    
    if all(char in ENG_TO_BRAILLE for char in braille_chars):
        return braille_chars

    return None

"""
Convert a list of English words into their corresponding Braille representation.

Parameters: words (list of str): The list of English words to be converted to Braille.

Returns: str: A single string representing the concatenated Braille translation of the input English text.
"""
def english_to_braille(words):
    braille_text = []
    for word in words:
        numeric_mode = False
        for char in word:
            if char.isupper():
                braille_text.append(ENG_TO_BRAILLE["capital"])
            
            if char.isdigit() and not numeric_mode:
                numeric_mode = True
                braille_text.append(ENG_TO_BRAILLE["number"])

            if numeric_mode:
                if char == ".":
                    braille_text.extend([ENG_TO_BRAILLE["decimal"], ENG_TO_BRAILLE["."]])
                elif char == " ":
                    braille_text.append(ENG_TO_BRAILLE[" "])
                    numeric_mode = False
                else:
                    braille_text.append(NUM_TO_BRAILLE.get(char, "......"))  # Default to space if unknown
            else:
                braille_text.append(ENG_TO_BRAILLE.get(char.lower(), "......"))  # Default to space if unknown
        
        braille_text.append(ENG_TO_BRAILLE[" "])  # Add space between words
    
    return ''.join(braille_text[:-1])  # Remove the last space

"""
Convert a list of Braille character strings into their corresponding English text.

Parameters: braille_chars (list of str): The list of six-character Braille strings to be converted.

Returns: str: A single string representing the translated English text from the Braille input.
"""
def braille_to_english(braille_chars):
    english_text = []
    numeric_mode = False
    capital_mode = False
    
    for char in braille_chars:
        symbol = ENG_TO_BRAILLE.get(char, " ")  # Default to space if unknown
        
        if symbol == "capital":
            capital_mode = True
        elif symbol == "number":
            numeric_mode = True
        elif symbol == " ":
            english_text.append(" ")
            numeric_mode = False
        elif symbol == "decimal":
            continue  # Skip the decimal marker
        else:
            if capital_mode:
                english_text.append(symbol.upper())
                capital_mode = False
            elif numeric_mode:
                english_text.append(NUM_TO_BRAILLE.get(char, ''))  # Append numeric character
            else:
                english_text.append(symbol)
    
    return ''.join(english_text)

"""
The main function that serves as the entry point of the program.
"""
def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python script.py <text>")
        sys.exit(1)

    braille_chars = detect_input_type(args)
    
    if braille_chars:
        print(braille_to_english(braille_chars))
    else:
        print(english_to_braille(args[1:]))

if __name__ == "__main__":
    main()
