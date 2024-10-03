import sys

BRAILLE_TO_ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", ".....O": "capital", ".O...O": "decimal",
    ".O.OOO": "number", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "OOOOOO": ">", "O.O..O": "(",
    ".O.OO.": ")", "......": " "
}

BRAILLE_TO_NUMBERS = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "capital": ".....O", "decimal": ".O...O", "number": ".O.OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "OOOOOO",
    "(": "O.O..O", ")": ".O.OO.", " ": "......"
}

NUMBERS_TO_BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def isBraille(string):
    return all(char in "O." for char in string)


def translateToBraille(string):
    braille = ''
    i = 0
    numberMode = False
    while i < len(string):
        if string[i].isdigit():
            if not numberMode:
                braille += ENGLISH_TO_BRAILLE['number']
                numberMode = True
            braille += NUMBERS_TO_BRAILLE[string[i]]
        # character is a decimal assuming '.' is followed by a number
        elif string[i] == '.' and i+1 < len(string) and string[i+1].isdigit():
            braille += ENGLISH_TO_BRAILLE['decimal']
        elif string[i].isupper():
            braille += ENGLISH_TO_BRAILLE['capital']
            braille += ENGLISH_TO_BRAILLE[string[i].lower()]
        else:
            if numberMode and string[i] == ' ':
                numberMode = False
            braille += ENGLISH_TO_BRAILLE[string[i]]
        i += 1
    return braille

def translateToEnglish(string):
    brailleArray = [string[i:i+6] for i in range (0, len(string), 6)]
    english = ''
    i = 0
    numberMode = False
    while i < len(brailleArray):
        if BRAILLE_TO_ENGLISH[brailleArray[i]] == 'capital':
            # skip capital
            i += 1
            english += BRAILLE_TO_ENGLISH[brailleArray[i]].upper()
            # skip to next letter
            i += 1
        elif BRAILLE_TO_ENGLISH[brailleArray[i]] == 'number':
            if not numberMode:
                numberMode = True
            i += 1
        elif BRAILLE_TO_ENGLISH[brailleArray[i]] == 'space':
            if numberMode:
                numberMode = False
        if numberMode:
            english += BRAILLE_TO_NUMBERS[brailleArray[i]]
        else:
            english += BRAILLE_TO_ENGLISH[brailleArray[i]]
        i += 1
    return english

def main():
    if len(sys.argv) < 2:
        print("Usage: translator.py <message>")
        sys.exit(1)

    input = ' '.join(sys.argv[1:])
    if isBraille(input):
        print(translateToEnglish(input))
    else:
        print(translateToBraille(input))

if __name__ == '__main__':
    main()