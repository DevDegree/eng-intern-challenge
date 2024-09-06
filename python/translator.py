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

#converts Braille text to English
def convertBrailleToEnglish(brailleText): 
    #end result string after conversion
    result = ""
    
    #flag to indicate brailleToNumbers dict should be referenced
    numbersOnly = False

    #flag to indicate that next letter should be capitalized
    capitalize = False

    #symbol set for inputted braille text
    brailleSymbols = [brailleText[i:i+6] for i in range(0, len(brailleText), 6)]

    for symbol in brailleSymbols:
        #accounting for pre-capitalization symbol
        if symbol == '.....O':
            capitalize = True
            continue
        #accounting for pre-number symbol
        elif symbol == '.O.OOO':
            numbersOnly = True
            continue
        #accounting for space symbol, indicating that referencing for numbers is over
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
            try:
                result += brailleToEnglish[symbol]
            except: 
                result += '?'
                
        
    return result


def convertEnglishToBraille(englishText):
    result=""

    #flag to indicate whether numbersToBraille should be referenced or not 
    numberFlag = False

    for char in englishText:
        if char.isupper():
            result += '.....O' + englishToBraille[char.lower()]
        elif char.isnumeric() and numberFlag == False:
            result += '.O.OOO' + numbersToBraille[char]
            numberFlag = True
        elif char.isnumeric() and numberFlag == True:
            result += numbersToBraille[char]
        elif char == ' ':
            result += englishToBraille[char]
            numberFlag = False
        else:
            try:
                result += englishToBraille[char]
            except:
                result += '??????'

    return result

def isBraille(brailleText):

    #length of inputted braille text
    brailleTextLength = len(brailleText)

    #checking if braille length is valid
    if brailleTextLength % 6 != 0 and brailleTextLength > 0:
        return False

    #checking if input text contains valid characters
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
