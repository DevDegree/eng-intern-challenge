# problems found:
# output for sample test case is wrong
# Braille alphabet for "o" and ">" are the same


engToBraille = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
                "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
                "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
                "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
                "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
                "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
                "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
                "0": ".OOO..", ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.",
                ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O",
                "(": "O.O..O", ")": ".O.OO."}
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("input error")




print(brailleToEngTranslator(".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO"))

# Abc 12.3 -> .....OO.....O.O...OO...........O.OOOO.....O.O....O...OOO....
# AaBC     -> .....OO.....O..........OO.O........OOO....
# 12 Ya.y  -> .O.OOOO.....O.O..............OOO.OOOO.......OO.OOO.OOO
# 0        -> .O.OOO.OOO..
# A        -> .....OO.....
# ./       -> ..OO.O.O..O.
# ( 09 ) ? -> O.O..O.......O.OOO.OOO...OO..........O.OO.........O.OO
# ;.234.9 : -> ..O.O...OO.O.O.OOOO.O...OO....OO.O...O...O.OO...........OO..
# Hello world -> .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
# Abc 123 xYz -> .....O  O.....  O.O...  OO....  ......  .O.OOO  O.....  O.O...  OO....  ......  OO..OO  .....O  OO.OOO  O..OOO

#                .....O  O.....  O.O...  OO....  ......  .O.OOO  O.O...  OO.... OO.O..   ......  OO..OO  .....O  OO.OOO  O..OOO
