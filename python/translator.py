import sys

let_to_braille = {
    "A": ".....OO.....",
    "B": ".....OO.O...",
    "C": ".....OOO....",
    "D": ".....OOO.O..",
    "E": ".....OO..O..",
    "F": ".....OOOO...",
    "G": ".....OOOOO..",
    "H": ".....OO.OO..",
    "I": ".....O.OO...",
    "J": ".....O.OOO..",
    "K": ".....OO...O.",
    "L": ".....OO.O.O.",
    "M": ".....OOO..O.",
    "N": ".....OOO.OO.",
    "O": ".....OO..OO.",
    "P": ".....OOOO.O.",
    "Q": ".....OOOOOO.",
    "R": ".....OO.OOO.",
    "S": ".....O.OO.O.",
    "T": ".....O.OOOO.",
    "U": ".....OO...OO",
    "V": ".....OO.O.OO",
    "W": ".....O.OOO.O",
    "X": ".....OOO..OO",
    "Y": ".....OOO.OOO",
    "Z": ".....OO..OOO",
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
    " ": "......",
}

num_to_braille = {
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

braille_to_let = {
    ".....OO.....": "A",
    ".....OO.O...": "B",
    ".....OOO....": "C",
    ".....OOO.O..": "D",
    ".....OO..O..": "E",
    ".....OOOO...": "F",
    ".....OOOOO..": "G",
    ".....OO.OO..": "H",
    ".....O.OO...": "I",
    ".....O.OOO..": "J",
    ".....OO...O.": "K",
    ".....OO.O.O.": "L",
    ".....OOO..O.": "M",
    ".....OOO.OO.": "N",
    ".....OO..OO.": "O",
    ".....OOOO.O.": "P",
    ".....OOOOOO.": "Q",
    ".....OO.OOO.": "R",
    ".....O.OO.O.": "S",
    ".....O.OOOO.": "T",
    ".....OO...OO": "U",
    ".....OO.O.OO": "V",
    ".....O.OOO.O": "W",
    ".....OOO..OO": "X",
    ".....OOO.OOO": "Y",
    ".....OO..OOO": "Z",
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

braille_to_num = {
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

words = sys.argv[1:]
is_braille = False

def translate():
    is_number = False
    translated = ""
    if (is_braille):
        braille_string = words[0]
        i = 0

        while i < len(braille_string):
            part = braille_string[i:i+6]
            if (part == ".....O"):
                is_number = False
                i=i+6
                part = part + braille_string[i:i+6]

            elif (part == ".O.OOO"):
                is_number = True
                i=i+6
                continue

            elif (part == "......"):
                is_number = False

            if (is_number):
                translated += braille_to_num[part]
            else:
                translated += braille_to_let[part]

            i=i+6

    else:
        for word in words:
            is_number = False
            for char in word:
                if (is_number or char.isnumeric()):
                    if (not is_number):
                        is_number = True
                        translated += ".O.OOO"
                    translated += num_to_braille[char]

                else:
                    translated += let_to_braille[char]

            if (not word == words[len(words)-1]):
                translated += "......"

    return translated

if (len(words) > 0):
    if ('.' in words[0] and 'O' in words[0]):
        is_braille = True
    print(translate())
