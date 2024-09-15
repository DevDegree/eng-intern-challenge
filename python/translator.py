
import sys

alphabet = {'a': '0.....',
            'b': '0.0...',
            'c': '00....',
            'd': '00.0..',
            'e': '0..0..',
            'f': '000...',
            'g': '0000..',
            'h': '0.00..',
            'i': '.00...',
            'j': '.000..',
            'k': '0...0.',
            'l': '0.0.0.',
            'm': '00..0.',
            'n': '00.00.',
            'o': '0..00.',
            'p': '000.0.',
            'q': '00000.',
            'r': '0.000.',
            's': '.00.0.',
            't': '.0000.',
            'u': '0...00',
            'v': '0.0.00',
            'w': '.000.0',
            'x': '00..00',
            'y': '00.000',
            'z': '0..000',
            '1': '0.....',
            '2': '0.0...',
            '3': '00....',
            '4': '00.0..',
            '5': '0..0..',
            '6': '000...',
            '7': '0000..',
            '8': '0.00..',
            '9': '.00...',
            '0': '.000..',
            'cf': '.....0',
            'df': '.0...0',
            'nf': '.0.000',
            '.': '..00.0',
            ',': '..0...',
            '?': '..0.00',
            '!': '..000.',
            ':': '..00..',
            ';': '..0.0.',
            '-': '....00',
            '/': '.0..0.',
            '<': '.00..0',
            '>': '0..00.',
            ')': '.0.00.',
            '(': '0.0..0',
            ' ': '......'}
braille_alphabet = {'0.....': 'a', 
                    '0.0...': 'b',
                    '00....': 'c',
                    '00.0..': 'd',
                    '0..0..': 'e',
                    '000...': 'f',
                    '0000..': 'g',
                    '0.00..': 'h',
                    '.00...': 'i',
                    '.000..': 'j',
                    '0...0.': 'k',
                    '0.0.0.': 'l',
                    '00..0.': 'm',
                    '00.00.': 'n',
                    '0..00.': 'o',
                    '000.0.': 'p',
                    '00000.': 'q',
                    '0.000.': 'r',
                    '.00.0.': 's',
                    '.0000.': 't',
                    '0...00': 'u',
                    '0.0.00': 'v',
                    '.000.0': 'w',
                    '00..00': 'x',
                    '00.000': 'y',
                    '0..000': 'z',
                    '.....0': 'cf',
                    '.0...0': 'df',
                    '.0.000': 'nf',
                    '..00.0': '.',
                    '..0...': ',',
                    '..0.00': '?',
                    '..000.': '!',
                    '..00..': ':',
                    '..0.0.': ';',
                    '....00': '-',
                    '.0..0.': '/',
                    '.0.00.': ')',
                    '0.0..0': '(',
                    '......': ' '}

def braille_translator(braille):
  segments = []
  word = ''
  for i in range(0, len(braille), 6):
    segment = braille[i:i + 6]
    word += braille_alphabet[segment]
    segments.append(segment)

  print(word)
  return

def word_translator(string):
  braille = ''
  first_number = False
  for letter in string:

    if letter.isupper():
      braille += alphabet['cf']
      braille += alphabet[letter.lower()]

    elif letter.isdigit():
      if not first_number:
        braille += alphabet['nf']
        first_number = True
      braille += alphabet[letter]

    elif letter == ' ':
      braille += alphabet[' ']
      first_number = False

    else:
      braille += alphabet[letter]
  print(string)
  print(braille)
  print(len(braille))
  return braille
    
def translator(argument):
    braille_char = ['.', '0']
    if all(letter in braille_char for letter in argument):
        return braille_translator(argument) 
    else:
        return word_translator(argument)

    
if __name__ == '__main__':
  argument = ' '.join(sys.argv[1:])
  translator(argument)