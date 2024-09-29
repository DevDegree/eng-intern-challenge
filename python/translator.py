import sys

englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "_cap": ".....O", "_num": ".O.OOO", " ": "......"
}

numberToBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

brailleToEnglish = {v: k for k, v in englishToBraille.items()}
brailleToNumber = {v: k for k, v in numberToBraille.items()}

englishToBraille.update(numberToBraille)

def convertBraille(braille):
    english = ""    
    isCapital = False
    isNumber = False
    
    for i in range(0, len(braille), 6):
        letter = brailleToEnglish[braille[i:i+6]]
        
        if letter == "_cap":
            isCapital = True
            continue
        
        elif letter == "_num":
            isNumber = True
            continue
        
        if letter == " ":
            isNumber = False
        if isCapital:
            english += letter.capitalize()
            isCapital = False
        elif isNumber:
            english += brailleToNumber[braille[i:i+6]]
        else:
            english += letter
            
    return english

def convertEnglish(english):
    braille = ""    
    isNumber = False

    for letter in english:
        if letter.isupper():
            braille += englishToBraille["_cap"]
            braille += englishToBraille[letter.lower()]
        
        elif letter.isdigit():
            if not isNumber:
                braille += englishToBraille["_num"]
                isNumber = True
            braille += englishToBraille[letter]
        
        else:
            isNumber = False
            braille += englishToBraille[letter]
            
    return braille

text = " ".join(sys.argv[1:])
isBraille = set(text) == set(["O", "."])

if (isBraille):
    print(convertBraille(text))
else:
    print(convertEnglish(text))