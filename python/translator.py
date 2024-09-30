import sys

# Creating dictionaries for translation
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

NUMBERS_TO_BRAILLE = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}


BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {value: key for key, value in NUMBERS_TO_BRAILLE.items()}

# Special Strings
CAPITAL_FOLLOWS_STR = ".....O"
NUMBER_FOLLOWS_STR = ".O.OOO"
SPACE_STR = "......"


def is_braille(st: str) -> bool:
    """
    Check if a string is a valid braille string
    """
    return all(c in "O." for c in st)


def translate_english_to_braille(st: str) -> str:
    """
    Translate an english string to braille
    """
    braille_text = ""
    digit_mode = False
    for char in st:
        if char.isupper():
            braille_text += CAPITAL_FOLLOWS_STR
            char = char.lower()
        if char.isdigit() and not digit_mode:
            braille_text += NUMBER_FOLLOWS_STR
            digit_mode = True
        if char in ENGLISH_TO_BRAILLE:
            if digit_mode:
                braille_text += SPACE_STR
                digit_mode = False
            braille_text += ENGLISH_TO_BRAILLE[char]
        elif char in NUMBERS_TO_BRAILLE:
            braille_text += NUMBERS_TO_BRAILLE[char]
        elif char == " ":
            digit_mode = False
            braille_text += SPACE_STR
        else:
            raise ValueError(f"Invalid character: {char}")
    return braille_text


def translate_braille_to_english(st: str) -> str:
    """
    Translate a braille string to english
    """
    if len(st) % 6 != 0:
        raise ValueError("Invalid braille string. Length must be a multiple of 6")

    english_text = ""
    digit_mode = False
    capital_mode = False
    for i in range(0, len(st), 6):
        char = st[i : i + 6]
        if char == CAPITAL_FOLLOWS_STR:
            capital_mode = True
        elif char == NUMBER_FOLLOWS_STR:
            digit_mode = True
        elif char == SPACE_STR:
            english_text += " "
            digit_mode = False
        elif digit_mode:
            english_text += BRAILLE_TO_NUMBERS[char]
        else:
            if capital_mode:
                english_text += BRAILLE_TO_ENGLISH[char].upper()
                capital_mode = False
            else:
                english_text += BRAILLE_TO_ENGLISH[char]

    return english_text


def main():
    if len(sys.argv) < 2:
        raise ValueError("The input must contain a string to translate")

    # Get the input string and remove the whitespaces
    input_text = " ".join(sys.argv[1:]).strip()

    # Check if the input is braille or english
    if is_braille(sys.argv[1]):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))


if __name__ == "__main__":
    main()
