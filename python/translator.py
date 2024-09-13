"""
Pseudocode:

Check if the string is braille():
    if the string is div by 6 AND has only "O" and ".":
        return true

Braille to english map: {}

English to braille map: {}

Numbers mapping: {}

Translate the string func():

Testing():
"""
# A dictionary that maps braille characters to english characters.
# Does not include capital letters as they are identitical to lowercase letters, except 
# for the placement of a "Capitalization indicator" symbol before the letter to be capitalized.
# Contains symbols to indicate capitalization, numbers, and spaces.
bra_to_eng_dict = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.OO..": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.OOOO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".O.OOO": "#", ".....O": "^", "......": " "
}

# A dictionary that maps english characters to braille characters.
# Is a reverse mapping of the bra_to_eng dictionary.
eng_to_bra_dict = {x: y for y, x in bra_to_eng_dict.items()}

# A dictionary that maps numbers to their corresponding braille characters.
# Uses the eng_to_bra dictionary to map numbers to their corresponding braille characters.
bra_to_num_dict = {"O.....": "1" , "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
                   "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"}


def braille(input):
    """
    Checks if the input string, input, is a valid braille string.
    A valid braille string is a string that is divisible by 6 and contains only "O" and "."
    Returns True is the input string is a valid braille string.
    """
    return len(input) % 6 == 0 and all(c in "O." for c in input)


def braille_to_english(bra_string):
    """
    Translates a braille string, bra_string, to an english string.
    Returns the translated english string.
    """
    i = 0
    eng_string = []
    number = False
    capital = False

    # Iterate through the braille string in increments of 6 as each braille character is 6 characters long
    while i < len(bra_string):
        text = bra_string[i:i+6]
        i += 6

        # If the braille text is a number 'indicator', set the number flag to True
        if text == ".O.OOO":
            number = True
            continue
        # If the braille text is a capital letter 'indicator', set the capital flag to True
        elif text == ".....O":
            capital = True
            continue
        # If the braille text is space 'indicator', append a space to the english string
        elif text == "......":
            eng_string.append(" ")
            continue

        char = bra_to_eng_dict.get(text, "")

        # If the number flag is set, convert the character to it's respective number
        if number:
            char = bra_to_num_dict.get(text, "")
            number = False
        # If the capital flag is set, capitalize the character
        if capital:
            char = char.upper()
            capital = False
        
        # Append the character to the english string
        eng_string.append(char)

    return "".join(eng_string)


def english_to_braille(eng_string):
    """
    Translates an english string, eng_string, to a braille string.
    Returns the translated braille string.
    """
    text = []
    is_num = False

    for char in eng_string:
        if char.isupper():
            text.append(eng_to_bra_dict["^"])
            char = char.lower()
        
        if char.isdigit():
            if not is_num:
                text.append(eng_to_bra_dict["#"])
                is_num = True
            text.append(eng_to_bra_dict[chr(ord('a') + int(char) - 1)])
        else:
            is_num = False
            text.append(eng_to_bra_dict.get(char, eng_to_bra_dict[" "]))

    return "".join(text)


def translator(input):
    """
    Translates a string, input, to either braille or english depening on what language 
    the input string is in.
    Returns the translated string.
    """
    if braille(input):
        return braille_to_english(input)
    else:
        return english_to_braille(input)
