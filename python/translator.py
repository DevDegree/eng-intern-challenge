import sys

brailleAlphabet = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
}

brailleNumbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
    "......": " ",
}

letterTranslator = {
"0": ".....O",
"1": ".O.OOO",
"a": "O.....",
"b": "O.O...",
"c": "OO....",
"d": "OO.O..",
"e": "O..O..",
"f": "OOO...",
"g": "OOOO..",
"h": "O.OO..",
"i": ".OO...",
"j": ".OOO..",
"k": "O...O.",
"l": "O.O.O.",
"m": "OO..O.",
"n": "OO.OO.",
"o": "O..OO.",
"p": "OOO.O.",
"q": "OOOOO.",
"r": "O.OOO.",
"s": ".OO.O.",
"t": ".OOOO.",
"u": "O...OO",
"v": "O.O.OO",
"w": ".OOO.O",
"x": "OO..OO",
"y": "OO.OOO",
"z": "O..OOO",
" ": "......",
"1": "O.....",
"2": "O.O...",
"3": "OO....",
"4": "OO.O..",
"5": "O..O..",
"6": "OOO...",
"7": "OOOO..",
"8": "O.OO..",
"9": ".OO...",
"0": ".OOO..",
}

def translateBraille(chars):
    translatedText = ""
    numberStart = False
    for char in chars:
        if char.isupper():
            translatedText += ".....O"
            numberStart = False
        elif char.isnumeric() and not numberStart:
            numberStart = True
            translatedText += ".O.OOO"
        elif not char.isnumeric() and numberStart:
            numberStart = False
        translatedText += letterTranslator[char.lower()]
    return translatedText

def translateLetters(chars):
    pointer1 = 0
    pointer2 = 6
    alpha = True
    translatedText = ""

    while pointer2 <= len(chars):
        char = chars[pointer1:pointer2]
        if char == ".....O":
            alpha = True
            pointer2 += 6
            pointer1 += 6
            char = chars[pointer1:pointer2]
            translatedText += brailleAlphabet[char].upper()
        elif char == ".O.OOO":
            alpha = False
            pointer2 += 6
            pointer1 += 6
            char = chars[pointer1:pointer2]
            translatedText += brailleNumbers[char]
        elif char == "......":
            translatedText += brailleAlphabet[char]
            alpha = True
        else:
            if alpha:
                translatedText += brailleAlphabet[char]
            else:
                translatedText += brailleNumbers[char]
        pointer2 += 6
        pointer1 += 6
    return translatedText


def translate(letters):
    if len(letters.replace("O", "").replace(".", "")) == 0:
        return translateLetters(letters)
    else:
        return translateBraille(letters)


if __name__ == '__main__':

    sentence = " ".join(sys.argv[1:])
    print(translate(sentence), end='')