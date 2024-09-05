from enum import Enum

class Language (Enum):
    BRAILLE = 0
    ENGLISH = 1

class Modifier (Enum):
    CAPITAL_FOLLOWS = 0
    NUM_FOLLOWS = 1
    DECIMAL_FOLLOWS = 2

class Dictionaries:
    brailleSymbols = {'o', '.'}

    brailleToEnglish = {
        'o.....': 'a',
        'o.o...': 'b',
        '.o.ooo': Modifier.NUM_FOLLOWS,
        '.....o': Modifier.CAPITAL_FOLLOWS,
        '.o...o': Modifier.DECIMAL_FOLLOWS,
        '......': ' '
        #think about ideas on how to do this in a less manual / error-prone way before continuing
    }

    brailleToNum = {
        'o.....': '1',
    }

    englishToBraille = {
        'a': 'o.....',
        'b': 'o.o...',
        ' ': '......',
        Modifier.NUM_FOLLOWS: '.o.ooo',
        Modifier.CAPITAL_FOLLOWS: '.....o',
        Modifier.DECIMAL_FOLLOWS: '.o...o',
    }

    numToBraille = {
        '1': 'o.....',
    }


def detectLanguage(input):
    for char in input:
        if char not in Dictionaries.brailleSymbols:
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
        translatedChar = Dictionaries.brailleToEnglish[char]
        if isNum and translatedChar not in [Modifier.DECIMAL_FOLLOWS, ' ']:
            translatedChar = Dictionaries.brailleToNum[char] #search the number dictionary instead of the letter / symbol dictionary
            output += translatedChar
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
    translatedChar = ''
    isNum = False
    for n in range(len(input)):
        char = input[n]
        # Periods and decimals
        if char == '.':
            # If current position is not in the middle of a number
            if isNum == False:
                next_char = input[n+1]
                # If current character is a decimal at the beginning of a number
                if next_char.isnumeric():
                    isNum = True
                    output += Dictionaries.englishToBraille[Modifier.NUM_FOLLOWS]
                else:
                    output += Dictionaries.englishToBraille[char]
            # If current position is in the middle of a number
            else:
                output += Dictionaries.englishToBraille[Modifier.DECIMAL_FOLLOWS]

        # Numeric characters
        elif char.isnumeric():
            if isNum == False:
                isNum = True
                output += Dictionaries.englishToBraille[Modifier.NUM_FOLLOWS]
            output += Dictionaries.numToBraille[char]

        # Letters and non-period punctuation
        else:
            # End of numeric characters
            if isNum == True: #Adds a space to signify the end of a number
                isNum = False
                output += Dictionaries.englishToBraille[' ']
        
            # Capitals
            if char.isupper():
                output += Dictionaries.englishToBraille[Modifier.CAPITAL_FOLLOWS]
                output += Dictionaries.englishToBraille[char.lower()]

            # Lowercase or non-period punctuation
            else:
                output += Dictionaries.englishToBraille[char]
        
    return output

def translateInput(input):
    inputLanguage = detectLanguage(input)
    if inputLanguage == Language.BRAILLE:
        return translateBrailleToEnglish(input)
    elif inputLanguage == Language.ENGLISH:
        return translateEnglishToBraille(input)
    
def main():
    input = input("Enter text to translate: ")
    return translateInput(input)
