import sys

englishToBrailleDict = {
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
    'capital follows': '.....O',
    'number follows': '.O.OOO',
    'space': '......'
}

brailleToEnglishDict = {
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
    'O.....0': '1',
    'O.O...0': '2',
    'OO....0': '3',
    'OO.O..0': '4',
    'O..O..0': '5',
    'OOO...0': '6',
    'OOOO..0': '7',
    'O.OO..0': '8',
    '.OO...0': '9',
    '.OOO..0': '0',
    '.....O': 'capital follows',
    '.O.OOO': 'number follows',
    '......': 'space'
}

def brailleToEnglish(braille):
    text = ""

    capital = False
    number = False

    for i in range(0, len(braille), 6):
        char = braille[i:i+6]

        if brailleToEnglishDict[char] == 'capital follows':
            capital = True
            continue

        if brailleToEnglishDict[char] == 'number follows':
            number = True
            continue

        if brailleToEnglishDict[char] == 'space':
            text += " "
            number = False
            continue

        if capital:
            text += brailleToEnglishDict[char].upper()
            capital = False
        else:
            if number:
                char += '0'

            text += brailleToEnglishDict[char]

    print(text)

def englishToBraille(english):
    braille = ""

    number = False

    for char in english:
        if char.isupper():
            braille += englishToBrailleDict['capital follows']
            char = char.lower()
        elif char.isdigit() and not number:
            braille += englishToBrailleDict['number follows']
            number = True

        if char == " ":
            braille += englishToBrailleDict['space']
            number = False
        else:
            braille += englishToBrailleDict[char]

    print(braille)

def main():
    text = ' '.join(sys.argv[1:])

    if text.strip(".O") == "":
        brailleToEnglish(text)
    else:
        englishToBraille(text)

if __name__ == "__main__":
    main()