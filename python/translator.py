import sys
# English to braille dictionary
english_to_braille = {
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
  'z': 'O..OOO'
}

# Number to braille dictionary
number_to_braille = {
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


SPACE = '......'
CAPITAL_FLAG = '.....O'
NUMBER_FLAG = '.O.OOO'

# braille to english dictionaries
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}


# Translate the string from braille to english
def translate_braille(input):
  result = ""
  is_upper = False
  is_number = False

  index = 0

  while index < len(input)/6:
    start_index = 6*index
    next_char = input[start_index:start_index + 6]

    if next_char == CAPITAL_FLAG:
      is_upper = True
    elif next_char == NUMBER_FLAG:
      is_number = True
    elif next_char == SPACE:
      is_number = False
      result += ' '
    else:
      if is_number:
        result += braille_to_number[next_char]
      elif is_upper:
        result += braille_to_english[next_char].upper()
        is_upper = False
      else:
        result += braille_to_english[next_char]
    
    index += 1

  return result


# Translate the string from english to braille
def translate_english(input):
  result = ""
  is_number = False

  for char in input:
    if char == ' ':
      is_number = False
      result += SPACE

    elif char.isdigit():
      if not is_number:
        is_number = True
        result += NUMBER_FLAG
      result += number_to_braille[char]
    
    else:
      if char.isupper():
        result += CAPITAL_FLAG
        char = char.lower()
        
      result += english_to_braille[char]

  return result


# check if the input is provided in braille
def is_braille(input):
  if len(input) % 6 != 0:
    return False

  for char in input:
    if char != 'O' and char != '.':
      return False
  return True


# Take in a string as a command line argument and translate it
def main(argv):
  input = ' '.join(str(arg) for arg in argv[1:])
  result = ""

  if is_braille(input):
    result = translate_braille(input)
  else:
    result = translate_english(input)

  print(result)


if __name__ == '__main__':
  main(sys.argv)