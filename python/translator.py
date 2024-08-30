import sys

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
DECIMAL_FOLLOWS = '.O...O'
SPACE = '......'
BRAILLE_STRING_LENGTH = 6

BRAILLE_TO_ENGLISH = {
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

BRAILLE_TO_NUMBERS = {
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '.OOO..': '0'
}

# The use of these is not mentioned in the README under `Technical Requirements` - `Braille Alphabet`
# so assuming they will not be used (along with the DECIMAL_FOLLOWS special string)
# braille_to_punctuation = {
#   '..OO.O': '.',
#   '..O...': ',',
#   '..O.OO': '?',
#   '..OOO.': '!',
#   '..OO..': ':',
#   '..O.O.': ';',
#   '....OO': '-',
#   '.O..O.': '/',
#   '.OO..O': '<',
#   'O..OO.': '>',
#   'O.O..O': '(',
#   '.O.OO.': ')',
# }

# Reversing the dictionaries to be used for english/number to Braille
english_to_braille = {value: key for key, value in BRAILLE_TO_ENGLISH.items()}
numbers_to_braille = {value: key for key, value in BRAILLE_TO_NUMBERS.items()}


def is_braille(input_string):
  return all(char in 'O. ' for char in input_string) and len(input_string) % BRAILLE_STRING_LENGTH == 0


def braille_to_text(braille_str):
  chunks = [braille_str[i : i + BRAILLE_STRING_LENGTH] for i in range(0, len(braille_str), BRAILLE_STRING_LENGTH)]
  
  translated_text = []
  capitalize_next = False
  number_mode = False
  
  for chunk in chunks:
    if chunk == CAPITAL_FOLLOWS:
      capitalize_next = True
      continue
    elif chunk == NUMBER_FOLLOWS:
      number_mode = True
      continue
    elif chunk == SPACE:
      translated_text.append(' ')
      number_mode = False
      continue
    
    if number_mode:
      char = BRAILLE_TO_NUMBERS[chunk]
    else:
      char = BRAILLE_TO_ENGLISH[chunk]

    if capitalize_next:
      char = char.upper()
      capitalize_next = False

    translated_text.append(char)
  
  return ''.join(translated_text)


def text_to_braille(text_str):
  braille_text = []
  number_mode = False

  for char in text_str:
    if char == ' ':
      braille_text.append(SPACE)
      number_mode = False
      continue
    
    if char.isupper():
      braille_text.append(CAPITAL_FOLLOWS)
      braille_text.append(english_to_braille[char.lower()])
    elif char.isnumeric():
      if not number_mode:
        braille_text.append(NUMBER_FOLLOWS)
        number_mode = True
      braille_text.append(numbers_to_braille[char])
    else:
      braille_text.append(english_to_braille[char.lower()])

  return ''.join(braille_text)


def main():
  input_string = " ".join(sys.argv[1:])

  if is_braille(input_string):
    print(braille_to_text(input_string))
  else:
    print(text_to_braille(input_string))

if __name__ == "__main__":
    main()