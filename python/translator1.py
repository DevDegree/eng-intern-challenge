

# accept cli text input
# translate text to braille or braille to text

LETTERS = {
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
}
NUMBERS = {
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
}

KEYS = {
  "capital_follows": ".....O",
  "decimal_follows": ".O...O",
  "number_follows": ".O.OOO",
}

PUNCTIOATION = {  
  "decimal": "..OO.O",
  "comma": "..O...",
  "question": "..O.OO",
  "exclamation": "..OOO.",
  "colon": "..OO..",
  "semicolon": "..O.O.",
  "dash": "....OO",
  "slash": ".O..O.",
  "lt": ".OO..O",
  "gt": "O..OO.",
  "open_paren": "O.O..O",
  "close_paren": ".O.OO.",
  "space": "......",
}

def translate_to_braille(text):
  string = ""
  for token in text:
    
    if token.isdigit():
      string+=KEYS["number_follows"]
    if token.isupper():
      string+=KEYS["capital_follows"]
      token = token.lower()
    if token == ".":
      string+=KEYS["decimal_follows"]
      string+=PUNCTIOATION["decimal"]
      
    if token in LETTERS.keys():
      string+=LETTERS[token]
    elif token in NUMBERS.keys():
      string+=NUMBERS[token]
    elif token in KEYS.keys():
      string+=KEYS[token]
    elif token in PUNCTIOATION.keys():
      string+=PUNCTIOATION[token]
    elif token == ",":
      string+=PUNCTIOATION["comma"]
    elif token == "?":
      string+=PUNCTIOATION["question"]
    elif token == "!":
      string+=PUNCTIOATION["exclamation"]
    elif token == ":":
      string+=PUNCTIOATION["colon"]
    elif token == ";":
      string+=PUNCTIOATION["semicolon"]
    elif token == "-":
      string+=PUNCTIOATION["dash"]
    elif token == "/":
      string+=PUNCTIOATION["slash"]
    elif token == "<":
      string+=PUNCTIOATION["lt"]
    elif token == ">":
      string+=PUNCTIOATION["gt"]
    elif token == "(":
      string+=PUNCTIOATION["open_paren"]
    elif token == ")":
      string+=PUNCTIOATION["close_paren"]
    elif token == " ":
      string+=PUNCTIOATION["space"]
  
  return string
  
def translate_to_text(text):
  string = ""
  capitalFlag = 0
  numFlag = False
  for i in range(0,len(text),6):
    cur = text[i:i+6]

    if cur == KEYS["capital_follows"]:
      capitalFlag += 1
    elif cur == KEYS["number_follows"]:
      numFlag = True
    elif cur == KEYS["decimal_follows"]:
      pass
    
    if not numFlag:
      if capitalFlag == 2:
        if cur in LETTERS.values():
          for key, value in LETTERS.items():
            if value == cur:
              string+=key.upper()
              capitalFlag = 0
      else:
        if cur in LETTERS.values():
          for key, value in LETTERS.items():
            if value == cur:
              string+=key
    else:
      if cur in NUMBERS.values():
        for key, value in NUMBERS.items():
          if value == cur:
            string+=key
            
    # check for punctuation
    if cur in PUNCTIOATION.values():
      for key, value in PUNCTIOATION.items():
        if value == cur:
          string+=key
          
    capitalFlag += 1
    numFlag = False
    
  return string
    

def main():
  text = input("Enter Braile or Text: ")
  if "O" not in text or "." not in text:
    val = translate_to_braille(text)
    print(val)
    print(translate_to_text(val))
  else:
    val = translate_to_text(text)
    print(val)
    print(translate_to_braille(val))
  
  
    
    
if __name__ == "__main__":
    main()