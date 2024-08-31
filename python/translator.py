import sys

BrailleCharacters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    ' ': '......', '.': '..OO.O', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.'
}

CapitalFollows = '.....O'
DecimalFollows = '.O...O'
NumberFollows = '.O.OOO'

def EngOrBrail(args):
    for arg in args:
        for char in arg:
            if char.lower() not in ['o', '.', ' ']:
                return "English"
    return "Braille"

def convertToBraille(String):
    length = len(String)
    numMode = False
    for j in range(length):
        if String[j].isupper():
            print(CapitalFollows, end='')
            print(BrailleCharacters.get(String[j].lower()), end='')
            numMode = False
        elif String[j].isdigit():
            if not numMode:
                print(NumberFollows, end='')
                numMode = True
            print(BrailleCharacters.get(String[j]), end='')
        elif String[j] == ' ':
            print(BrailleCharacters.get(' '), end='')
            numMode = False
        else:
            print(BrailleCharacters.get(String[j]), end='')
            numMode = False

def convertToEnglish(String):
    length = len(String)
    i = 0
    numMode = False
    
    while i < length:
        curBraiChar = String[i:i+6]
        if curBraiChar == CapitalFollows:
            i += 6
            nextBraiChar = String[i:i+6]
            for key, value in BrailleCharacters.items():
                if value == nextBraiChar:
                    print(key.upper(), end='')
                    break
            i += 6
        elif curBraiChar == NumberFollows:
            numMode = True
            i += 6
        elif curBraiChar == BrailleCharacters[' ']:
            print(' ', end='')
            numMode = False
            i += 6
        else:
            if numMode:
                for key, value in BrailleCharacters.items():
                    if value == curBraiChar and key.isdigit():
                        print(key, end='')
                        break
            else:
                for key, value in BrailleCharacters.items():
                    if value == curBraiChar:
                        print(key, end='')
                        break
            i += 6

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    conversion_type = EngOrBrail(sys.argv[1:])
    if conversion_type == "English":
        for index, arg in enumerate(sys.argv[1:]):
            if index > 0:
                print(BrailleCharacters.get(' '), end='')
            convertToBraille(arg)
    else:
        for index, arg in enumerate(sys.argv[1:]):
            if index > 0:
                print(" ", end='')
            convertToEnglish(arg)

    sys.exit(0)
