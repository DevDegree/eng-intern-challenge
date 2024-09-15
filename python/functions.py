from braille import *
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


def detect(phrase):
    """
    Detects whether a phrase in written in English or Braille.

    Args:
        phrase (str): The phrase in question

    Returns:
        str literal: either 'english' or 'braille'
    """

    for char in phrase:
        if char not in [Braille.RAISED_DOT, Braille.BLANK_DOT]:
            return 'english'

    return 'braille'

def parseBraille(braille):
    '''
    Parses braille

    Args:
        braille (str): The braille string

    Returns:
        list of tokens (strings)
    '''
    tokens = []

    for i in range(0, len(braille), 6): # Taking chuncks of length 6 (Assuming len(braille) % 6 == 0)
        tokens.append(braille[i:i+6])

    return tokens


def parseEnglish(sentence):
    '''
    Parses English

    Args:
        English (str): The English string

    Returns:
        list of tokens (strings)
    '''
    return [char for char in sentence]


def translateEnglish2Braille(tokens):
    '''
    Returns a list of translated items
    '''

    numberFollowFlag = False
    result = []

    for token in tokens:

        if token in ' ':
            numberFollowFlag = False
            result.append(char2Braille[' '])
            continue

        # Letter is uppercase
        if token in ascii_uppercase:
            result.append(char2Braille['capital_follows'])
            result.append(char2Braille[token.lower()])
            continue

        # Numbers
        if token in digits:
            if not numberFollowFlag:
                numberFollowFlag = True
                result.append(char2Braille['number_follows'])

            result.append(char2Braille[token])
            continue

        # Lowercase and punctuations
        result.append(char2Braille[token])

    return result




def translateBraille2English(tokens):
    '''
    Returns a list of translated items
    '''
    
    result = []
    capitalFlag = False
    numberFlag = False

    for token in tokens:

        translatedToken = braille2Char[token]

        # Space
        if translatedToken == ' ':
            result.append(translatedToken)
            numberFlag = False
            continue

        if translatedToken in ascii_lowercase:
            if capitalFlag:
                result.append(translatedToken.upper())
            elif numberFlag:
                result.append(chr(ord(translatedToken) - 48))
            else:
                result.append(translatedToken)

            capitalFlag = False
            continue

        if translatedToken == 'capital_follows':
            capitalFlag = True
            continue

        if translatedToken == 'number_follows':
            numberFlag = True
            continue

    return result

        

if __name__ == '__main__':
    # tokens = parseEnglish('Hello world')
    # t = translateEnglish2Braille(tokens)

    # print(t)
    # print(parseBraille('.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'))

    tokens = parseBraille('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....')
    print(tokens)
    t = translateBraille2English(tokens)

    print(t)
   