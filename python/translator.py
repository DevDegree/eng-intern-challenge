import sys

# Constants for Braille symbol representation
BRAILLE_SYMBOL_LENGTH = 6
BRAILLE_RAISED = "O"
BRAILLE_LOWERED = "."
BRAILLE_SPACE = "......"
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

# Dictionaries for translating between English/Braille and numbers/Braille
ENGLISH_TO_BRAILLE = {
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
    "p": "OOOOO.",
    "q": "OOOOOO",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
}

NUMBERS_TO_BRAILLE = {
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
}

# Inverted dictionaries for translating Braille back to English and numbers
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}


def is_english(string: str) -> bool:
    """
    Determine if the string contains characters other than Braille symbols.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is English (not Braille), False otherwise.
    """
    for char in string:
        if char not in {
            BRAILLE_RAISED,
            BRAILLE_LOWERED,
            " ",
        }:  # Added space for clarity
            return True
    return False


def english_to_braille(english: str) -> str:
    """
    Convert an English string to Braille representation.

    Args:
        english (str): The English string to convert.

    Returns:
        str: The Braille representation of the input string.
    """
    braille = ""
    is_number = False

    for char in english:
        if char.isupper():
            braille += CAPITAL_FOLLOWS
        if char.isdigit():
            if not is_number:
                braille += NUMBER_FOLLOWS
            braille += NUMBERS_TO_BRAILLE[char]
            is_number = True
        else:
            braille += ENGLISH_TO_BRAILLE.get(char.lower(), BRAILLE_SPACE)
            if char == " ":
                is_number = False  # Reset number flag on space

    return braille


def braille_to_english(braille: str) -> str:
    """
    Convert a Braille string to English representation.

    Args:
        braille (str): The Braille string to convert.

    Returns:
        str: The English representation of the input Braille string.
    """
    english = ""
    is_capital = False
    is_number = False

    for i in range(0, len(braille), BRAILLE_SYMBOL_LENGTH):
        symbol = braille[i : i + BRAILLE_SYMBOL_LENGTH]

        if symbol == CAPITAL_FOLLOWS:
            is_capital = True
            continue

        if symbol == NUMBER_FOLLOWS:
            is_number = True
            continue

        if is_number:
            english += BRAILLE_TO_NUMBERS.get(symbol, "?")
            continue

        if is_capital:
            english += BRAILLE_TO_ENGLISH.get(symbol, "?").upper()
            is_capital = False
            continue

        english += BRAILLE_TO_ENGLISH.get(symbol, "?")
        if symbol == BRAILLE_SPACE:
            is_number = False

    return english


def main():
    """
    Main function to process command-line arguments and perform translation.
    """
    # Combine all command-line arguments into a single string
    arguments = " ".join(sys.argv[1:])

    # Determine whether to translate from English to Braille or vice versa
    if is_english(arguments):
        print(english_to_braille(arguments))
    else:
        print(braille_to_english(arguments))


if __name__ == "__main__":
    main()
