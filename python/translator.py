#!/usr/bin/env python3
import sys

# Braille to English dictionary
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"}
braille_to_numbers ={"O.....": "1", "O.O...": "2", "OO....": "3", "OOO...": "4", "O..O..": "5",
    "OOOO..": "6", "OOOOO.": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",}
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO"
}
numbers_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OOO...", "5": "O..O..",
    "6": "OOOO..", "7": "OOOOO.", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def braille_to_english_func(braille_string):
    result = ""
    i = 0
    capitalize_next = False
    in_number_mode = False
    while i < len(braille_string):
        symbol = braille_string[i:i+6]
        if symbol == ".....O":  # Capitalization marker
            capitalize_next = True
        elif symbol == ".O.OOO":  # Number mode indicator
            in_number_mode = True
        elif symbol == "......":  # Space
            result += " "
            in_number_mode = False  # Exit number mode after a space
        elif in_number_mode and symbol in braille_to_numbers:
            # If in number mode, interpret as a number
            result += braille_to_numbers[symbol]
        elif symbol in braille_to_english:
            # If not in number mode, interpret as a regular character
            char = braille_to_english[symbol]
            result += char.upper() if capitalize_next else char
            capitalize_next = False
            in_number_mode = False  # Exit number mode if a letter is encountered
        
        i += 6
    
    return result

def english_to_braille_func(english_string):
    result = ""
    in_number_mode = False
    
    for char in english_string:
        if char.isupper():
            result += ".....O" + english_to_braille[char.lower()] #Add the capitalization marker before the letter
            in_number_mode = False  # Reset number mode after a capital letter
        elif char.isdigit():
            if in_number_mode == False:
                result += ".O.OOO"  # Add the number indicator only once
                in_number_mode = True
            result += numbers_to_braille[char]
        elif char in english_to_braille:
            result += english_to_braille[char]
            in_number_mode = False  # Reset number mode after a regular character
        elif char == " ":
            result += "......"
            in_number_mode = False  # Reset number mode after a space
    
    return result

def translate(input_string):
    # Determine if input is Braille or English
    if all(char in ['O', '.'] for char in input_string):
        # Braille to English
        return braille_to_english_func(input_string)
    else:
        # English to Braille
        return english_to_braille_func(input_string)

# Command-line execution
if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:]).strip()
    translated_text = translate(input_text)
    print(translated_text)
