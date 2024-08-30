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

    def next(self):
        if not self.has_next():
            return

        x = ""

        for _ in range(6):
            x += self.input[self.i]
            self.i += 1
        self.curr = x

        print(self.curr)

    def has_next(self):
        return self.i < len(self.input)


def handle_braille():
    test = ".O.OOOOO.O..O.O..."
    # test = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O.."
    # ".....O O..... O.O... OO.... ...... .O.OOO O.O... OO.... OO.O.."
    # ".....O O..... O.O... OO.... ...... .O.OOO O.O... OO.... OO.O.."

    lexer = Braille_Lexer(test)
def handle_braille(input):

    out = ""
    is_number = False
    while lexer.has_next():
        is_capital = False
        char = ""

        lexer.next()

        if lexer.curr == ENG_TO_BRAILLE["number"]:
            is_number = True
            continue
        elif lexer.curr == ENG_TO_BRAILLE[" "]:
    return out


def handle_eng(input: str):
    out = ""
            is_number = False
        elif lexer.curr == ENG_TO_BRAILLE["capital"]:
            is_capital = True
            lexer.next()

        if is_number:
            char = BRAILLE_TO_NUMBER[lexer.curr]
        elif is_capital:
            char = BRAILLE_TO_LETTER[lexer.curr].upper()
        else:
            char = BRAILLE_TO_LETTER[lexer.curr]

        out += char
        print(char)

    print(out)
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
