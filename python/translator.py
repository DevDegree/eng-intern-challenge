import sys

brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# reverse the brailleDict to get the englishDict
englishDict = {v: k for k, v in brailleDict.items()}

def isBraille(str):
    return all(c in "O." for c in str)

def engToBraille(engStr):
    brailleStr = []
    numFlag = False

    for char in engStr:

        if char.isdigit() and not numFlag:
            numFlag = True
            brailleStr.append(brailleDict['number'])
        elif char.isalpha() and numFlag:
            numFlag = False
            brailleStr.append('......')
        
        if char.isupper():
            brailleStr.append(brailleDict['capital'])
            char = char.lower()

        brailleStr.append(brailleDict.get(char, '......'))
    
    return ''.join(brailleStr)


def main():
    inputStr = ' '.join(sys.argv[1:])

    print(engToBraille(inputStr))

if __name__ == "__main__":
    main()