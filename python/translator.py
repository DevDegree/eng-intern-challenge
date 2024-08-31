import sys
from constants import *
from typing import List


class InvalidBrailleException(Exception):
    def __init__(self, message, invalid_string):
        super().__init__(message)
        self.invalid_string = invalid_string

    def __str__(self):
        return f"{self.args[0]}: '{self.invalid_string}'"


class InvalidEnglishException(Exception):
    def __init__(self, message, invalid_string):
        super().__init__(message)
        self.invalid_string = invalid_string

    def __str__(self):
        return f"{self.args[0]}: '{self.invalid_string}'"


def is_braille(args: List[str]) -> bool:
    # assuming that braille can only be inputted as a single string
    if len(args) > 1:
        return False

    if len(args) == 1:
        # check that the string only contains '.' and 'O' and is of a valid length
        return set(args[0]) == {".", "O"} and len(args[0]) % 6 == 0

    return False


def braille_to_english(string: str) -> str:
    res = []
    l = 0
    is_capital = is_number = False
    # sliding window approach iterating through the array by chunks of length 6
    for r in range(6, len(string) + 1, 6):
        cur = string[l:r]

        if cur == SPACE:
            is_number = False
            res.append(" ")

        elif cur == CAPITAL_FOLLOWS:
            is_capital = True

        elif cur == NUMBER_FOLLOWS:
            is_number = True

        elif is_number:
            if cur in BRAILE_TO_NUMBER:
                res.append(BRAILE_TO_NUMBER[cur])
            else:
                raise InvalidBrailleException(
                    "a non-number has been detected inside a number", cur
                )

        elif cur in BRAILLE_TO_CHAR:
            if is_capital:
                res.append(BRAILLE_TO_CHAR[cur].upper())
                is_capital = False
            else:
                res.append(BRAILLE_TO_CHAR[cur])

        else:
            raise Exception("an invalid braille character has been detected", cur)

        l += 6

    return "".join(res)


def english_to_braille(strings: List[str]) -> str:
    res = []

    for string in strings:
        cur = []
        is_number = False

        for c in string:
            if c.isupper():
                cur.append(CAPITAL_FOLLOWS)
                cur.append(CHAR_TO_BRAILLE[c.lower()])

            elif c.isnumeric():
                if not is_number:
                    cur.append(NUMBER_FOLLOWS)
                    is_number = True

                cur.append(NUMBER_TO_BRAILLE[c])

            elif c in CHAR_TO_BRAILLE:
                cur.append(CHAR_TO_BRAILLE[c])

            else:
                raise InvalidEnglishException(
                    "an unsupported character has been detected", c
                )

        res.append("".join(cur))

    return SPACE.join(res)


def main():
    args = sys.argv[1:]
    if is_braille(args):
        print(braille_to_english(args[0]))
    else:
        print(english_to_braille(args))


if __name__ == "__main__":
    main()
