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

def translateBrailleToEnglish(input):


def translateEnglishToBraille(input):


def translateInput(input, inputLanguage):
    if inputLanguage == Language.BRAILLE:
        return translateBrailleToEnglish(input)
    elif inputLanguage == Language.ENGLISH:
        return translateEnglishToBraille(input)
    

input = 'FISH'
inputLength = len(input)
inputLanguage = detectLanguage(input)
translatedOutput = translateInput(input, inputLanguage)

print (inputLanguage)