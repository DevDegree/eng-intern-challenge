import sys

# Maps: English -> Braille
ALPHABET_TO_BRAILLE_DICT = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
  'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
  'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
  's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO'
}
NUMBER_TO_BRAILLE_DICT = {
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
  '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
SPECIAL_TO_BRAILLE_DICT = {
  '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', 
  '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
  ' ': '......'
}

# Maps: Braille -> English
BRAILLE_TO_ALPHABET_DICT = {v: k for k, v in ALPHABET_TO_BRAILLE_DICT.items()}
BRAILLE_TO_NUMBER_DICT = {v: k for k, v in NUMBER_TO_BRAILLE_DICT.items()}
BRAILLE_TO_SPECIAL_DICT = {v: k for k, v in SPECIAL_TO_BRAILLE_DICT.items()}

# Braille modifier constants
BRAILLE_CAPITAL_NEXT = '.....O'
BRAILLE_DECIMAL_NEXT = '.O...O'
BRAILLE_NUMBER_NEXT  = '.O.OOO'

# Other constant(s)
CHARS_PER_BRAILLE_CELL = 6

def text_is_braille(text: str) -> bool:
  """
  Check if the given text is Braille or English
  
  Args:
    text (str): Text to be checked

  Returns:
    bool: True if the text is Braille, False if English
  """
  for char in text:
    if char not in {'O', '.'}:
      return False

  return len(text) % CHARS_PER_BRAILLE_CELL == 0


def split_braille_into_cells(braille_text: str) -> list:
  """
  Splits braille_text string into length 6 Braille cells
  
  Args:
    braille_text (str): Braille text to be split into cells

  Returns:
    list: List of valid Braille cells
  """
  braille_cells = []

  for i in range(int(len(braille_text) / CHARS_PER_BRAILLE_CELL)):
    braille_cell = braille_text[(i * CHARS_PER_BRAILLE_CELL):((i + 1) * CHARS_PER_BRAILLE_CELL)]
    braille_cells.append(braille_cell)

  return braille_cells


def is_decimal_ahead(english_text: str, begin_index: int) -> bool:
  """
  Checks if the numeric value of the english_text starting at begin_index is
  a decimal or non-decimal number

  Args:
    english_text (str): english text to be scanned
    begin_index (int): index to start scanning english_text

  Returns:
    bool: True if the number is a decimal, False if not
  """
  for char in english_text[begin_index:]:
    if char == '.':
      return True
    elif char == ' ':
      return False
  return False


def braille_to_english(input_text: str) -> str:
  """
  Translates Braille text into corresponding English text

  Args:
    input_text (str): input Braille text

  Returns:
    str: output English text
  """
  INPUT_BRAILLE_CELLS = split_braille_into_cells(input_text)
  current_cell_index = 0
  mode = 'default'
  translated_text = ''

  while current_cell_index < len(INPUT_BRAILLE_CELLS):
    current_cell = INPUT_BRAILLE_CELLS[current_cell_index]

    if mode == 'default':
      if current_cell == BRAILLE_CAPITAL_NEXT:
        mode = 'capital'
      elif current_cell == BRAILLE_DECIMAL_NEXT:
        mode = 'decimal'
      elif current_cell == BRAILLE_NUMBER_NEXT:
        mode = 'number'
      elif current_cell in BRAILLE_TO_ALPHABET_DICT:
        translated_text += BRAILLE_TO_ALPHABET_DICT[current_cell]
      else:
        translated_text += BRAILLE_TO_SPECIAL_DICT[current_cell]
    elif mode == 'capital':
      translated_text += BRAILLE_TO_ALPHABET_DICT[current_cell].upper()
      mode = 'default'
    elif mode == 'decimal':
      if current_cell != SPECIAL_TO_BRAILLE_DICT['.']:
        translated_text += BRAILLE_TO_NUMBER_DICT[current_cell]
      else:
        translated_text += '.'
        mode = 'number'
    elif mode == 'number':
      if current_cell != SPECIAL_TO_BRAILLE_DICT[' ']:
        translated_text += BRAILLE_TO_NUMBER_DICT[current_cell]
      else:
        translated_text += ' '
        mode = 'default'
    current_cell_index += 1
  
  return translated_text


def english_to_braille(input_text: str) -> str:
  """
  Translates English text into corresponding Braille text

  Args:
    input_text (str): input English text

  Returns:
    str: output Braille text
  """
  current_char_index = 0
  mode = 'default'
  translated_text = ''

  while current_char_index < len(input_text):
    current_char = input_text[current_char_index]
    if mode == 'default':
      if current_char.isalpha():
        if current_char.isupper():
          translated_text += BRAILLE_CAPITAL_NEXT
        translated_text += ALPHABET_TO_BRAILLE_DICT[current_char.lower()]
      elif current_char == ' ':
        translated_text += SPECIAL_TO_BRAILLE_DICT[' ']
      elif current_char.isnumeric():
        is_decimal = is_decimal_ahead(input_text, current_char_index)
        translated_text += BRAILLE_DECIMAL_NEXT if is_decimal else BRAILLE_NUMBER_NEXT
        mode = 'decimal' if is_decimal else 'number'
        continue
      else:
        translated_text += SPECIAL_TO_BRAILLE_DICT[current_char]
    elif mode == 'number':
      if current_char != ' ':
        translated_text += NUMBER_TO_BRAILLE_DICT[current_char]
      else:
        translated_text += SPECIAL_TO_BRAILLE_DICT[' ']
        mode = 'default'
    elif mode == 'decimal':
      if current_char != '.':
        translated_text += NUMBER_TO_BRAILLE_DICT[current_char]
      else:
        translated_text += SPECIAL_TO_BRAILLE_DICT['.']
        mode = 'number'
    current_char_index += 1

  return translated_text


def main():
  INPUT_TEXT = ' '.join(sys.argv[1:])
  output_text = ''

  if text_is_braille(INPUT_TEXT):
    output_text = braille_to_english(INPUT_TEXT)
  else:
    output_text = english_to_braille(INPUT_TEXT)
  print(output_text)

if __name__ == "__main__":
  main()
