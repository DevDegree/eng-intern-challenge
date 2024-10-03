import sys
# Braille to Eng
ENGLISH_TO_BRAILLE_CHAR = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "CAPITAL": ".....O", "NUMBER": ".O.OOO", " ": "......",
}

ENGLISH_TO_BRAILLE_NUM = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

# Eng to Braille
BRAILLE_TO_ENGLISH_CHAR = {v: k for k, v in ENGLISH_TO_BRAILLE_CHAR.items()}

BRAILLE_TO_ENGLISH_NUM = {v: k for k, v in ENGLISH_TO_BRAILLE_NUM.items()}

def isBraille(text):
    return all(char in 'O.' for char in text)

def brailleToEnglish(braille):
    res = []
    isCapital, isNumber = False, False
    for i in range(0, len(braille), 6):
        segment = braille[i:i+6]
        if segment == ENGLISH_TO_BRAILLE_CHAR["CAPITAL"]:
            isCapital = True
        elif segment == ENGLISH_TO_BRAILLE_CHAR["NUMBER"]:
            isNumber = True
        elif segment == ENGLISH_TO_BRAILLE_CHAR[" "]:
            isNumber = False
            res.append(" ")
        else:
            if isNumber:
                res.append(BRAILLE_TO_ENGLISH_NUM[segment])
            elif isCapital:
                res.append(BRAILLE_TO_ENGLISH_CHAR[segment].upper())
                isCapital = False
            else:
                res.append(BRAILLE_TO_ENGLISH_CHAR[segment])
    return "".join(res)
        
def englishToBraille(english):
    res = []
    isNumber = False
    for char in english:
        if char == " ":
            res.append(ENGLISH_TO_BRAILLE_CHAR[" "])
            isNumber = False
        elif char.isdigit():
            if not isNumber:
                isNumber = True
                res.append(ENGLISH_TO_BRAILLE_CHAR["NUMBER"])
            res.append(ENGLISH_TO_BRAILLE_NUM[char])
        elif char.isalpha():
            if char.isupper():
                res.append(ENGLISH_TO_BRAILLE_CHAR["CAPITAL"])
            res.append(ENGLISH_TO_BRAILLE_CHAR[char.lower()])
            isNumber = False
    return "".join(res)
            
def main():
    if (len(sys.argv) > 1):
        ## formalize input string 
        input = " ".join(sys.argv[1:]) 
        if isBraille(input): 
            print(brailleToEnglish(input))
        else: 
            print(englishToBraille(input))
    else:
        print("No input for translator")

if __name__ == '__main__':
	main()