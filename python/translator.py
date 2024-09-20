import sys

alphabetAndSymbols = {
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

nums = {
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
    ' ': '......'
}

xFollows = {
    'decimal': '.O...O',
    'capital': '.....O',
    'number': '.O.OOO',
}

def xFollowsChecker(char, isBraille):
    if char.isupper() and not isBraille:
        return xFollows['capital']
    elif char.isnumeric():
        return xFollows['number']
    elif char == '.':
        return xFollows['decimal']
    return ''

def translateFromCharToBraille(currChar, prevChar):
    output = ''
    isBraille = 0
    if(prevChar == '' or prevChar == ' '):
        checkedChar = xFollowsChecker(currChar, isBraille)
        output += checkedChar + alphabetAndSymbols[currChar.lower()]
    else:
        output += alphabetAndSymbols[currChar]

    return output

def translateFromNumToBraille(currChar, prevChar):
    output = ''
    isBraille = 0
    if(prevChar == '' or prevChar == ' '):
        checkedChar = xFollowsChecker(currChar, isBraille)
        output += checkedChar + nums[currChar.lower()]
    else:
        output += nums[currChar]
        
    return output

def iterateAndTranslate(string):
    output = ''
    prevChar = ''
    isNum = 0
    isCap = 0
    if(len(string)%6 == 0 and set(string).issubset({'.', 'O'})):
        brailleKeys = [string[i:i+6] for i in range(0, len(string), 6)]
        for i in range(len(brailleKeys)):
            if(brailleKeys[i] in xFollows.values()):
                if(brailleKeys[i] == ".O.OOO"):
                    isNum = 1
                elif(brailleKeys[i] == ".....O"):
                    isCap = 1
            elif(brailleKeys[i] in nums.values() and isNum):
                output += translateFromBrailleToNum(brailleKeys[i], prevChar)
                prevChar = brailleKeys[i]
            elif(brailleKeys[i] in alphabetAndSymbols.values() and isCap):
                output += translateFromBrailleToChar(brailleKeys[i], prevChar).upper()
                prevChar = brailleKeys[i]
                isCap = 0
            else:
                output += translateFromBrailleToChar(brailleKeys[i], prevChar)
                prevChar = brailleKeys[i]
            
            if(brailleKeys[i] == "......"):
                isNum = 0
                isCap = 0

    else:    
        for char in string:

            if(char.isnumeric()):
                output += translateFromNumToBraille(char, prevChar)
            else:
                output += translateFromCharToBraille(char, prevChar)
            
            prevChar = char

    return output

def translateFromBrailleToNum(currChar, prevChar):
    brailleToNums = dict((v,k) for k,v in nums.items())
    output = ''
    isBraille = 1
    if(prevChar == '' or prevChar == '......'):
        checkedChar = xFollowsChecker(currChar, isBraille)
        output += checkedChar + brailleToNums[currChar]
    else:
        output += brailleToNums[currChar]
        
    return output

def translateFromBrailleToChar(currChar, prevChar):
    brailleToChar = dict((v,k) for k,v in alphabetAndSymbols.items())
    output = ''
    isBraille = 1
    if(prevChar == '' or prevChar == '......'):
        checkedChar = xFollowsChecker(currChar, isBraille)
        output += checkedChar + brailleToChar[currChar]
    else:
        output += brailleToChar[currChar]
        
    return output

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input = sys.argv[1:]
    fullInput = " ".join(input)
    translatedInput = iterateAndTranslate(fullInput)
    print(translatedInput)

if __name__ == "__main__":
    main()