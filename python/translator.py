from enum import Enum

class BrailleType(Enum):
  LOWER_CASE = 0
  UPPER_CASE = 1
  NUMBER = 2

LETTER_BRAILLE_MAP = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OOO...': 'd', 'O..O..': 'e',
  'OOOO..': 'f', 'OOOOO.': 'g', 'O.OO..': 'h', '.OOO..': 'i', '.OOOO.': 'j',
  'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OOO.O.': 'n', 'O..OO.': 'o',
  'OOOOO.': 'p', 'OOOOOO': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOOO': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOOO.': 'w', 'OO..OO': 'x', 'OOO.OO': 'y',
  'O..OOO': 'z'
}

NUMBER_BRAILLE_MAP = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OOO...': '4', 'O..O..': '5',
  'OOOO..': '6', 'OOOOO.': '7', 'O.OO..': '8', '.OOO..': '9', '.OOOO.': '0'
}

SPECIAL_BRAILLE_MAP = {
  '......': ' ', '.O....': '.', '..O...': ',', '....O.': '?', '..OO..': '!',
  '.....O': ':', '....OO': ';', '..O.O.': '-', '....O.': '/', '.O.O..': '<',
  '.O.OOO': '>', '....OO': '(', '....OO': ')'
}

SEPARATOR_BRAILLE_MAP = {
  '.OOO.O': 'C', '.OOOO.': 'N', '..OOO.': 'D'
}


def fromBrailleToEnglish(braille) -> str:
  english = ""
  braille_status = BrailleType.LOWER_CASE
  i : int = 0
  while i < len(braille):
    current_code = braille[i:i+6]
    if current_code in SEPARATOR_BRAILLE_MAP:
      if braille_status == BrailleType.LOWER_CASE:
        if SEPARATOR_BRAILLE_MAP[current_code] == 'C':
          braille_status = BrailleType.UPPER_CASE
        elif SEPARATOR_BRAILLE_MAP[current_code] == 'N':
          braille_status = BrailleType.NUMBER
        i += 6
      else:
        raise Exception("Invalid Braille")
    else:
      if braille_status == BrailleType.LOWER_CASE:
        if current_code in SPECIAL_BRAILLE_MAP:
          english += SPECIAL_BRAILLE_MAP[current_code]
        elif current_code in LETTER_BRAILLE_MAP:
          english += LETTER_BRAILLE_MAP[current_code]
        else:
          raise Exception("Invalid Braille")
      elif braille_status == BrailleType.UPPER_CASE:
        if current_code in LETTER_BRAILLE_MAP:
          english += LETTER_BRAILLE_MAP[current_code].upper()
        else:
          raise Exception("Invalid Braille")
        braille_status = BrailleType.LOWER_CASE
      elif braille_status == BrailleType.NUMBER:
        while i < len(braille):
          number_code = braille[i:i+6]
          i += 6
          if number_code in NUMBER_BRAILLE_MAP:
            english += NUMBER_BRAILLE_MAP[number_code]
          elif number_code in SPECIAL_BRAILLE_MAP and SPECIAL_BRAILLE_MAP[number_code] == ' ':
            english += SPECIAL_BRAILLE_MAP[number_code]
            break
          else:
            raise Exception("Invalid Braille")
        braille_status = BrailleType.LOWER_CASE
      else:
        raise Exception("Invalid Braille")
  return english

def fromEnglishToBraille(english) -> str:
  braille = ""
  for char in english:
    braille += ENGLISH_TO_BRAILLE_MAP[char]
  return braille


def isBraille(code) -> bool:
  if len(code) & 6 == 1 and set(code[:-1]) == {"0", "."}:
    return False
  return True


def translator(code):
  if isBraille(code):
    return "Invalid input"
  else
    return ""
    

def main():
  i = input()
  result = translator(i)
  print(result)