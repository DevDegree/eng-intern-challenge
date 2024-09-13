# Felix Carpentier

import sys

# Constants needed for the program
ENGLISH_TO_BRAILLE_ALPHABET = {
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

ENGLISH_TO_BRAILLE_NUMBERS = {
    '0': '.OOO..', 
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}

# Reverse dictionnaries for braille to english
BRAILLE_TO_ENGLISH_ALPHABET = {braille:english for english, braille in ENGLISH_TO_BRAILLE_ALPHABET.items()}
BRAILLE_TO_ENGLISH_NUMBERS = {braille:number for number, braille in ENGLISH_TO_BRAILLE_NUMBERS.items()}

BRAILLE_SPACE = '......'
BRAILLE_CAPITAL_FOLLOWS = '.....O'
BRAILLE_NUMBER_FOLLOWS = '.O.OOO'

"""
checkIfBraille will check if the text is only consisted of braille characters and is a multiple of 6

:param text: text that was provided in cli
:return: bool that represents if the text provided is braille or not
"""
def checkIfBraille(text):
    if len(text)%6 != 0:
        return False
    
    for char in text :
        if char not in ['O','.']:
            return False
    
    return True

"""
translateFromBraille will translate every brailleCharacters to english

:param text: text that was provided in cli 
:return: the text provided translated in english (textTranslated)
"""
def translateFromBraille(text):
    capital = False
    numbers = False
    translatedText = ""

    for i in range(0,len(text),6):
        brailleSymbol = text[i:i + 6] 
        if brailleSymbol == BRAILLE_SPACE :
            translatedText += " "
            numbers = False
            continue

        if brailleSymbol == BRAILLE_CAPITAL_FOLLOWS :
            capital = True
            continue
        
        if  brailleSymbol == BRAILLE_NUMBER_FOLLOWS :
            numbers = True
            continue

        if numbers:
            translatedText += BRAILLE_TO_ENGLISH_NUMBERS.get(brailleSymbol)
        
        
        else:
            char = BRAILLE_TO_ENGLISH_ALPHABET.get(brailleSymbol)
            if capital:
                char = char.capitalize()
            translatedText += char
            capital = False

    return translatedText

"""
translateFromEnglish will translate from braille to english while ensuring characters provided are supported

:param text: text that was provided in cli 
:return: the text provided translated in braille (textTranslated)
"""
def translateFromEnglish(text):
    numberFollowsNeeded = True
    translatedText = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                translatedText += BRAILLE_CAPITAL_FOLLOWS
                char = char.lower()
            translatedText += ENGLISH_TO_BRAILLE_ALPHABET.get(char)
            continue
        
        if char.isnumeric():
            if (numberFollowsNeeded):
                translatedText += BRAILLE_NUMBER_FOLLOWS
                numberFollowsNeeded = False
            translatedText += ENGLISH_TO_BRAILLE_NUMBERS.get(char)
            continue
        
        if char == ' ':
            translatedText += BRAILLE_SPACE
            numberFollowsNeeded = True
            continue

        else :
            print("Non supported character was provided")
            sys.exit()
    
    return translatedText

"""
main will check text provided and print the translated one
"""
def main():
    args = sys.argv[1:]

    if not args:
        print("No input provided")
        sys.exit()
    
    translatedText = ""

    text = " ".join(args).strip()
    if checkIfBraille(text):
        translatedText = translateFromBraille(text)
    else:
        translatedText = translateFromEnglish(text)
    
    print(translatedText)

if __name__ == "__main__":
    main()
