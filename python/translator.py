import sys

englishToBrailleLetters = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
}

englishToBrailleNumbers = {
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

brailleToEnglishLetters = {}
for c in englishToBrailleLetters:
    brailleToEnglishLetters[englishToBrailleLetters[c]] = c

brailleToEnglishNumbers = {}
for n in englishToBrailleNumbers:
    brailleToEnglishNumbers[englishToBrailleNumbers[n]] = n

capitalFollows = '.....O'
numberFollows = '.O.OOO'
space = '......'

def englishToBraille(englishStr):
    brailleStr = ""
    isNumber = False

    for c in englishStr:
        if c.isdigit():
            if not isNumber:
                isNumber = True
                brailleStr += numberFollows
            brailleStr += englishToBrailleNumbers[c]
        elif c.isalpha():
            if c.isupper():
                brailleStr += capitalFollows
                c = c.lower()
            isNumber = False
            brailleStr += englishToBrailleLetters[c]
        elif c == ' ':
            isNumber = False
            brailleStr += space

    return brailleStr
    

def brailleToEnglish(brailleStr):
    englishStr = ""

    curIndex = 0
    isNumber = False

    while curIndex < len(brailleStr):
        c = brailleStr[curIndex:curIndex+6]

        if c == numberFollows:
            isNumber = True
        elif c == space:
            englishStr += ' '
            isNumber = False
        elif c == capitalFollows:
            curIndex += 6
            c = brailleStr[curIndex:curIndex+6]
            englishStr += brailleToEnglishLetters[c].upper()
        elif isNumber:
            englishStr += brailleToEnglishNumbers[c]
        else:
            englishStr += brailleToEnglishLetters[c]
        
        curIndex += 6

    return englishStr


def main():
    s = ' '.join(sys.argv[1:])

    isBraille = True

    for c in s:
        if c != '.' and c != 'O':
            isBraille = False
            break
    
    if isBraille:
        print(brailleToEnglish(s))
    else:
        print(englishToBraille(s))

main()
