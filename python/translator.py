import sys

# Define a dictionary that maps the English alphabets and numbers to Braille 
ENGNUM_TO_BRAILLE = {
  'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
  'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
  'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
  'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
  'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
  'z': "O..OOO", ' ': "......", 'capital': ".....O", 'number': ".O.OOO",
  '0': ".OOOO.", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
  '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO..."
}

BRAILLE_TO_NUMS = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
  'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
# Reverse the dictionary to map Braille to English alphabets and numbers
BRAILLE_TO_ENG = {v: k for k, v in ENGNUM_TO_BRAILLE.items() if not k.isdigit()}

# check if input is in Braille - input should be empty when all occurences of '0' and'.' are removed (i.e. replaced with '')
def is_braille(input):
  return input.replace('O', '').replace('.', '') == ''

# translate English/numbers to Braille
def engnum_to_braille(eng_input):
  braille_output = ''
  is_number = False
  for char in eng_input:
    if char.isupper():
      braille_output += ENGNUM_TO_BRAILLE['capital']
      char = char.lower()
    if char.isdigit():
      if not is_number:
        braille_output += ENGNUM_TO_BRAILLE['number']
        is_number = True
      braille_output += ENGNUM_TO_BRAILLE[char]
    else:
      is_number = False
      braille_output += ENGNUM_TO_BRAILLE.get(char, '......')
  return braille_output

# translate Braille to English/numbers
def braille_to_engnum(braille_input):
  eng_output = ''
  index = 0
  is_capital = False
  is_number = False
  while index < len(braille_input):
    symbol = braille_input[index:index+6]
    if symbol == ENGNUM_TO_BRAILLE['capital']:
      is_capital = True
      index += 6
      continue
    if symbol == ENGNUM_TO_BRAILLE['number']:
      is_number = True
      index += 6
      continue
    if symbol == ENGNUM_TO_BRAILLE[' ']:
      eng_output += ' '
      is_number = False 
      is_capital = False
      index += 6
      continue
    
    if is_number:
      char = BRAILLE_TO_NUMS[symbol]
    else:
      char = BRAILLE_TO_ENG[symbol]
      if is_capital:
        char = char.upper()
        is_capital = False
    eng_output += char
    index += 6
    
  return eng_output

def main():
  input = ' '.join(sys.argv[1:])
  if is_braille(input):
    print(braille_to_engnum(input))
  else:
    print(engnum_to_braille(input))

if __name__ == "__main__":
  main()
