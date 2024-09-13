import sys

braille_characters = {
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
}

braille_numbers = {
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

braille_rules = {
  'capital_follows': '.....O',
  'number_follows': '.O.OOO',
}


def is_braille_input(input_text):
  return all( c in '.O' for c in input_text ) and len(input_text) % 6 == 0


def convert_text_to_braille(input_text):
  braille_text = ''
  is_number = False
  
  for c in input_text:
    if c.isupper():
      braille_text += braille_rules['capital_follows']
      c = c.lower()

    if c.isdigit():
      if not is_number:
        braille_text += braille_rules['number_follows']
        is_number = True
      braille_text += braille_numbers[c]

    elif c in braille_characters:
      braille_text += braille_characters[c]
      is_number = False

  return braille_text


def convert_braille_to_text(input_text):
  text = []
  is_number = False
  is_capital = False

  for i in range(0, len(input_text), 6):
    a_braille = input_text[i:i+6]

    if a_braille == braille_rules['number_follows']:
      is_number = True
      continue

    if a_braille == braille_rules['capital_follows']:
      is_capital = True
      continue

    if a_braille == braille_characters[' ']:
      text.append(' ')
      is_number = False
      continue

    if is_number:
      for k, v in braille_numbers.items():
        if v == a_braille:
          text.append(k)
          break
    
    else:
      for k, v in braille_characters.items():
        if v == a_braille:
          if is_capital:
            text.append(k.upper())
            is_capital = False
          else:
            text.append(k)
          break
  
  return ''.join(text)

    
if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit(1)
  
  input_text = ' '.join(sys.argv[1:])

  if is_braille_input(input_text):
    print(convert_braille_to_text(input_text))

  else:
    print(convert_text_to_braille(input_text))