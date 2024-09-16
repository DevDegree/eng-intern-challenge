
import sys

alphabet = {
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

braille_alphabet = {
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
braille_alphabet_numbers = {
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

def braille_translator(braille):
  segments = []
  string = ''
  for i in range(0, len(braille), 6):
    segment = braille[i:i + 6]
    segments.append(segment)
  
  index = 0
  numbermode = False
  while index < len(segments):
    if braille_alphabet[segments[index]] == 'cf':
      if index + 1 < len(segments):
          string += braille_alphabet[segments[index + 1]].upper()
          index += 2 

    elif braille_alphabet[segments[index]] == 'nf':
      numbermode = True
      index += 1
      
    elif numbermode:
      if braille_alphabet[segments[index]] == ' ':
        numbermode = False
        string += braille_alphabet[segments[index]]
      else:
        string += braille_alphabet_numbers[segments[index]]
      index += 1
    else:
      string += braille_alphabet[segments[index]]
      index += 1

  return string

def string_translator(string):
  braille = ''
  first_number = False
  for char in string:

    if char.isupper():
      braille += alphabet['cf']
      braille += alphabet[char.lower()]

    elif char.isdigit():
      if not first_number:
        braille += alphabet['nf']
        first_number = True
      braille += alphabet[char]

    elif char == ' ':
      braille += alphabet[' ']
      first_number = False

    else:
      braille += alphabet[char]
  
  return braille
    
def translator(argument):
    braille_char = ['.', 'O']
    if all(char in braille_char for char in argument) and len(argument) >= 6:
        return braille_translator(argument) 
    else:
        return string_translator(argument)
    
if __name__ == '__main__':
  argument = ' '.join(sys.argv[1:])
  result = translator(argument)
  print(result)
  