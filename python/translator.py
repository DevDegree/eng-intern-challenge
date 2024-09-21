brailleAlphabetDict = {"a":"0.....", "b":"0.0...", "c":"00....", "d":"00.0..", "e":"0..0..", "f":"000...", "g":"0000..", "h":"0.00..", "i":".00...", 
              "j":".000..", "k":"0...0.", "l":"0.0.0.", "m":"00..0.", "n":"00.00.", "o":"0..00.", "p":"000.0.", "q":"00000.", "r":"0.000.",
              "s":".00.0.", "t":".0000.", "u":"0...00", "v":"0.0.00", "w":".000.0", "x":"00..00", "y":"00.000", "z":"0..000"}

brailleNumberDict = {1:"0.....", 2:"0.0...", 3:"00....", 4:"00.0..", 5:"0..0..", 6:"000...", 7:"0000..", 8:"0.00..", 9:".00...",
                    0:".000.."}

brailleSpecialCharacters = {".":"..00.0", ",":"..0...", "?":"..0.00", "!":"..000.", ":":"..00..", ";":"..0.0.", "-":"....00", 
                            "/":".0..0.", "<":".00..0", ">":"0..00.", "(":"0.0..0", ")":".0.00.", " ":"......"}

brailleCapitalLetter = ".....0"

brailleDecimal = ".0...0"

def inputToBraille(userInput):
  brailleOutput = ""
  for char in userInput:
    # if letter
    if char.isalpha():
      # if capital letter
      if char.isupper():
        brailleOutput += brailleCapitalLetter
      brailleOutput += brailleAlphabetDict[char.lower()]
    # if digit
    elif char.isdigit():
      brailleOutput += brailleDecimal + brailleNumberDict[int(char)]
    # if special character
    elif char in brailleSpecialCharacters:
      brailleOutput += brailleSpecialCharacters[char]
    else:
      brailleOutput += "unknown"
  # print(len(brailleOutput))
  return brailleOutput

def brailleToStrings(userInput):
  strings = ""
  isCapital = False
  isDigit = False
  
  # cut userInput into 6 characters
  for i in range(0, len(userInput), 6):
    braille_char = userInput[i:i+6]  # braille characters in 6 characters
    
    # if capital letter check
    if braille_char == brailleCapitalLetter:
      isCapital = True 
      continue  

    # if digit check
    if braille_char == brailleDecimal:
      isDigit = True
      continue 
    
    # if letter
    if braille_char in brailleAlphabetDict.values() and isDigit == False:
      for key, value in brailleAlphabetDict.items():
        if value == braille_char:
          strings += key.upper() if isCapital else key 
          isCapital = False  # reset isCapital
          break
        
    # if digit 
    elif isDigit and braille_char in brailleNumberDict.values():
      for key, value in brailleNumberDict.items():
        if value == braille_char:
          strings += str(key)
          break

    # if special character
    elif braille_char in brailleSpecialCharacters.values():
      for key, value in brailleSpecialCharacters.items():
        if value == braille_char:
          strings += key
          break
  
  return strings

# check braile to strings
#.....00.....0.0...00...........0...00.....0.0...00....

# call function
userPrompt = input()
if len(userPrompt) % 6 == 0 and all(char in "01." for char in userPrompt):
  print(brailleToStrings(userPrompt))
else:
  print(inputToBraille(userPrompt))