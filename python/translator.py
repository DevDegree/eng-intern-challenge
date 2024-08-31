import argparse

braille_to_letters = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z",
    ".....O": "capital follows",
    ".O.OOO": "number follows",
    "......": "space",
}

letters_to_braille = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    "space": "......",
}


braille_to_numbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "O",
}

numbers_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "O": ".OOO..",
}




parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()
original_input = args.input


def braille_to(braille):
    print(braille)


def to_braille(english):
    print(english)


if original_input.isalnum():
    to_braille(original_input)
else:
    braille_to(original_input)
