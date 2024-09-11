import sys

braille_to_alpha = {
  'O.....': 'a',
  'O.O...': 'b',
  'OO....': 'c',
  'OO.O..': 'd',
  'O..O..': 'e',
  'OOO...': 'f',
  'OOOO..': 'g',
  'O.OO..': 'h',
  '.OO...': 'i',
  '.OOO..': 'j',
  'O...O.': 'k',
  'O.O.O.': 'l',
  'OO..O.': 'm',
  'OO.OO.': 'n',
  'O..OO.': 'o',
  'OOO.O.': 'p',
  'OOOOO.': 'q',
  'O.OOO.': 'r',
  '.OO.O.': 's',
  '.OOOO.': 't',
  'O...OO': 'u',
  'O.O.OO': 'v',
  '.OOO.O': 'w',
  'OO..OO': 'x',
  'OO.OOO': 'y',
  'O..OOO': 'z',
  '......': ' '
}

braille_to_num = {
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '.OOO..': '0',
  '......': ' '
}

alphanum_to_braille = {
  '0': '.....O',
  '1': '.O.OOO',
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
  ' ': '......',
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
}

CAPITAL_BRAILLE = '.....O'
NUMBER_BRAILLE = '.O.OOO'
SPACE_BRAILLE = '......'

def translate_alphanum_to_braille(text: str) -> str:
  IS_NUMBER = False
  return_string = ''
  for c in text:
    if c.isspace() and IS_NUMBER:
      IS_NUMBER = False
    if c.isupper():
      return_string += CAPITAL_BRAILLE
    if c.isnumeric() and not IS_NUMBER:
      return_string += NUMBER_BRAILLE
      IS_NUMBER = True
    return_string += alphanum_to_braille[c.lower()]
  return return_string

def translate_braille_to_alphanum(braille: str) -> str:
  braille_char_begin = 0
  braille_char_end = 6
  braille_substring = ''
  return_string = ''
  braille_substring = braille[braille_char_begin:braille_char_end]
  IS_NUMBER = False
  while braille_char_end <= len(braille):
    print(braille_substring)
    braille_substring = braille[braille_char_begin:braille_char_end]
    if braille_substring == CAPITAL_BRAILLE:
      braille_char_begin += 6
      braille_char_end += 6
      braille_substring = braille[braille_char_begin:braille_char_end]
      return_string += braille_to_alpha[braille_substring].upper()
    elif braille_substring == NUMBER_BRAILLE and not IS_NUMBER:
      IS_NUMBER = True
      braille_char_begin += 6
      braille_char_end += 6
      braille_substring = braille[braille_char_begin:braille_char_end]
      return_string += braille_to_num[braille_substring]
    elif braille_substring == SPACE_BRAILLE:
      IS_NUMBER = False
      return_string += braille_to_alpha[braille_substring]
    elif IS_NUMBER:
      return_string += braille_to_num[braille_substring]
    else:
      return_string += braille_to_alpha[braille_substring]
    braille_char_begin += 6
    braille_char_end += 6
  return return_string

def is_braille(text: str) -> bool:
  text = text.replace('O', '').replace('.', '')
  return len(text) == 0

if __name__ == '__main__':
  arg_v = ' '.join(sys.argv[1:])
  if is_braille(arg_v):
    print(translate_braille_to_alphanum(arg_v))
  else:
    print(translate_alphanum_to_braille(arg_v))