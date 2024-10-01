import sys
# Braille Mapping using O and .
brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.', 
    ' ': '......',
}

capital, number, decimal = '.....O', '.O.OOO', '.O...O'

#Reverse Map
reverseBrailleMap = {val: key for key, val in brailleMap.items()}

# Braille Mapping for nums
reverseBrailleMapNums = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

brailleMapNums = {val: key for key, val in reverseBrailleMapNums.items()}

def englishToBraille(input):
    ret, isNum = '', False
    
    for letter in input:
        if(letter.isupper()):
            ret += (capital + brailleMap[letter.lower()])
            isNum = False
        elif(letter.isdigit()):
            if(not isNum):
                ret += number
                isNum = True
            ret += brailleMapNums[letter]
        elif(letter == '.'):
            ret += (decimal + brailleMap[letter])
        else:
            ret += brailleMap[letter]
            isNum = False
    return(ret)

def brailleToEnglish(input):
    ret, isNum, isCap, lenInput = '', False, False, len(input)

    for i in range(0, lenInput, 6):
        word = input[i:i+6]
        if(word == capital and not isCap):
            isCap = True
        elif(word in reverseBrailleMap and not isNum):
            if(isCap):
                ret += reverseBrailleMap[word].upper()
                isCap = False
            else:
                ret += reverseBrailleMap[word]
        elif(word == number and not isNum):
            isNum = True
        elif(isNum and word in reverseBrailleMapNums):
            ret += reverseBrailleMapNums[word]
        elif(word == brailleMap[' ']):
            ret += ' '
            isNum = False
        elif(word == decimal):
            pass
        else:
            ret += reverseBrailleMap[word]
    return(ret)




def isEnglish(inputText):
    #Check if is a mutliple of 6
    if(len(inputText) % 6 != 0):
        return(True)
    
    #Check the letters
    for letter in inputText:
        if(letter not in ".O"):
            return(True)
    return(False)

if __name__ == "__main__":
    #Check if valid input
    if(len(sys.argv) <= 1):
        print("Invalid Number of Argument. Please try again")
    
    inputText = ' '.join(sys.argv[1:])

    #Check if English or Braille
    if(isEnglish(inputText)):
        ret = englishToBraille(inputText)
    else:
        ret = brailleToEnglish(inputText)
    print(ret)
