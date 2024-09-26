import sys

char_to_braille = {
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
  "cap_follows": ".....O",
  "number_follows": ".O.OOO",
  " ": "......"
}

# generated to prevent looping through original map
braille_to_char = {v : k for k, v in char_to_braille.items()}

number_to_braille = {
  "0": ".OOO..",
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO..."
}

# generated to prevent looping through original map
braille_to_number = {v : k for k, v in number_to_braille.items()}

BRAILLE_SYMBOL_SIZE = 6

# brailleToText(braille) -> str
# converts a set of "." and "O" to valid braille
def brailleToText(braille: str) -> str:
  braille_symbols = [
    braille[i:i+BRAILLE_SYMBOL_SIZE] 
    for i in range(0, len(braille), BRAILLE_SYMBOL_SIZE)
  ]

  result = ''

  cap_lock = False
  num_lock = False

  for symbol in braille_symbols:
    char = braille_to_char[symbol]

    if char == "cap_follows":
      cap_lock = True
      continue

    if char == "number_follows":
      num_lock = True
      continue

    if cap_lock: # only one symbol cap
      char = char.upper()
      cap_lock = False
    elif num_lock: # assume numbers OR space
      if char == " ":
        num_lock = False
      else:
        char = braille_to_number[symbol]
    
    result += char

  return result

# textToBraille(str) -> str
# converts alphanumeric text to braille
def textToBraille(text: str) -> str:
  result = ''

  num_lock = False
  for char in text:
    if char == " " or char.isalpha():
      num_lock = False
      braille_symbol = char_to_braille[char.lower()]
      if char.isupper(): # capital symbol for each capital letter
        result += char_to_braille["cap_follows"]
      result += braille_symbol
    else:
      if not num_lock: # only add number symbol once
        result += char_to_braille["number_follows"]
        num_lock = True
      
      braille_symbol = number_to_braille[char]
      result += braille_symbol

  return result

# determineBraille(text) -> bool
# return true if and only if text is valid braille
def determineBraille(text: str) -> bool:
  return all(char in {'.', 'O'} for char in text)

def main():
  arguments = sys.argv[1:]
  inp = " ".join(arguments)

  if determineBraille(inp):
    print(brailleToText(inp))
  else:
    print(textToBraille(inp))

if __name__ == "__main__":
  main()
