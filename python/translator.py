import sys
import logging

# Constants

# Error message format for incorrect input
FORMAT_ERR = "{input_type} input '{input}' is not formatted correctly."

# Logger setup
LOGGER = logging.getLogger(__name__)

# Mappings between braille and plain text
PLAIN_TO_BRAILLE = {
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
    " ": "......",
    ".": ".O..OO",
    ",": "..O...",
    "?": ".OO.OO",
    "!": "O.OO.O",
    ":": "OO..OO",
    ";": "O.O.OO",
    "-": "O....O",
    "/": "O...O.",
    "<": "O..OOO",
    ">": ".O.OOO",
    "(": "O..O.O",
    ")": ".OO..O",
    " ": "......",
}

# Reverse mapping from braille to plain text (only for alphabetic characters)
BRAILLE_TO_ALPHABET = {
    braille: plain for plain, braille in PLAIN_TO_BRAILLE.items() if not plain.isdigit()
}

# Reverse mapping from braille to numeric characters
BRAILLE_TO_NUMBER = {
    braille: number for number, braille in PLAIN_TO_BRAILLE.items() if number.isdigit()
}

# Special symbols in braille (capital letter, number sign, etc.)
SPECIAL_SYMBOLS = {"capital": ".....O", "number": ".O.OOO", "decimal": ".O...O"}

# Reverse mapping for special braille symbols
SPECIAL_SYMBOLS_BRAILLE = {
    braille: symbol for symbol, braille in SPECIAL_SYMBOLS.items()
}


def is_braille(text: str) -> bool:
    """Determine whether the input text is braille or not.

    Args:
        text: Braille or plain text.
    """
    # Check if all characters in text are valid braille characters ('O' or '.')
    for t in text:
        if t not in ["O", "."]:
            return False

    # Ensure the length of the braille text is a multiple of 6 (one braille character)
    return len(text) % 6 == 0


def translate(text):
    """
    Translate between Braille and English. Determine the type of text and convert accordingly.
    """
    input_type = "Braille" if is_braille(text) else "English"

    try:
        return (
            braille_to_english(text) if is_braille(text) else english_to_braille(text)
        )
    except KeyError:
        # Log an error if input text is not formatted correctly
        LOGGER.error(FORMAT_ERR.format(input_type=input_type, input=text))


def braille_to_english(braille):
    """Translate braille to english.

    Precondition:
        braille is a valid braille text.
    """
    english = ""

    # Flags to track if the next letter should be capitalized or treated as a number
    is_capital = False
    is_number = False

    i = 0
    while i + 6 <= len(braille):
        # Extract the next braille character (6 dots)
        bchar = braille[i : i + 6]
        symbol = SPECIAL_SYMBOLS_BRAILLE.get(bchar, None)

        # Set flags based on special symbols (capital or number)
        if symbol:
            if symbol == "capital":
                is_capital = True
            elif symbol == "number":
                is_number = True

            i += 6
            continue

        alphabets = BRAILLE_TO_ALPHABET

        if alphabets[bchar] == " ":
            is_number = False
        elif is_number:
            alphabets = BRAILLE_TO_NUMBER

        # Add the corresponding English character to the result
        english += alphabets[bchar].upper() if is_capital else alphabets[bchar]

        # Reset the capital flag and move to the next character
        is_capital = False
        i += 6

    return english


def english_to_braille(plain):
    """Translate english to braille.

    Precondition:
        Input plain is a valid english text.
    """
    braille = ""
    is_digit = False

    for char in plain:
        # Add special braille symbol for capital letters
        if char.isupper():
            braille += SPECIAL_SYMBOLS["capital"]
        # Add special braille symbol for numbers
        elif char.isdigit() and not is_digit:
            braille += SPECIAL_SYMBOLS["number"]
            is_digit = True
        # Reset digit flag when encountering a space
        elif char == " ":
            is_digit = False

        # Add corresponding braille character to the result
        braille += PLAIN_TO_BRAILLE[char.lower()]

    return braille


if __name__ == "__main__":
    # Check if there is text provided for translation
    if len(sys.argv) < 2:
        print("Usage: python translator.py text to translate")
        sys.exit(1)

    # Combine all arguments into a single string for translation
    text_to_translate = " ".join(sys.argv[1:])
    translated_text = translate(text_to_translate)
    print(translated_text)
