import sys

#English to Braille Mapping
englishToBraille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",
    
    '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': '..OOO.', '-':"....OO", 
    '/': ".O..O.", '<': ".O.O.O", '>': "O.O.O.", '(': "O.O..O", ')': ".O.OO.",
    
    ' ': "......"
}

#Numbers to Braille Mapping
numbersToBraille = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
}

#Braille to English Mapping
brailleToEnglish = dict((v,k) for k,v in englishToBraille.items())

#Braille to Numbers Mapping
brailleToNumbers = dict((v,k) for k,v in numbersToBraille.items())

def convertBrailleToEnglish(brailleText): 
    result = ""
    numbersOnly = False
    capitalize = False
    brailleSymbols = [brailleText[i:i+6] for i in range(0, len(brailleText), 6)]

    for symbol in brailleSymbols:
        if symbol == '.....O':
            capitalize = True
            continue
        elif symbol == '.O.OOO':
            numbersOnly = True
            continue
        elif symbol == '......' and numbersOnly == True:
            result += ' '
            numbersOnly = False
            continue

        if capitalize:
            result += brailleToEnglish[symbol].upper()
            capitalize = False
        elif numbersOnly:
            result += brailleToNumbers[symbol]
        else:
            result += brailleToEnglish[symbol]
        
    return result


def convertEnglishToBraille(englishText):
    result=""
    numberFlag = False

    for char in englishText:
        if char.isupper():
            result += '.....O' + englishToBraille[char.lower()]
        elif char.isnumeric() and numberFlag == False:
            result += '.O.OOO' + numbersToBraille[char]
            numberFlag = True
        elif char.isnumeric() and numberFlag == True:
            result += numbersToBraille[char]
        else:
            result += englishToBraille[char]

    return result

def isBraille(brailleText):
    if len(brailleText) % 6 != 0 and len(brailleText) > 0:
        return False

    for char in brailleText:
        if char not in ['.', 'O']:
            return False
    return True

args = sys.argv

textInput = ' '.join(args[1:])

if isBraille(textInput):
    print(convertBrailleToEnglish(textInput))
else: 
    print(convertEnglishToBraille(textInput))

