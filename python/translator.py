import sys

english_to_braille_dict = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    " ": "......",
    "capitalize": ".....O", 
    "number": ".O.OOO"
}

braille_to_english_alphabet = dict((v, k) for (k, v) in english_to_braille_dict.items() if not k.isdigit())
braille_to_english_number = dict((v, k) for (k, v) in english_to_braille_dict.items() if k.isdigit())
braille_to_english_number["......"] = " "

def braille_to_english(str) -> str:
  english = ""
  get_numbers = False
  capitalize = False
  for i in range(0, len(str), 6):
    braille = str[i:i+6]
    if (not get_numbers):
      action = braille_to_english_alphabet[braille]
    else:
      action = braille_to_english_number[braille]
    
    if action == " ":
      english += action
      get_numbers = False
    elif action == "capitalize":
      capitalize = True
    elif action == "number":
      get_numbers = True
    elif capitalize:
      english += action.upper()
      capitalize = False
    else:
      english += action
  return english

def english_to_braille(str) -> str:
  braille = ""
  get_numbers = False
  for c in str:
    if c.isupper():
      braille += english_to_braille_dict['capitalize']
      c = c.lower()
    if c.isdigit() and not get_numbers:
      braille += english_to_braille_dict['number']
      get_numbers = True
    elif not c.isdigit():
      get_numbers = False
    braille += english_to_braille_dict[c]
    
  return braille

def is_braille(str):
  # check if all characters in str are consist of O and .
  for c in str:
    if c not in 'O.':
      return False
  return True


input = " ".join(sys.argv[1:])
if (is_braille(input)):
  print(braille_to_english(input))
else:
  print(english_to_braille(input))
