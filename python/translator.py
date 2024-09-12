import sys

braille_int = {
    "capital": ".....O",
    "number": ".O.OOO",
    "space": "......",
}
braille_alpha = {
    "a": "O.....", "b": "O.O...",
    "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO",
    "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
}
braille_num = {
    "1": "O.....", "2": "O.O...",
    "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..",
}
capital = {
    "A", "B", "C", "D",
    "E", "F", "G", "H",
    "I", "J", "K", "L",
    "M", "N", "O", "P",
    "Q", "R", "S", "T",
    "U", "V", "W", "X",
    "Y", "Z",
}
num_braille = {v: k for k, v in braille_num.items()}
alpha_braille = {v: k for k, v in braille_alpha.items()}


def isBraille(s: str):
    for c in s:
        if c != "O" and c != ".":
            return False
    return True


def engToBraille(s: str):
    ans = ""
    prevNum = False
    for i in range(len(s)):
        if s[i] in braille_num:
            ans += (braille_int["number"] if not prevNum else "") + braille_num[s[i]]
            prevNum = True
            continue
        prevNum = False
        if s[i] == " ":
            ans += braille_int["space"]
            continue
        if s[i] in braille_alpha:
            ans += braille_alpha[s[i]]
            continue
        if s[i] in capital:
            ans += braille_int["capital"] + braille_alpha[s[i].lower()]
            continue

    return ans


def brailleToEng(s: str):
    ans = ""
    capitalNext = False
    numberNext = False
    for i in range(0, len(s), 6):
        br = s[i : i + 6]
        if br == braille_int["space"]:
            numberNext = False
            capitalNext = False
            ans += " "
            continue
        if br == braille_int["number"]:
            numberNext = True
            continue
        if br == braille_int["capital"]:
            capitalNext = True
            continue
        if br in num_braille and numberNext:
            ans += num_braille[br]
            continue
        if br in alpha_braille:
            ans += alpha_braille[br].upper() if capitalNext else alpha_braille[br]
            capitalNext = False
            continue
    return ans


sentence = " ".join(sys.argv[1:])
if isBraille(sentence):
    print(brailleToEng(sentence))
else:
    print(engToBraille(sentence))
