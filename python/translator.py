import sys

# define dictionaries to store the mappings

english_to_braille = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".O.O.O",
    ">:": "O.O.O.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

english_to_braille_special = {
    "capital_follows": ".....O",
    "decimal_follows": ".O...O",
    "number_follows": ".O.OOO",
}

braille_to_english = {
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
    ".....O": "capital_follows",
    ".O...O": "decimal_follows",
    ".O.OOO": "number_follows",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".O.O.O": "<",
    "O.O.O.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
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
    "0": ".OOO..",
}


# function to determine input type
# def is_english(input):
#     input = input.upper()
#     return all(i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,?!:;-/<>()" for i in input)


def is_braille(input):
    return all(i in "O." for i in input)


# function to translate input
def translate(input):

    if is_braille(input):
        word = ""
        for c in input:
            word += braille_to_english[c]
        return word
    else:
        word = ""
        for i, c in enumerate(input):
            if c.isupper():
                word += english_to_braille_special["capital_follows"]
                while c.isupper():
                    word += english_to_braille[c]
                    i += 1
                    if i >= len(input):
                        return word
                    c = input[i]
            elif c.islower():
                c = c.upper()
                word += english_to_braille[c]
            elif c.isdigit():
                word += english_to_braille_special["number_follows"]
                while c.isdigit():
                    word += numbers_to_braille[c]
                    i += 1
                    if i >= len(input):
                        return word
                    c = input[i]
            else:
                word += english_to_braille[c]
        return word


def main():

    if len(sys.argv) < 2:
        print("Usage: python translator.py <input>")
        return

    input = " ".join(sys.argv[1:])
    if is_braille(input):
        print(translate(input))
    else:
        print(translate(input))


if __name__ == "__main__":
    main()
