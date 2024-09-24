import sys

CAP_FOLLOWS = ".....O"
NUM_FOLLOWS = ".O.OOO"
ETBDict = {
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
}

BTEDict = {
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

BTENumDict = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
}


def isBraille(string: str) -> bool:
    """Returns True if string appears to be a valid braille string, i.e. consists only of characters in {., O} and is a multiple of 6 chars long.

    Args:
        string (str): _description_

    Returns:
        bool: True if string is a valid braille string, False otherwise.
    """
    return all(char in {'.', 'O'} for char in str) and (len(str) % 6 == 0)


def englishToBraille(string: str) -> str:
    r_string = ""
    for i in range(0, len(string)):
        char = string[i]
        if char.isupper():
            r_string += CAP_FOLLOWS + ETBDict[char.lower()]
        elif char.isnumeric():
            if i==0 or string[i-1].isalpha() or string[i-1] == " ":
                r_string += NUM_FOLLOWS
            r_string += ETBDict[char]
        else:
            r_string += ETBDict[char]
    return r_string


def brailleToEnglish(string: str) -> str:
    r_string = ""
    i = 0
    cap = False
    num = False
    try:
        for i in range(0, len(string), 6):
            braille = string[i : i + 6]
            if num == True:
                r_string += BTENumDict[braille]
            elif cap == True:
                r_string += BTEDict[braille].upper()
                cap = False
            elif braille == "......":
                r_string += " "
                num = False
                continue
            elif braille == CAP_FOLLOWS:
                cap = True
                continue
            elif braille == NUM_FOLLOWS:
                num = True
                continue
            else:
                r_string += BTEDict[braille]
        return r_string
    except:
        print("Invalid braille!")

string = " ".join(sys.argv[1:])
if string.replace(" ", "").isalnum():
    print(englishToBraille(string))
elif isBraille(string):
    print(brailleToEnglish(string))
else:
    print("There's a problem with the input: " + string)
