import sys

CAPITALFOLLOWS = "CAPITALFOLLOWS"
NUMBERFOLLOWS = "NUMBERFOLLOWS"

brailleToAlphabetMap = {
  "O.....": 'a',
  "O.O...": 'b',
  "OO....": 'c',
  "OO.O..": 'd',
  "O..O..": 'e',
  "OOO...": 'f',
  "OOOO..": 'g',
  "O.OO..": 'h',
  ".OO...": 'i',
  ".OOO..": 'j',
  "O...O.": 'k',
  "O.O.O.": 'l',
  "OO..O.": 'm',
  "OO.OO.": 'n',
  "O..OO.": 'o',
  "OOO.O.": 'p',
  "OOOOO.": 'q',
  "O.OOO.": 'r',
  ".OO.O.": 's',
  ".OOOO.": 't',
  "O...OO": 'u',
  "O.O.OO": 'v',
  ".OOO.O": 'w',
  "OO..OO": 'x',
  "OO.OOO": 'y',
  "O..OOO": 'z',
}
brailleToNumberMap = {
  "O.....": '1',
  "O.O...": '2',
  "OO....": '3',
  "OO.O..": '4',
  "O..O..": '5',
  "OOO...": '6',
  "OOOO..": '7',
  "O.OO..": '8',
  ".OO...": '9',
  ".OOO..": '0',
}
brailleToSymbolMap = {
  ".....O": CAPITALFOLLOWS,
  ".O.OOO": NUMBERFOLLOWS,
  "......": " ",
}

alphabetToBrailleMap = {val: key for key, val in brailleToAlphabetMap.items()}
numberToBrailleMap = {val: key for key, val in brailleToNumberMap.items()}
symbolToBrailleMap = {val: key for key, val in brailleToSymbolMap.items()}

def isBraille(s: str):
  if len(s) % 6 != 0:
    return False # Braille consists of 6 character strings and each character consists of at least one unraised rea

  for c in s:
    if c != '.' and c != 'O':
      return False # Braille only consists of '.' and 'O'
    
  if '.' not in s:
    return False # Braille characters contain at least one unraised area

  return True

def brailleToEnglish(s: str):
  res = ""

  addCapital = False
  addNumber = False
  
  for currCharStart in range(0, len(s) - 5, 6):
    currCharEnd = currCharStart + 6
    currBraille = s[currCharStart: currCharEnd]

    # CASE 1: SYMBOL
    if currBraille in brailleToSymbolMap:
      symbol = brailleToSymbolMap[currBraille]

      if symbol == CAPITALFOLLOWS:
        addCapital = True
      elif symbol == NUMBERFOLLOWS:
        addNumber = True
      else: # Space
        res += symbol
        addNumber = False
      
      continue

    # CASE 2: NUMBER
    if addNumber:
      res += brailleToNumberMap[currBraille]
      continue
    
    # CASE 3: LETTER
    if currBraille in brailleToAlphabetMap:
      res += brailleToAlphabetMap[currBraille].upper() if addCapital else brailleToAlphabetMap[currBraille]
      addCapital = False

  return res

def englishToBraille(s: str):
  res = ""

  for i, c in enumerate(s):
    # Case 1: Symbol read (space)
    if c == " ":
      res += symbolToBrailleMap[c]

    # Case 2: Uppercase Letter read
    elif c.isalpha() and c.isupper():
      res += symbolToBrailleMap[CAPITALFOLLOWS] + alphabetToBrailleMap[c.lower()]
    
    # Case 3: Lowercase Letter read
    elif c.isalpha() and c.islower():
      res += alphabetToBrailleMap[c]

    # Case 4: Start of number read
    elif (c.isnumeric() and not res) or (c.isnumeric() and res and not s[i-1].isnumeric()):
      res += symbolToBrailleMap[NUMBERFOLLOWS] + numberToBrailleMap[c]

    # Case 5: Subsequent digit of number read
    elif c.isnumeric():
      res += numberToBrailleMap[c]

  return res

def main():
  arg = ""
  for i in range(1, len(sys.argv)-1, 1):
    arg += sys.argv[i] + ' ' # Extract the provided arguments
  
  arg += sys.argv[len(sys.argv) - 1]

  if isBraille(arg):
    print(brailleToEnglish(arg))
  else:
    print(englishToBraille(arg))

if __name__ == "__main__":
  main()