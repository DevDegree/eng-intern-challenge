import sys

ENGLISH_TO_BRAILLE = {
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
    "n": "..O.O.",
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
}

NUMBER_TO_BRAILLE = {
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

CAPITAL = ".....O"
NUMBER = ".O.OOO"

def englishFromBraille(s):
    # check if length makes for a valid braille string
    if len(inputText) % 6 != 0:
        return None
    
    BRAILLE_TO_ENGLISH = {b:a for a,b in ENGLISH_TO_BRAILLE.items()}
    BRAILLE_TO_NUMBER = {b:a for a,b in NUMBER_TO_BRAILLE.items()}

    res = ""
    i = 0

    while i < len(s):
        el = s[i:i+6]

        if el in BRAILLE_TO_ENGLISH:
            res += BRAILLE_TO_ENGLISH[el]
            i+=6
        elif el == CAPITAL:
            i+=6 # skip capital follows
            el = s[i:i+6]
            res += BRAILLE_TO_ENGLISH[el].upper()
            i+=6
        elif el == NUMBER:
            i+=6 # skip number follows
            subString = ""
            while i+6 <= len(s) and s[i:i+6] in BRAILLE_TO_NUMBER:
                subString += BRAILLE_TO_NUMBER[s[i:i+6]]
                i+=6
            
            # must include a number + assume space after if not end of string
            if len(subString) == 0 or \
                (i+6 <= len(s) and s[i:i+6] != ENGLISH_TO_BRAILLE[" "]):
                return None
            
            res += subString
        else:
            # symbol not found (no behaviour provided)
            return None
    
    return res

def brailleFromEnglish(s):
    res = ""
    i = 0

    while i < len(s):
        el = s[i]
        if el in ENGLISH_TO_BRAILLE:
            # lower case character
            res += ENGLISH_TO_BRAILLE[el]
            i+=1
        elif el.lower() in ENGLISH_TO_BRAILLE:
            # upper case character
            res += CAPITAL
            res += ENGLISH_TO_BRAILLE[el.lower()]
            i+=1
        elif el in NUMBER_TO_BRAILLE:
            res += NUMBER

            while i < len(s) and s[i] in NUMBER_TO_BRAILLE:
                res += NUMBER_TO_BRAILLE[s[i]]
                i+=1
            
            # fails assume space character after number (no behaviour provided)

        else:
            # unknown symbol (no behaviour provided), skip for no TLE
            i+=1

    return res

if __name__ == '__main__':
    inputText = " ".join(sys.argv[1:])

    # attempt to convert from braille if fails then assume english
    outputText = englishFromBraille(inputText)

    # fails at converting braille hence assume it is english
    if not outputText:
        outputText = brailleFromEnglish(inputText)

    print(outputText)
