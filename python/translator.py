"""
Braille Translator Script

This Python script translates text between English and Braille. The script supports the conversion of 
alphabetic characters, numbers, and spaces. It handles uppercase letters and numbers using special Braille 
format markers.

Functionality:
1. The script can translate an English string to Braille, accounting for uppercase letters and numbers.
2. It can also translate a Braille string back to English, recognizing format markers for uppercase 
   letters and numbers.
3. The translation assumes that once a Braille number format marker is encountered, all subsequent 
   characters are treated as numbers until a space is encountered.

Constraints:
- Only alphabetic characters (A-Z, a-z), digits (0-9), and spaces are supported for translation.
- Any other character in the input string will raise a ValueError, indicating that it cannot be 
  translated to Braille.
- When translating from Braille to English, unrecognized Braille patterns will be replaced with a 
  question mark ('?') in the output.
- The Braille representation assumes a 6-dot cell structure, where each Braille character is 
  represented by a combination of 'O' (raised dot) and '.' (flat dot) in a 3x2 matrix.

Usage:
- Run the script from the command line, providing the input string as an argument.
- Example:
  $ python3 translator.py "Hello 123"
  $ python3 translator.py ".....O.OO.OO.O..OO.O.OO..OOO.."

The script will detect whether the input is in English or Braille based on the character set and will 
automatically choose the appropriate translation function.
"""

import argparse

class BrailleConstants:
    """"
    Functionality: Stores constants and mappings for Braille translation.
    Attributes: Contains mappings between English characters, numbers, and Braille patterns.
    """
    BRAILLE_LENGTH = 6  # Length of each Braille character

    # Map for translating English letters, numbers, and spaces to Braille
    BRAILLE_DICT = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
        "z": "O..OOO",
        "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
        "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
        " ": "......"
    }

    # Special Braille characters for uppercase letters and numbers
    BRAILLE_FORMAT_MARK = {
        "uppercase": ".....O", "number": ".O.OOO"
    }

    REV_DICT = {v: k for k, v in BRAILLE_DICT.items()}
    REV_FORMAT_DICT = {v: k for k, v in BRAILLE_FORMAT_MARK.items()}

def translate_to_braille(text):
    """
    Functionality: Translates English text to Braille, handling special cases for uppercase letters and numbers.
    Input: A string in English.
    Output: A string representing the Braille translation.
    Exceptions: Raises ValueError for unsupported characters.
    """
    braille_output = []
    number_mode = False  # Flag to track if we're in "number mode"

    for char in text:
        if char.isalpha():
            # If we were in number mode, reset it for the new character
            if number_mode:
                number_mode = False

            if char.isupper():
                braille_output.append(BrailleConstants.BRAILLE_FORMAT_MARK["uppercase"])
            braille_output.append(BrailleConstants.BRAILLE_DICT[char.lower()])
        elif char.isdigit():
            # If this is the first number after a non-number, add the number format mark
            if not number_mode:
                braille_output.append(BrailleConstants.BRAILLE_FORMAT_MARK["number"])
                number_mode = True  # Now we are in number mode
            
            braille_output.append(BrailleConstants.BRAILLE_DICT[char])
        elif char == " ":
            # A space ends the number mode
            if number_mode:
                number_mode = False
            
            braille_output.append(BrailleConstants.BRAILLE_DICT[char])
        else:
            raise ValueError(f"Character '{char}' cannot be translated to Braille")

    return "".join(braille_output)



def translate_to_english(braille):
    """
    Functionality: Converts Braille text back to English, recognizing format markers.
    Input: A string in Braille.
    Output: A string representing the English translation.
    Exceptions: Raises ValueError for invalid Braille patterns.
    """
    # Initialize variables
    english_output = []
    i = 0
    length = len(braille)
    
    while i < length:
        # Check if the current segment is a format mark (uppercase or number)
        if braille[i:i + BrailleConstants.BRAILLE_LENGTH] == BrailleConstants.BRAILLE_FORMAT_MARK["uppercase"]:
            # The next character should be uppercase
            i += BrailleConstants.BRAILLE_LENGTH
            braille_char = braille[i:i + BrailleConstants.BRAILLE_LENGTH]
            english_output.append(BrailleConstants.REV_DICT[braille_char].upper())
        elif braille[i:i + BrailleConstants.BRAILLE_CELL_LENGTH] == BrailleConstants.BRAILLE_FORMAT_MARK["number"]:
            # The next characters are numbers until the next space or non-number symbol
            i += BrailleConstants.BRAILLE_LENGTH
            braille_char = braille[i:i + BrailleConstants.BRAILLE_LENGTH]
            while braille_char in BrailleConstants.REV_DICT and BrailleConstants.REV_DICT[braille_char].isdigit():
                english_output.append(BrailleConstants.REV_DICT[braille_char])
                i += BrailleConstants.BRAILLE_LENGTH
                if i >= length:
                    break
                braille_char = braille[i:i + BrailleConstants.BRAILLE_LENGTH]
            continue  # Skip further increment of i since it's handled within the loop
        else:
            # Normal letter or space
            braille_char = braille[i:i + BrailleConstants.BRAILLE_LENGTH]
            english_output.append(BrailleConstants.REV_DICT.get(braille_char, "?"))  # Use '?' for unknown patterns
        
        # Move to the next Braille character
        i += BrailleConstants.BRAILLE_LENGTH

    # Join the output list into a single string and return it
    return "".join(english_output)

def main():
    """
    Functionality: Handles command-line input and determines whether to translate from English to Braille or vice versa.
    Input: Command-line arguments (text to be translated).
    Output: Prints the translated text to the console.
    """
    parser = argparse.ArgumentParser(description="Braille Translator")
    parser.add_argument("input", type=str, nargs='+', help="Input string to translate")
    args = parser.parse_args()
    
    # Join the input arguments into a single string
    input_text = ' '.join(args.input)
    
    # Decide if input is Braille or English and call the appropriate function
    if set(input_text).issubset({'0', '.'}):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()


