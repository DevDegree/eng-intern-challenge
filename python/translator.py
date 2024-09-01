import sys 
from translationDict import LETTERS_TO_BRAILLE, NUMBERS_TO_BRAILLE, SPECIAL_SYMBOLS

BRAILLE_TO_LETTERS = {v: k for k, v in LETTERS_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

# If braille, the string length will be multiple of 6 and only contain '.' and 'O'
def isBraille(str):
  if len(str) % 6 != 0: 
    return False

  for char in str:
    if char != '.' and char != 'O':
      return False
    
  return True

def convertBrailleToEnglish(str):
  output = ""
  capital = False
  numbers = False

  for i in range(0, len(str), 6):
    char = str[i:i+6]

    if char == SPECIAL_SYMBOLS['capital']:
      capital = True
    elif char == SPECIAL_SYMBOLS['number']:
      numbers = True
    elif char == SPECIAL_SYMBOLS['space']: 
      numbers = False
      output += " "
    else: 
      if numbers:
        output += BRAILLE_TO_NUMBERS[char]
      elif capital: 
        output += BRAILLE_TO_LETTERS[char].upper()
        capital = False
      else:
        output += BRAILLE_TO_LETTERS[char]
  
  return output

def convertEnglishToBraille(str):
  output = ""
  numbers = False
  
  for char in str: 
    if char == " ": 
      numbers = False
      output += SPECIAL_SYMBOLS['space']
    elif char.isnumeric():
      if not numbers:
        numbers = True
        output += SPECIAL_SYMBOLS['number'] 
      output += NUMBERS_TO_BRAILLE[char]
    else: 
      if char.isupper():
        output += SPECIAL_SYMBOLS['capital']
      output += LETTERS_TO_BRAILLE[char.lower()]

  return output

# Check if input string is actually provided
if len(sys.argv) <= 1:
  print("Please provide an input string to be translated.")
  sys.exit()

string = " ".join(sys.argv[1:])

if isBraille(string):
  translation = convertBrailleToEnglish(string)
else:
  translation = convertEnglishToBraille(string)

print(translation)