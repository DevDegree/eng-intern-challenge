# Shopify Coding Challenge - A Braille translator 
# It converts English text to Braille and vice versa.

# Imports
import sys

# Mapping of English alphabet and numbers to Braille
ENG_TO_BRAILLE_DICT = {
    "a": "O.....", "b": "O.O...",
    "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO",
    "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO"
}

NUMBER_TO_BRAILLE_DICT = {
    "0": ".OOO..", "1": "O.....",
    "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO..."
}

# Number Follows
NUMBER = ".O.OOO"

# Space Follows
SPACE = "......"

# Capitalization Follows
CAPITAL = ".....O"

# Now, we reverse the above dictionaries for vice-versas conversions
BRAILLE_TO_ENG_DICT = {value: key for key,
                       value in ENG_TO_BRAILLE_DICT.items()}

BRAILLE_TO_NUMBER_DICT = {value: key for key,
                          value in NUMBER_TO_BRAILLE_DICT.items()}

# Input Validation to check for English/Braille
def is_braille(text):
    return all(char in "O." for char in text)

# Function for Braille to English text conversion
def braille_to_english(input):
    is_capital = False
    is_number = False
    
    #final output
    output = []
    
    # Get braille characters as each is of length 6
    braille_alph = [input[i:i+6] for i in range(0, len(input), 6)]

    for char in braille_alph:
        if char == CAPITAL:  # set capital to true, and number to false, and vice versa for number case
            is_capital = True
            is_number = False 
        elif char == NUMBER:
            is_number = True
            is_capital = False
        elif char == SPACE:
            output.append(" ")
            is_number = False # set number to false when we encounter space
        elif is_number:
            if char in BRAILLE_TO_NUMBER_DICT: # Validation
                output.append(BRAILLE_TO_NUMBER_DICT[char])
            else:
                raise KeyError(f"Unrecognized Braille pattern: {char}")
        elif is_capital:
            output.append(BRAILLE_TO_ENG_DICT[char].upper())
            is_capital = False  # Capital only applies to one next letter
        else:
            output.append(BRAILLE_TO_ENG_DICT[char])

    return "".join(output)

# Function for English text to Braille conversion 
def english_to_braille(input):
    is_number = False
    
    output = []

    for char in input:
        if char.isupper():
            output.append(CAPITAL)  # Append a capital symbol for braille
            output.append(ENG_TO_BRAILLE_DICT[char.lower()]) 
            is_number = False
        elif char.isdigit():
            if not is_number:
                output.append(NUMBER)  # Append a number symbol for braille
                is_number = True  # Continue in number flag, until space is found
            output.append(NUMBER_TO_BRAILLE_DICT[char])
        elif char == " ":
            output.append(SPACE)  # Append a space symbol
            is_number = False 
        else:
            output.append(ENG_TO_BRAILLE_DICT[char])
            is_number = False  # Reset number flag

    return "".join(output)

# Main function
if __name__ == "__main__":

    input = " ".join(sys.argv[1:])

    if is_braille(input):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))