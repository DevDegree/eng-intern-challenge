import sys

# Dictionaries for English and Braille translation
englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "_cap": ".....O", "_num": ".O.OOO", " ": "......"
}

numberToBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Merge number-to-braille into the main dictionary
englishToBraille.update(numberToBraille)

# Reverse dictionary mappings for decoding Braille back to text
brailleToEnglish = {v: k for k, v in englishToBraille.items()}

def convertBraille(braille):
    res = []  # Using list for efficient string concatenation
    isCapital = False
    isNumber = False

    # Iterating through braille in chunks of 6
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        symbol = brailleToEnglish.get(braille_char)

        if symbol == "_cap":
            isCapital = True
            continue
        elif symbol == "_num":
            isNumber = True
            continue
        elif symbol == " ":
            isNumber = False
        
        # Process the character with the appropriate flags
        if isCapital:
            res.append(symbol.capitalize())
            isCapital = False
        elif isNumber:
            res.append(symbol)
        else:
            res.append(symbol)

    return ''.join(res)

def convertEnglish(text):
    braille = []
    isNumber = False

    for char in text:
        if char.isupper():
            braille.append(englishToBraille["_cap"])
            braille.append(englishToBraille[char.lower()])
        elif char.isdigit():
            if not isNumber:
                braille.append(englishToBraille["_num"])
                isNumber = True
            braille.append(englishToBraille[char])
        else:
            isNumber = False
            braille.append(englishToBraille[char])

    return ''.join(braille)

def main():
    text = " ".join(sys.argv[1:])
    
    # Determine if the input is Braille by checking for Braille characters
    isBraille = '.' in text or 'O' in text

    if isBraille:
        print(convertBraille(text))
    else:
        print(convertEnglish(text))

if __name__ == "__main__":
    main()
