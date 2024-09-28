
######################## BUILD DICTIONARY 
# build braille dictionary
BRAILLE_ROOTS = [
  'O...', 'O.O.', 'OO..', 'OO.O', 'O..O', 
  'OOO.', 'OOOO', 'O.OO', '.OO.', '.OOO',
]

BRAILLE_TO_NUMBERS = {}
BRAILLE_TO_LETTERS = {}
BRAILLE_TO_SYMBOLS = {}
NUMBERS_TO_BRAILLE = {}
LETTERS_TO_BRAILLE = {}
SYMBOLS_TO_BRAILLE = {
  '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
  ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
  '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

# build basic map
for i in range(10):
  root = BRAILLE_ROOTS[i]
  LETTERS_TO_BRAILLE[chr(ord('a')+i)] = root + '..'
  LETTERS_TO_BRAILLE[chr(ord('k')+i)] = root + 'O.'
  LETTERS_TO_BRAILLE[chr(ord('u')+i)] = root + 'OO'
  NUMBERS_TO_BRAILLE[str((i+1)%10)] = root + '..'

# fix letter edge case
LETTERS_TO_BRAILLE.update({
  'w': '.OOO.O',
  'x': LETTERS_TO_BRAILLE['w'],
  'y': LETTERS_TO_BRAILLE['x'],
  'z': LETTERS_TO_BRAILLE['y']
})

# fix number edge case
NUMBERS_TO_BRAILLE['.'] = '.O...O' # decimal point

# reverse the map
BRAILLE_TO_LETTERS = {v: k for k, v in LETTERS_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}
BRAILLE_TO_SYMBOLS = {v: k for k, v in SYMBOLS_TO_BRAILLE.items()}

# reserve special characters
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'

######################## DONE BUILD DICTIONARY 
