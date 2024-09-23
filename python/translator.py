import sys

letter_to_braille_dict = {
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
}

num_to_braille_dict = {
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

braille_to_letter_dict = {
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
}

braille_to_number_dict = {
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '.OOO..': '0',
}

def is_braille(input_language) -> bool:
  # function to check if input is braille or not
  # if all the characters are alphanumeric the string is english otherwise it is braille 
  return not input_language.replace(' ', '').isalnum()

def translate_braille(translate_string) -> str:
  # function that translates braille to english
  result_string = []
  number_follows = False
  capital_follows = False
  # each braille character is represented by a 3X2 matrix, meaning we want to jump every 6 characters in the string
  for i in range(0,len(translate_string),6):
    # we slice the string from i to i + 6 (not included) because of the 0 index
    char = translate_string[i: i + 6]
    # if the character is a space then we set number_follows as false since number follows last until a space is encountered
    if char == '......':
      number_follows = False
      result_string.append(' ')
    # if the character is not a capital follows or a number follows it is either (1) a number (2) a capital letter or (3) a lowercase letter
    elif char != '.....O' and char != '.O.OOO':
      if number_follows:
        number = braille_to_number_dict[char]
        result_string.append(number)
      else:
        letter = braille_to_letter_dict[char]
        # after we append a capital letter we change capital_follows to false since capital follows is only for the next braille symbol
        if capital_follows:
          result_string.append(letter.upper())
          capital_follows = False
        else:
          result_string.append(letter)
    # if the character is a capital follows or number follows, set the flags accordingly 
    else:
      if char == '.....O':
        capital_follows = True
      else:
        number_follows = True
  return ''.join(result_string)
           

def translate_english(translate_string) -> str:
  result_string = []
  number_follows = False
  for char in translate_string:
    if char == ' ':
      result_string.append('......')
      number_follows = False
    else:
      if char.isalpha():
        letter = letter_to_braille_dict[char.lower()]
        if char.isupper():
          result_string.append('.....O')
          result_string.append(letter)
        else:
          result_string.append(letter)
      else:
        number = num_to_braille_dict[char]
        if number_follows:
          result_string.append(number)
        else:
          result_string.append('.O.OOO')
          result_string.append(number)
          number_follows = True
  return ''.join(result_string)


def translator() -> None:
  # program to run to translate
  args = sys.argv
  translate_string = ' '.join(args[1:])
  if len(args) >= 2:
    if is_braille(translate_string):
      print(translate_braille(translate_string))
    else:
      print(translate_english(translate_string))
  else:
    print('')
  
translator()