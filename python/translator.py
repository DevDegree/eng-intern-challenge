import sys

# ASSUMPTIONS: Braille length is always multiple of 6, "english" matches ^[a-zA-Z0-9 ]+$, and letters will not immediately follow numbers

BRAILLE_SYMBOL_LENGTH = 6
NUMBER_INDICATOR = 'N'
CAPITAL_INDICATOR = 'C'

char_to_braille = {
    'a1': 'O.....', 'b2': 'O.O...', 'c3': 'OO....', 'd4': 'OO.O..', 'e5': 'O..O..',
    'f6': 'OOO...', 'g7': 'OOOO..', 'h8': 'O.OO..', 'i9': '.OO...', 'j0': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    ' ': '......', 
    NUMBER_INDICATOR: '.O.OOO',
    CAPITAL_INDICATOR: '.....O', 
}

braille_to_char = {v: k for k, v in char_to_braille.items()}

# Mapping between letters and digits that share a Braille symbol
digit_char_pairs = {}
for idx, key in enumerate(char_to_braille.keys()):
  if idx > 9:
    break
  digit_char_pairs[key[1]] = key[0]
  digit_char_pairs[key[0]] = key[1]

# Check whether a given string consists of only Braille symbols
def is_braille(string: str) -> bool:
  return all(b in ['.', 'O'] for b in string)

# Translate English to Braille
def english_to_braille(english: str) -> str:
  braille = ''
  is_num = False

  for char in english:
    if char.isdigit():
      if not is_num:
        is_num = True
        braille += char_to_braille['N']

      # Get letter-digit shared key
      key = digit_char_pairs[char] + char
      braille += char_to_braille[key]
    else:
      is_num = False

      if char.isupper():
        braille += char_to_braille['C']

      lower_char = char.lower()
      if lower_char in digit_char_pairs:
        # Get letter-digit shared key
        key = lower_char + digit_char_pairs[lower_char]
        braille += char_to_braille[key]
      else:
        braille += char_to_braille[lower_char]

  return braille

# Translate Braille to English
def braille_to_english(braille: str) -> str:
  english = ''
  is_num = False
  is_capital = False

  for idx in range(0, len(braille), BRAILLE_SYMBOL_LENGTH):
    symbol = braille[idx:idx+6]
    char = braille_to_char[symbol]

    if char == ' ':
      is_num = False
    
    if char == NUMBER_INDICATOR:
      is_num = True
      continue

    # Get digit or letter
    if is_num:
      char = char[1]
    else:
      char = char[0]
    
    if char == CAPITAL_INDICATOR:
      is_capital = True
      continue

    if is_capital:
      char = char.upper()
      is_capital = False

    english += str(char)

  return english

# Main function
def translate() -> None:
  input = ' '.join(sys.argv[1:])

  if is_braille(input):
    print(braille_to_english(input))
  else:
    print(english_to_braille(input))

if __name__ == "__main__":
  translate()