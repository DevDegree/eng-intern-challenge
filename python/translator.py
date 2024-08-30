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

BRAILLE_TO_LETTER = {v: k for k, v in ENG_TO_BRAILLE.items() if not k.isnumeric()}

BRAILLE_TO_NUMBER = {v: k for k, v in ENG_TO_BRAILLE.items() if k.isnumeric()}


class Braille_Lexer:
    def __init__(self, input) -> None:
        # input to scan
        self.input = input

        # pointer to next char to scan
        self.i = 0

        # flags for scanning
        self.is_number = False
        self.is_capital = False

    def next(self):
        # don't scan if at end
        if not self.has_next():
            return

        # scan next token
        self.curr = ""

        for _ in range(6):
            self.curr += self.input[self.i]
            self.i += 1

        # update flags
        self.set_flags()

    def set_flags(self):
        # reset is capital on each scan
        self.is_capital = False

        # handle special tokens
        if self.curr == ENG_TO_BRAILLE["number"]:
            self.is_number = True
            self.next()
        elif self.curr == ENG_TO_BRAILLE[" "] and self.is_number:
            self.is_number = False
        elif self.curr == ENG_TO_BRAILLE["capital"]:
            self.next()
            self.is_capital = True

    def get_char(self):
        # return english translation of current token
        if self.is_number:
            return BRAILLE_TO_NUMBER[self.curr]
        elif self.is_capital:
            return BRAILLE_TO_LETTER[self.curr].upper()
        else:
            return BRAILLE_TO_LETTER[self.curr]

    def has_next(self):
        # determine if scan is at end
        return self.i < len(self.input)


def handle_braille(input):
    # lexer to scan braille
    lexer = Braille_Lexer(input)

    # start braille scan
    out = ""
    while lexer.has_next():
        lexer.next()
        out += lexer.get_char()

    return out


def handle_eng(input: str):
    out = ""
    is_number = False
    for c in input:
        # handle and mark special tokens
        if c.isnumeric():
            if not is_number:
                is_number = True
                out += ENG_TO_BRAILLE["number"]
        elif c == " ":
            is_number = False
        elif c.isupper():
            out += ENG_TO_BRAILLE["capital"]

        # add char to output
        out += ENG_TO_BRAILLE[c.lower()]

    return out


def is_braille(text: str):
    # ASSUMPTION: "OOOOOO" is an english string since no braille matches in legend
    # ASSUMPTION: If a string starts with a valid braille token, the rest of the string is assumed to be braille (no mixing)

    # a valid braille string must have a length as a multiple of 6
    if len(text) < 6 or len(text) % 6 != 0 or text.startswith("OOOOOO"):
        return False

    # check if text starts with a valid braille token
    for i in range(6):
        if text[i] != "O" and text[i] != ".":
            return False

    return True


def main():
    if len(argv) < 2:
        print(
            "No input recieved to translate, please input an english or braille string"
        )
        return

    # ASSUMPTION: only valid braille or english strings are passed in
    text = " ".join(argv[1:])

    if is_braille(text):
        print(handle_braille(text))
    else:
        print(handle_eng(text))


if __name__ == "__main__":
    main()
