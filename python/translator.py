
import sys 
from translationDict import lettersToBraille, numbersToBraille, specialSymbols

args = sys.argv
output = ""

if '.' in args[1]:
  capital = False
  numbers = False

  for i in range(0, len(args[1]), 6):
    char = args[i][i:i+6]

    if char == ".....O":
      capital = True
    elif char == ".O.OOO":
      numbers = True
    elif char == "......": 
      numbers = False
      output += " "
    else: 
      print("kjansd")
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
      output += numbersToBraille[char.lower()]
    else: 
      if char.isupper():
        output += specialSymbols['capital']
      output += lettersToBraille[char.lower()]
  

print(output)
