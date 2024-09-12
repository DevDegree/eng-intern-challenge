import sys

braille_alpha_dict = {
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
  ' ': '......'
}

braille_num_dict = {
  '1': 'O.....',
  '2': 'O.O...',
  '3': 'OO....',
  '4': 'OO.O..',
  '5': 'O..O..',
  '6': 'OOO...',
  '7': 'OOOO..',
  '8': 'O.OO..',
  '9': '.OO...',
  '0': '.OOO..'
}

braille_sign_dict = {
    '.': 'O.O.OO',
    ',': 'O.....',
    '?': 'OO..O.',
    '!': 'OO.O.O',
    ':': 'O.OOO.',
    ';': 'O.O.O.',
    '-': 'O....O',
    '/': 'O..OO.',
    '<': 'OO.O..',
    '>': '.OO.OO',
    '(': 'OO....',
    ')': '.OOOO.'
}

braille_capital = '.....O'
braille_num = '.O.OOO'

def eng_to_braille (txt):
  braille = ""
  is_num = False

  for char in txt:
    if char == ' ':
      braille += braille_alpha_dict[char]
      is_num = False
    elif 'A' <= char <= 'Z':
      braille += braille_capital + braille_alpha_dict[char.lower()]
      is_num = False
    elif '0' <= char <= '9':
      if not is_num:
        braille += braille_num
        is_num = True
      braille += braille_num_dict[char]
    elif char in braille_sign_dict:
      braille += braille_sign_dict[char]
    else:
      braille += braille_alpha_dict[char]
      is_num = False

  return braille

def braille_to_eng(braille_txt):
  engl = ""
  is_cap = False
  is_num = False
  braille_chars = [braille_txt[i:i+6] for i in range(0, len(braille_txt), 6)]

  for char in braille_chars:
    if char == braille_capital:
      is_cap = True
    elif char == braille_num:
      is_num = True
    elif char == '......':
      engl += ' '
      is_num = False
    elif is_num:
      for num, braille in braille_num_dict.items():
        if char == braille:
          engl += num
          break
      is_num = False
    elif char in braille_sign_dict.values():  # 구두점 처리 추가
      for sign, code in braille_sign_dict.items():
        if char == code:
          engl += sign
          break
    else:
      for letter, braille in braille_alpha_dict.items():
        if char == braille:
          if is_cap:
            engl += letter.upper()
          else:
            engl += letter
          is_cap = False
          break
  return ''.join(engl)

def main():
  if len(sys.argv) != 2:
    print("Usage: python translator.py <text>")
  else:
    input_text = sys.argv[1]
    if set(input_text).issubset({'O', '.'}):
      print(braille_to_eng(input_text))
    else:
      print(eng_to_braille(input_text))

if __name__ == "__main__":
  main()
