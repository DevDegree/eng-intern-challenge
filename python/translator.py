from sys import argv
from enum import Enum
from itertools import batched
from collections.abc import Iterator

# Each decade in the Braille system shares the same ten squares of data, here
# called the "core". Each decade is obtained by appending (or in the case of the
# fifth decade, prepending) the final two symbols.
decade_core: list[str] = [
    "O...",
    "O.O.",
    "OO..",
    "OO.O",
    "O..O",
    "OOO.",
    "OOOO",
    "O.OO",
    ".OO.",
    ".OOO",
    ".O..",
    ".O.O",
]
decade_affices: dict[int, tuple[str, str]] = {
    1: ("", ".."),
    2: ("", "O."),
    3: ("", "OO"),
    4: ("", ".O"),
    5: ("..", ""),
}


def get_decade(n: int) -> list[str]:
    """Given one of the five decades in the Braille system, return a list of
    each symbol, written in left-to-right, top-down notation, with a '.'
    representing an empty space, and an 'O' representing a raised dot.
    """
    return list(
        map(
            lambda s: decade_affices[n][0] + s + decade_affices[n][1],
            decade_core,
        )
    )


number_follows = ".O.OOO"
capital_follows = ".....O"


def ascii_upper(s: str) -> str:
    return s.upper()


def braille_upper(s: str) -> str:
    return capital_follows + s


digits = list(map(str, list(range(1, 9 + 1)) + [0]))

a_to_j = list("abcdefghij")
k_to_t = list("klmnopqrst")
uvxyz = list("uvxyz")

EnglishState = Enum("EnglishState", ["Number", "NonNumber"])
ascii_to_braille_table: dict[str, str] = {
    **dict(zip(a_to_j, get_decade(1))),
    **dict(zip(k_to_t, get_decade(2))),
    **dict(zip(uvxyz, get_decade(3))),
    **dict(zip(map(ascii_upper, a_to_j), map(braille_upper, get_decade(1)))),
    **dict(zip(map(ascii_upper, k_to_t), map(braille_upper, get_decade(2)))),
    **dict(zip(map(ascii_upper, uvxyz), map(braille_upper, get_decade(3)))),
    "w": get_decade(4)[10 - 1],
    "W": braille_upper(get_decade(4)[10 - 1]),
    " ": "......",
    **dict(zip(digits, get_decade(1))),
}

BrailleState = Enum("BrailleState", ["Number", "Capital", "Normal"])
braille_to_ascii_table: dict[tuple[BrailleState, str], str] = {
    **dict(zip(map(lambda c: (BrailleState.Normal, c), get_decade(1)), a_to_j)),
    **dict(zip(map(lambda c: (BrailleState.Normal, c), get_decade(2)), k_to_t)),
    **dict(zip(map(lambda c: (BrailleState.Normal, c), get_decade(3)), uvxyz)),
    **dict(
        zip(
            map(lambda c: (BrailleState.Capital, c), get_decade(1)),
            map(ascii_upper, a_to_j),
        )
    ),
    **dict(
        zip(
            map(lambda c: (BrailleState.Capital, c), get_decade(2)),
            map(ascii_upper, k_to_t),
        )
    ),
    **dict(
        zip(
            map(lambda c: (BrailleState.Capital, c), get_decade(3)),
            map(ascii_upper, uvxyz),
        )
    ),
    **dict(zip(map(lambda c: (BrailleState.Number, c), get_decade(1)), digits)),
    (BrailleState.Normal, get_decade(4)[10 - 1]): "w",
    (BrailleState.Capital, get_decade(4)[10 - 1]): "W",
    (BrailleState.Normal, "......"): " ",
}


def parse_english_to_braille(s: str) -> Iterator[str]:
    state = EnglishState.NonNumber
    for c in s:
        if state is EnglishState.NonNumber and c in list("0123456789"):
            state = EnglishState.Number
            yield number_follows + ascii_to_braille_table[c]
        elif state is EnglishState.Number and c == " ":
            state = EnglishState.NonNumber
            yield ascii_to_braille_table[c]
        else:
            yield ascii_to_braille_table[c]


def parse_braille_to_english(s: str) -> Iterator[str]:
    state = BrailleState.Normal
    for c in map("".join, batched(s, 6)):
        if c == capital_follows:
            state = BrailleState.Capital
            yield ""
        elif c == number_follows:
            state = BrailleState.Number
            yield ""
        else:
            if state is BrailleState.Number and c == ascii_to_braille_table[" "]:
                state = BrailleState.Normal
            yield braille_to_ascii_table[(state, c)]
            if state is BrailleState.Capital:
                state = BrailleState.Normal


def parse(s: str) -> str:
    """
    Convert a string from English to Braille.

    Given either an alphanumeric string with spaces or a string containing
    only '.' and 'O' of length 6n, `parse` detects the transcription form, then
    performs the appropriate translation.

    `parse` is an involution, i.e. for valid inputs `x`, `parse(parse(x)) == x`.

    """
    if "." in s and set(s).issubset(set(".O")):
        return "".join(parse_braille_to_english(s))
    return "".join(parse_english_to_braille(s))


if __name__ == "__main__":
    print(parse(" ".join(argv[1:])))
