import sys

BRAILLE_LENGTH = 6

CAPITAL_FOLLOWS = 1
NUMBER_FOLLOWS = 3

BRAILLE_TO_ALPHA = {
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
    ".....O": CAPITAL_FOLLOWS,
    ".O.OOO": NUMBER_FOLLOWS,
    "......": " ",
}  # alphas + symbols
BRAILLE_TO_NUMBERS = {
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
}  # numbers

ASCII_TO_BRAILLE = {}
for k, v in BRAILLE_TO_ALPHA.items():
    ASCII_TO_BRAILLE[v] = k

for k, v in BRAILLE_TO_NUMBERS.items():
    ASCII_TO_BRAILLE[v] = k


def braille_to_alpha(arg: str, is_capital: bool, is_number: bool):
    if is_number:
        return BRAILLE_TO_NUMBERS[arg]

    res = BRAILLE_TO_ALPHA[arg]
    if is_capital:
        res = res.upper()

    return res


def try_braille_to_alpha(arg: str):
    if " " in arg:  # braille inputs should only be one 'word'
        raise Exception

    if len(arg) < BRAILLE_LENGTH:
        raise Exception

    res = ""
    capital = number = False

    # try to slide over the entire input 6 chars at a time, to parse & translate the braille
    # we only know an input is braille if it fully translates from braille
    # (since it could just be an ascii string of O's and dots) so we need to check the entire input
    for i in range(0, len(arg) - BRAILLE_LENGTH + 1, BRAILLE_LENGTH):
        char = braille_to_alpha(arg[i : i + BRAILLE_LENGTH], capital, number)

        # process flags
        capital = char == CAPITAL_FOLLOWS
        if char == NUMBER_FOLLOWS:
            number = True
        elif char == " ":
            number = False

        if type(char) == str:
            res += char

    return res


# convert one word to braille
def word_to_braille(word: str):
    res = ""
    first_number = True
    for char in word:
        if char.isalpha():
            if char.isupper():
                res += ASCII_TO_BRAILLE[CAPITAL_FOLLOWS]
        elif char.isnumeric() and first_number:
            res += ASCII_TO_BRAILLE[NUMBER_FOLLOWS]
            first_number = False
        res += ASCII_TO_BRAILLE[char.lower()]
    return res


# convert an entire string of ascii characters to braille
def alpha_to_braille(words: list[str]):
    braille_words = [word_to_braille(w) for w in words]
    return ASCII_TO_BRAILLE[" "].join(braille_words)


def main():
    try:
        arg = " ".join(sys.argv[1:])
        res = try_braille_to_alpha(arg)
    except Exception:
        arg = sys.argv[1:]
        res = alpha_to_braille(arg)
    print(res)


main()
