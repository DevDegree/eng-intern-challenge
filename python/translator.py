import sys
import re


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
}

UPPER_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE_SPECIAL = "......"

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

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}


def to_english(braille: str) -> str:
    batches = (braille[i : i + 6] for i in range(0, len(braille), 6))
    isUpper = False
    isNumber = False
    out = ""
    for pos, batch in enumerate(batches):
        if batch == UPPER_FOLLOWS:
            isUpper = True
            continue
        elif batch == NUMBER_FOLLOWS:
            isNumber = True
            isUpper = False
            continue
        elif batch == SPACE_SPECIAL:
            isNumber = False
            isUpper = False
            c = " "
        elif isNumber:
            c = BRAILLE_TO_NUMBER.get(batch)
            if not c:
                raise ValueError(
                    f"Expected number at position {pos} but recieved invalid characters {batch}"
                )
        else:
            c = BRAILLE_TO_ENGLISH.get(batch)
            if not c:
                raise ValueError(
                    f"Expected letter at position {pos} but recieved invalid characters {batch}"
                )
            if isUpper:
                isUpper = False
                c = c.upper()
        out += c
    return out


def to_braille(text: str) -> str:
    isNumber = False
    out = ""
    for char in text:
        if char == " ":
            isNumber = False
            out += SPACE_SPECIAL
        elif char.isdigit():
            if not isNumber:
                isNumber = True
                out += NUMBER_FOLLOWS
            out += NUMBER_TO_BRAILLE[char]
        else:
            if isNumber:
                raise ValueError("Numbers must be followed by a space or number")
            if char.isupper():
                out += UPPER_FOLLOWS
            out += ENGLISH_TO_BRAILLE[char.lower()]
    return out


def main() -> None:
    inputStr = " ".join(sys.argv[1:])
    out = ""
    if re.match("^([.O]{6})*$", inputStr):
        # matches braille format required
        out = to_english(inputStr)
    elif re.match("^[a-zA-Z0-9 ]*$", inputStr):
        # matches english format required
        out = to_braille(inputStr)
    else:
        raise ValueError(
            "Input must be braille with chars 'O' and '.' or english with chars a-z, A-Z, 0-9 or ' '"
        )
    sys.stdout.write(out)

main()