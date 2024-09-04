from enum import Enum

class dictionaries:
    brailleSymbols = {'o', '.'}

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
    output = ""
    brailleCharacters = separateBrailleCharacters(input)

def translateEnglishToBraille(input):
    output = ""


def translateInput(input, inputLanguage):
    if inputLanguage == Language.BRAILLE:
        return translateBrailleToEnglish(input)
    elif inputLanguage == Language.ENGLISH:
        return translateEnglishToBraille(input)
    

input = 'ooo...oo..oo'
inputLanguage = detectLanguage(input)
translatedOutput = translateInput(input, inputLanguage)
brailleCharacters = separateBrailleCharacters(input)

print (inputLanguage)
print (brailleCharacters)