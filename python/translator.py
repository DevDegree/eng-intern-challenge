# Dictionary mappings for Braille to English letters
B_TO_E = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z"
}

# Dictionary mappings for Braille to numbers
B_TO_N = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

E_TO_B = {val: key for key,val in B_TO_E.items()}
N_TO_B = {val: key for key,val in B_TO_N.items()}

CAPITAL_FOLLOW = ".....O"  # Indicates the next character is capitalized
NUMBER_FOLLOW = ".O.OOO"  # Indicates the start of a number sequence
SPACE = "......"  # Represents a space

def check_braille(input: str) -> bool:
    """Check if the input string contains only valid Braille characters (. and O)"""
    return set(input).issubset({".", "O"})

def english_TO_braille(input: str) -> str:
    """Convert English text to Braille"""
    output = ""
    number_flag = False
    for char in input:
        if char == " ":
            output += SPACE
            number_flag = False
        elif char.isdigit():
            if not number_flag:
                output += NUMBER_FOLLOW
                number_flag = True
            output += N_TO_B[char]
        else:
            lowered = char.lower()
            if char != lowered:
                output += CAPITAL_FOLLOW
            output += E_TO_B[lowered]
            number_flag = False
    return output

def braille_TO_english(input: str) -> str:
    """Convert Braille to English text"""
    output = ""
    import re
    braille = re.findall('.'*6, input) # Split input into chunks of 6 characters
    number_flag = False
    capital_flag = False
    for chunk in braille:
        if chunk == SPACE:
            output += ' '
            number_flag = capital_flag = False
        elif chunk == NUMBER_FOLLOW:
            number_flag = True
        elif chunk == CAPITAL_FOLLOW:
            capital_flag = True
        elif number_flag:
            output += B_TO_N[chunk]
        else:
            letter = B_TO_E[chunk]
            if capital_flag:
                letter = letter.upper()
                capital_flag = False
            output += letter
    return output

def translate() -> None:
    """Main function to handle translation based on command-line input"""
    import sys
    input = " ".join(sys.argv[1:]).strip()
    if check_braille(input):
        print(braille_TO_english(input))
    else:
        print(english_TO_braille(input))
    
if __name__ == "__main__":
    translate()

