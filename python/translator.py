import sys

# English to Braille mapping
alphabet_to_braille = {
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
}

# Braille to English Mapping
braille_to_alphabet = {
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


# Number to Braille mapping
numbers_to_braille = {
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

# Braille to English mapping
braille_to_numbers = {
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


# Symbol to Braille mapping
symbol_to_braille = {
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "_": "....OO",
    "/": ".O..O.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

# Braille to symbol mapping
braille_to_symbols = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "_",
    ".O..O.": "/",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}


# Indicator to Braille mapping
indicator_to_braille = {
    "capital": ".....O",
    "number": ".O.OOO",
    "decimal": ".O...O"
}

# Braille to indicator mapping
braille_to_indicator = {
    ".....O": "capital",
    ".O.OOO": "number",
    ".O...O": "decimal"
}


def detect_system(input_string: str) -> str:
    """
    Checks a given string and returns its type as a string:
        - "english"
        - "braille"

    Will also throw an error if fed an empty string
    """

    # Handle empty string
    if not input_string:
        raise ValueError("Cannot process empty string")

    # Create a set of valid English characters, removing '.' as to not collide with braille
    valid_english = set(alphabet_to_braille.keys()) | set(
        numbers_to_braille.keys() | symbol_to_braille.keys()
    )
    valid_english.remove(".")

    # Check for existence of a valid english characters in the string
    for char in input_string:
        if char in valid_english:
            return "english"

    # Return braille if no presense of english
    return "braille"


def translate_braille(braille_string: str) -> str:
    """Will take a Braille string and return a translated English string"""

    translated_string = []
    capital_processing = False
    number_processing = False

    # Convert Braille string into Braille characters, known as "cells"
    braille_cells = [
        braille_string[i:i + 6] for i in range(0, len(braille_string), 6)
    ]

    for cell in braille_cells:
        if cell in braille_to_indicator:
            # Check for special indicator cell for next character
            if braille_to_indicator[cell] == "capital":
                capital_processing = True
            elif braille_to_indicator[cell] == "number":
                number_processing = True

        # Check if number is currently being written
        elif number_processing and cell in braille_to_numbers:
            translated_string.append(braille_to_numbers[cell])

        # Check if number is being written with decimal
        elif number_processing and cell in braille_to_indicator:
            translated_string.append(".")

        # Check alphabet cells
        elif cell in braille_to_alphabet:
            letter = braille_to_alphabet[cell]

            # Handle capital letter
            if capital_processing:
                letter = letter.upper()
                capital_processing = False

            translated_string.append(letter)

        # Check symbol cells
        elif cell in braille_to_symbols:
            symbol = braille_to_symbols[cell]
            if symbol == " ":
                # Stop number processing if space is next
                number_processing = False

            translated_string.append(symbol)

    return "".join(translated_string)


def translate_english(english_string) -> str:
    """Will take a English string and return a translated Braille string"""

    translated_string = []
    number_processing = False

    for char in english_string:
        # Checks for alphabet letters
        if char.isalpha():
            # Checks for uppercase letter
            if char.isupper():
                translated_string.append(indicator_to_braille["capital"])
                char = char.lower()

            translated_string.append(alphabet_to_braille[char])

        # Checks for numeral digits
        elif char.isdigit():
            # Handles subsequent digits in number
            if not number_processing:
                number_processing = True
                translated_string.append(indicator_to_braille["number"])

            translated_string.append(numbers_to_braille[char])
        # Checks for symbols
        elif char in symbol_to_braille:
            # Handles end of number
            if char == " ":
                number_processing = False

            translated_string.append(symbol_to_braille[char])

    return "".join(translated_string)


def main():
    # Grab arguments
    user_input = " ".join(sys.argv[1:])
    system = detect_system(user_input)

    # Determine which translations is appropriate
    if system == "english":
        translated_text = translate_english(user_input)
    elif system == "braille":
        translated_text = translate_braille(user_input)

    print(translated_text)


if __name__ == "__main__":
    main()
