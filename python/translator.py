import sys

# Letter mappings in Braille
BRAILLE_ALPHABET = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
  'z': 'O..OOO', ' ': '......'
}

# Number mappings in Braille
BRAILLE_NUMBERS = {
    '1': BRAILLE_ALPHABET['a'], '2': BRAILLE_ALPHABET['b'], '3': BRAILLE_ALPHABET['c'], 
    '4': BRAILLE_ALPHABET['d'], '5': BRAILLE_ALPHABET['e'], '6': BRAILLE_ALPHABET['f'], 
    '7': BRAILLE_ALPHABET['g'], '8': BRAILLE_ALPHABET['h'], '9': BRAILLE_ALPHABET['i'], 
    '0': BRAILLE_ALPHABET['j']
}

# Capital and number follows symbols
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

BRAILLE_TO_ENGLISH = {v: k for k, v in BRAILLE_ALPHABET.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

def isBraille(inputStr: str) -> bool:
  """Check if the input string is in Braille format (contains only 'O' and '.')"""
  return all(c in 'O.' for c in inputStr)

def translateToBraille(engText: str) -> str:
  """Translate English to Braille"""
  brailleTranslation = []
  numberMode = False

  for char in engText:
    if char.isupper():
      brailleTranslation.append(CAPITAL_FOLLOWS)
      brailleTranslation.append(BRAILLE_ALPHABET[char.lower()])
      numberMode = False # Reset number mode after letters
    elif char.isdigit():
      if not numberMode:
        brailleTranslation.append(NUMBER_FOLLOWS)
        numberMode = True
      brailleTranslation.append(BRAILLE_NUMBERS[char])
    elif char == ' ':
      brailleTranslation.append(BRAILLE_ALPHABET[char])
      numberMode = False # Reset number mode after space
    else:
      brailleTranslation.append(BRAILLE_ALPHABET[char])
      numberMode = False # Reset number mode after letters
  return ''.join(brailleTranslation)

def translateToEnglish(brailleText: str) -> str:
  """Translate Braille to English"""
  engTranslation = []
  i = 0
  capitalNext, numberMode = False, False

  while i < len(brailleText):
    brailleChar = brailleText[i:i+6]

    if brailleChar == CAPITAL_FOLLOWS:
      capitalNext = True
      i += 6
      continue
    if brailleChar == NUMBER_FOLLOWS:
      numberMode = True
      i += 6
      continue
    if brailleChar == BRAILLE_ALPHABET[' ']:
      engTranslation.append(' ')
      numberMode = False # Reset number mode after a space
    else:
      if numberMode:
        char = BRAILLE_TO_NUMBERS.get(brailleChar)
      else:
        char = BRAILLE_TO_ENGLISH.get(brailleChar)
        if capitalNext:
          char = char.upper()
          capitalNext = False
      engTranslation.append(char)
    i += 6
  return ''.join(engTranslation)

def main():
  # Get the input argument from the command line
  if len(sys.argv) < 2:
    print("Please provide a string for translation.")
    return
  
  inputStr = ' '.join(sys.argv[1:])
  # Detect if it's Braille or English
  if isBraille(inputStr):
    translated = translateToEnglish(inputStr) # Translate Braille to English
  else:
    translated = translateToBraille(inputStr) # Translate English to Braille
  print(translated)

if __name__ == "__main__":
    main()

