import sys
from typing import Dict, List

ENGLISH_TO_BRAILLE_MAP: Dict[str, str] = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    "CAPITAL": ".....O",
    "DECIMAL": ".O...O",
    "NUMBER": ".O.OOO",
}

BRAILLE_TO_ENGLISH_MAP: Dict[str, str] = {
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

BRAILLE_TO_ENGLISH_COMMANDS_MAP: Dict[str, str] = {
    ".....O": "CAPITAL",
    ".O...O": "DECIMAL",
    ".O.OOO": "NUMBER",
}

BRAILLE_TO_ENGLISH_NUMBERS_MAP: Dict[str, str] = {
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

BRAILLE_SIZE = 6
BRAILLE_CHARS = {".", "O"}


def english_to_braille(input: str) -> str:
    translation = []

    for i in range(len(input)):
        char = input[i]

        if char.isalpha():
            if char.isupper():
                capital = ENGLISH_TO_BRAILLE_MAP["CAPITAL"]
                translation.append(capital)
                char = char.lower()
            braille = ENGLISH_TO_BRAILLE_MAP[char]
            translation.append(braille)

        elif char.isnumeric():
            if i == 0 or not input[i - 1].isnumeric():
                number = ENGLISH_TO_BRAILLE_MAP["NUMBER"]
                translation.append(number)
            braille = ENGLISH_TO_BRAILLE_MAP[char]
            translation.append(braille)

        elif char in ENGLISH_TO_BRAILLE_MAP:
            remain = ENGLISH_TO_BRAILLE_MAP[char]
            translation.append(remain)

    return "".join(translation)


def braille_to_chunks(input: str) -> str:
    chunks = []
    for i in range(len(input) // BRAILLE_SIZE):
        chunk_start = i * BRAILLE_SIZE
        chunk_end = i * BRAILLE_SIZE + BRAILLE_SIZE
        chunk = input[chunk_start:chunk_end]
        chunks.append(chunk)
    return chunks


def braille_to_english(input: str) -> str:
    translations = []
    chunks = braille_to_chunks(input)

    is_capital = False
    is_number = False
    for braille in chunks:
        # skip translation for commands
        if braille in BRAILLE_TO_ENGLISH_COMMANDS_MAP:
            command = BRAILLE_TO_ENGLISH_COMMANDS_MAP[braille]
            if command == "CAPITAL":
                is_capital = True
            if command == "NUMBER":
                is_number = True
            continue

        # translate to numbers until the next space
        if braille == BRAILLE_TO_ENGLISH_MAP[" "]:
            is_number = False

        english = ""
        if is_number:
            english = BRAILLE_TO_ENGLISH_NUMBERS_MAP[braille]
        else:
            english = BRAILLE_TO_ENGLISH_MAP[braille]
            if is_capital:
                english = english.upper()
                is_capital = False
        translations.append(english)

    return "".join(translations)


def is_input_braille(input: str) -> bool:
    for char in input:
        if char not in BRAILLE_CHARS:
            return False
    return True


def main(argv: List[str]):
    inputs = argv[1:]
    input = " ".join(inputs)

    if is_input_braille(input):
        sys.stdout.write(braille_to_english(input))
    else:
        sys.stdout.write(english_to_braille(input))


if __name__ == "__main__":
    main(sys.argv)
