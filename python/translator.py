import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
}

braille_numbers = {
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', '.': '..OO.O'
}

def main():
  if len(sys.argv) >= 2:
    input_text = ' '.join(sys.argv[1:])
    if all(char in {'O', '.'} for char in input_text):
      braille_chars = [input_text[i:i+6] for i in range(0, len(input_text), 6)]
      print(braille_to_english(braille_chars))
    else:
      words = input_text.split(' ')
      print(english_to_braille(words))
  else:
    print("Usage: python translator.py <text-to-translate>")

def braille_to_english(braille_array):
  translated = []
  i = 0
  while i < len(braille_array):
    if braille_array[i] == '.O.OOO':
      i += 1
      while i < len(braille_array) and not check_space(braille_array[i], translated):
        translated.append(match_char_braille_to_english(braille_array[i], braille_numbers))
        i += 1
    elif braille_array[i] == '.....O':
      i += 1
      if i < len(braille_array):
        translated.append(match_char_braille_to_english(braille_array[i], braille_alphabet).upper())
    elif not check_space(braille_array[i], translated):
      translated.append(match_char_braille_to_english(braille_array[i], braille_alphabet))
    i += 1
  return ''.join(translated)

def english_to_braille(text_array):
  translated = []
  for text in text_array:
    if not text:
      continue
    if text[0].isdigit():
      translated.append('.O.OOO')
      for char in text:
        translated.append(match_char_english_to_braille(char, braille_numbers))
    else:
      for char in text:
        if char.isupper():
          translated.append('.....O')
        translated.append(match_char_english_to_braille(char.lower(), braille_alphabet))
    if text_array.index(text) != len(text_array) - 1: 
      translated.append('......')
  return ''.join(translated)

def check_space(char, input_array):
  if char == '......':
    input_array.append(' ')
    return True
  return False

def match_char_braille_to_english(char, dict_chars):
  for key, value in dict_chars.items():
    if char == value:
      return key
  return ''

def match_char_english_to_braille(char, dict_chars):
  for key, value in dict_chars.items():
    if char == key:
      return value
  return ''

main()

