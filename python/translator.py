import sys

def translator(word):
    englishToBrailleAlpha = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    ',': '..O...',
    ';': '..OO..',
    ':': '...O..',
    '.': '...OO.',
    '?': '..O.O.',
    '!': '..OOO.',
    '-': '....O.',
    '/': '.O.O..',
    '(': 'O.O..O',
    ')': '.O.OO.',
    'capital follows': '.....O',
    'decimal follows': '.O...O',
    'number follows': '.O.OOO',
    ' ': '......'
    }
    
    englishToBrailleNumeric = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    }

    brailleToEnglishAlpha = {v:k for k,v in englishToBrailleAlpha.items()}
    brailleToEnglishNumeric = {v:k for k,v in englishToBrailleNumeric.items()}

    if brailleOrEnglish(word):
        return toBraille(word, {**englishToBrailleAlpha, **englishToBrailleNumeric})
    else: 
        return toEnglish(word, brailleToEnglishAlpha, brailleToEnglishNumeric)

def brailleOrEnglish(word):
    english = False
    for i in word[:6]: 
        if i == "O" or i == ".":
            continue 
        else: 
            english = True
    return english

def toBraille(english, englishToBrailleAlphaNumeric):
    brailleString = ""
    numberFlag = False
    for letter in english:
        if numberFlag and (not letter.isnumeric()):
            numberFlag = False
            brailleString += "......" # add space

        if (not numberFlag) and letter.isupper():
            brailleString += ".....O" # add capital follows

        if letter.isnumeric():
            if not numberFlag:
                brailleString += ".O.OOO" # add number follows
            numberFlag = True
            
        brailleString += englishToBrailleAlphaNumeric[letter.upper()]
    return brailleString

def toEnglish(braille, brailleToEnglishAlpha, brailleToEnglishNumeric):
    brailleString = ""
    englishString = ""
    count = 0
    brailleHaveNumbers = False
    capitalFollows = False
    for group in braille:
        brailleString += group
        count += 1
        if count == 6:
            if brailleString == "......": # space
                englishString += brailleToEnglishAlpha[brailleString]
                capitalFollows = False
                brailleHaveNumbers = False
            elif brailleString == '.....O': # capital follows
                capitalFollows = True
            elif brailleHaveNumbers:
                englishString += brailleToEnglishNumeric[brailleString]
            elif brailleString == ".O.OOO": # number follows
                brailleHaveNumbers = True
            else: # not number follows, not capital, not space
                if capitalFollows:
                    englishString += brailleToEnglishAlpha[brailleString].upper()
                    capitalFollows = False
                else:
                    englishString += brailleToEnglishAlpha[brailleString].lower()
            count = 0
            brailleString = ""
    return englishString

args = sys.argv
args.pop(0)
for i, word in enumerate(args):
    if not i == 0:
        print("......", end = '')
    print(translator(word), end = '')
