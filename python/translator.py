import sys

# Dictionaries and constants
LETTER_TO_BRAILLE = {
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

NUMBER_TO_LETTER = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    0: 'j'
}

CAPITAL = '.....O'
NUMBER = '.O.OOO'

def isBraille(s: str) -> bool:
    return all(c == 'O' or c == '.' for c in s)

def brailleToEnglish(b: str) -> str:
    output = ''
    brailleLetters = list(LETTER_TO_BRAILLE.values())
    letterKeys = list(LETTER_TO_BRAILLE.keys())
    isCapital = False
    isNumber = False
    for i in range(0, len(b), 6):
        cell = b[i:i+6]
        if cell == CAPITAL:
            isCapital = True
        elif cell == NUMBER:
            isNumber = True
        elif (cell == '......'):
            isNumber = False
            output += ' '
        elif isNumber:
            output += str((brailleLetters.index(cell) + 1) % 10)
        elif isCapital:
            output += letterKeys[brailleLetters.index(cell)].upper()
            isCapital = False
        else:
            output += letterKeys[brailleLetters.index(cell)]
    return output

def englishToBraille(e: str) -> str:
    output = ''
    isNumber = False
    brailleLetters = list(LETTER_TO_BRAILLE.values())
    for c in e:
        if c.isdigit() and not isNumber:
            isNumber = True
            output += NUMBER + LETTER_TO_BRAILLE[NUMBER_TO_LETTER[int(c)]]
        elif c.isdigit():
            output += LETTER_TO_BRAILLE[NUMBER_TO_LETTER[int(c)]]
        elif c == ' ':
            output += '......'
            isNumber = False
        elif c.isupper():
            output += CAPITAL + LETTER_TO_BRAILLE[c.lower()]
        elif c in LETTER_TO_BRAILLE:
            output += LETTER_TO_BRAILLE[c]
    return output

def main():
    input = ' '.join(sys.argv[1:])
    if isBraille(input):
        print(brailleToEnglish(input))
    else:
        print(englishToBraille(input))

if __name__ == '__main__':
    main()
