import sys
import textwrap

braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OO.O', ':': '...OO.', ';': '...O..', '-': '...O.O', '/': '..O..O',
    '(': '..OO..', ')': '..OOO.', 'capital': '.....O', 'number': '.O.OOO'
}

reversed_braille_map = {
   'O.....': ['a', '1'], 'O.O...': ['b', '2'], 'OO....': ['c', '3'], 'OO.O..': ['d', '4'], 'O..O..': ['e', '5'], 
   'OOO...': ['f', '6'], 'OOOO..': ['g', '7'], 'O.OO..': ['h', '8'], '.OO...': ['i', '9'], '.OOO..': ['j', '0'], 
   'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 
   'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 
   'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
   'O..OOO': 'z', '......': ' ', '..OO.O': '!', '..O...': ',', '..O.OO': '?', 
   '...OO.': ':', '...O..': ';', '...O.O': '-', '..O..O': '/', '..OO..': '(', 
   '..OOO.': ')', '.....O': 'capital', '.O.OOO': 'number'
}

def translate_to_braille(text):
  result = []
  number_mode = False

  for char in text:
    if char.isupper():
      result.append(braille_map['capital'])
      char = char.lower()
    if char.isdigit() and number_mode == False:
      result.append(braille_map['number'])
      number_mode = True
    if char == ' ':
       number_mode = False

    result.append(braille_map.get(char, ''))
  return ''.join(result)

def translate_to_english(braille):
  result = []
  arr = textwrap.wrap(braille, 6)
  capital_mode, number_mode = False, False

  for b in arr:

    if b == '..OO.O':
       number_mode = False
    if reversed_braille_map[b] == 'capital':
       capital_mode = True
       continue
    if capital_mode:
       letter = reversed_braille_map.get(b, '')[0]
       result.append(letter.capitalize())
       capital_mode = False
       continue
    if reversed_braille_map[b] == 'number':
       number_mode = True
       continue
    if number_mode:
       number = reversed_braille_map.get(b, '')[1]
       result.append(number)
       continue

    result.append(reversed_braille_map.get(b, '')[0])

  return ''.join(result)



if __name__ == "__main__":
    input = sys.argv[1:]
    input = ' '.join(input)
    
    if 'O' in input or '.' in input:
        print(translate_to_english(input))
    else:
        print(translate_to_braille(input))
