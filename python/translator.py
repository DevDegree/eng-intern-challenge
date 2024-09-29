import sys
import re

BRAILLE_CHAR_LENGTH = 6


def translate_braille(text):

  braille_dict = {
    'O.....': 'A',
    'O.O...': 'B',
    'OO....': 'C',
    'OO.O..': 'D',
    'O..O..': 'E',
    'OOO...': 'F',
    'OOOO..': 'G',
    'O.OO..': 'H',
    '.OO...': 'I',
    '.OOO..': 'J',
    'O...O.': 'K',
    'O.O.O.': 'L',
    'OO..O.': 'M',
    'OO.OO.': 'N',
    'O..OO.': 'O',
    'OOO.O.': 'P',
    'OOOOO.': 'Q',
    'O.OOO.': 'R',
    '.OO.O.': 'S',
    '.OOOO.': 'T',
    'O...OO': 'U',
    'O.O.OO': 'V',
    '.OOO.O': 'W',
    'OO..OO': 'X',
    'OO.OOO': 'Y',
    'O..OOO': 'Z',
    '.....O': 'capital_follow',
    '.O.OOO': 'number_follow',
    '......': ' '
  }

  braille_numbers_dict = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
  }

  result = ""
  is_number = False
  is_capital = False

  text = text[0]

  for i in range(0, len(text), BRAILLE_CHAR_LENGTH):
    code = text[i:i+BRAILLE_CHAR_LENGTH]
    trans = braille_dict[code]
    if trans == "number_follow":
      is_number = True
    elif trans == "capital_follow":
      is_capital = True
      is_number = False
    elif is_capital:
      result += trans
      is_capital = False
    elif is_number and trans != " ":
      trans = braille_numbers_dict[code]
      result += trans
    else:
      result+= trans.lower()

    if trans == " ":
      is_number = False

  return result

def translate_english(text):

  english_dict = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'capital_follow': '.....O',
    'number_follow': '.O.OOO',
    ' ': '......'
  }
  
  result = ""
  is_number = False

  for word in text:
    for char in word:
      if char.isdigit() and not is_number:
        result += english_dict['number_follow']
        is_number = True
      elif char.isupper():
        result += english_dict['capital_follow']
      result+= english_dict[char.upper()]
    is_number = False
    result+= english_dict[" "]

  result = result[:-6] # remove extra space
  return result

def is_braille(l):
  return len(l) == 1 and bool(re.fullmatch(r'^[.O]+$', l[0]))

if __name__ == "__main__":

  input_args = sys.argv[1:]
  if is_braille(input_args):
    print(translate_braille(input_args))
  else:
    print(translate_english(input_args))