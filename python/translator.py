import sys

engToBraille = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
                "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
                "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
                "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
                "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
                "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
                "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
                "0": ".OOO.."}
brailleToAlph = {}
brailleToNum = {}
for key in engToBraille:
    if key.isnumeric():
        brailleToNum[engToBraille[key]] = key
    else:
        brailleToAlph[engToBraille[key]] = key

capital = ".....O"
decimal = ".O...O"
number = ".O.OOO"
space = "......"

def brailleToEngTranslator(word):
    res = []
    isNum = False
    isCapital = False
    for i in range(0, len(word), 6):
        braille = word[i:i + 6]
        if braille == capital:
            isCapital = True
            continue
        elif braille == number:
            isNum = True
            continue
        elif braille == decimal:
            res.append(".")
            continue
        elif braille == space:
            isNum = False
            res.append(" ")
            continue

        if isCapital:
            res.append(brailleToAlph[braille].upper())
            isCapital = False
        elif isNum:
            res.append(brailleToNum[braille])
        else:
            res.append(brailleToAlph[braille])
    return "".join(res)


def engToBralieTranslator(word):
    res = []
    isNum = False
    for w in word:
        if isNum and w == ".":
            # encounter . when in num mode
            res.append(decimal)
        elif w == " ":
            isNum = False
            res.append(space)
        else:
            if w.isupper():
                res.append(capital)
            elif w.isnumeric() and not isNum:
                isNum = True
                res.append(number)
            res.append(engToBraille[w.lower()])
    return "".join(res)

def isAlphanumeric(word):
    for w in word:
        if not(ord('a') <= ord(w) <= ord('z') or
               ord('A') <= ord(w) <= ord('Z') or
               ord('0') <= ord(w) <= ord('9') or
               w == " "):
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input")
    else:
        word = ' '.join(sys.argv[1:])
        if isAlphanumeric(word):
            print(engToBralieTranslator(word))
        elif all(w in "O." for w in word):
            print(brailleToEngTranslator(word))
        else:
            print("Invalid input")
