from sys import argv

ENG_TO_BRAILLE = {
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
    " ": "......",
    "capital": ".....O",
    "number": ".O.OOO",
}

BRAILLE_TO_ENG = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
    ".....0": "capital",
    ".O.OOO": "number",
}

BRAILLE_TO_NUMBER = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}


class Braille_Lexer:
    def __init__(self, input) -> None:
        self.input = input
        self.i = 0
        self.is_number = False
        self.is_capital = False

    def next(self):
        if not self.has_next():
            return

        x = ""

        for _ in range(6):
            x += self.input[self.i]
            self.i += 1
        self.curr = x

        self.set_flags()

    def set_flags(self):
        self.is_capital = False
        if self.curr == ENG_TO_BRAILLE["number"]:
            self.is_number = True
            self.next()
        elif self.curr == ENG_TO_BRAILLE[" "]:
            self.is_number = False
        elif self.curr == ENG_TO_BRAILLE["capital"]:
            self.next()
            self.is_capital = True

    def get_char(self):
        if self.is_number:
            return BRAILLE_TO_NUMBER[self.curr]
        elif self.is_capital:
            return BRAILLE_TO_ENG[self.curr].upper()
        else:
            return BRAILLE_TO_ENG[self.curr]

    def has_next(self):
        return self.i < len(self.input)


def handle_braille(input):
    lexer = Braille_Lexer(input)

    out = ""
    while lexer.has_next():
        lexer.next()
        out += lexer.get_char()

    return out


def handle_eng(input: str):
    out = ""
    is_number = False
    for c in input:
        if c.isnumeric():
            if not is_number:
                is_number = True
                out += ENG_TO_BRAILLE["number"]
        elif c == " ":
            is_number = False
        elif c.isupper():
            out += ENG_TO_BRAILLE["capital"]

        out += ENG_TO_BRAILLE[c.lower()]

    return out


def main():
    text = " ".join(argv[1:])

    if is_braille(text):
        print(handle_braille(text))
    else:
        print(handle_eng(text))


def is_braille(text):
    if len(text) < 6:
        return False
    if text == "OOOOOO":
        return True

    for i in range(6):
        if not (text[i] == "O" or text[i] == "."):
            return False

    return True


if __name__ == "__main__":
    main()
