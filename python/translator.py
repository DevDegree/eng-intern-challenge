import sys

BRAILLE_TO_ENGLISH_DICT = {
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
    "......": " ",
}

BRAILLE_TO_NUMBER_DICT = {
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

ENGLISH_TO_BRAILLE_DICT = {value: key for key,
                           value in BRAILLE_TO_ENGLISH_DICT.items()}
NUMBER_TO_BRAILLE_DICT = {value: key for key,
                          value in BRAILLE_TO_NUMBER_DICT.items()}

CAPITALIZE_BRAILL = ".....O"
NUMBER_BRAILL = ".O.OOO"
SPACE = "......"


def translate_input(input_str: str) -> str:
    """Determines if the input is Braille or English and translates accordingly."""
    is_braill: bool = validate_braill_str(input_str)

    return braille_to_english(input_str) if is_braill else english_to_braill(input_str)


def braille_to_english(input_str: str) -> str:
    """Converts a Braille string to English."""

    # break braille down into 6 segments
    segments = [input_str[i: i + 6] for i in range(0, len(input_str), 6)]

    results: list[str] = []
    capitalize_flag: bool = False
    number_flag: bool = False

    for segment in segments:
        # check for capital following
        if segment == CAPITALIZE_BRAILL:
            capitalize_flag = True
        elif segment == NUMBER_BRAILL:
            number_flag = True
        else:
            char = BRAILLE_TO_ENGLISH_DICT[segment]
            # capitalize if prior segment was capital follows
            if capitalize_flag:
                capitalize_flag = False
                char = char.upper()
            elif number_flag:
                char = BRAILLE_TO_NUMBER_DICT[segment]
            results.append(char)
        if segment == "......" and number_flag:
            number_flag = False

    return "".join(results)


def english_to_braill(input_str: str) -> str:
    """Converts an English string to Braille."""

    results: list[str] = []

    number_flag: bool = False
    prev: str = None

    for char in input_str:
        if char.isupper():
            # logic for upper case
            results.append(CAPITALIZE_BRAILL)
            results.append(ENGLISH_TO_BRAILLE_DICT[char.lower()])
        elif char.isnumeric():
            # logic for numeric
            if not number_flag:
                results.append(NUMBER_BRAILL)
                number_flag = True
            results.append(NUMBER_TO_BRAILLE_DICT[char])
        else:
            results.append(ENGLISH_TO_BRAILLE_DICT[char])
        if prev and prev.isnumeric() and number_flag:
            number_flag = False
            results.append(SPACE)

    return "".join(results)


def validate_braill_str(input_str: str) -> bool:
    """Validates if the input string is a valid Braille string."""

    # input is too short to be braill
    if len(input_str) % 6 != 0:
        return False

    for char in input_str:
        if char != "O" and char != ".":
            return False

    return True


if __name__ == "__main__":
    args = " ".join(sys.argv[1:])
    print(translate_input(args))
