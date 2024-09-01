import sys

# This program translates text between Braille and English.

# Braille mappings for letters, numbers, and symbols
BRAILLE_LETTERS = {
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
}

BRAILLE_NUMBERS = {
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
}

BRAILLE_SYMBOLS = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

# Create a mapping from English characters to Braille cells
ENGLISH_TO_BRAILLE = {}

for braille_cell, letter in BRAILLE_LETTERS.items():
    ENGLISH_TO_BRAILLE[letter] = braille_cell

for braille_cell, number in BRAILLE_NUMBERS.items():
    ENGLISH_TO_BRAILLE[number] = braille_cell

for braille_cell, symbol in BRAILLE_SYMBOLS.items():
    ENGLISH_TO_BRAILLE[symbol] = braille_cell

# Special Braille indicators
CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"


def translator():
    """
    Takes input from command line and produces a translated output
    in either Braille or English relative to the input type.

    Args:
        string (str): The input text to translate.

    Returns:
        str: The translated text.
    """

    args = sys.argv[1:]
    input = []
    string = ""

    if len(args) > 1:
        for arg in args:
            input.append(arg)
        string = " ".join(input)
    else:
        string = args[0]

    if is_braille(string):
        translation = translate_to_english(string)
    else:
        translation = translate_to_braille(string)

    return translation


def translate_to_braille(text: str) -> str:
    """
    Translate an English string into Braille.

    Args:
        string (str): The English text to translate.

    Returns:
        str: The translated Braille text.
    """

    # Time Complexity: O(n), where n is the length of the input text.
    #                  Each character is processed once.
    # Space Complexity: O(n) for storing the Braille translation result

    num_mode = False  # Flag to indicate if numeric mode is active
    braille_result = []

    for char in text:
        if char.isalpha():
            if char.isupper():
                # If an alphabetic character is uppercase, add a capital follows indicator
                braille_result.append(CAPITAL_FOLLOWS)
            # Translate the alphabetic character (convert to lowercase for mapping)
            braille_result.append(ENGLISH_TO_BRAILLE.get(char.lower(), ""))
            num_mode = False  # Reset numeric mode after processing a letter

        elif char.isnumeric():
            if not num_mode:
                # If not already in numeric mode, add a number follows indicator
                braille_result.append(NUMBER_FOLLOWS)
                num_mode = True  # Set numeric mode active
            # Translate the numeric character
            braille_result.append(ENGLISH_TO_BRAILLE.get(char, ""))

        else:
            # Handle other characters (e.g., punctuation, spaces)
            if char == " ":
                # If the character is a space, reset numeric mode
                num_mode = False
            # Translate other characters (punctuation, special symbols)
            braille_result.append(ENGLISH_TO_BRAILLE.get(char, ""))

    return "".join(braille_result)


def translate_to_english(braille_text: str) -> str:
    """
    Translate a Braille string into English.

    Args:
        string (str): The Braille text to translate.

    Returns:
        str: The translated English text.
    """

    # Time Complexity: O(m), where m is the length of the Braille
    #                  text divided by 6 (size of braille cell). Each chunk is processed
    #                  only once.
    # Space Complexity: O(m) for storing the Braille translation result

    num_mode = False  # Flag for numeric mode
    cap_mode = False  # Flag for capitalization
    dec_mode = False  # Flag for decimal mode

    translated_char = ""
    result = []

    for i in range(0, len(braille_text), 6):
        cell = braille_text[i : i + 6]

        if cell == CAPITAL_FOLLOWS:
            cap_mode = True
            continue

        elif cell == DECIMAL_FOLLOWS:
            dec_mode = True
            continue

        elif cell == NUMBER_FOLLOWS:
            num_mode = True
            dec_mode = False
            continue

        # Translate Braille cell to English character
        else:
            if not num_mode and cell in BRAILLE_LETTERS:
                translated_char = BRAILLE_LETTERS.get(cell, "")
            elif num_mode and cell in BRAILLE_NUMBERS:
                translated_char = BRAILLE_NUMBERS.get(cell, "")

            elif dec_mode or cell in BRAILLE_SYMBOLS:
                translated_char = BRAILLE_SYMBOLS.get(cell, "")
                if translated_char == " ":
                    num_mode = False  # Reset number mode after encountering a space

            # Apply capitalization if needed
            if cap_mode:
                translated_char = translated_char.upper()
                cap_mode = False  # Reset capitalization mode after applying
        result.append(translated_char)

    return "".join(result)


def is_braille(braille_text: str) -> bool:
    """
    Validate if the given text consists of valid Braille characters.

    Args:
        braille_text (str): The text to validate.

    Returns:
        bool: True if all characters are valid Braille characters, False otherwise.
    """

    braille_chars = ".O"

    return all(char in braille_chars for char in braille_text)


print(translator())
