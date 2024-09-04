from enum import Enum

class dictionaries:
    brailleSymbols = {'o', '.'}
    brailleToEnglish = {
        'o.....': 'a',
        'o.o...': 'b',
        #think about ideas on how to do this in a less manual / error-prone way before continuing
    }

class Language (Enum):
    BRAILLE = 0
    ENGLISH = 1

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
    for char in brailleCharacters:
        translatedChar = dictionaries.brailleToEnglish[char]
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
