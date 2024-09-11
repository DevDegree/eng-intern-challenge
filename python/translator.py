import sys

BrailleToEng = {
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
    ".....O": "shift",
    ".O...O": "decimal",
    ".O.OOO": "num"
}

EngToBraille = {BrailleToEng[a]:a for a in BrailleToEng}

BrailleToNum = {
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
}

NumToBraille = {BrailleToNum[a]:a for a in BrailleToNum}

def translateBraille(string):
    res = ""
    isCaps = False
    isNum = False
    isDec = False
    for i in range(0, len(string)//6):
        segment = string[6*i:6*i+6]
        token = BrailleToEng[segment]
        if token == "shift":
            isNum = isDec = False
            isCaps = True
        elif token == "num":
            isCaps = isDec = False
            isNum = True
        elif token == "decimal":
            isCaps = isNum = False
            isDec = True
        else:
            if isCaps and token.isalpha():
                res += token.capitalize()
            elif isNum or isDec:
                if isDec and token == ".":
                        res += token
                elif segment in BrailleToNum:
                    res += BrailleToNum[segment]
                else:
                    isNum = isDec = False
                    res += token
            else:
                res += token
            isCaps = False
    return res
               

def translateEnglish(string):
    res = ""
    isNum = False
    for letter in string:
        if letter.isnumeric():
            if not isNum:
                res += EngToBraille["num"]
                isNum = True
            res += NumToBraille[letter]
        else:
            isNum = False
            if letter.isupper():
                res += EngToBraille["shift"]
            res += EngToBraille[letter.lower()]
    return res

def translate(string):
    if len(string) % 6 == 0:
        for char in string:
            if char != 'O' or char != '.':
                return translateBraille(string)
    return translateEnglish(string)
    
if __name__ == "__main__":
    inputStr = ' '.join(sys.argv[1:])
    print(translate(inputStr))
