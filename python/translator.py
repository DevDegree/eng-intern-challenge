import sys

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
    " ": "......",
    "CAPITAL": ".....O",
    "NUMBER": ".O.OOO",
}

BRAILLE_TO_ENGLISH = {
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
    ".....O": "CAPITAL",
    ".O.OOO": "NUMBER",
}
BRAILLE_TO_NUMBER = {
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


def english_to_braille(english_string):
    result = []
    curr_number = False

    for char in english_string:
        if char.isdigit():
            if not curr_number:
                result.append(ENGLISH_TO_BRAILLE["NUMBER"])
                curr_number = True
            result.append(ENGLISH_TO_BRAILLE[char])
        elif char.isalpha():
            if curr_number:
                curr_number = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE["CAPITAL"])
            result.append(ENGLISH_TO_BRAILLE[char.lower()])
        elif char == " ":
            result.append(ENGLISH_TO_BRAILLE[" "])
            curr_number = False

    return "".join(result)


def braille_to_english(braille_string):
    result = []
    curr_number = False
    i = 0

    while i < len(braille_string):
        char = braille_string[i : i + 6]
        if BRAILLE_TO_ENGLISH[char] == "CAPITAL":
            i += 6
            char = braille_string[i : i + 6]
            result.append(BRAILLE_TO_ENGLISH[char].upper())
        elif BRAILLE_TO_ENGLISH[char] == "NUMBER":
            curr_number = True
        elif BRAILLE_TO_ENGLISH[char] == " ":
            result.append(" ")
            curr_number = False
        else:
            if curr_number:
                num = BRAILLE_TO_NUMBER[char]
                result.append(num)
            else:
                letter = BRAILLE_TO_ENGLISH[char]
                result.append(letter)
                curr_number = False
        i += 6

    return "".join(result)


input_string = " ".join(sys.argv[1:])

if all(char in "O." for char in input_string):
    print(braille_to_english(input_string))
else:
    print(english_to_braille(input_string))
