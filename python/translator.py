import sys
brailleMap = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.O.',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '.OO...',
    '-': '...O.O',
    '/': '...OO.',
    '<': '.OOO..',
    '>': 'O...OO',
    '(': '...OOO',
    ')': '...OOO',
    ' ': '......',
    'decimalFollow': '.O...O',
    'capFollow': '.....O',
    'numberFollow': '.O.OOO'
}
brailleMapNums = {
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
englishMap = {val: letter for letter, val in brailleMap.items()}
NumsMap = {val: letter for letter, val in brailleMapNums.items()}
def isBraille(text):
    return len(text) % 6 == 0 and all(letter in "O." for letter in text)
def BrailleToEnglish(txt):
    isCapital = False
    isNumber = False
    res = ""
    for i in range(0, len(txt), 6):
        substr = txt[i:i+6]
        translation = englishMap.get(substr, '')
        if translation == 'capFollow':
            isCapital = True
            isNumber = False
        elif translation == 'numberFollow':
            isNumber = True
            isCapital = False
        elif isNumber:
            if substr in NumsMap:
                res += NumsMap[substr]
            else:
                isNumber = False
                res += translation.lower()
        else:
            if isCapital:
                res += translation.upper()
                isCapital = False
            else:
                if translation.isalpha():
                    translation = translation.lower()
                res += translation
    return res                
def EnglishToBraille(txt):
    numberMode = False
    res = ""
    for letter in txt:
        if letter.isdigit():
            if not numberMode:
                res += brailleMap['numberFollow']
                numberMode = True
            res += brailleMapNums.get(letter, '')
        elif letter.isalpha():
            if letter.isupper():
                res += brailleMap['capFollow']
            res += brailleMap.get(letter.upper(), '')
        elif letter == ' ':
            numberMode = False
            res += brailleMap.get(letter, '')
        elif letter == '.' and numberMode:
            res += brailleMap.get('decimalFollow', '')
        else:
            res += brailleMap.get(letter, '')
    return res

"""
Main Function that reads input from stdin, translates from english to braille and vice versa 
and prints the translated output to stdout.
"""
def main():
    args = sys.argv[1:]
    input = ' '.join(args)
    if isBraille(input):
        print(BrailleToEnglish(input))
    else:
        print(EnglishToBraille(input))

if __name__ == "__main__":
    main()
