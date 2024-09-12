import sys
engToBraille = {
    'a': 'O.....',      'b': 'O.O...',      'c': 'OO....',      'd': 'OO.O..',      'e': 'O..O..',
    'f': 'OOO...',      'g': 'OOOO..',      'h': 'O.OO..',      'i': '.OO...',      'j': '.OOO..',
    'k': 'O...O.',      'l': 'O.O.O.',      'm': 'OO..O.',      'n': 'OO.OO.',      'o': 'O..OO.',
    'p': 'OOO.O.',      'q': 'OOOOO.',      'r': 'O.OOO.',      's': '.OO.O.',      't': '.OOOO.',
    'u': 'O...OO',      'v': 'O.O.OO',      'w': '.OOO.O',      'x': 'OO..OO',      'y': 'OO.OOO',      'z': 'O..OOO',
    # Numbers (same as letters a-j with number indicator)
    '1': 'O.....',      '2': 'O.O...',      '3': 'OO....',      '4': 'OO.O..',      '5': 'O..O..',
    '6': 'OOO...',      '7': 'OOOO..',      '8': 'O.OO..',      '9': '.OO...',      '0': '.OOO..',
    # Special symbols (follows)
    'cap': '.....O',    'num': '.O.OOO',     ' ': '......',
}

# constants used for translation CLI. 
CAPITAL = 'cap'
NUM = 'num'
SPACE = ' '
SIX_O = "OOOOOO"

# flips the KVP and subdivides it into 2 maps. 
# brailleToEng includes non braille mapping to non digits (letters and space)
# brailleToDigit includes braille mapping to digits (0 -9)
brailleToEng = {j: i for i, j in engToBraille.items() if not i.isdigit()}
brailleToDigit = {j: i for i, j in engToBraille.items() if i.isdigit()}

# Params: s: the input string
# Output: true if the string is of valid Braille syntax, false otherwise
# Logic: all brailles have length as multiples of 6 and all chars are in "O."
def isBraille(s):
    if (s == SIX_O): # edge case OOOOOO is not valid Braile but valid english
        return False
    return (len(s) % 6 == 0) and all(c == 'O' or c == '.' for c in s)
   
# Params: s: the input braille string
# Output: the list of translated english words from the braille string
def convertBraToEng(s):
    res = [] # list of translated words
    capNext = False # flag to set the next one to capital letter. 
    numNext = False # flag to check if we are in the middle of a number. Use to differentiate (1, a) (2, b) ... duplicates
    for i in range(0, len(s), 6):
        token = s[i : i + 6] # parse 6 braille tokens at once
        if token in brailleToDigit: # if the current input is a digit and we are already in a number, we can append the digit
            if numNext:
                res.append(brailleToDigit[token]) # directly append the number. this takes care of (1, a) (2, b) ... duplicates
                continue
        if token in brailleToEng:
            if token == engToBraille[CAPITAL]: 
                capNext = True
            elif token == engToBraille[NUM]:
                numNext = True
            elif token == engToBraille[SPACE]: # set numNext to false once space is hit, per requirements
                res.append(SPACE) # insert space
                numNext = False
            else:
                if capNext: # capitalizes the char
                    res.append(brailleToEng[token].upper())
                    capNext = False # flip flag after every capital letter per requirements
                else: # regular lowercase
                    res.append(brailleToEng[token])
    return res

# Params: s: the input braille string
# Output: the list of translated braille tokens from the english words
def convertEngToBra(s):
    res = [] # list of translated braille tokens
    isNum = False
    for i in range (0, len(s)):
        c = s[i] # cur char being processed
        if c.isdigit(): # if current char is a digit, we know we are either starting a number or in a number
            if not isNum: # logic falls through, therefore only add in the numFollows braille if needed
                res.append(engToBraille[NUM]) 
                isNum = True
        elif c.isupper(): # flips capital flag
            res.append(engToBraille[CAPITAL])
        if not c.isdigit(): # we are no longer in a number whenever we see a char that is not a digit
            isNum = False
        res.append(engToBraille[c.lower()]) # adds the appropriate braille mapping with the current char after all preprocessing is finished
    return res

def main():
    args = ' '.join(sys.argv[1:]) # join all arugments
    braille = isBraille(args) # check if arguments is braille
    res = []
    if braille: # use appropriate conversion logic
        res = convertBraToEng(args)
    else:
        res = convertEngToBra(args)
    print(''.join(res)) # print the list joined by the empty string
        
if __name__ == "__main__":
    main()
