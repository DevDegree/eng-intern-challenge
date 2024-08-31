import sys

"""
This script converts Braille to English and English to Braille based on the input String
"""

# Converter containing the mapping between Braille and English characters (and vice versa)
converter = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
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
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
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
    "O..OOO": "z",
    "..OO.O": ".", # normal period (not decimal follows)
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    # "O..OO.": ">", commented due to conflict with "o"
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " "
}

# Extra mapping for Braille to english when converting to a number rather than a letter
num_map = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
    ".O...O": ".", # Decimal follows
}

def convert_braille_to_english(input_string):
    """
    Convert a Braille String to English

    input_string (int) -- The Braille String
    """
    return_string = ""
    # Check if the Braille string is divisible by 6
    if len(input_string) % 6 != 0:
        # print("Braille string must be divisible by 6")
        sys.exit(1)
    
    # Variables to keep track of current states
    number_follows = False
    capital_follows = False
    decimal_follows = False
    for i in range(0, len(input_string), 6):
        curr_character = input_string[i:i+6]
        if curr_character not in converter and curr_character not in num_map and curr_character != ".....O" and curr_character != ".O.OOO":
            # print("The following character does not exist: " + curr_character)
            sys.exit(1)
        elif capital_follows == True:
            # Need to actually check if the braille is an alphabet character. (cannot capitalize a number or another token)
            if converter[curr_character] in "abcdefghijklmnopqrstuvwxyz":
                return_string += converter[curr_character].upper()
                capital_follows = False
            else:
                # print("Cannot capitalize: " + converter[curr_character])
                sys.exit(1)
        elif curr_character == "......":
            number_follows = False
            decimal_follows = False
            return_string += converter[curr_character]
        elif number_follows == True:
            if curr_character in num_map:
                if curr_character == ".O...O":
                    if decimal_follows == True:
                        # print("Cannot have more than 1 decimal in a number")
                        sys.exit(1)
                    else:
                        decimal_follows = True
                return_string += num_map[curr_character]
            else:
                # print("The following is not a decimal when it should be: " + curr_character)
                sys.exit(1)
        elif curr_character == ".....O":
            capital_follows = True
        elif curr_character == ".O.OOO":
            number_follows = True
        else:
            return_string += converter[curr_character]
    return return_string

def convert_english_to_braille(input_string):
    """
    Convert an English String to Braille

    input_string (int) -- The English String
    """
    return_string = ""
    number_follows = False
    decimal_follows = False
    for letter in input_string:
        if letter.isupper():
            return_string += ".....O"
            return_string += converter[letter.lower()]
        elif letter == " ":
            number_follows = False
            decimal_follows = False
            return_string += converter[letter]
        elif letter == "." and number_follows == True:
            if decimal_follows == False:
                return_string += ".O...O"
                decimal_follows = True
            else:
                # print("Cannot have two decimals in a number")
                sys.exit(1)
        elif letter in "0123456789":
            if number_follows == False:
                number_follows = True
                return_string += ".O.OOO"
            return_string += converter[letter]
        elif letter not in converter:
            # print("The following character: " + letter + ", cannot be converted to Braille")
            sys.exit(1)
        else:
            return_string += converter[letter]
    return return_string

# Validation that the user passed enough input arguments
if len(sys.argv) < 2:
    # print("Please pass at least 1 argument")
    sys.exit(1)

# Storing arguments in an input String
input_string = ""
for i, word in enumerate(sys.argv):
    if i == 0:
        continue
    input_string += word
    if i != len(sys.argv) - 1:
        input_string += " "

is_braille = True

# Check if the input String is Braille
for letter in input_string:
    if letter != "O" and letter != ".":
        is_braille = False
        break

# Treat as english if only O and . are in the String but it is less than 6 characters
if is_braille and len(input_string) %6 != 0 and len(input_string) < 6:
    is_braille = False

if is_braille:
    return_string = convert_braille_to_english(input_string)

else:
    return_string = convert_english_to_braille(input_string)
        
# Printing the output
print(return_string)