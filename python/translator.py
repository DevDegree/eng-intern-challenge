import sys

ENGLISH_TO_BRAILLE = {"a": "O.....",
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
                      " ": "......"}
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
    "......": " "
}
BRAILLE_TO_NUMBERS = {"O.....": "1",
                      "O.O...": "2",
                      "OO....": "3",
                      "OO.O..": "4",
                      "O..O..": "5",
                      "OOO...": "6",
                      "OOOO..": "7",
                      "O.OO..": "8",
                      ".OO...": "9",
                      ".OOO..": "0"
                      }

cmdInput = " ".join(sys.argv[1:])

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

def isBraille(input):
    brailleTest = input.replace(".", "").replace("O", "")

    return len(brailleTest) == 0 and len(input) % 6 == 0

def brailleToEnglish(input):
    output = ""
    nextNumber = False
    nextCaps = False
    for i in range(0, len(input), 6):
        char = input[i: i + 6]

        if char == CAPITAL_FOLLOWS:
            nextCaps = True
            continue

        if char == NUMBER_FOLLOWS:
            nextNumber = True
            continue

        if nextNumber:
            if char in BRAILLE_TO_NUMBERS:
                output += BRAILLE_TO_NUMBERS[char]
                continue

        eng = BRAILLE_TO_ENGLISH[char]
        if eng == " ":
            nextNumber = False
        elif nextCaps:
            eng = eng.upper()
            nextCaps = False

        output += eng

    return output


def englishToBraille(input):
    output = ""
    isNumber = False
    for char in input:
        if char in "0123456789":
            if not isNumber:
                output += NUMBER_FOLLOWS
            isNumber = True
        else:
            isNumber = False

            if char.isupper():
                output += CAPITAL_FOLLOWS
                char = char.lower()

        output += ENGLISH_TO_BRAILLE[char]

    return output

if isBraille(cmdInput):
    print(brailleToEnglish(cmdInput), end="")
else:
    print(englishToBraille(cmdInput), end="")
