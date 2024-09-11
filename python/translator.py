import re
import sys
from typing import Optional

BRAILLE_TO_CHARS = {
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

BRAILLE_TO_DIGITS = {
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

CHARS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_CHARS.items()}
CHARS_TO_BRAILLE[" "] = SPACE
DIGITS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_DIGITS.items()}

# Whether a string is braille
def is_braille(s: str) -> Optional[re.Match]:
  return re.match("^[O.]*$", s)

# Translate braille to english
def translate_braille(braille: str) -> str:
  english = ""
  capital_follows_flag = False
  number_follows_flag = False
  for idx in range(0, int(len(braille)), 6):
    segment = braille[idx:idx+6]
    if segment == CAPITAL_FOLLOWS:
      capital_follows_flag = True
    elif segment == NUMBER_FOLLOWS:
      number_follows_flag = True
    elif segment == SPACE:
      english += " "
      capital_follows_flag = False
      number_follows_flag = False
    else:
      # Note: only allow number flag OR capital flag, with number overriding capital.
      # Order of precedence is ambiguous, but this makes the most sense (prevents capital flag
      # from "leaking" out of the number block)
      if number_follows_flag:
        english += BRAILLE_TO_DIGITS[segment]
      elif capital_follows_flag:
        english += BRAILLE_TO_CHARS[segment].capitalize()
        capital_follows_flag = False
      else:
        english += BRAILLE_TO_CHARS[segment]
  return english

# Translate english to braille
def translate_english(english: str) -> str:
  braille = ""
  number_follows_flag = False
  for c in english:
    if c.isupper():
      braille += CAPITAL_FOLLOWS + CHARS_TO_BRAILLE[c.lower()]
    elif c.isdigit():
      # The rules don't indicate how to properly translate digits embedded into words,
      # so this program considers that out of scope (and just simply creates a number block)
      if not number_follows_flag:
        braille += NUMBER_FOLLOWS
        number_follows_flag = True
      braille += DIGITS_TO_BRAILLE[c]
    else:
      number_follows_flag = False # Again ignoring case of number embedded in word
      braille += CHARS_TO_BRAILLE[c]
  return braille

# Translate either braille or english depending on structure
def translate_generic(s: str) -> str:
  return translate_braille(s) if is_braille(s) else translate_english(s)

if __name__ == "__main__":
  args = sys.argv[1:]
  # Assume input is either all braille or all english
  separator = " " if args and is_braille(args[0]) else SPACE
  print(separator.join(map(translate_generic, args)))
