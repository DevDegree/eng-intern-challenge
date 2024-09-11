import sys

brailleLetterMap = {
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
    ' ': '......'
}

brailleNumberMap = {
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
}

numberFollow = ".O.OOO"
capitalFollow = ".....O"

reverseBrailleLetterMap = {value: key for key, value in brailleLetterMap.items()}
reverseBrailleNumberMap = {value: key for key, value in brailleNumberMap.items()}

def brailleToText(combinedString):
    i = 0
    numberMode = False
    capitalNext = False

    while i < len(combinedString):
        symbol = combinedString[i:i+6]
        if symbol == numberFollow:
            numberMode = True
        elif symbol == capitalFollow:
            capitalNext = True
        elif symbol == '......':
            print(' ', end='')
            numberMode = False
        else:
            if numberMode:
                print(reverseBrailleNumberMap[symbol], end='')
            else:
                if capitalNext:
                    print(reverseBrailleLetterMap[symbol].upper(), end='')
                    capitalNext = False
                else:
                    print(reverseBrailleLetterMap[symbol], end='')
        i += 6

def textToBraille(combinedString):
    numberMode = False
    for letter in combinedString:
        if letter == ' ':
            print(brailleLetterMap[' '], end='')
            numberMode = False
        elif letter.isdigit():
            if not numberMode:
                numberMode = True
                print(numberFollow, end='')
            print(brailleNumberMap[letter], end='')
        elif letter.isupper():
            print(capitalFollow + brailleLetterMap[letter.lower()], end='')
        else:
            print(brailleLetterMap[letter], end='')


combinedString = ' '.join(sys.argv[1:])
if len(combinedString) % 6 == 0 and all(char in 'O.' for char in combinedString):
    brailleToText(combinedString)
else:
    textToBraille(combinedString)