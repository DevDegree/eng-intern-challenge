import sys
import re

args = sys.argv[1:]
isBraille = False
if len(args) == 1 and re.search("^(O|\.)*$", args[0]):
    isBraille = True

brailleToChar = {
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
}
brailleToNum = {
    "O......": "1",
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
brailleCap = ".....O"
brailleNum = ".O.OOO"
brailleSpace = "......"
strToBraille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".O.O..",
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


def printString(input):
    res = ""
    braille = input
    isCap = False
    isNum = False
    for i in range(0, len(braille), 6):
        c = braille[i : i + 6]
        if isNum:
            res += brailleToNum[c]
        elif isCap:
            isCap = False
            res += brailleToChar[c].upper()
        elif c in brailleToChar:
            res += brailleToChar[c]
        elif c == brailleSpace:
            res += " "
            isCap = False
            isNum = False
        elif c == brailleCap:
            isCap = True
            isNum = False
        elif c == brailleNum:
            isNum = True
            isCap = False
    print(res)


def printBraille(input):
    res = ""
    isDigit = False
    for c in input:
        if c == " ":
            res += brailleSpace
            isDigit = False
            continue
        elif c.isupper():
            res += brailleCap
            c = c.lower()
        elif c.isdigit() and not isDigit:
            res += brailleNum
            isDigit = True
        res += strToBraille[c]

    print(res)


if isBraille:
    printString(args[0])
else:
    joined = " ".join(args)
    printBraille(joined)
