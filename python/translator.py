import argparse

englishToBraille = {
    # Letters a to z
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
    
    # Digits 0-9 (use number marker before digits)
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
    
    # Special characters
    ' ': '......',     # Space
    
    # Markers
    'capital': '.....O',  # Capitalization marker
    'number': '.O.OOO',   # Number marker
}

brailleToEnglish = {
    # Letters a to z
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
    
    # Digits 0-9 (after a number marker)
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
    
    # Special characters
    '......': ' ',     # Space
    
    # Markers
    '.....O': 'capital',  # Capitalization marker
    '.O.OOO': 'number',   # Number marker
}

# function Braille to English translator
def brailleToEnglish_function(braille_string):
  english_output = []
  i = 0

  while i < len(braille_string):
    # each braille character uses 6 dots to represent one character 2*3 (2 column and 3 rows)
    symbol = braille_string[i:i+6]

    # check if capital follows after symbol
    if symbol == ".....O":
      # next character is converted to capital
      next_symbol = braille_string[i+6:i+12]
      english_output.append(brailleToEnglish[next_symbol].upper())
      i += 12
    
    # check if number follows after symbol
    elif symbol == ".O.OOO":
      i += 6

      while i < len(braille_string) and braille_string[i:i+6] != "......":
        num_symbol = braille_string[i:i+6]
        english_output.append(brailleToEnglish[num_symbol])
        i += 6
    
    # normal letters / space
    else:
      english_output.append(brailleToEnglish.get(symbol, '?')) #Cannot find symbol
      i += 6
  return ''.join(english_output)

# function English to Braille translator
def englishToBraille_function(english_string):
  braille_output = []

  for char in english_string:
    if char.isupper():
      braille_output.append(englishToBraille['capital'])
      braille_output.append(englishToBraille[char.lower()])
    elif char.isdigit():
      braille_output.append(englishToBraille['number'])
      braille_output.append(englishToBraille[char])
    elif char == " ":
      braille_output.append("......")
    else:
      braille_output.append(englishToBraille.get(char.lower(), '......'))
  return ''.join(braille_output)

# checking input type taking from command is it Braille or English words
def if_braille(input_sentence):
  return all(c in 'O. ' for c in input_sentence)

# based on input_sentence call translator function
def translate_input(input_sentence):
  if if_braille(input_sentence):
    return brailleToEnglish_function(input_sentence)
  else:
    return englishToBraille_function(input_sentence)

# To implement command line argument
if __name__=="__main__":
  parser = argparse.ArgumentParser(description='Braille to English and English to Braille translator')
  parser.add_argument('text', help='Text to be traslated - Braille and English')
  args = parser.parse_args()

  input_text = ' '.join(args.text)
  output = translate_input(args.text)
  print(output)
