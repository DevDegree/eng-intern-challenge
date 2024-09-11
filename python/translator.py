import sys
from collections import Counter

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
    " ": "......",
}
# THIS IS THE CORRECT TRANSLATION (ONE INDEXED). THE TEST CASES ARE WRONG (THEY START AT 0)
NUM_TO_BRAILLE = {
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
BRAILLE_TO_ALPHA = dict(reversed(item) for item in ALPHA_TO_BRAILLE.items())
BRAILLE_TO_NUM = dict(reversed(item) for item in NUM_TO_BRAILLE.items())

NUM_TOGGLER = ".O.OOO"
SPACE_TOGGLER = "......"
CAP_TOGGLER = ".....O"


def is_braille(s):
    freq = Counter(s)
    return len(s) % 6 == 0 and len(freq) == 2 and "O" in freq and "." in freq


def convert_braille_to_alpha(s):
    brailles = [s[i : i + 6] for i in range(0, len(s), 6)]
    res = ""
    is_num_toggle = False
    is_upper_toggle = True
    for b in brailles:
        if b == NUM_TOGGLER:
            is_num_toggle = True
            continue
        elif b == CAP_TOGGLER:
            is_upper_toggle = True
            continue
        elif b == SPACE_TOGGLER:
            is_num_toggle = False
        if is_num_toggle:
            res += BRAILLE_TO_NUM[b]
        elif is_upper_toggle:
            res += BRAILLE_TO_ALPHA[b].upper()
            is_upper_toggle = False
        else:
            res += BRAILLE_TO_ALPHA[b]
    return res


def convert_alpha_to_braille(s):
    res = ""
    is_num_toggle = False
    for char in s:
        is_upper = char.isupper()
        char = char.lower()
        if char == " ":  # reset if char is space
            is_num_toggle = False
            res += ALPHA_TO_BRAILLE[char]

        elif char.isdigit():
            if not is_num_toggle:
                is_num_toggle = True
                res += NUM_TOGGLER
            res += NUM_TO_BRAILLE[char]

        elif char.isalpha():
            if is_num_toggle:
                is_num_toggle = False
                res += SPACE_TOGGLER  # add space to escape numbers
            if is_upper:
                res += CAP_TOGGLER
            res += ALPHA_TO_BRAILLE[char]
    return res


def main():
    s = " ".join(sys.argv[1:])
    if is_braille(s):
        print(convert_braille_to_alpha(s))
    else:
        print(convert_alpha_to_braille(s))


if __name__ == "__main__":
    main()
