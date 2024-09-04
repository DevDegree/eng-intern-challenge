from enum import Enum

class Language (Enum):
    BRAILLE = 0
    ENGLISH = 1

class Modifier (Enum):
    CAPITAL_FOLLOWS = 0
    NUM_FOLLOWS = 1
    DECIMAL_FOLLOWS = 2

class dictionaries:
    brailleSymbols = {'o', '.'}
    brailleToEnglish = {
        'o.....': 'a',
        'o.o...': 'b',
        '.o.ooo': Modifier.NUM_FOLLOWS,
        '.....o': Modifier.CAPITAL_FOLLOWS,
        '.o...o': Modifier.DECIMAL_FOLLOWS

        #think about ideas on how to do this in a less manual / error-prone way before continuing
    }
    brailleToNum = {
        'o.....': 1,
    }

def detectLanguage(input):
    for char in input:
        if char not in dictionaries.brailleSymbols:
            return Language.ENGLISH
    return Language.BRAILLE

def separateBrailleCharacters(input):
    brailleCharacters = []
    charStart = 0
    charEnd = 6
    inputLength = len(input)
    while charEnd <= inputLength:
        brailleCharacters.append(input[charStart:charEnd])
        charStart += 6
        charEnd +=6
    return brailleCharacters

def translateBrailleToEnglish(input):
    output = ''
    translatedChar = ''
    brailleCharacters = separateBrailleCharacters(input)
    isCapital = False
    isNum = False
    for char in brailleCharacters:
        translatedChar = dictionaries.brailleToEnglish[char]
        if isNum and translatedChar is not Modifier.DECIMAL_FOLLOWS:
            translatedChar = dictionaries.brailleToNum[char] #search the number dictionary instead of the letter / symbol dictionary
            output += str(translatedChar)
        elif isCapital:
            output += translatedChar.upper()
            isCapital = False #only capitalize the character immediately after capital follows symbol
        else:
            if translatedChar == Modifier.CAPITAL_FOLLOWS:
                isCapital = True
            elif translatedChar == Modifier.NUM_FOLLOWS:
                isNum = True
            elif isNum and translatedChar == ' ':
                isNum = False
                output += ' '
            elif translatedChar == Modifier.DECIMAL_FOLLOWS:
                output += '.'
            else:
                output += translatedChar
    return output

def translateEnglishToBraille(input):
    output = ''


def translateInput(input):
    inputLanguage = detectLanguage(input)
    if inputLanguage == Language.BRAILLE:
        return translateBrailleToEnglish(input)
    elif inputLanguage == Language.ENGLISH:
        return translateEnglishToBraille(input)
    

input = input("Enter text to translate: ")
translatedOutput = translateInput(input)
brailleCharacters = separateBrailleCharacters(input)

print (translatedOutput)
