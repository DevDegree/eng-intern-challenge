import sys

alphaToBrailleDict = {
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
    'z': 'O..OOO'
}
numToBrailleDict = {
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

modifierDict = {
    'capital': '.....O', 
    'number': '.O.OOO'
}

brailleToAlphaDict = {i: j for j, i in alphaToBrailleDict.items()}
brailleToNumDict = {i: j for j, i in numToBrailleDict.items()}



chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ1234567890 '

def isBraille(input): # checks if input string is braille or english
    if any((char in chars) for char in input):
        return False
    else:
        return True
    


# braille -> english
def translateBraille(input):
    inputSplit = [input[i:i+6] for i in range(0, len(input), 6)] # splits input string into groups of 6

    caps, num = False, False

    output = ''

    for char in inputSplit:
        if (char in modifierDict.values()):
            if (char == modifierDict['capital']):
                caps = True
            elif (char == modifierDict['number']):
                num = True

        elif(char == '......'):
            num, caps = False, False
            output += ' '

        elif(num):
            output += brailleToNumDict[char]

        elif(caps):
            output += brailleToAlphaDict[char].upper()
            caps = False

        else:
            output += brailleToAlphaDict[char]

        
    return output
        
# english -> braille
def translateEnglish(input):
    output = ''

    num = False

    for char in input:
        if(char.isdigit()):
            if(not num):
                num = True
                output += modifierDict['number']
            output += numToBrailleDict[char]

        elif(char.isupper()):
            output += modifierDict['capital']
            output += alphaToBrailleDict[char.lower()]
        
        else:
            output += alphaToBrailleDict[char]
    return output


if __name__ == '__main__':

    input = sys.argv[1]

    if (isBraille(input)):
        print(translateBraille(input))

    elif (not isBraille(input)):
        output = ''
        for i in range(1, len(sys.argv)):
            output += (translateEnglish(sys.argv[i]))
            if(i != len(sys.argv)-1):
                output += '......'
        print(output)



