#!/opt/homebrew/bin/python3.8

import sys
from typing import Optional

BRA_TO_CHA_MAP = {
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


BRA_TO_NUM_MAP = {
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

# Braille to special characters
BRA_TO_SPE_MAP = {
    "..OO.O": '.',
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....00": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    # "O..OO.": ">", # share the same pattern as o --> omit due to ambiguity
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

CHA_TO_BRA_MAP = {v: k for k, v in BRA_TO_CHA_MAP.items()}
NUM_TO_BRA_MAP = {v: k for k, v in BRA_TO_NUM_MAP.items()}
SPE_TO_BRA_MAP = {v: k for k, v in BRA_TO_SPE_MAP.items()}

# Return None upon failure
def convertToEnglish(inputStr: str) -> Optional[str]:
    l = len(inputStr)
    if l % 6 != 0:
        return None

    isNumber = False
    isUpper  = False
    res = ""
    for i in range(0, l, 6):
        section = inputStr[i:i+6] 
        if isNumber:
            if section in BRA_TO_NUM_MAP: # Convert to number
                res += BRA_TO_NUM_MAP[section]
            elif section in BRA_TO_SPE_MAP and BRA_TO_SPE_MAP[section] == " ": # turn off number mode
                res += " "
                isNumber = False
            else:
                return None
        else:
            if section in BRA_TO_CHA_MAP:
                if isUpper: # appen upper case
                    res += BRA_TO_CHA_MAP[section].upper()
                    isUpper = False
                else: # append lower case
                    res += BRA_TO_CHA_MAP[section]
            elif section in BRA_TO_SPE_MAP: # append special character
                res += BRA_TO_SPE_MAP[section]
            elif section == CAPITAL_FOLLOWS: # turn on captial mode
                isUpper = True
                isNumber = False
            elif section == NUMBER_FOLLOWS:  # turn on number mode
                isNumber = True
            else:
                return None
     
    return res

# Return empty string upon failure
def convertToBraille(inputStr: str) -> Optional[str]:
    res = ""
    isNumber = False
    for c in inputStr:
        if c.isdigit():
            if not isNumber:
                res += NUMBER_FOLLOWS
                isNumber = True
            res += NUM_TO_BRA_MAP[c]
        else:
            if c.isupper():
                res += CAPITAL_FOLLOWS
                res += CHA_TO_BRA_MAP[c.lower()]
            elif c in CHA_TO_BRA_MAP:
                res += CHA_TO_BRA_MAP[c]
            elif c in SPE_TO_BRA_MAP:
                if c == " ":
                    isNumber = False
                res += SPE_TO_BRA_MAP[c]
            else: # unsupported character
                return None
        
    return res

if __name__ == "__main__":
    # Take in arguments
    args = sys.argv
    if len(args) <= 1:
        print("Incorrect number of arguments. Requires: 2 or more.")
        exit(1)

    inputStr = ' '.join(args[1:])

    # Assume that the input string is Braille
    res = convertToEnglish(inputStr)

    # if not braille then, convert the string to Braille instead
    if res is None:
        res = convertToBraille(inputStr)

    # there's a chance that converting to braille could fail as well
    if res is not None:
        print(res)
    else:
        print("Invalid string: " + inputStr)

