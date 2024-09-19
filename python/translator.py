import re
import sys

# notes:
# O is where the dot is
# . is where there is no dot
# read left-to-right from top left
# capital follows = .....O
# number follows = .O.OOO

def translator(input) -> str:
    is_braille = "^(?:[O.]{6})+$"
    is_english = "[a-z]"
    is_capitalized = "[A-Z]"
    is_number = "[0-9]"

    if re.search(is_braille, input):
        # translate from values to keys in dictionary.json
        return braille_to_english(input)
    elif re.search(is_english, input):
        # translate from keys to values in dictionary.json
        return english_to_braille(input)

def braille_to_english(input) -> str:
    return "BRAILLE TO ENGLISH"

def english_to_braille(input) -> str:
    return "ENGLISH TO BRAILLE"


if __name__ == "__main__":
    print(translator(sys.argv[1]))