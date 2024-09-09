import sys

ENGLISH_TO_BRAILLE_DICT = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.", # This is same as letter O, there is no way to distinguish.
  "(": "O.O..O",
  ")": ".O.OO.",
}


BRAILLE_TO_NON_ALPHA_DICT = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
  "......": " ",
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "..O.O.": ";",
  "....OO": "-",
  ".O..O.": "/",
  ".OO..O": "<",
  "O..OO.": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
}

BRAILLE_TO_ALPHA_DICT = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
}

CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O" # from the tech reqs this is unused
NUMBER_FOLLOWS = ".O.OOO"

BRAILLE_COMMANDS = [CAPITAL_FOLLOWS, DECIMAL_FOLLOWS, NUMBER_FOLLOWS]

BRAILLE_LENGTH = 6

def translate(text: str) -> str:
  if validBraille(text):
    return brailleToEnglish(text)
  return englishToBraille(text)

'''
  Helper function which checks if text is valid braille
  If not, it assumes it is english text

  
'''
def validBraille(text : str) -> bool:
  # Valid braille should have a length of a multiple of 6
  if len(text) % BRAILLE_LENGTH != 0: return False

  # helper flag booleans
  checkCapital = False
  checkNumber = False

  for i in range(0, len(text)-(BRAILLE_LENGTH-1), BRAILLE_LENGTH):
    brailleCh = text[i:i+BRAILLE_LENGTH]
    if brailleCh not in BRAILLE_TO_ALPHA_DICT and brailleCh not in BRAILLE_TO_NON_ALPHA_DICT and brailleCh not in BRAILLE_COMMANDS:
      return False
    
    # both flags cannot be true
    if checkCapital and checkNumber: return False

    # if we expect the next character is not a letter, it's not valid
    if checkCapital and brailleCh not in BRAILLE_TO_ALPHA_DICT:
      return False
    # otherwise it is, so we set it to false
    else: 
      checkCapital = False

    if checkNumber and brailleCh not in BRAILLE_TO_NON_ALPHA_DICT:
      return False
    # if we expect number and get a space, we set the flag to false
    if checkNumber and BRAILLE_TO_NON_ALPHA_DICT[brailleCh] == " ":
      checkNumber = False
    # if we expect number and get something else, then it's not valid
    elif checkNumber and not BRAILLE_TO_NON_ALPHA_DICT[brailleCh].isnumeric():
      return False
    
    # if we see a captial follows, a letter should follow!
    if not checkCapital and brailleCh == CAPITAL_FOLLOWS:
      checkCapital = True
    # if we see a number follows, we should see only numbers until a space/EOF
    if not checkNumber and brailleCh == NUMBER_FOLLOWS:
      checkNumber = True
  
  return True

'''
  Helper function which converts braille to english
  Assumes that input text is valid braille
'''
def brailleToEnglish(braille: str) -> str:
  englishText = ""

  # helper flag to capitalized characters
  capitalized = False
  isNumber = False

  for i in range(0, len(braille)-(BRAILLE_LENGTH-1), BRAILLE_LENGTH):
    brailleCh = braille[i:i+BRAILLE_LENGTH]
    if brailleCh == DECIMAL_FOLLOWS:
      continue
    elif brailleCh == NUMBER_FOLLOWS:
      isNumber = True
    elif brailleCh == CAPITAL_FOLLOWS:
      capitalized = True
    elif capitalized:
      englishText += BRAILLE_TO_ALPHA_DICT[brailleCh].upper()
      capitalized = False
    elif isNumber:
      englishText += BRAILLE_TO_NON_ALPHA_DICT[brailleCh]
      if BRAILLE_TO_NON_ALPHA_DICT[brailleCh] == " ":
        isNumber = False
    elif brailleCh in BRAILLE_TO_ALPHA_DICT:
      englishText += BRAILLE_TO_ALPHA_DICT[brailleCh]
    else:
      englishText += BRAILLE_TO_NON_ALPHA_DICT[brailleCh]
    
  return englishText

'''
  Helper function which converts english to braille
  Assumes that input text uses the only characters from the provided alphabet
'''
def englishToBraille(englishText: str) -> str:
  braille = ""
  isConvertingDigits = False

  for ch in englishText:
    if ch.isalpha():     # for alphabet characters
      if ch.isupper():
        braille += CAPITAL_FOLLOWS
      braille += ENGLISH_TO_BRAILLE_DICT[ch.lower()]
      continue
    elif ch.isnumeric():
      if not isConvertingDigits:
        isConvertingDigits = True
        braille += NUMBER_FOLLOWS
    elif ch == " ":
      isConvertingDigits = False

    braille += ENGLISH_TO_BRAILLE_DICT[ch]

  return braille

if __name__ == '__main__':
  input = sys.argv[1:]

  for text in input:
    print(translate(text))
