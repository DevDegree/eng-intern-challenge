import argparse
from typing import List

eng_to_braille = {
  'a': 'O.....',
  'b': 'O.O...',
  'c': 'OO....',
  'd': 'OO.O..',
  'e': 'O..O..',
  'f': 'OOO...',
  'g': 'OOOO..',
  'h': 'O.OO..',
  'i': '.OO...',
  'j': '.OOO..',
  'k': 'O...O.',
  'l': 'O.O.O.',
  'm': 'OO..O.',
  'n': 'OO.OO.',
  'o': 'O..OO.',
  'p': 'OOO.O.',
  'q': 'OOOOO.',
  'r': 'O.OOO.',
  's': '.OO.O.',
  't': '.OOOO.',
  'u': 'O...OO',
  'v': 'O.O.OO',
  'w': '.OOO.O',
  'x': 'OO..OO',
  'y': 'OO.OOO',
  'z': 'O..OOO',
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
  '.': '..OO.O',
  ',': '..O...',
  '?': '..O.OO',
  '!': '..OOO.',
  ':': '..OO..',
  ';': '..O.O.',
  '-': '....OO',
  '/': '.O..O.',
  '<': '.OO..O',
  '>': 'O..OO.',
  '(': 'O.O..O',
  ')': '.O.OO.',
  ' ': '......',
  'capital_follows': '.....O',
  'decimal_follows': '.O...O',
  'number_follows': '.O.OOO',
}

braille_to_eng = {}
for k, v in eng_to_braille.items():
  if v in braille_to_eng:
    braille_to_eng[v].append(k)
  else:
    braille_to_eng[v] = [k]

def translate_eng_to_braille(chars: List[str]) -> str:
  prev_char = chars[0]
  chars.pop(0)
  if prev_char.isupper():
    return eng_to_braille['capital_follows'] + eng_to_braille[prev_char.lower()]
  elif prev_char == '.':
    return eng_to_braille['decimal_follows'] + eng_to_braille[prev_char]
  elif prev_char.isnumeric():
    result = eng_to_braille['number_follows'] + eng_to_braille[prev_char]
    while chars and chars[0].isnumeric():
      result += eng_to_braille[chars[0]]
      chars.pop(0)
    return result
  else:
    return eng_to_braille[prev_char]

def translate_braille_to_eng(strings: List[str]) -> str:
  prev_braille = strings[0]
  strings.pop(0)
  if prev_braille == eng_to_braille['capital_follows']:
    char = [k for k in braille_to_eng[strings[0]] if k.isalpha()][0].upper()
    strings.pop(0)
    return char
  elif prev_braille == eng_to_braille['decimal_follows']:
    char = braille_to_eng[strings[0]][0]
    strings.pop(0)
    return char
  elif prev_braille == eng_to_braille['number_follows']:
    result = ''
    while strings and strings[0] != eng_to_braille[' ']:
      result += [k for k in braille_to_eng[strings[0]] if k.isnumeric()][0]
      strings.pop(0)
    return result
  else:
    return braille_to_eng[prev_braille][0]
  
def is_english(str: str) -> bool:
  if len(str) % 6 != 0:
    return True
  if 'O' not in str and '.' not in str:
    return True
  if 'O' in str and eng_to_braille['capital_follows'] not in str:
    return True
  if '.' in str and eng_to_braille['number_follows'] not in str:
    return True
  return False

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    prog='Braille Translator',
    description='Translate between English and Braille',
  )
  parser.add_argument(
    'string',
    help='Input String, English or Braille',
    nargs='+',
  )
  args = parser.parse_args()
  arg_str = ' '.join(args.string)

  result = ''
  args = []
  if is_english(arg_str):
    for char in arg_str:
      args.append(char)
    while args:
      result += translate_eng_to_braille(args)
  else:
    for i in range(0, len(arg_str), 6):
      args.append(arg_str[i:i+6])
    while args:
      result += translate_braille_to_eng(args)
  print(result)