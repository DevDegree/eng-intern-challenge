import sys

braille_to_english = {
    "O.....": ["a", "1"], "O.O...": ["b", "2"], "OO....": ["c", "3"], "OO.O..": ["d", "4"], "O..O..": ["e", "5"],
    "OOO...": ["f", "6"], "OOOO..": ["g", "7"], "O.OO..": ["h", "8"], ".OO...": ["i", "9"], ".OOO..": ["j", "0"],
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z", "..OO.O": '.', "..O...": ",", "..O.OO": "?", "..OOO.": "!", 
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", 
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")", "......": " ", ".....O": "capital",
    ".O.OOO": "number", ".O...O": "decimal"
}

english_to_braille = {
    "a": "O.....", "1": "O.....", "b": "O.O...", "2": "O.O...", 
    "c": "OO....", "3": "OO....", "d": "OO.O..", "4": "OO.O..", 
    "e": "O..O..", "5": "O..O..", "f": "OOO...", "6": "OOO...", 
    "g": "OOOO..", "7": "OOOO..", "h": "O.OO..", "8": "O.OO..", 
    "i": ".OO...", "9": ".OO...", "j": ".OOO..", "0": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", 
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", 
    "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", 
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", 
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.", 
    "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", 
    " ": "......", "capital": ".....O", "number": ".O.OOO", 
    "decimal": ".O...O"
}

def translate_to_braille(str):
    result = []
    isNum = False
    for char in str:
        if char.isalpha() and char.isupper():
            result.append(english_to_braille["capital"])  # capital
            result.append(english_to_braille[char.lower()])
            isNum = False
        elif char.isdigit():
            if isNum == False:
                result.append(english_to_braille["number"])  # capital
            result.append(english_to_braille[char])
            isNum = True
        else:
            result.append(english_to_braille[char])
            isNum = False
    return ''.join(result)

def translate_to_english(braille):
    result = []
    isNum = False
    isCapital = False
    for i in range(0, len(braille), 6):
        if braille[i:i+6] in braille_to_english:
            if braille_to_english[ braille[i:i+6] ] == "capital":
                isNum = False
                isCapital = True
            elif isCapital:
                result.append(braille_to_english[ braille[i:i+6] ][0].upper())
                isCapital = False
            elif braille_to_english[ braille[i:i+6] ] == "number":
                isNum = True
            elif isNum:
                result.append(braille_to_english[ braille[i:i+6] ][1])
            elif isinstance(braille_to_english[ braille[i:i+6] ], list):
                result.append(braille_to_english[ braille[i:i+6] ][0])
                isNum = False
            else:
                result.append(braille_to_english[ braille[i:i+6] ])
                isNum = False
    return ''.join(result)

def main():
    isBraille = True
    inputStr = ' '.join(sys.argv[1:])
    
    for i in range(0, len(inputStr)):
        if inputStr[i] != 'O' and inputStr[i] != '.':
            isBraille = False
    
    if isBraille:
        return translate_to_english(inputStr)
        
    return translate_to_braille(inputStr)

if __name__ == "__main__":
    print(main(), end='')




