import sys
from typing import List, Dict

ENGLISH_TO_BRAILLE: Dict[str, str] = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'capital': '.....O', 'number': '.O.OOO', 'space': '......',
}

BRAILLE_TO_ENGLISH: Dict[str, str] = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if not k.isdigit()}
BRAILLE_TO_ENGLISH_NUMBERS: Dict[str, str] = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k.isdigit()}

def translate_to_braille(text: str) -> str:
  """Translates an English text string to its Braille representation."""
  
  result: List[str] = []
  is_number: bool = False # Flag for number

  for char in text:
    if char.isdigit():
      if not is_number:
        result.append(ENGLISH_TO_BRAILLE['number'])
        is_number = True
      result.append(ENGLISH_TO_BRAILLE[char])
    elif char.isalpha():
      if char.isupper():
        result.append(ENGLISH_TO_BRAILLE['capital'])
      result.append(ENGLISH_TO_BRAILLE[char.lower()])
      is_number = False
    elif char == ' ':
      result.append(ENGLISH_TO_BRAILLE['space'])
      is_number = False
    else:
      result.append(ENGLISH_TO_BRAILLE[char])
      is_number = False
          
  return ''.join(result)

def translate_to_english(braille: str) -> str:
  """Translates a Braille string to its English representation."""
  
  result: List[str] = []
  is_capital: bool = False # Flag for next capital
  is_number: bool = False # Flag for next number

  for i in range(0, len(braille), 6):
    braille_chunk: str = braille[i:i+6]

    if braille_chunk == ENGLISH_TO_BRAILLE['capital']:
      is_capital = True
    elif braille_chunk == ENGLISH_TO_BRAILLE['number']:
      is_number = True
    elif braille_chunk == ENGLISH_TO_BRAILLE['space']:
      result.append(' ')
      is_number = False
    else:
      if is_number and braille_chunk in BRAILLE_TO_ENGLISH_NUMBERS:
        char = BRAILLE_TO_ENGLISH_NUMBERS[braille_chunk]
      else:
        char = BRAILLE_TO_ENGLISH[braille_chunk]
        if is_capital:
          char = char.upper()
          is_capital = False
      result.append(char)

  return ''.join(result)

def is_braille(text: str) -> bool:
  """Checks if the input string is in Braille format (consisting of only 'O' and '.')"""
  return all(char in ('O', '.') for char in text)

def main():
  """Main function to handle input arguments and call the appropriate translation function."""
  input_array: List[str] = sys.argv[1:]
  text: str = ' '.join(input_array)

  if is_braille(text):
    translated_text: str = translate_to_english(text)
  else:
    translated_text: str = translate_to_braille(text)
  
  print(translated_text)

if __name__ == "__main__":
  main()
