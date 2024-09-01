# Author: Nguyen-Hanh Nong
# File: translator.py
# Purpose: To create a Python converter, that will convert English text to Braille or Braille text to English text that is passed in as a command-line argument into the script
# Assumptions:
## - If there is a number that is followed by a capital letter, with the same braille conversion, that there will always will be the "follows" indicator

## Importing the sys library to be able to access cmd-line arguments in Python 3.8
import sys

# Creating 3 separate dictionaries, to hold all the various mappings between all the possible inputs from English to Braille conversion
defaultCharacterDictionary: dict = {
  'a':'O.....',
  'b':'O.O...',
  'c':'OO....',
  'd':'OO.O..',
  'e':'O..O..',
  'f':'OOO...',
  'g':'OOOO..',
  'h':'O.OO..',
  'i':'.OO...',
  'j':'.OOO..',
  'k':'O...O.',
  'l':'O.O.O.',
  'm':'OO..O.',
  'n':'OO.OO.',
  'o':'O..OO.',
  'p':'OOO.O.',
  'q':'OOOOO.',
  'r':'O.OOO.',
  's':'.OO.O.',
  't':'.OOOO.',
  'u':'O...OO',
  'v':'O.O.OO',
  'w':'.OOO.O',
  'x':'OO..OO',
  'y':'OO.OOO',
  'z':'O..OOO',
  ' ':'......',
  '.':'..OO.O',
  ',':'..O...',
  '?':'..O.OO',
  '!':'..OOO.',
  ':':'..OO..',
  ';':'..O.O.',
  '-':'....OO',
  '/':'.O..O.',
  '<':'.OO..O',
  '>':'O..OO.',
  '(':'O.O..O',
  ')':'.O.OO.',
}

specialCharactersDictionary: dict = {
  'capital':'.....O',
  'decimal':'.O...O',
  'number':'.O.OOO'
}

numberLetterMapping: dict = {
  '1':'a',
  '2':'b',
  '3':'c',
  '4':'d',
  '5':'e',
  '6':'f',
  '7':'g',
  '8':'h',
  '9':'i',
  '0':'j'
}

# Creating three dictionaries, that do the reverse of the conversion (which we need when converting from braille to english)
reverseDefaultCharacterDictionary: dict = {
  'O.....':'a',
  'O.O...':'b',
  'OO....':'c',
  'OO.O..':'d',
  'O..O..':'e',
  'OOO...':'f',
  'OOOO..':'g',
  'O.OO..':'h',
  '.OO...':'i',
  '.OOO..':'j',
  'O...O.':'k',
  'O.O.O.':'l',
  'OO..O.':'m',
  'OO.OO.':'n',
  'O..OO.':'o',
  'OOO.O.':'p',
  'OOOOO.':'q',
  'O.OOO.':'r',
  '.OO.O.':'s',
  '.OOOO.':'t',
  'O...OO':'u',
  'O.O.OO':'v',
  '.OOO.O':'w',
  'OO..OO':'x',
  'OO.OOO':'y',
  'O..OOO':'z',
  '......':' ',
  '..OO.O':'.',
  '..O...':',',
  '..O.OO':'?',
  '..OOO.':'!',
  '..OO..':':',
  '..O.O.':';',
  '....OO':'-',
  '.O..O.':'/',
  '.OO..O':'<',
  'O.O..O':'(',
  '.O.OO.':')',
}

reverseSpecialCharactersDictionary: dict = {
  '.....O':'capital',
  '.O...O':'decimal',
  '.O.OOO':'number',
}

reverseNumberLetterMapping: dict = {
  'a':'1',
  'b':'2',
  'c':'3',
  'd':'4',
  'e':'5',
  'f':'6',
  'g':'7',
  'h':'8',
  'i':'9',
  'j':'0',
}

