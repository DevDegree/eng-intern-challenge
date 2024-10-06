import sys

alphabet = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
  'z': 'O..OOO',

  '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
  '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',

  ',': '.O....', '.': '.OO..O', '?': '..O.OO', '!': '.OO.O.', ':': '..OO..',
  ';': '..O.O.', '-': '....OO', '(': 'O.O..O', ')': 'O..OO.', '/': '.O..O.',
  '<': '.OO..O', '>': 'O..OO.', ' ': '......',
}

special = {
  'upper': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
}

def english_to_braille(text: str) -> str:
  result = []
  words = text.split(' ')
  for word in words:
    is_number = False
    is_decimal_used = False
    curr_word = []
    for char in word:
      if char == '.' and is_number and not is_decimal_used:
        curr_word.append(special['decimal'])
        is_decimal_used = True
      if char.isdigit() and not is_number:
        curr_word.append(special['number'])
        is_number = True
      if char.isupper():
        curr_word.append(special['upper'])
        char = char.lower()
      curr_word.append(alphabet[char])
    result.append(''.join(curr_word))
  return alphabet[' '].join(result)


def braille_to_english(text: str) -> str:
  if len(text) % 6 != 0:
    return
  result = []

  is_upper = False
  is_number = False
  for i in range(0, len(text), 6):
    char = text[i:i+6]
    if char == special['upper']:
      is_upper = True
    elif char == special['number']:
      is_number = True
    else:
      for english, braille in alphabet.items():
        if char == braille:
          if english == ' ':
            result.append(' ')
            is_number = False
          elif english.isalpha() and not is_number:
            if is_upper:
              result.append(english.upper())
              is_upper = False
            else:
              result.append(english)
          elif english.isdigit() and is_number:
            result.append(english)
  return ''.join(result)

def main():
  text = ' '.join(sys.argv[1:])
  if all(char in '.O' for char in text):
    print(braille_to_english(text))
  else:
    print(english_to_braille(text))

if __name__ == '__main__':
    main()