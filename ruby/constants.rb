CAPITAL_FOLLOWS = '.....O'.freeze
NUMBERS_FOLLOW = '.O.OOO'.freeze

ALPHABET_BRAILLE_MAP = {
  "a": 'O.....',
  "b": 'O.O...',
  "c": 'OO....',
  "d": 'OO.O..',
  "e": 'O..O..',
  "f": 'OOO...',
  "g": 'OOOO..',
  "h": 'O.OO..',
  "i": '.OO...',
  "j": '.OOO..',
  "k": 'O...O.',
  "l": 'O.O.O.',
  "m": 'OO..O.',
  "n": 'OO.OO.',
  "o": 'O..OO.',
  "p": 'OOO.O.',
  "q": 'OOOOO.',
  "r": 'O.OOO.',
  "s": '.OO.O.',
  "t": '.OOOO.',
  "u": 'O...OO',
  "v": 'O.O.OO',
  "w": '.OOO.O',
  "x": 'OO..OO',
  "y": 'OO.OOO',
  "z": 'O..OOO',
  " ": '......'
}.freeze
NUMBERS_BRAILLE_MAP = {
  "1": 'O.....',
  "2": 'O.O...',
  "3": 'OO....',
  "4": 'OO.O..',
  "5": 'O..O..',
  "6": 'OOO...',
  "7": 'OOOO..',
  "8": 'O.OO..',
  "9": '.OO...',
  '0': '.OOO..'
}.freeze

BRAILLE_ALPHABET_MAP = ALPHABET_BRAILLE_MAP.invert.freeze
BRAILLE_NUMBERS_MAP = NUMBERS_BRAILLE_MAP.invert.freeze
