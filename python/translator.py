import sys

# Braille mappings for alphabet, numbers, and special characters
ENG_TO_BRAILLE = {
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
    " ": "......",
}

NUMBER_TO_BRAILLE = {
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

BRAILLE_TO_ENG = {v: k for k, v in ENG_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

# Special Braille markers for capitalization and numbers
CAPITAL_MARKER = ".....O"
NUMBER_MARKER = ".O.OOO"


def detect_input_type(input_str: str) -> str:
    """
    Detect if the input string is Braille or English.
    Braille consists of O and ., while English has a wider character set.
    """
    if all(c in {"O", ".", " "} for c in input_str):
        return "braille"
    return "english"


def process_english_input(input_str: str) -> str:
    """
    Converts English input to Braille, handling capitalization and numbers.
    """
    output = []
    number_mode = False

    for char in input_str:
        if char.isupper():
            output.append(CAPITAL_MARKER)
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                output.append(NUMBER_MARKER)
                number_mode = True
            output.append(NUMBER_TO_BRAILLE[char])
        else:
            if number_mode and not char.isdigit():
                number_mode = False
            if char in ENG_TO_BRAILLE:
                output.append(ENG_TO_BRAILLE[char])
            else:
                output.append(
                    ENG_TO_BRAILLE[" "]
                )  # Replace unrecognized chars with space Braille

    return "".join(output)


def process_braille_input(input_str: str) -> str:
    """
    Converts Braille input to English, handling capitalization and numbers.
    """
    output = []
    number_mode = False
    capital_mode = False
    input_str = input_str.replace(" ", "")  # Remove spaces for proper chunking

    # Process in chunks of 6 characters
    for i in range(0, len(input_str), 6):
        chunk = input_str[i : i + 6]

        if chunk == CAPITAL_MARKER:
            capital_mode = True
        elif chunk == NUMBER_MARKER:
            number_mode = True
        else:
            if number_mode:
                output.append(BRAILLE_TO_NUMBER.get(chunk, ""))
                if chunk == "......":  # Reset number mode after space
                    number_mode = False
            else:
                char = BRAILLE_TO_ENG.get(chunk, " ")
                if capital_mode:
                    char = char.upper()
                    capital_mode = False
                output.append(char)

    return "".join(output)


def translator() -> None:
    """
    Main function to handle translation from either English to Braille or Braille to English.
    """
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input-string>")
        sys.exit(1)

    input_string = " ".join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == "english":
        result = process_english_input(input_string)
    else:
        result = process_braille_input(input_string)

    print(result)


if __name__ == "__main__":
    translator()
