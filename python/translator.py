import argparse

braille_to_letters = {
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
    ".....O": "capital follows",
    ".O.OOO": "number follows",
    "......": "space",
}

letters_to_braille = {
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
parser.add_argument("input", nargs="+")  # "+" allows for one or more arguments
args = parser.parse_args()
original_input = " ".join(args.input)


def braille_to_text(braille):
    is_number = False
    is_capital = False
    text = ""
    for i in range(0, len(braille), 6):
        chunk = braille[i:i + 6]

        if chunk == ".....O":
            is_capital = True
        elif is_capital:
            text += braille_to_letters[chunk].upper()
            is_capital = False
        elif chunk == "......":
            text += " "
            is_number = False
        elif is_number:
            text += braille_to_numbers[chunk]
        elif chunk == ".O.OOO":
            is_number = True
        else:
            text += braille_to_letters[chunk]

    return text


def text_to_braille(text):
    braille = ''
    number_on = False
    for i in range(len(text)):
        if text[i].isnumeric():
            if number_on:
                braille += numbers_to_braille[text[i]]
            else:
                number_on = True
                braille += letters_to_braille["number follows"]
                braille += numbers_to_braille[text[i]]
        else:
            if text[i] == ' ':
                braille += letters_to_braille['space']
                number_on = False
            elif text[i].isupper():
                braille += letters_to_braille["capital follows"]
                braille += letters_to_braille[text[i].lower()]
            else:
                braille += letters_to_braille[text[i]]

    return braille


## as the text to braille does not support punctuation, as per the technical reqs, this is a sufficient check
if "." in original_input:
    print(braille_to_text(original_input))
else:
    print(text_to_braille(original_input))
