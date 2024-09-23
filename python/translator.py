#
# Shopify Winter 2025 Developer Intern Challenge
# By: Carlos Andres Montoro (gh: shadow-maker)
#

import sys

LETTERS = "abcdefghijklmnopqrstuvwxyz"
BRAILLE = [
    "O.....",  # A
    "O.O...",  # B
    "OO....",  # C
    "OO.O..",  # D
    "O..O..",  # E
    "OOO...",  # F
    "OOOO..",  # G
    "O.OO..",  # H
    ".OO...",  # I
    ".OOO..",  # J
    "O...O.",  # K
    "O.O.O.",  # L
    "OO..O.",  # M
    "OO.OO.",  # N
    "O..OO.",  # O
    "OOO.O.",  # P
    "OOOOO.",  # Q
    "O.OOO.",  # R
    ".OO.O.",  # S
    ".OOOO.",  # T
    "O...OO",  # U
    "O.O.OO",  # V
    ".OOO.O",  # W
    "OO..OO",  # X
    "OO.OOO",  # Y
    "O..OOO"   # Z
]
BRAILLE_CAP = ".....O"
BRAILLE_NUM = ".O.OOO"
BRAILLE_SPC = "......"

# Check if text is Braille
def is_braille(text: str) -> bool:
    return "." in text # Since the program doesn't support symbols, having any "." in the input means it's Braille

# Convert English to Braille
def to_braille(text: str) -> str:
    output = ""
    number = False

    for char in text:
        if char == " ":
            output += BRAILLE_SPC
            number = False
        elif char.isdigit():
            if not number:
                output += BRAILLE_NUM
            output += BRAILLE[(int(char) - 1) % 10] # i: 1->0, 2->1, ..., 0->9
            number = True
        else:
            if number:
                output += BRAILLE_SPC
            number = False
            if char in LETTERS:
                output += BRAILLE[LETTERS.index(char)]
            elif char.lower() in LETTERS:
                output += BRAILLE_CAP + BRAILLE[LETTERS.index(char.lower())]

    return output

# Convert Braille to English
def to_english(text: str) -> str:
    output = ""
    number = False
    next_cap = False

    for i in range(0, len(text), 6):
        char = text[i:i+6]
        if char == BRAILLE_NUM:
            number = True
        elif char == BRAILLE_SPC:
            output += " "
            number = False
        elif char == BRAILLE_CAP:
            next_cap = True
        elif char in BRAILLE:
            if number:
                output += str((BRAILLE.index(char) + 1) % 10) # i: 0->1, 1->2, ..., 9->0
            else:
                letter = LETTERS[BRAILLE.index(char)]
                if next_cap:    
                    output += letter.upper()
                    next_cap = False
                else:
                    output += letter

    return output

# Translate text to/from Braille
def translate(text: str) -> str:
    if is_braille(text):
        return to_english(text)
    else:
        return to_braille(text)
    
# Command line interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)
    print(translate(" ".join(sys.argv[1:])))
