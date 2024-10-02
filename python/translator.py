import sys

brailleToAlpha = {
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
}

brailleToNum = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
  }

brailleToSpecialChar = {
    "......": " ",
    '.O....': ',', 
    '.OO...': ';', 
    '.O.O..': ':', 
    '.O.OO.': '.', 
    '.OO.O.': '!', 
    '.OO..O': '?', 
    '..O.O.': '-', 
    '.O.O..': '/', 
    '.O.O.O': '(', 
    'O..O.O': ')', 
    'OO...O': '<', 
    '..OO.O': '>', 
    '.....O': 'capital_indicator', 
    '.O.OOO': 'number_indicator'    
}


alphaToBraille = {v: k for k, v in brailleToAlpha.items()}
numsToBraille = {v: k for k, v in brailleToNum.items()}
specialCharToBraille = {v: k for k, v in brailleToSpecialChar.items()}


def isBraille(text):
    braille = ['.', 'O']

    for char in text:
        if char not in braille:
            return False
    return True


def convert_to_braille(text):
    result = []
    isNumber = False

    for char in text:
        if char.isdigit():
            if not isNumber:
                result.append(specialCharToBraille['number_indicator'])
                isNumber = True
            result.append(numsToBraille[char])
        elif char.isalpha():
            if isNumber:
                isNumber = False
            if char.isupper():
                result.append(specialCharToBraille['capital_indicator'])
            result.append(alphaToBraille[char.lower()])
        elif char == ' ':
            result.append(specialCharToBraille[char])
            isNumber = False

    return ''.join(result)


def convert_to_english(text):
    result = []
    isCapital = False
    isNumber = False

    for i in range(0, len(text), 6):
        brailleChar = text[i:i+6]
        
        if brailleChar == specialCharToBraille['capital_indicator']:
            isCapital = True
            continue
        elif brailleChar == specialCharToBraille['number_indicator']:
            isNumber = True
            continue
        elif brailleChar == "......":  
            result.append(" ")
            isCapital = False
            isNumber = False
            continue

        if isNumber:
            result.append(brailleToNum[brailleChar])
        else:
            letter = brailleToAlpha[brailleChar]

            if isCapital and letter:
                result.append(letter.upper())
                isCapital = False
            else:
                result.append(letter)
    
    return ''.join(result)



def main():
    text = ' '.join(sys.argv[1:])

    if isBraille(text):
        print(convert_to_english(text))
    else:
        print(convert_to_braille(text))


if __name__ == '__main__':
    main()