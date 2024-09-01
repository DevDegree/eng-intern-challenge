import sys

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

# Python dicts are well optimized, could combine letters and numbers
# but kept separate for readability
LETTER_TO_BRAILLE = {
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
    " ": SPACE,
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
    " ": SPACE,
}

BRAILLE_TO_LETTER = {b: l for l, b in LETTER_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {b: n for n, b in NUMBER_TO_BRAILLE.items()}


def is_braille(input_string: str) -> bool:
    """
    Checks if the input string is Braille.
    Braille inputs should contain only "O" and ".", at least 1 ".",
    and have a length divisible by 6.

    Parameters
    ----------
    input_string : str
        The input string to check.

    Returns
    -------
    bool : True if the input string is Braille, otherwise False.
    """
    return (
        all(char in {"O", "."} for char in input_string)
        and "." in input_string
        and len(input_string) % 6 == 0
    )


def braille_to_english(input_string: str) -> str:
    """
    Translates Braille to English.

    Parameters
    ----------
    input_string : str
        The Braille input string to translate.

    Returns
    -------
    str : The translated English string.
    """
    # Split input string into 6 character Braille symbols
    braille_symbols = [
        input_string[i : i + 6] for i in range(0, len(input_string), 6)
    ]

    english_result = []
    is_capital = False
    is_number = False

    for symbol in braille_symbols:
        # Number follows stops at next space
        if symbol == SPACE:
            is_number = False
            english_result.append(BRAILLE_TO_NUMBER[symbol])
        # Check for numbers must come first as numbers and letters share symbols
        elif is_number:
            english_result.append(BRAILLE_TO_NUMBER[symbol])
        elif symbol in BRAILLE_TO_LETTER:
            english_char = BRAILLE_TO_LETTER[symbol]

            if is_capital:
                # Capital follows only capitalizes the next char
                is_capital = False
                english_result.append(english_char.upper())
            else:
                english_result.append(english_char)
        # Indicate next symbol will be a number or capital
        elif symbol == CAPITAL_FOLLOWS:
            is_capital = True
        elif symbol == NUMBER_FOLLOWS:
            is_number = True
    # str.join() is faster than string concatenation, O(n)
    return "".join(english_result)


def english_to_braille(input_string: str) -> str:
    """
        Translates English to Braille.

    Parameters
    ----------
    input_string : str
        The English input string to translate.

    Returns
    -------
    str : The translated Braille string.
    """
    braille_result = []
    is_number = False

    for char in input_string:
        # Check for space first to set is_number correctly
        if char == " ":
            # Number follows stops at next space
            is_number = False
            braille_result.append(SPACE)
        # char is a number
        elif char in NUMBER_TO_BRAILLE:
            # Only add number follows before the first number
            # if there are consecutive numbers
            if not is_number:
                is_number = True
                braille_result.append(NUMBER_FOLLOWS)
            braille_result.append(NUMBER_TO_BRAILLE[char])
        # char is uppercase
        elif char.isupper():
            braille_result.append(CAPITAL_FOLLOWS)
            braille_result.append(LETTER_TO_BRAILLE[char.lower()])
        # char is lowercase
        else:
            braille_result.append(LETTER_TO_BRAILLE[char])
    return "".join(braille_result)


if __name__ == "__main__":
    # < 2 (instead of != 2) required to be able to process spaces in the input
    if len(sys.argv) < 2:
        print("Usage: python translator.py text_to_translate")
        sys.exit(1)

    # Join with " "to maintain spaces in the input
    text_to_translate = " ".join(sys.argv[1:])

    if is_braille(text_to_translate):
        print(braille_to_english(text_to_translate))
    else:
        print(english_to_braille(text_to_translate))
