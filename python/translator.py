
import sys

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
    'z': 'O..OOO',
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
    'cf': '.....O',
    'df': '.O...O',
    'nf': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    ')': '.O.OO.',
    '(': 'O.O..O',
    ' ': '......'
}

braille_to_english = {
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
    '.....O': 'cf',
    '.O...O': 'df',
    '.O.OOO': 'nf',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.O.OO.': ')',
    'O.O..O': '(',
    '......': ' '
}
braille_to_englsh_numbers = {
    'O.....': '1',
    'O.O...': '2', 
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8', 
    '.OO...': '9', 
    '.OOO..': '0'}

def braille_to_english_translator(braille):
  # segments is used to store the 6-charachter braille segments.
  segments = []
  english = ''

  # Loop to break braille into 6-charachter segments.
  for i in range(0, len(braille), 6):
    segment = braille[i:i + 6]
    segments.append(segment)
  
  index = 0
  # Number mode is used to track if numbers are being translated.
  number_mode = False

  # Loop through segments to translate each one.
  while index < len(segments):

    # To handle capiital letters.
    if braille_to_english[segments[index]] == 'cf':
      if index + 1 < len(segments):
          english += braille_to_english[segments[index + 1]].upper()
          index += 2 

    # To enter number mode.
    elif braille_to_english[segments[index]] == 'nf':
      number_mode = True
      index += 1
      
    # To exit number mode if a space is encountered and add charachters accordingly.
    elif number_mode:
      if braille_to_english[segments[index]] == ' ':
        numbermode = False
        english += braille_to_english[segments[index]]
      else:
        english += braille_to_english_numbers[segments[index]]
      index += 1
    
    # Normal translation.
    else:
      english += braille_to_english[segments[index]]
      index += 1

  return english

def english_to_braille_translator(english):
  braille = ''
  number_mode = False
  for char in english:

    if char.isupper():
      braille += english_to_braille['cf']
      braille += english_to_braille[char.lower()]

    elif char.isdigit():
      if not number_mode:
        braille += english_to_braille['nf']
        number_mode = True
      braille += english_to_braille[char]

    elif char == ' ':
      braille += english_to_braille[' ']
      number_mode = False

    else:
      braille += english_to_braille[char]
  
  return braille
    
def translator(argument):
    braille_char = ['.', 'O']
    # To check whether the input(argument) is braille or english and run functions accordingly.
    if all(char in braille_char for char in argument) and len(argument) >= 6:
        return braille_to_english_translator(argument) 
    else:
        return english_to_braille_translator(argument)
    
if __name__ == '__main__':
  argument = ' '.join(sys.argv[1:])
  result = translator(argument)
  print(result)
  