import re  # Access: regex parsing

# High-level idea:
# 
# Braille follows this set of rules:
# - Each "character" has length 6
# - Each "character" is composed solely from "O" or "."
# - There is a defined alphabet, BUT:
#       - Some special instructions, such as "capitalize" / "number" / "decimal" exist
# 
# 
# 
# Observations:
# Problem is broken up into two steps; classifying and translating.
# 
# To classify:
# - Can probably use regex to check if strings match the "O" or "." requirements
# - Can also assert that inputString.length() % 6 == 0 to match Braille length
# 
# ===================================================================================
# 
# To translate (FROM Braille):
# - Can tokenize each Braille character
# - Can check the edge cases (capitalize, number)
#       - Handle it
# - Can reference a dictionary to replace the characters
# 
# POTENTIAL EDGE CASE: The string "OOOOOO" passes the regex and length requirement,
#                      but would still be an English string, because that character isn't in the Braille ALPHABET.
#                      => if token not in Braille dict, translate the input string from English -> Braille
# 
# 
# * To translate (FROM ENGLISH):
# - For each char, check:
#       - is number or decimal
#       - is capital
# - Apply transformation rules
# - Replace with Braille alphabet entry
# 
# ===================================================================================



CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS  = ".O.OOO"

ALPHABET = {
    "j": ".OOO..",  # Value may also be 0
    "a": "O.....",  # Value may also be 1
    "b": "O.O...",  # Value may also be 2
    "c": "OO....",  # Value may also be 3
    "d": "OO.O..",  # Value may also be 4
    "e": "O..O..",  # Value may also be 5
    "f": "OOO...",  # Value may also be 6
    "g": "OOOO..",  # Value may also be 7
    "h": "O.OO..",  # Value may also be 8
    "i": ".OO...",  # Value may also be 9
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
    " ": "......"
}

def english_to_braille(str: str) -> str:
    out = ""
    return out
def braille_to_english(user_str: str) -> str:
    out = ""
    return out

if __name__ == "__main__":
    # user_str = input()
    # print(user_str)
    if(re.fullmatch('^(\\.|O)*$', user_str) and (len(user_str) % 6 == 0)):
        # print("Potentially Braille\n")
        print("$" + braille_to_english(user_str) + "$")

    else:
        # print("Not Braille\n")
        print(english_to_braille(user_str))
