
import sys

ALPHA_TO_BRAILLE = {
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
}

SPECIAL_CHARS = {
    "capital": ".....O",  # Indicator for capitalization
    "number": ".O.OOO",  # Indicator for numbers
    "space": "......",
    
}

NUMBER_TO_BRAILLE = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}


def convertTextToBraille(inputText):
    result = ""
    isNumber = False
    for char in inputText:
        if char.isupper():
            result += SPECIAL_CHARS["capital"]
            char = char.lower()
            result += ALPHA_TO_BRAILLE[char]
        elif char.isdigit():
            if not isNumber:
                isNumber = True
                result += SPECIAL_CHARS["number"]
            result += NUMBER_TO_BRAILLE[char]
        elif char.isspace():
            isNumber = False
            result += SPECIAL_CHARS["space"]
        else:
            result += ALPHA_TO_BRAILLE[char]
    print(result)   
    return result


def convertBrailleToText(inputBraille):
    result = ""
    isNumber = False
    isCapital = False    
    for i in range(0, len(inputBraille), 6):
        char = inputBraille[i : i + 6]        
        if char == SPECIAL_CHARS["capital"]:
            isCapital = True
            continue
        if char == SPECIAL_CHARS["number"]:
            isNumber = True
            continue
        if char == SPECIAL_CHARS["space"]:
            result += " "
            isNumber = False
            continue    
        if isCapital:
            result += list(ALPHA_TO_BRAILLE.keys())[
                list(ALPHA_TO_BRAILLE.values()).index(char)
            ].upper()
            isCapital = False
        elif isNumber:
            result += list(NUMBER_TO_BRAILLE.keys())[
                list(NUMBER_TO_BRAILLE.values()).index(char)
            ]
        else:
            result += list(ALPHA_TO_BRAILLE.keys())[
                list(ALPHA_TO_BRAILLE.values()).index(char)
            ]

    print(result)
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input text")
        print("Usage: python translator.py <text to translate>")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    if all(c in [".", "O"] for c in input_text):
        convertBrailleToText(input_text)
    else:
        convertTextToBraille(input_text)
