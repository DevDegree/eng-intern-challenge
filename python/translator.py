import re
import sys
from typing import Optional

BRAILLE_TO_ABC = {
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

BRAILLE_TO_NUM = {
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

SPACE = "......"
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

ABC_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ABC.items()}
ABC_TO_BRAILLE[" "] = SPACE
NUM_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUM.items()}

# return braille-ity of a string
def is_braille(s):
  return re.match("^[O.]*$", s)

# braille -> english
def braille_to_english(braille):
    english = []
    flags = {"capital": False, "number": False}
    
    for segment in [braille[i:i+6] for i in range(0, len(braille), 6)]:
        if segment == CAPITAL_FOLLOWS:
            flags["capital"] = True
        elif segment == NUMBER_FOLLOWS:
            flags["number"] = True
        elif segment == SPACE:
            english.append(" ")
            flags = {"capital": False, "number": False}
        else:
            if flags["number"]:
                english.append(BRAILLE_TO_NUM[segment])
            elif flags["capital"]:
                english.append(BRAILLE_TO_ABC[segment].upper())
                flags["capital"] = False
            else:
                english.append(BRAILLE_TO_ABC[segment])
            
            # Reset number flag only if we've processed a character
            flags["number"] = False
    
    return "".join(english)

# english -> braille
def english_to_braille(english):
    braille = []
    number_mode = False
    
    for char in english:
        if char.isdigit():
            if not number_mode:
                braille.append(NUMBER_FOLLOWS)
                number_mode = True
            braille.append(NUM_TO_BRAILLE[char])
        else:
            number_mode = False
            if char.isupper():
                braille.append(CAPITAL_FOLLOWS)
                braille.append(ABC_TO_BRAILLE[char.lower()])
            elif char == " ":
                braille.append(SPACE)
            else:
                braille.append(ABC_TO_BRAILLE[char])
    
    return "".join(braille)

# default translator
def translator(s):
   if is_braille(s):
    return braille_to_english(s)
   else:
    return english_to_braille(s)

if __name__ == "__main__":
    args = sys.argv[1:]
    separator = " " if args and is_braille(args[0]) else SPACE
    result = separator.join(map(translator, args))
    print(result)
