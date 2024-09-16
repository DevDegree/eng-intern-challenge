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
    'O.....N': '1',
    'O.O...N': '2',
    'OO....N': '3',
    'OO.O..N': '4',
    'O..O..N': '5',
    'OOO...N': '6',
    'OOOO..N': '7',
    'O.OO..N': '8',
    '.OO...N': '9',
    '.OOO..N': '0',
    '.....O': 'capital follows',
    '.O.OOO': 'number follows',
    '......': 'space'
}

def brailleToEnglish(braille):
    text = ""
    number = False
    capital = False

    for i in range(0, len(braille), 6): # each braille letter has 6 characters
        char = braille[i:i+6]

        if brailleToEnglishDict[char] == 'number follows':
            number = True
            continue

        elif brailleToEnglishDict[char] == 'capital follows':
            capital = True
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
                char += 'N'

            text += brailleToEnglishDict[char]

    return(text)

def englishToBraille(english):
    braille = ""

    number = False

    for char in english:
        if char.isdigit() and not number:
            braille += englishToBrailleDict['number follows']
            number = True
        elif char.isupper():
            braille += englishToBrailleDict['capital follows']
            char = char.lower()
        if char == " ":
            braille += englishToBrailleDict['space']
            number = False
        else:
            braille += englishToBrailleDict[char]

    return(braille)

def main():
    text = " ".join(sys.argv[1:])

    if set(text) <= {'0', '.'}: #if text contains only "0" or ".", then it is braille.
        print(brailleToEnglish(text))
    else:
        print(englishToBraille(text))

if __name__ == "__main__":

    main()
