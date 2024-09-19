# initializing mappings
ENGLISH_TO_BRAILLE = {
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
    ' ': '......',
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
    'cap': '.....O',
    'num': '.O.OOO'
}

BRAILLE_TO_LETTER = {
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
    'O..OOO': 'z'
}

BRAILLE_TO_NUMBER = {
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

def translate_braille(input_string):
  result = ''
  
  if input_string[0] == '.' or input_string[0] == 'O':
    # braille to english
    
    i = 0
    chars = [input_string[j:j+6] for j in range(0, len(input_string), 6)]
    is_number_mode = False

    while i < len(chars):
      braille_char = chars[i]
      
      if braille_char == ENGLISH_TO_BRAILLE['cap']:
        # capitalize the next character
        i += 1
        next_char = BRAILLE_TO_LETTER.get(chars[i], '')
        result += next_char.upper()
      elif braille_char == ENGLISH_TO_BRAILLE['num']:
        # switch to number mode
        is_number_mode = True
      elif braille_char == '......':
        # space resets number mode
        result += ' '
        is_number_mode = False
      else:
        if is_number_mode:
          result += BRAILLE_TO_NUMBER[braille_char]
        else:
          result += BRAILLE_TO_LETTER[braille_char]
      
      i += 1
  else:
    # english to braille
    
    is_number_mode = False
    
    for char in input_string:
      if char.isupper():
        result += ENGLISH_TO_BRAILLE['cap'] + ENGLISH_TO_BRAILLE[char.lower()]
      elif char.isdigit() and not is_number_mode:
        is_number_mode = True
        result += ENGLISH_TO_BRAILLE['num'] + ENGLISH_TO_BRAILLE[char]
      elif char.isdigit():
        result += ENGLISH_TO_BRAILLE[char]
      else:
        is_number_mode = False
        result += ENGLISH_TO_BRAILLE[char]

  return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        print(translate_braille(input_string))
