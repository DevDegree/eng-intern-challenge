# English to Braille mapping
# Mapped from [[1, 2], [3, 4], [5, 6]] = 123456
# OR left to right, new row, left to right, new row, left to right

english_mapping = {
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
    "O": "_.OOO..",
    "1": "_O.....",
    "2": "_O.O...",
    "3": "_OO....",
    "4": "_OO.O..",
    "5": "_O..O..",
    "6": "_OOO...",
    "7": "_OOOO..",
    "8": "_O.OO..",
    "9": "_.OO...",
    ".": "_.OOO..",
    "cap_follows": ".....O",
    "num_follows": ".O.OOO",
    " ": "......"
}

# reversed dictionary of english_mapping to serve as braille --> English
# as { braille: english}
braille_mapping = {value: key for key, value in english_mapping.items()}


def to_braille(char: str) -> str:
    """
    Converts a character to Braille

    :param char: char to convert
    :return:
    """
    # Adds num_follows braille before any numbers.
    # Converts the Os and dots to braille.
    mapped = english_mapping[char.lower()].replace("_", "")
    return mapped


def to_english(cell: str) -> str:
    """
    Converts a braille cell to English. Interpreted as left->right, new line, left->right, new line, left->right
    :param cell: 6 character cell to convert to English
    :return:
    """
    mapped = braille_mapping[cell]
    return mapped
