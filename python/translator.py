import re
import sys
from typing import Optional

# Maps for converting braille patterns to their corresponding English letters or digits
BRAILLE_TO_TEXT = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
}

BRAILLE_TO_DIGITS = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Special braille patterns for modifiers and spaces
SPACE = "......"
CAPITAL_PREFIX = ".....O"
NUMBER_PREFIX = ".O.OOO"

# Reverse lookup tables for converting text back to braille patterns
TEXT_TO_BRAILLE = {char: pattern for pattern, char in BRAILLE_TO_TEXT.items()}
TEXT_TO_BRAILLE[" "] = SPACE
DIGITS_TO_BRAILLE = {digit: pattern for pattern, digit in BRAILLE_TO_DIGITS.items()}

# Determines if a given string is formatted in braille
def is_braille_input(s: str) -> Optional[re.Match]:
    return re.fullmatch(r"^[O.]*$", s)

# Translates a braille string into its English representation
def braille_to_english(braille: str) -> str:
    english = ""
    capital_flag = False
    number_flag = False
    for i in range(0, len(braille), 6):
        cell = braille[i:i+6]
        if cell == CAPITAL_PREFIX:
            capital_flag = True
        elif cell == NUMBER_PREFIX:
            number_flag = True
        elif cell == SPACE:
            english += " "
            capital_flag = number_flag = False
        else:
            if number_flag:
                english += BRAILLE_TO_DIGITS.get(cell, "")
            else:
                letter = BRAILLE_TO_TEXT.get(cell, "")
                english += letter.capitalize() if capital_flag else letter
                capital_flag = False
    return english

# Converts an English text string into its equivalent braille representation
def english_to_braille(english: str) -> str:
    braille = ""
    in_number_mode = False
    for char in english:
        if char.isupper():
            braille += CAPITAL_PREFIX + TEXT_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            if not in_number_mode:
                braille += NUMBER_PREFIX
                in_number_mode = True
            braille += DIGITS_TO_BRAILLE[char]
        else:
            in_number_mode = False
            braille += TEXT_TO_BRAILLE[char]
    return braille

# Main translation function that decides based on input type
def translate_input(text: str) -> str:
    return braille_to_english(text) if is_braille_input(text) else english_to_braille(text)

if __name__ == "__main__":
    input_texts = sys.argv[1:]
    # Select the appropriate separator for the output
    separator = " " if input_texts and is_braille_input(input_texts[0]) else SPACE
    # Print the translated results joined by the determined separator
    print(separator.join(map(translate_input, input_texts)))