""" 
Input: A string that is in the Braille language
Output: The input string but translated to the English language
"""
def convertFromBrailleToEnglish(input: str) -> str:
  res: str = ''
  isCapital: bool = False
  isNum: bool = False

  # Now that we know that the string given to us is in braille, we want to parse the braille, 6 characters at a time
  while input:
      currentBrailleString: str = input[:6]
      input: str = input[6:]

      # Check if the current braille string converts to a normal alpha numeric/special character
      if currentBrailleString in reverseDefaultCharacterDictionary:
        if isCapital:
            res += reverseDefaultCharacterDictionary[currentBrailleString].upper()
            isCapital = False
        
        # Check if we're supposed to put a number instead of the letter corresponding to the braille
        elif isNum and reverseDefaultCharacterDictionary[currentBrailleString] in reverseNumberLetterMapping:
            res += reverseNumberLetterMapping[reverseDefaultCharacterDictionary[currentBrailleString]]
        else:
            isNum = False
            res += reverseDefaultCharacterDictionary[currentBrailleString]

      # Check if we're supposed to have one of the special characters
      elif currentBrailleString in reverseSpecialCharactersDictionary:
          if reverseSpecialCharactersDictionary[currentBrailleString] == 'decimal' or reverseSpecialCharactersDictionary[currentBrailleString] == 'number':
            isNum = True
            if reverseSpecialCharactersDictionary[currentBrailleString] == 'decimal':
              res += '.'
          elif reverseSpecialCharactersDictionary[currentBrailleString] == 'capital':
            isCapital = True

      # If it doesn't fit into any of the translations given above, then we can't find a corresponding mapping in English, so we just skip that entry and keep going
      else:
          continue
      
  return res + ' '  

""" 
Input: A string that is in the English language
Output: The input string but translated to the Braille language
"""
def convertFromEnglishToBraille(input: str) -> str:
  res: str = ''
  isNumber: bool = False

  # Now that we know that the string given to us is in English, we want to parse the string, one character at a time
  while input:
      currentCharacter: str = input[0]
      input = input[1:]

      # We now have to handle all the non-alpha numeric characters and their corresponding braille translations
      if currentCharacter.isnumeric() is False and currentCharacter.isalpha() is False:
        if currentCharacter == '.' and input and input[0].isnumeric():
          isNumber = True
          res += specialCharactersDictionary['decimal']
        elif currentCharacter in defaultCharacterDictionary:
          isNumber = False
          res += defaultCharacterDictionary[currentCharacter]
        else:
           continue
      # Check if the char is numeric or not
      elif currentCharacter.isnumeric():
        if isNumber:
          res += defaultCharacterDictionary[numberLetterMapping[currentCharacter]]
        else:
          res += specialCharactersDictionary['number'] + defaultCharacterDictionary[numberLetterMapping[currentCharacter]]
          # Change isNumber to True since we know that the current number is numeric
        isNumber = True
      # If the current character is not a number, then check if it's a letter in the normal alphabet
      elif currentCharacter.isalpha():
        if currentCharacter.isupper():
            res += specialCharactersDictionary['capital'] + defaultCharacterDictionary[currentCharacter.lower()]
        else:
            res += defaultCharacterDictionary[currentCharacter]
        # Change isNumber to false since we know the current character is not numeric
        isNumber = False
      else:
        continue

  return res + '......'

if __name__ == "__main__":
  # This is the variable we will print to the terminal, containing the translation output
  res: str = ''

  # Language given
  isBraille: bool = False

  # Capture all arguments except the script name
  allArguments: list[str] = sys.argv[1:]

  # For cases with multiple arguments
  for word in allArguments:
    # Check if the word that we get from the command-line is in braille or in English
    if len(word) % 6 == 0 and set(word) == set('O.'):
      res += convertFromBrailleToEnglish(word)
      isBraille = True
    else:
      res += convertFromEnglishToBraille(word)
      isBraille = False

  # Removing the padded spacing depending on whether the conversion was into Braille or English before printing the string
  if isBraille is True:
    print(res[:-1].strip())
  else:
    print(res[:-6].strip())