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

input = 'FISH'
inputLength = len(input)
inputLanguage = detectLanguage(input)

print (inputLanguage)