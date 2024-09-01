
import sys 
from translationDict import lettersToBraille, numbersToBraille, specialSymbols

args = sys.argv
output = ""

if '.' in args[1]:
  capital = False
  numbers = False
  brailleToLetters = {v: k for k, v in lettersToBraille.items()}
  brailleToNumbers = {v: k for k, v in numbersToBraille.items()}

  for i in range(0, len(args[1]), 6):
    char = args[1][i:i+6]

    if char == specialSymbols['capital']:
      capital = True
    elif char == specialSymbols['number']:
      numbers = True
    elif char == specialSymbols['space']: 
      numbers = False
      output += " "
    else: 
      if numbers:
        output += brailleToNumbers[char]
      elif capital: 
        output += brailleToLetters[char].upper()
        capital = False
      else:
        output += brailleToLetters[char]
else:
  string = " ".join(args[1:])
  numbers = False
  
  for char in string: 
    if char == " ": 
      numbers = False
      output += specialSymbols['space']
    elif char.isnumeric():
      if not numbers:
        numbers = True
        output += specialSymbols['number'] 
      output += numbersToBraille[char]
    else: 
      if char.isupper():
        output += specialSymbols['capital']
      output += lettersToBraille[char.lower()]
  
print(output)
