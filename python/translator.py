import sys
from typing import Dict, List, Tuple

# For Braille to english translation
braille_to_letter_dict: Dict[Tuple[str, ...], str] = {
    ("O", ".", ".", ".", ".", "."): "a",
    ("O", ".", "O", ".", ".", "."): "b",
    ("O", "O", ".", ".", ".", "."): "c",
    ("O", "O", ".", "O", ".", "."): "d",
    ("O", ".", ".", "O", ".", "."): "e",
    ("O", "O", "O", ".", ".", "."): "f",
    ("O", "O", "O", "O", ".", "."): "g",
    ("O", ".", "O", "O", ".", "."): "h",
    (".", "O", "O", ".", ".", "."): "i",
    (".", "O", "O", "O", ".", "."): "j",
    ("O", ".", ".", ".", "O", "."): "k",
    ("O", ".", "O", ".", "O", "."): "l",
    ("O", "O", ".", ".", "O", "."): "m",
    ("O", "O", ".", "O", "O", "."): "n",
    ("O", ".", ".", "O", "O", "."): "o",
    ("O", "O", "O", ".", "O", "."): "p",
    ("O", "O", "O", "O", "O", "."): "q",
    ("O", ".", "O", "O", "O", "."): "r",
    (".", "O", "O", ".", "O", "."): "s",
    (".", "O", "O", "O", "O", "."): "t",
    ("O", ".", ".", ".", "O", "O"): "u",
    ("O", ".", "O", ".", "O", "O"): "v",
    (".", "O", "O", "O", ".", "O"): "w",
    ("O", "O", ".", ".", "O", "O"): "x",
    ("O", "O", ".", "O", "O", "O"): "y",
    ("O", ".", ".", "O", "O", "O"): "z",
    (".", ".", ".", ".", ".", "O"): "CAPITAL",
    (".", "O", ".", "O", "O", "O"): "NUMBER",
    (".", ".", ".", ".", ".", "."): " ",  # SPACE
}

braille_to_number_dict: Dict[Tuple[str, ...], str] = {
    ("O", ".", ".", ".", ".", "."): "1",
    ("O", ".", "O", ".", ".", "."): "2",
    ("O", "O", ".", ".", ".", "."): "3",
    ("O", "O", ".", "O", ".", "."): "4",
    ("O", ".", ".", "O", ".", "."): "5",
    ("O", "O", "O", ".", ".", "."): "6",
    ("O", "O", "O", "O", ".", "."): "7",
    ("O", ".", "O", "O", ".", "."): "8",
    (".", "O", "O", ".", ".", "."): "9",
    (".", "O", "O", "O", ".", "."): "0",
    (".", ".", ".", ".", ".", "."): " ",  # SPACE
}

