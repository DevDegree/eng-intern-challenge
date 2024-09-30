import sys

ENGLISH = "english"
BRAILLE = "braille"
CAPITAL = "capital"
NUMBER  = "number"

INVALID_INPUT_MSG = "Invalid input. Only alphanumeric characters and spaces are allowed for english. Only '.' and 'O' are allowed for braille."

PERMITTED_NON_ALPHANUMERIC_CHARS = set([" "])
PERMITTED_MODIFIERS              = set([CAPITAL, NUMBER])
NUMBER_TERMINATING_CHARS         = set([" "])

ENGLISH_TO_BRAILLE = {
    " "     : "......",
    "a"     : "O.....",
    "b"     : "O.O...",
    "c"     : "OO....",
    "d"     : "OO.O..",
    "e"     : "O..O..",
    "f"     : "OOO...",
    "g"     : "OOOO..",
    "h"     : "O.OO..",
    "i"     : ".OO...",
    "j"     : ".OOO..",
    "k"     : "O...O.",
    "l"     : "O.O.O.",
    "m"     : "OO..O.",
    "n"     : "OO.OO.",
    "o"     : "O..OO.",
    "p"     : "OOO.O.",
    "q"     : "OOOOO.",
    "r"     : "O.OOO.",
    "s"     : ".OO.O.",
    "t"     : ".OOOO.",
    "u"     : "O...OO",
    "v"     : "O.O.OO",
    "w"     : ".OOO.O",
    "x"     : "OO..OO",
    "y"     : "OO.OOO",
    "z"     : "O..OOO",
    CAPITAL : ".....O",
    NUMBER  : ".O.OOO"
}
BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}

NUMBERS_TO_LETTERS = {
    "1" : "a",
    "2" : "b",
    "3" : "c",
    "4" : "d",
    "5" : "e",
    "6" : "f",
    "7" : "g",
    "8" : "h",
    "9" : "i",
    "0" : "j"
}
LETTERS_TO_NUMBERS = {value: key for key, value in NUMBERS_TO_LETTERS.items()}


def process_args(args: list[str]) -> str:
    if len(args) == 0:
        print("Usage: python3 translator.py <text>")
        sys.exit(1)

    input_text = " ".join(args)
    return input_text


def detect_language(text: str) -> str:
    return BRAILLE if (len(text) % 6 == 0 and "." in text) else ENGLISH


def english_to_braille(text: str) -> str:
    braille_chars = []

    next_is_number = False
    for char in text:
        validate_english_char(char, next_is_number)

        if char in NUMBER_TERMINATING_CHARS:
            next_is_number = False
        
        if char.isnumeric():
            if not next_is_number:
                braille_chars.append(ENGLISH_TO_BRAILLE[NUMBER])
                next_is_number = True
            char = NUMBERS_TO_LETTERS[char]
        elif char.isupper():
            braille_chars.append(ENGLISH_TO_BRAILLE[CAPITAL])
            char = char.lower()

        braille_chars.append(ENGLISH_TO_BRAILLE[char])

    return "".join(braille_chars)


def validate_english_char(char: str, next_is_number: bool) -> None:
    if not (char.isalnum() or char in PERMITTED_NON_ALPHANUMERIC_CHARS):
        # Invalid character
        print(INVALID_INPUT_MSG)
        sys.exit(1)
    elif next_is_number and not (char.isnumeric() or char in NUMBER_TERMINATING_CHARS):
        # Non-numeric, non-terminating character immediately following a number character
        print(INVALID_INPUT_MSG)
        sys.exit(1)


def braille_to_english(text: str) -> str:
    english_chars = []

    next_is_capital = False
    next_is_number = False
    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]
        validate_braille_char(braille_char, text[i-6:i] if i > 0 else "", i + 6 == len(text), next_is_capital, next_is_number)

        english_char = BRAILLE_TO_ENGLISH[braille_char]
        if braille_char == ENGLISH_TO_BRAILLE[CAPITAL]:
            next_is_capital = True
        elif braille_char == ENGLISH_TO_BRAILLE[NUMBER]:
            next_is_number = True
        else:
            if next_is_capital:
                english_char = english_char.upper()
                next_is_capital = False
            elif next_is_number:
                if english_char in NUMBER_TERMINATING_CHARS:
                    next_is_number = False
                else:
                    english_char = LETTERS_TO_NUMBERS[english_char]

            english_chars.append(english_char)

    return "".join(english_chars)


def validate_braille_char(char: str, prev_char: str, is_last: bool, next_is_capital: bool, next_is_number: bool) -> None:
    if char not in BRAILLE_TO_ENGLISH:
        # Invalid braille character
        print(INVALID_INPUT_MSG)
        sys.exit(1)

    english_char = BRAILLE_TO_ENGLISH[char]
    if is_last and english_char in PERMITTED_MODIFIERS:
        # Capital or number character as the last character
        print(INVALID_INPUT_MSG)
        sys.exit(1)
    elif next_is_capital and english_char in PERMITTED_NON_ALPHANUMERIC_CHARS:
        # Non-alphanumeric character after a capital character
        print(INVALID_INPUT_MSG)
        sys.exit(1)
    elif next_is_number and english_char not in LETTERS_TO_NUMBERS and not english_char in NUMBER_TERMINATING_CHARS:
        # Non-numeric, non-terminating character where a numeric or number-terminating character is expected
        print(INVALID_INPUT_MSG)
        sys.exit(1)
    elif prev_char == ENGLISH_TO_BRAILLE[NUMBER] and english_char in NUMBER_TERMINATING_CHARS:
        # Number character immediately followed by a number-terminating character
        print(INVALID_INPUT_MSG)
        sys.exit(1)
    

if __name__ == "__main__":
    args = sys.argv[1:]

    input_text = process_args(args)
    if detect_language(input_text) == BRAILLE:
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))