import sys
import re

from dictionary import BRAILLE_CAPITAL, BRAILLE_NUMBER, \
    NUMBERS_TO_BRAILLE, LETTERS_TO_BRAILLE, SYMBOLS_TO_BRAILLE, \
    BRAILLE_TO_NUMBERS, BRAILLE_TO_LETTERS, BRAILLE_TO_SYMBOLS

######################## TRANSLATION FUNCTIONS

def to_braille(input: str):
  numbers_mode = False
  ans = ""
  for c in input:
    # numbers
    if c >= '0' and c <='9':
      if not numbers_mode:
        ans += BRAILLE_NUMBER
        numbers_mode = True
      ans += NUMBERS_TO_BRAILLE[c]
    # decimal or period
    elif c == '.':
      ans += NUMBERS_TO_BRAILLE[c] if numbers_mode else SYMBOLS_TO_BRAILLE[c]
    # cap letters
    elif c >= 'A' and c <= 'Z':
      ans += BRAILLE_CAPITAL
      ans += LETTERS_TO_BRAILLE[c.lower()]
    # lowercase letters
    elif c >= 'a' and c <= 'z':
      ans += LETTERS_TO_BRAILLE[c]
    # symbols and spaces
    elif c in SYMBOLS_TO_BRAILLE:
      if c == ' ':
        numbers_mode = False
      ans += SYMBOLS_TO_BRAILLE[c]
  return ans

def to_english(input: str):
  n = 6
  ans = ""
  numbers_mode = False
  capitalize_next = False

  for i in range(0, len(input), n):
    c = input[i:i+n]
    # speial characters
    if c == BRAILLE_CAPITAL:
      capitalize_next = True
    elif c == BRAILLE_NUMBER:
      numbers_mode = True
    else:
      # non-special characters
      # numbers
      if numbers_mode:
        if c in BRAILLE_TO_NUMBERS:
          ans += BRAILLE_TO_NUMBERS[c]
          continue
        else:
          # not a valid number mode input, exit number mode, continue below
          numbers_mode = False
      
      # letters
      # letters takes precedence over symbols when the braille is both a letter and a symbol
      if c in BRAILLE_TO_LETTERS:
        letter = BRAILLE_TO_LETTERS[c]
        ans += letter.upper() if capitalize_next else letter
        capitalize_next = False
      # symbols
      elif c in BRAILLE_TO_SYMBOLS:
        ans += BRAILLE_TO_SYMBOLS[c]

  return ans

######################## DONE TRANSLATION FUNCTIONS

######################## HELPER FUNCTIONS

def is_braille(input: str) -> bool:
  num_diff_chars = len(set(input))
  only_dots = re.match("[^O.]", input) == None
  valid_length = len(input) % 6 == 0
  return only_dots and num_diff_chars==2 and valid_length

######################## DONE HELPER FUNCTIONS

if __name__ == '__main__':
  input = " ".join(sys.argv[1:])
  if is_braille(input):
    print(to_english(input))
  else:
    print(to_braille(input)) 

