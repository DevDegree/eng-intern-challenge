import sys

# A python program/script that translates english to braille and vice versa.
# (Values to be translated should be passed in as a runtime argument).
# Made for Shopify's 2025 Summer Software Engineer Intern challenge.
# By: Athanasios Topaltsis

# Runtime arguments
args = sys.argv

# --- Braille related variable declarations ---

# Dictionary of english letters mapped to their braille equivalent.
alphabet = {
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
    "z": "O..OOO"
}

# Inverted alphabet dictionary with braille as keys
alphabet_inverted = {value: key for key, value in alphabet.items()}

# Dictionary of numbers mapped to their braille equivalent.
numbers = {
    "1": "O.....",  # Same as 'a'
    "2": "O.O...",  # Same as 'b'
    "3": "OO....",  # Same as 'c'
    "4": "OO.O..",  # Same as 'd'
    "5": "O..O..",  # Same as 'e'
    "6": "OOO...",  # Same as 'f'
    "7": "OOOO..",  # Same as 'g'
    "8": "O.OO..",  # Same as 'h'
    "9": ".OO...",  # Same as 'i'
    "0": ".OOO.."   # Same as 'j'
}

# Inverted numbers dictionary with braille as keys
numbers_inverted = {value: key for key, value in numbers.items()}

# Dictionary of symbols mapped to their braille equivalent.
symbols = {
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
    ")": ".O.OO."
}

# Inverted symbols dictionary with braille as keys
symbols_inverted = {value: key for key, value in symbols.items()}

# Other braille variables
braille_space = "......"
braille_capital_prefix = ".....O"
braille_decimal_prefix = ".O...O"
braille_number_prefix = ".O.OOO"

# --- Translation Logic ---


# Returns true if the passed in value is Braille.
def is_braille(value: str) -> bool:
    return all(c in "O." for c in value)


# Translates braille to english and returns the result.
def braille_to_english(braille: str) -> str:
    # If the passed in string is not braille (therefore english),
    # just return the passed in value.
    if not is_braille(braille):
        return braille

    # Convert braille into a list where values are defined every 6 characters.
    braille_list = [braille[i:i + 6] for i in range(0, len(braille), 6)]

    # The resulting english string.
    english = ""

    # Looping through all characters of the string passed in
    # and translate accordingly.
    index = 0
    while index < len(braille_list):
        c = braille_list[index]  # current character
        if c == braille_capital_prefix:  # add capital letter
            # Get the letter from the next character over, as this is the prefix.
            english += alphabet_inverted[braille_list[index + 1]].capitalize()
            # Increment the index to skip the letter on the next iteration.
            index = index + 1
        elif c in braille_number_prefix:  # add number
            # Assume all following characters are numbers until we hit a space.
            index = index + 1
            while index < len(braille_list):
                if braille_list[index] != braille_space:
                    english += numbers_inverted[braille_list[index]]
                    index = index + 1
                else:
                    english += " "
                    break

        elif c in symbols_inverted.keys():
            english += symbols_inverted[c]
        elif c == braille_space:
            english += " "
        else:
            # must be a regular lowercase letter
            english += alphabet_inverted[c]

        index = index + 1  # increment the index

    # Return the built english string.
    return english


# Translates english to braille and returns the result.
def english_to_braille(english: str) -> str:
    # If the passed in string is braille (therefore not english),
    # just return the passed in value.
    if is_braille(english):
        return english

    # The resulting braille string.
    braille = ""

    # Looping through all characters of the string passed in
    # and translate accordingly.
    index = 0
    while index < len(english):
        c = english[index]  # current character
        if c.isupper():  # add upper prefix + translated value
            braille += braille_capital_prefix + alphabet[c.lower()]
        elif c in numbers.keys():  # add number prefix + translated value
            # add current number, then assume the rest are all numbers until we hit a space.
            braille += braille_number_prefix + numbers[c]
            index = index + 1
            while index < len(english):
                if english[index] != " ":
                    braille += numbers[english[index]]
                    index = index + 1
                else:
                    braille += braille_space
                    break
        elif c in symbols.keys():
            braille += symbols[c]
        elif c == " ":
            braille += braille_space
        else:
            # must be a regular lowercase letter
            braille += alphabet[c]

        index = index + 1

    # Return the built braille string.
    return braille


# If no runtime args were passed in, send a message and exit.
# (<= 1 as pyton passes in the file name by default as a runtime arg).
if len(args) <= 1:
    print("Nothing was passed in, therefore nothing to translate!")
    exit()

# Checking if all args passed in are braille or not.
# If there is any arg that is not braille, all args passed in will be treated as english.
for i in range(1, len(args)):
    # An arg is not braille, therefore the args are english.
    if not is_braille(args[i]):
        # Join all the args into a string with a space in between them.
        joined_string = " ".join(args[1:])
        # Call to translate the string and print the returned result.
        print(english_to_braille(joined_string))
        break  # stop the iteration
    # When arguments passed in are braille.
    else:
        # Join all the args into a string with a space in between them.
        joined_string = " ".join(args[1:])
        # Call to translate the string and print the returned result.
        print(braille_to_english(joined_string))
        break  # stop the iteration
