import sys

braille_set = set("O.")

br_en_table = [
    ["O.....", "a", "1"],
    ["O.O...", "b", "2"],
    ["OO....", "c", "3"],
    ["OO.O..", "d", "4"],
    ["O..O..", "e", "5"],
    ["OOO...", "f", "6"],
    ["OOOO..", "g", "7"],
    ["O.OO..", "h", "8"],
    [".OO...", "i", "9"],
    [".OOO..", "j", "0"],
    ["O...O.", "k"],
    ["O.O.O.", "l"],
    ["OO..O.", "m"],
    ["OO.OO.", "n"],
    ["O..OO.", "o"],
    ["OOO.O.", "p"],
    ["OOOOO.", "q"],
    ["O.OOO.", "r"],
    [".OO.O.", "s"],
    [".OOOO.", "t"],
    ["O...OO", "u"],
    ["O.O.OO", "v"],
    [".OOO.O", "w"],
    ["OO..OO", "x"],
    ["OO.OOO", "y"],
    ["O..OOO", "z"],
    [".....O", "CAP"],
    [".O.OOO", "NUM"],
    ["......", " "],
    # ".O...O": "DEC",
    # "..OO.O": ".",
    # "..O...": ",",
    # "..O.OO": "?",
    # "..OOO.": "!",
    # "..OO..": ":",
    # "..O.O.": ";",
    # "....OO": "-",
    # ".O..O.": "/",
    # ".OO..O": "<",
    # "O..OO.": ">",
    # "O.O..O": "(",
    # ".O.OO.": ")",
]


def lookup(key: str, number: bool = False) -> str:
    braille = len(key) == 6
    for item in br_en_table:
        if braille:
            if key == item[0]:
                return item[1] if not number else item[2]
        else:
            k = item[2] if key.isnumeric() else item[1]
            if key == k:
                return item[0]
    return "?"


def eng_to_braille(en: str) -> str:
    braille = ""
    number = False
    for char in en:
        if char.isupper():
            braille += lookup("CAP")
            char = char.lower()
        if char.isnumeric() and not number:
            braille += lookup("NUM")
            number = True
        if char == " ":
            number = False
        braille += lookup(char)
    return braille


def braille_to_eng(br: str) -> str:
    message = ""
    capital = False
    number = False
    for i in range(0, len(br), 6):
        char = br[i : i + 6]
        val = lookup(char, number)
        if val == "CAP":
            capital = True
        elif val == "NUM":
            number = True
        else:
            if capital:
                val = val.upper()
                capital = False
            elif val == " ":
                number = False
            message += val
    return message


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translatorOpy <text>")
        sys.exit(1)
    text = " ".join(sys.argv[1:])
    if len(text) % 6 != 0 or set(text) != braille_set:
        print(eng_to_braille(text))
    else:
        print(braille_to_eng(text))
