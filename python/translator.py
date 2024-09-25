import sys


BRAILLE_LENGTH = 6

BRAILLE_MAP = {
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

ENGLISH_MAP = {
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

BRAILLE_CAPS = ".....O"

NUMBER_AFTER_BRAILLE = ".O.OOO"

VALID_BRAILLE_CHARS = set(
    list(BRAILLE_MAP.values())
    + list(ENGLISH_MAP.values())
    + [BRAILLE_CAPS, NUMBER_AFTER_BRAILLE]
)

VALID_ENGLISH_CHARS = set(
    list(BRAILLE_MAP.keys())
    + [char.upper() for char in list(BRAILLE_MAP.keys())]
    + list(ENGLISH_MAP.keys())
)


def swap_keys(d):
    return {value: key for key, value in d.items()}


BRAILLE_TO_ENGLISH_CHARS = swap_keys(BRAILLE_MAP)

BRAILLE_TO_ENGLISH_NUMS = swap_keys(ENGLISH_MAP)


def process_input():
    if len(sys.argv) < 2:
        sys.exit("At least one argument required")

    return " ".join(sys.argv[1:])


def slice_str_length(string, chunk_len):
    return [string[i : i + chunk_len] for i in range(0, len(string), chunk_len)]


def is_braille(string):
    if not string or len(string) % BRAILLE_LENGTH != 0:
        return False

    string_chunks = slice_str_length(string, BRAILLE_LENGTH)

    return all(string_chunk in VALID_BRAILLE_CHARS for string_chunk in string_chunks)


def is_english(string: str) -> bool:
    return string and all(char in VALID_ENGLISH_CHARS for char in string)


def translate_to_english(braille_text):

    result = ""

    is_capital = False
    is_num = False

    braille_chars = slice_str_length(braille_text, BRAILLE_LENGTH)

    for braille_char in braille_chars:
        if braille_char == BRAILLE_CAPS:
            is_capital = True

        elif braille_char == NUMBER_AFTER_BRAILLE:
            is_capital = False
            is_num = True

        elif braille_char == BRAILLE_MAP[" "]:
            is_capital = False
            is_num = False
            result += BRAILLE_TO_ENGLISH_CHARS[braille_char]

        elif is_capital:
            is_capital = False
            result += BRAILLE_TO_ENGLISH_CHARS[braille_char].upper()

        elif is_num:
            result += BRAILLE_TO_ENGLISH_NUMS[braille_char]

        else:
            result += BRAILLE_TO_ENGLISH_CHARS[braille_char]

    return result


def to_braille(english_text):
    result = ""

    for i, english_char in enumerate(english_text):
        if english_char in BRAILLE_MAP:
            result += BRAILLE_MAP[english_char]

        elif english_char.lower() in BRAILLE_MAP:
            result += (
                BRAILLE_CAPS + BRAILLE_MAP[english_char.lower()]
            )

        else:
            if i == 0 or english_text[i - 1] not in ENGLISH_MAP:
                result += NUMBER_AFTER_BRAILLE

            result += ENGLISH_MAP[english_char]

    return result


def main():
    """
    Main function to handle input, check if it's Braille or English, and perform the appropriate translation.
    If the input is not valid Braille or English, it prints an error message and exits.
    """
    text = process_input()

    if is_braille(text):
        print(translate_to_english(text))

    elif is_english(text):
        print(to_braille(text))

    else:
        sys.exit("Invalid Input: Input is not in english or braille")


if __name__ == "__main__":
    main()