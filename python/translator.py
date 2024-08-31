import sys

# braille: alphabet
brailleAlphabet = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}

# braille: nums
brailleNums = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '.OO..O': '<',
    'O..OO.': '>',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
}

# aphabet: braille
alphabetBraille = {
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
    'z': 'O..OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}

# nums: braille
numsBraille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    '<': '.OO..O',
    '>': 'O..OO.',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

global TABLE_B
TABLE_B = brailleAlphabet # initialize to braille -> alphabet until number follows

global TABLE_E
TABLE_E = alphabetBraille # initialize to aphabet -> braille until number follows

def main():
    # get text
    text = getText()

    # determine if it's braille or english
    braille = isBraille(text)

    # if it's braille convert it to english
    # if it's english convert it to braille
    if braille == True:
        translation = brailleToEnglish(text)
    else:
        translation = englishToBraille(text)

    print(translation)
    return translation

def getText() -> str:
    arglen = len(sys.argv)
    text = ''
    if arglen == 2:
        text = sys.argv[1]
    else:
        i = 1
        while i < arglen:
            text += sys.argv[i]
            if (i + 1) < arglen:
                text += ' '
            i += 1
    return text

def isBraille(text: str) -> bool:
    res = False
    count = 0
    for letter in text:
        count += 1
    if count < 6:
        return res
    brailleCell = text[0:6]
    if (brailleCell in TABLE_B) or (brailleCell == '.....O') or (brailleCell == '.O...O') or (brailleCell == '.O.OOO'):
        res = True
    return res

def brailleToEnglish(text: str) -> str:
    translation = ''
    brailleCell = ''
    capitalize = False
    global TABLE_B
    for letter in text:
        brailleCell += letter
        if len(brailleCell) == 6:
            if brailleCell in TABLE_B:
                if TABLE_B[brailleCell].isalpha() and capitalize == True:
                    # capitalize the current letter since capital follows from previous braille cell 
                    translation += TABLE_B[brailleCell].upper()
                    capitalize = False
                else:
                    translation += TABLE_B[brailleCell]
                    if (TABLE_B[brailleCell] == ' ') and (TABLE_B == brailleNums):
                        # change back to alphabet if there's a space after numbers
                        TABLE_B = brailleAlphabet
            elif brailleCell == '.....O':
                # capital follows
                capitalize = True
            elif brailleCell == '.O...O':
                # decimal follows
                translation += '.'
            elif brailleCell == '.O.OOO':
                # number follows
                TABLE_B = brailleNums
            brailleCell = '' 
            
    return translation

def englishToBraille(text: str) -> str:
    translation = ''
    global TABLE_E
    for i in range(len(text)):
        letter = text[i]
        # print(letter)
        if letter.isalpha() or letter == ' ':
            TABLE_E = alphabetBraille
            if letter.isupper():
                # capital follows
                translation += ('.....O' + TABLE_E[letter.lower()])
            else:
                translation += TABLE_E[letter]
        elif letter.isnumeric() or letter == ' ':
            TABLE_E = numsBraille
            # check to see if number follows after alphabet
            if (i > 0) and (text[i - 1].isnumeric() == False):
                # number does follow after non numeric value
                translation += ('.O.OOO' + TABLE_E[letter])
            else:
                translation += TABLE_E[letter]
        elif letter == '.':
            # decimal follows
            translation += '.O...O'
        # print(translation)
    return translation

main()