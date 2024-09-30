from argparse import ArgumentParser
from typing import List

BRAILLE_LENGTH = 6

ENGLISH_TO_BRAILLE = {
    "alpha": {
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
    },
    "numeral": {
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
        ".": ".O...O",
    },
    "punctuation": {
        ".": "..OO.O",
        ",": "..O...",
        "?": "..O.OO",
        "!": "..OOO.",
        ":": "..OO..",
        ";": "..O.O.",
        "-": "....OO",
        "/": ".O..O.",
        "<": ".OO..O",
        ">": "O..OO.",
        "(": "O.O..O",
        ")": ".O.OO.",
        " ": "......",
    },
}

CAPITAL = ".....O"
DECIMAL = ".O...O"
NUMBER = ".O.OOO"

BRAILLE_TO_ENGLISH = {
    group: {braille: english for english, braille in mappings.items()}
    for group, mappings in ENGLISH_TO_BRAILLE.items()
}

BRAILLE_ALPHABET = (
    set(BRAILLE_TO_ENGLISH["alpha"])
    | set(BRAILLE_TO_ENGLISH["punctuation"])
    | set(BRAILLE_TO_ENGLISH["numeral"])
    | {CAPITAL, DECIMAL, NUMBER}
)


def english_to_braille(english: str) -> str:
    ans: List[str] = []
    prev_c = None
    is_numeral = False

    for c in english:
        if c == ".":
            if is_numeral:
                ans.append(ENGLISH_TO_BRAILLE["numeral"]["."])
            else:
                ans.append(ENGLISH_TO_BRAILLE["punctuation"]["."])
            prev_c = c
            continue

        if c.lower() in ENGLISH_TO_BRAILLE["alpha"]:
            if c.isupper():
                ans.append(CAPITAL)
            ans.append(ENGLISH_TO_BRAILLE["alpha"][c.lower()])

            is_numeral = False

        elif c in ENGLISH_TO_BRAILLE["punctuation"]:
            ans.append(ENGLISH_TO_BRAILLE["punctuation"][c])

            is_numeral = False

        elif c in ENGLISH_TO_BRAILLE["numeral"]:
            if not is_numeral:
                is_punctuation_period = prev_c == "."
                if is_punctuation_period:
                    ans[-1] = NUMBER
                    ans.append(ENGLISH_TO_BRAILLE["numeral"]["."])
                else:
                    ans.append(NUMBER)
            ans.append(ENGLISH_TO_BRAILLE["numeral"][c])

            is_numeral = True

        prev_c = c

    return "".join(ans)


class BrailleToLatinContextTracker:
    def __init__(self):
        self.is_capital = False
        self.is_numeral = False

    def adding_capital(self):
        assert not self.is_numeral
        self.is_capital = True

    def adding_numeral(self):
        assert not self.is_capital
        self.is_numeral = True

    def should_alphabetize(self, braille: str) -> bool:
        return not self.is_numeral and braille in BRAILLE_TO_ENGLISH["alpha"]

    def should_punctualize(self, braille: str) -> bool:
        return not self.is_capital and braille in BRAILLE_TO_ENGLISH["punctuation"]

    def should_capitalize(self, braille: str) -> bool:
        return self.is_capital and self.should_alphabetize(braille)

    def should_numeralize(self, braille) -> bool:
        return (
            not self.is_capital
            and self.is_numeral
            and braille in BRAILLE_TO_ENGLISH["numeral"]
        )

    def added_alpha_or_punctuation(self):
        self.is_capital = False
        self.is_numeral = False

    def added_numeral(self):
        self.adding_numeral()


def braille_to_english(s: str) -> str:
    ans: List[str] = []
    tracker = BrailleToLatinContextTracker()

    for i in range(0, len(s), BRAILLE_LENGTH):
        braille_token = s[i : i + BRAILLE_LENGTH]

        if braille_token == CAPITAL:
            tracker.adding_capital()
        elif braille_token == NUMBER:
            tracker.adding_numeral()
        elif braille_token == DECIMAL:
            tracker.adding_numeral()
            ans.append(".")
            continue

        if tracker.should_alphabetize(braille_token):
            if tracker.should_capitalize(braille_token):
                ans.append(BRAILLE_TO_ENGLISH["alpha"][braille_token].upper())
            else:
                ans.append(BRAILLE_TO_ENGLISH["alpha"][braille_token])
            tracker.added_alpha_or_punctuation()

        elif tracker.should_punctualize(braille_token):
            ans.append(BRAILLE_TO_ENGLISH["punctuation"][braille_token])
            tracker.added_alpha_or_punctuation()

        elif tracker.should_numeralize(braille_token):
            ans.append(BRAILLE_TO_ENGLISH["numeral"][braille_token])
            tracker.added_numeral()

    return "".join(ans)


def is_braille(s: str) -> bool:
    is_separable_into_braille = len(s) % BRAILLE_LENGTH == 0
    if not is_separable_into_braille:
        return False
    all_symbols_are_braille = all(
        s[i : i + BRAILLE_LENGTH] in BRAILLE_ALPHABET
        for i in range(0, len(s), BRAILLE_LENGTH)
    )
    return all_symbols_are_braille


def main():
    parser = ArgumentParser(
        prog="Braille to English and English to Braille Translator",
        description="Can translate Braille to the English Alphabet and Vice versa.",
    )
    parser.add_argument(
        "sentence",
        nargs="+",
        help="Provide one or more arguments that are english or braille sentence(s)",
    )
    args = parser.parse_args()
    sentence = " ".join(args.sentence)
    if is_braille(sentence):
        print(braille_to_english(sentence))
    else:
        print(english_to_braille(sentence))


if __name__ == "__main__":
    main()
