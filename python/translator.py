
import sys

brailleToLetter = {
    'O.....' : 'a',
    'O.O...' : 'b',
    'OO....' : 'c',
    'OO.O..' : 'd',
    'O..O..' : 'e',
    'OOO...' : 'f',
    'OOOO..' : 'g',
    'O.OO..' : 'h',
    '.OO...' : 'i',
    '.OOO..' : 'j',
    'O...O.' : 'k',
    'O.O.O.' : 'l',
    'OO..O.' : 'm',
    'OO.OO.' : 'n',
    'O..OO.' : 'o',
    'OOO.O.' : 'p',
    'OOOOO.' : 'q',
    'O.OOO.' : 'r',
    '.OO.O.' : 's',
    '.OOOO.' : 't',
    'O...OO' : 'u',
    'O.O.OO' : 'v',
    '.OOO.O' : 'w',
    'OO..OO' : 'x',
    'OO.OOO' : 'y',
    'O..OOO' : 'z',
    '..OO.O' : '.',
    '..O...' : ',',
    '..O.OO' : '?',
    '..OOO.' : '!',
    '..OO..' : ':',
    '..O.O.' : ';',
    '....OO' : '-',
    '.O..O.' : '/',
    '.OO..O' : '<',
    'O..OO.' : '>',
    'O.O..O' : '(',
    '.O.OO.' : ')',
    '......' : ' ',
    '.....O' : 'capitalize',
    '.O.OOO' : 'number'
}

brailleToNumber = {
    'O.....' : '1',
    'O.O...' : '2',
    'OO....' : '3',
    'OO.O..' : '4',
    'O..O..' : '5',
    'OOO...' : '6',
    'OOOO..' : '7',
    'O.OO..' : '8',
    '.OO...' : '9',
    '.OOO..' : '0'
}

transToBraille = {
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
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

def engToBraille(input):
    translated = ""
    checkNum = False
    for c in input:
        if c.isdigit():
            if checkNum == False:
                translated += '.O.OOO'
            checkNum = True
            translated += transToBraille[c]
        elif c.isalpha():
            checkNum = False
            if c.isupper():
                translated += '.....O'
            translated += transToBraille[c.lower()]
        else:
            translated += transToBraille[c]
    
    return translated


def brailleToEng(input):
    left, right = 0, 5
    checkNum = False
    translated = ""
    while right < len(input):
        if checkNum == True:
            if input[left:right+1] == '......':
                checkNum = False
                translated += " "
            else:
                translated += brailleToNumber[input[left:right+1]]
        else:
            temp = brailleToLetter[input[left:right+1]]
            if temp == 'capitalize':
                left += 6
                right += 6
                translated += (brailleToLetter[input[left:right+1]]).upper()
            elif temp == 'number':
                checkNum = True
            else:
                translated += brailleToLetter[input[left:right+1]]
        left += 6
        right += 6 
    
    return translated


if __name__ == "__main__":
    if len(sys.argv) > 1:
        inputString = ' '.join(sys.argv[1:])
    else:
        print("No string was provided as an argument.")

    if any(c not in "O." for c in inputString):
        print(engToBraille(inputString))
    else:
        print(brailleToEng(inputString))