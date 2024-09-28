import sys

ENGLISH_KEY_ALPHA = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", "capital": ".....O",
    "number": ".O.OOO", " ": "......"
}

ENGLISH_KEY_NUMS = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...",  "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO..."
}

BRAILLE_KEY_ALPHA = {ENGLISH_KEY_ALPHA[i]: i for i in ENGLISH_KEY_ALPHA.keys()}
BRAILLE_KEY_NUMS = {ENGLISH_KEY_NUMS[i]: i for i in ENGLISH_KEY_NUMS.keys()}

def checkBraille(inp):
    return all(c in {'.', 'O'} for c in inp) and len(inp) % 6 == 0

def englishToBraille(inp):
    ans = ""
    num_added = False
    for c in inp:
        if c.isupper():
            ans += ENGLISH_KEY_ALPHA["capital"]
            ans += ENGLISH_KEY_ALPHA[c.lower()]
        elif c.isdigit():
            if not num_added:
                ans += ENGLISH_KEY_ALPHA["number"]
                num_added = True
            ans += ENGLISH_KEY_NUMS[c]
        else:
            if c == " ":
                num_added = False
            ans += ENGLISH_KEY_ALPHA[c]

    return ans

def brailleToEnglish(inp):
    ans = ""
    num_added = False
    cap_now = False

    braille = [inp[i:i+6] for i in range(0, len(inp), 6)]

    for b in braille:
        if b == ENGLISH_KEY_ALPHA["capital"]:
            cap_now = True
            continue
        elif b == ENGLISH_KEY_ALPHA["number"]:
            num_added = True
            continue
        elif b == ENGLISH_KEY_ALPHA[" "]:
            num_added = False
            ans += " "
            continue
        if cap_now:
            ans += BRAILLE_KEY_ALPHA[b].upper()
            cap_now = False
        elif num_added:
            ans += BRAILLE_KEY_NUMS[b]
        else:
            ans += BRAILLE_KEY_ALPHA[b]

    return ans

if __name__ == '__main__':
    inp = ' '.join(sys.argv[1:])
    # 2 conditions for braille: 6 characters long and only contains '.' and '0'
    if checkBraille(inp):
        print(brailleToEnglish(inp))
    else:
        print(englishToBraille(inp))
