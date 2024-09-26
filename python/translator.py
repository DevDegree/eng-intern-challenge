import sys
# Dictionaries
braille_to_english = {
  "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
  "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
  "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
  "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
  "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
  "O..OOO": "z", ".....O": "capital",  ".O...O": "decimal", ".O.OOO": "number", 
  "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
  "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO." : ">",
  "O.O..O": "(", ".O.OO.": ")", "......": " "
}

braille_num_to_english = {
  "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
  "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
  "......": " "
}

english_to_braille = {
  "a": "O.....", "b": "O.O...", "c": "OO....", "d":  "OO.O..", "e": "O..O..",
  "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
  "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
  "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
  "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
  "z": "O..OOO", "capital": ".....O", "decimal": ".O...O", "number": ".O.OOO",
  ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
  ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
  "(": "O.O..O", ")": ".O.OO.", " ": "......"
}

english_num_to_braille = {
  "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
  "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
  " ": "......"
}

# braille to english functionality
def braille_to_text(input):
  out = ""
  isCapital = False
  isNumber = False

  chars = [(input[i:i+6]) for i in range(0, len(input), 6)]

  for char in chars:
    if char == ".....O":
      isCapital = True 

    elif char == ".O.OOO":
      isNumber = True

    elif char == "......":
      translated_char = braille_to_english[char]
      isNumber = False
      out += translated_char

    elif isNumber:
      translated_char = braille_num_to_english[char]
      out += translated_char

    else:
      translated_char = braille_to_english[char]
      if isCapital:
        translated_char = translated_char.upper()
        isCapital = False
      out += translated_char

  return out

# english to braille functionality
def text_to_braille(input):
  out = ""
  isNumber = False

  for char in input:

    if char.isupper():
      out += english_to_braille["capital"]
      out += english_to_braille[char.lower()]
    
    elif char == " ":
      isNumber = False
      out += english_to_braille[char]
    
    elif isNumber == True:
      out += english_num_to_braille[char]

    elif char.isdigit():
      isNumber = True
      out += english_to_braille["number"]
      out += english_num_to_braille[char]
    
    else:
      out += english_to_braille[char]
    
  return out

# checks if input is text or braille
def check(input):
  if len(input) == input.count("O") + input.count("."):
      return braille_to_text(input)
  else:
      return text_to_braille(input)
if __name__ == "__main__":
  testInput = " ".join(sys.argv[1:])
  print(check(testInput))

