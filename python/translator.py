import sys

# get input string
original = " ".join(sys.argv[1:])


braille = {
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
    "CAP": ".....O",
    "NUM": ".O.OOO",
    " ": "......"
}

brailleNums = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

english = {v: k for k, v in braille.items()}
englishNums = {v: k for k, v in brailleNums.items()}


res = ""

# check if input string is a subset of {".", "O"}
if set(original) <= set([".", "O"]):
    # braille to english
    num = False
    chunked = []

    for i in range(len(original)//6):
        chunked.append(original[6*i:6*i+6])

    i = 0

    while i < len(chunked):
        c = chunked[i]

        if english[c] == "NUM":
            num = True
            i += 1
            continue

        if english[c] == " ":
            num = False

        if num:
            res += englishNums[c]

        elif english[c] == "CAP" and i < len(original) - 1:
            res += english[chunked[i + 1]].upper()
            i += 1

        else:
            res += english[c]

        i += 1

else:
    # english to braille
    num = False

    for c in original:
        if num and c.isdigit():
            res += brailleNums[c]

        elif c.isdigit():
            res += braille["NUM"]
            res += brailleNums[c]
            num = True

        elif c.isupper():
            res += braille["CAP"]
            res += braille[c.lower()]
            num = False

        else:
            res += braille[c]
            num = False

print(res)
