import sys

letter_to_braille = {
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

braille_to_letter = {v: k for k, v in letter_to_braille.items()}


deci_to_braille = {
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


braille_to_decimal = {v: k for k, v in deci_to_braille.items()}

capital = ".....O"
number = ".O.OOO"


def english_to_braille(txt):
    res = ""
    is_num = False
    for c in txt:
        if c.isdigit():
            if not is_num:
                res += number
                is_num = True
            res += deci_to_braille[c]
        else:
            if is_num:
                is_num = False
            if c.isupper():
                res += capital
                c = c.lower()
            res += letter_to_braille[c]
    return res


def braille_to_english(txt):
    res = ""
    chars = [txt[i : i + 6] for i in range(0, len(txt), 6)]
    is_capital = False
    is_num = False
    for c in chars:
        if c == capital:
            is_capital = True
        elif c == number:
            is_num = True
        elif c == letter_to_braille[" "]:
            is_num = False
            is_capital = False
            res += " "
        elif is_num:
            res += braille_to_decimal[c]
        else:
            braille_char = braille_to_letter[c]
            if is_capital:
                braille_char = braille_char.upper()
                is_capital = False
            res += braille_char

    return res


def is_braille(txt):
    return len(txt) % 6 == 0 and all(c == "." or c == "O" for c in txt)


if __name__ == "__main__":
    text = " ".join(sys.argv[1:])
    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))
