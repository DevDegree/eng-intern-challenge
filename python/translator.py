import sys

CAPITAL_FOLLOW = "#"
DECIMAL_FOLLOWS = "##"
NUMBER_FOLLOWS = "###"
SPACE = " "
BRAILLE_CHARACTER_LENGTH = 6
SLICE_OFFSET = 1


def reverseMapping(map: dict) -> dict:
    return {v: k for k, v in map.items()}


ALPHA_BRAILLE_MAPPINGS = {
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
}

BRAILLE_ALPHA_MAPPINGS = reverseMapping(ALPHA_BRAILLE_MAPPINGS)


CONTROL_SYMBOL_BRAILLE_MAPPINGS = {
    CAPITAL_FOLLOW: ".....O",
    DECIMAL_FOLLOWS: ".O...O",
    NUMBER_FOLLOWS: ".O.OOO",
}
BRAILLE_CONTROL_SYMBOL_MAPPINGS = reverseMapping(CONTROL_SYMBOL_BRAILLE_MAPPINGS)

NON_ALPHA_BRAILLE_MAPPINGS = {
    # Challenge only deal with alphabetical and spaces.
    # ".": "..OO.O",
    # ",": "..O...",
    # "?": "..O.OO",
    # "!": "..OOO.",
    # ":": "..OO..",
    # ";": "..O.O.",
    # "-": "....OO",
    # "/": ".O..O.",
    # "<": ".OO..O",
    # ">": "O..OO.",
    # "(": "O.O..O",
    # ")": ".O.OO.",
    SPACE: "......",
}
BRAILLE_NON_ALPHA_MAPPINGS = reverseMapping(NON_ALPHA_BRAILLE_MAPPINGS)

NUMBER_BRAILLE_MAPPINGS = {
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
BRAILLE_NUMBER_MAPPINGS = reverseMapping(NUMBER_BRAILLE_MAPPINGS)


def englishToBraille(string: str) -> str:
    res = ""
    firstNumber = True
    for s in string:
        if s.isalpha():
            if s.isupper():
                res += CONTROL_SYMBOL_BRAILLE_MAPPINGS[CAPITAL_FOLLOW]
            res += ALPHA_BRAILLE_MAPPINGS[s.lower()]
        elif s.isdigit():
            if firstNumber:
                res += CONTROL_SYMBOL_BRAILLE_MAPPINGS[NUMBER_FOLLOWS]
                firstNumber = False
            res += NUMBER_BRAILLE_MAPPINGS[s]
        elif s in NON_ALPHA_BRAILLE_MAPPINGS:
            res += NON_ALPHA_BRAILLE_MAPPINGS[s]
        else:
            raise ValueError(
                "Invalid english character (non-alphanumeric except for spaces)"
            )
    return res


def brailleToEnglish(string: str) -> str:
    res = ""
    number = False
    capitalize = False

    # When slicing substring, the end index does not count, and so, without accounting for
    # the SLICE_OFFSET, we would miss the last substring because range will end at end index - 1.
    # Hence the SLICE_OFFSET
    for i in range(
        BRAILLE_CHARACTER_LENGTH, len(string) + SLICE_OFFSET, BRAILLE_CHARACTER_LENGTH
    ):
        brailleChar = string[i - BRAILLE_CHARACTER_LENGTH : i]

        if brailleChar in BRAILLE_CONTROL_SYMBOL_MAPPINGS:
            symbol = BRAILLE_CONTROL_SYMBOL_MAPPINGS[brailleChar]
            if symbol == NUMBER_FOLLOWS:
                number = True
            elif symbol == CAPITAL_FOLLOW:
                capitalize = True
            elif symbol == DECIMAL_FOLLOWS:
                raise NotImplemented

        elif brailleChar in BRAILLE_NON_ALPHA_MAPPINGS:
            if BRAILLE_NON_ALPHA_MAPPINGS[brailleChar] == SPACE:
                number = False
            res += BRAILLE_NON_ALPHA_MAPPINGS[brailleChar]

        elif number:
            res += BRAILLE_NUMBER_MAPPINGS[brailleChar]

        elif brailleChar in BRAILLE_ALPHA_MAPPINGS:
            if capitalize:
                res += BRAILLE_ALPHA_MAPPINGS[brailleChar].upper()
                capitalize = False
            else:
                res += BRAILLE_ALPHA_MAPPINGS[brailleChar]

        else:
            raise ValueError(
                "Invalid braille character (non-alphanumeric except for spaces)"
            )
    return res


def main(args):
    inputStr = " ".join(args[1:])
    if all(s == "O" or s == "." for s in inputStr):
        print(brailleToEnglish(inputStr))
        return
    print(englishToBraille(inputStr))
    return


main(sys.argv)