# For english to Braille translation
english_to_braille_dict: Dict[str, Tuple[str, ...]] = {
    "a": ("O", ".", ".", ".", ".", "."),
    "b": ("O", ".", "O", ".", ".", "."),
    "c": ("O", "O", ".", ".", ".", "."),
    "d": ("O", "O", ".", "O", ".", "."),
    "e": ("O", ".", ".", "O", ".", "."),
    "f": ("O", "O", "O", ".", ".", "."),
    "g": ("O", "O", "O", "O", ".", "."),
    "h": ("O", ".", "O", "O", ".", "."),
    "i": (".", "O", "O", ".", ".", "."),
    "j": (".", "O", "O", "O", ".", "."),
    "k": ("O", ".", ".", ".", "O", "."),
    "l": ("O", ".", "O", ".", "O", "."),
    "m": ("O", "O", ".", ".", "O", "."),
    "n": ("O", "O", ".", "O", "O", "."),
    "o": ("O", ".", ".", "O", "O", "."),
    "p": ("O", "O", "O", ".", "O", "."),
    "q": ("O", "O", "O", "O", "O", "."),
    "r": ("O", ".", "O", "O", "O", "."),
    "s": (".", "O", "O", ".", "O", "."),
    "t": (".", "O", "O", "O", "O", "."),
    "u": ("O", ".", ".", ".", "O", "O"),
    "v": ("O", ".", "O", ".", "O", "O"),
    "w": (".", "O", "O", "O", ".", "O"),
    "x": ("O", "O", ".", ".", "O", "O"),
    "y": ("O", "O", ".", "O", "O", "O"),
    "z": ("O", ".", ".", "O", "O", "O"),
    " ": (".", ".", ".", ".", ".", "."),
    "CAPITAL": (".", ".", ".", ".", ".", "O"),
    "NUMBER": (".", "O", ".", "O", "O", "O"),
    "1": ("O", ".", ".", ".", ".", "."),
    "2": ("O", ".", "O", ".", ".", "."),
    "3": ("O", "O", ".", ".", ".", "."),
    "4": ("O", "O", ".", "O", ".", "."),
    "5": ("O", ".", ".", "O", ".", "."),
    "6": ("O", "O", "O", ".", ".", "."),
    "7": ("O", "O", "O", "O", ".", "."),
    "8": ("O", ".", "O", "O", ".", "."),
    "9": (".", "O", "O", ".", ".", "."),
    "0": (".", "O", "O", "O", ".", "."),
}


def translate_to_braille(arguments: List[str]) -> str:
    # List as a string builder
    output = []
    is_number = False

    for argument in arguments:

        for c in argument:
            if c.isnumeric():
                if not is_number:
                    is_number = True
                    output.extend(english_to_braille_dict["NUMBER"])
            elif c.isupper():
                output.extend(english_to_braille_dict["CAPITAL"])
            elif c == " ":
                is_number = False

            if c.lower() not in english_to_braille_dict:
                raise ValueError("Invalid character in the input")

            output.extend(english_to_braille_dict[c.lower()])

        # Add space between words
        if argument != arguments[-1]:
            output.extend(english_to_braille_dict[" "])
            is_number = False

    # Create string from list
    return "".join(output)


def process_braille_symbol(
    current_buffer: List[str],
    is_number: bool,
    is_capital: bool,
    given_output: List[str],
) -> Tuple[bool, bool]:
    if is_number:
        current_symbol = braille_to_number_dict[tuple(current_buffer)]
        if current_symbol is None:
            raise ValueError("Invalid braille symbol")

        if current_symbol == " ":
            is_number = False

        given_output.append(current_symbol)
    else:
        current_symbol = braille_to_letter_dict[tuple(current_buffer)]

        if current_symbol is None:
            raise ValueError("Invalid braille symbol")

        if current_symbol == "NUMBER":
            is_number = True
        elif current_symbol == "CAPITAL":
            is_capital = True
        else:
            if is_capital:
                given_output.append(current_symbol.upper())
                is_capital = False
            else:
                given_output.append(current_symbol)

    return is_number, is_capital


def translate_to_english(arguments: List[str]) -> str:
    # List as a string builder
    output = []
    is_number = False
    is_capital = False

    for argument in arguments:

        current_buffer = []

        for dots in argument:
            # Collect the 6 dots of the braille symbol
            current_buffer.append(dots)

            if len(current_buffer) == 6:
                # Process the current buffer when 6 dots collected
                # Update the booleans to reflect the current state
                is_number, is_capital = process_braille_symbol(
                    current_buffer, is_number, is_capital, output
                )
                current_buffer.clear()

        # Add space between arguments
        if argument != arguments[-1]:
            output.append(" ")

    # Create string from list
    return "".join(output)


if __name__ == "__main__":
    given_arguments = sys.argv[1:]

    first_arg = given_arguments[0]

    # There are not sequence in the braille alphabet where all six dots are raised
    # The presence of a dot in the argument indicates that the translation is from braille to english
    is_braille = first_arg.find(".") != -1

    if is_braille:
        print(translate_to_english(given_arguments))
    else:
        print(translate_to_braille(given_arguments))
