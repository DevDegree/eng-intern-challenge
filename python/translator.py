

# The dictionary maps each letter and space to its corresponding Braille representation.
# Braille is represented as a string of six characters, where 'O' denotes a raised dot, and '.' denotes an unraised dot.
BRAILLE_LETTER_MAP = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

# The dictionary contains mappings for number characters to its corresponding Braille representation, used in the translation process.
BRAILLE_NUMBER_MAP = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# The dictionary contains mappings for special Braille characters used in the translation process.
# 'capital' is used to indicate that the next letter is uppercase, and 'number' indicates that following characters are numbers.
BRAILLE_SPECIAL_MAP = {
    "capital": ".....O", "number": ".O.OOO"
}

# Combine the above maps for translation to Braille
# The combined map is used for easy lookup during the translation process.
BRAILLE_MAP = {**BRAILLE_LETTER_MAP, **BRAILLE_NUMBER_MAP, **BRAILLE_SPECIAL_MAP}

# Function to translate English text to Braille
def translate_english_to_braille(english):
    """
    Translates a given English string into its Braille representation.
    Handles uppercase letters by prefixing them with the 'capital' indicator,
    and handles numbers by prefixing them with the 'number' indicator.
    """
    result = ""
    number_mode = False  # Tracks whether the translation is currently in number mode

    # Iterate over each character in the input string
    for char in english:
        if char.isupper():
            # Add the capital indicator and translate the lowercase version of the character
            result += BRAILLE_SPECIAL_MAP["capital"] + BRAILLE_LETTER_MAP[char.lower()]
            number_mode = False  # Reset number mode after translating a letter
        elif char.isdigit():
            if not number_mode:
                # Activate number mode by adding the number indicator
                result += BRAILLE_SPECIAL_MAP["number"]
                number_mode = True
            # Translate the digit
            result += BRAILLE_NUMBER_MAP[char]
        elif char == " ":
            # Translate space and reset number mode
            result += BRAILLE_LETTER_MAP[" "]
            number_mode = False  # Reset number mode after space
        else:
            # Translate a regular lowercase letter
            result += BRAILLE_LETTER_MAP[char]
            number_mode = False  # Reset number mode after letters
    return result

# Function to translate Braille to English text
def translate_braille_to_english(braille):
    """
    Translates a given Braille string into its English representation.
    Handles uppercase letters when prefixed with the 'capital' indicator,
    and translates numbers when prefixed with the 'number' indicator.
    """
    # Invert the dictionaries for reverse lookup (Braille to English)
    INVERTED_BRAILLE_NUMBER_MAP = {v: k for k, v in BRAILLE_NUMBER_MAP.items()}
    INVERTED_BRAILLE_LETTER_MAP = {v: k for k, v in BRAILLE_LETTER_MAP.items()}
    
    result = ""
    i = 0
    capital_next = False  # Tracks whether the next letter should be capitalized
    number_mode = False  # Tracks whether the translation is currently in number mode

    # Iterate through the Braille string in chunks of 6 characters (each Braille character)
    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == BRAILLE_SPECIAL_MAP["capital"]:
            # Set flag to capitalize the next character
            capital_next = True
            i += 6
        elif chunk == BRAILLE_SPECIAL_MAP["number"]:
            # Set flag to translate subsequent chunks as numbers
            number_mode = True
            i += 6
        else:
            if number_mode and chunk in INVERTED_BRAILLE_NUMBER_MAP:
                # Translate the chunk as a number
                result += INVERTED_BRAILLE_NUMBER_MAP[chunk]
            elif capital_next and chunk in INVERTED_BRAILLE_LETTER_MAP:
                # Translate and capitalize the chunk as a letter
                result += INVERTED_BRAILLE_LETTER_MAP[chunk].upper()
                capital_next = False
            else:
                # Translate the chunk as a regular letter
                result += INVERTED_BRAILLE_LETTER_MAP.get(chunk, '')
                number_mode = False
            i += 6
    return result

# Function to determine whether the input is Braille or English and apply the appropriate translation
def translate(input_string):
    """
    Determines whether the input string is in Braille or English and translates accordingly.
    Assumes that Braille strings contain only 'O' and '.' characters.
    """
    if all(char in 'O.' for char in input_string):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)
    
# Main script execution
if __name__ == "__main__":
    # Capture input from the command line arguments, concatenate them into a single string, and translate
    import sys
    input_string = " ".join(sys.argv[1:])
    print(translate(input_string))
