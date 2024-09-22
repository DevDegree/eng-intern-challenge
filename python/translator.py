import sys
from itertools import islice

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
    ".....O": "capital_follows",
    ".O...O": "decimal_follows",
    ".O.OOO": "number_follows",
    "......": " ",
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
    ".OOO..": "0",
}

braille_to_english_special = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
}


def is_braille(input):
    return all(i in "O." for i in input)


def translate(input):

    if is_braille(input):
        n = 6
        symbols = [input[i : i + n] for i in range(0, len(input), n)]
        word = ""
        special_char = ".,?!:;-/<>()"
        count = -1
        num_found = False
        for i, s in enumerate(symbols):
            if num_found and count != 0:
                count -= 1
                continue

            count = -1
            num_found = False

            if braille_to_english[s] == "capital_follows":
                continue
            elif braille_to_english[s] == "number_follows":
                continue

            prev_symbol = braille_to_english[symbols[i - 1]]
            if prev_symbol == "capital_follows":
                word += braille_to_english[symbols[i]]
            elif prev_symbol == "number_follows":
                while s != "......":
                    word += braille_to_numbers[symbols[i]]
                    i += 1
                    if i >= len(symbols):
                        return word
                    s = symbols[i]
                    count += 1
                num_found = True
            else:
                letter_or_symbol = braille_to_english[s]
                if letter_or_symbol.isalpha():
                    letter_or_symbol = letter_or_symbol.lower()
                    word += letter_or_symbol
                elif letter_or_symbol in special_char:
                    word += braille_to_english_special[symbols[i]]
                else:
                    word += braille_to_english[symbols[i]]
        return word
    else:
        word = ""
        num_found = False
        count_num = -1
        for i, c in enumerate(input):
            if num_found and count_num != 0:
                count_num -= 1
                continue
            count_num = -1
            num_found = False

            if c.isupper():
                word += english_to_braille_special["capital_follows"]
                word += english_to_braille[c]
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
                    count_num += 1
                num_found = True
            else:
                word += english_to_braille[c]
        return word


def main():

    if len(sys.argv) < 2:
        print("Usage: python translator.py <input>")
        return

    input = " ".join(sys.argv[1:])
    print(translate(input))


if __name__ == "__main__":
    main()
