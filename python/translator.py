import sys
import collections

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

PUNCT_TO_BRAILLE = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '(': 'O.O..O',
    ')': '.O.OO.',
}
BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUM = {value: key for key, value in NUMBER_TO_BRAILLE.items()}
BRAILLE_TO_PUNCT = {value: key for key, value in PUNCT_TO_BRAILLE.items()}


NUM = ".O.OOO"
SPACE = "......"
CAP = ".....O"


def is_braille(s):
    contains = collections.defaultdict(int)
    for c in s:
        contains[c] += 1
    return len(s) % 6 == 0 and len(contains) == 2

    
def english(s):
    brailles = [s[i : i + 6] for i in range(0, len(s), 6)]
    res = ""
    num_flag = False
    capital_toggle = False
    for b in brailles:
        if b == NUM:
            num_flag = True
            continue
        elif b == CAP:
            capital_toggle = True
            continue
        elif b == SPACE:
            num_flag = False
            res += " "
            continue
        if num_flag:
            res += BRAILLE_TO_NUM.get(b, "")
        else:
            char = BRAILLE_TO_ENGLISH.get(b, "")
            if capital_toggle:
                char = char.upper()
                capital_toggle = False
            res += char
    return res

def braille(s):
    res = ""
    num_flag = False
    for char in s:
        cap = char.isupper()
        char = char.lower()
        if char == " ":  
            num_flag = False
            res += ENGLISH_TO_BRAILLE[char]
        elif char.isdigit():
            if not num_flag:
                num_flag = True
                res += NUM
            res += NUMBER_TO_BRAILLE[char]
        elif char.isalpha():
            if num_flag:
                num_flag = False
                res += SPACE  
            if cap:
                res += CAP
            res += ENGLISH_TO_BRAILLE[char]
        else:
            res += PUNCT_TO_BRAILLE[char]
    return res


def main():
    s = " ".join(sys.argv[1:])
    if is_braille(s):
        print(english(s))
    else:
        print(braille(s))


if __name__ == "__main__":
    main()