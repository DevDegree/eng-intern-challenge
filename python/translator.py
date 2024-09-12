import sys

BRAILLE_TO_NUMBER_MAP = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

BRAILLE_TO_ENGLISH_MAP = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",

    ".....O": "capital follows", ".O.OOO": "number follows", "......": " ",
}

ENGLISH_TO_BRAILLE_MAP = {v: k for k, v in BRAILLE_TO_ENGLISH_MAP.items()}
NUMBER_TO_BRAILLE_MAP = {v: k for k, v in BRAILLE_TO_NUMBER_MAP.items()}

def is_braille(input_str: str) -> bool:
    """Check if the provided input string represents Braille text."""
    if len(input_str) % 6 != 0:
        return False

    return all(char in ("O", ".") for char in input_str)

def translate_to_english(braille_str: str) -> str:
    """Translate Braille text into English."""
    result = []
    braille_chars = [braille_str[i:i + 6] for i in range(0, len(braille_str), 6)]
    number_mode = False
    capital_mode = False

    for char in braille_chars:
        if char == ".....O":  # Capital indicator
            capital_mode = True
        elif char == ".O.OOO":  # Number indicator
            number_mode = True
        elif char == "......":  # Space
            number_mode = False
            result.append(" ")
        else:
            if number_mode:
                result.append(BRAILLE_TO_NUMBER_MAP.get(char, ""))
            elif capital_mode:
                result.append(BRAILLE_TO_ENGLISH_MAP.get(char, "").upper())
                capital_mode = False
            else:
                result.append(BRAILLE_TO_ENGLISH_MAP.get(char, ""))

    return "".join(result)

def translate_to_braille(english_str: str) -> str:
    """Translate English text into Braille."""
    result = []
    number_mode = False

    for char in english_str:
        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE_MAP["capital follows"])
            result.append(ENGLISH_TO_BRAILLE_MAP[char.lower()])
        elif char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE_MAP["number follows"])
                number_mode = True
            result.append(NUMBER_TO_BRAILLE_MAP[char])
        else:
            if number_mode:
                number_mode = False
            result.append(ENGLISH_TO_BRAILLE_MAP.get(char, ""))

    return "".join(result)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Invalid command line arguments.")

    input_string = " ".join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))
