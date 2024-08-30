import sys

letter_to_braille: dict[str, str] = {
    " ": "......",
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
braille_to_letter = {v: k for k, v in letter_to_braille.items()}

num_to_braille: dict[str, str] = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}
braille_to_num = {v: k for k, v in num_to_braille.items()}

capital_follows = ".....O"
number_follows = ".O.OOO"


def english_to_braille(words: list[str]) -> str:
    res = ""
    is_number = False
    for word in words:
        for char in word:
            if not char.isnumeric():
                is_number = False
            if char.isupper():
                res += capital_follows
            if char.isnumeric() and not is_number:
                res += number_follows
                is_number = True
            if is_number:
                res += num_to_braille[char]
            else:
                res += letter_to_braille[char.lower()]

        res += letter_to_braille[" "]
        is_number = False

    return res[:-6]


def braille_to_english(braille: str) -> str:
    assert len(braille) % 6 == 0, "Invalid braille"
    is_number, is_capital = False, False
    braille = [braille[i : i + 6] for i in range(0, len(braille), 6)]
    res = ""

    for substr in braille:
        if substr == number_follows:
            is_number = True
        elif substr == capital_follows:
            is_capital = True
        else:
            if substr == "......":
                is_number = False
            if is_capital:
                res += braille_to_letter[substr].upper()
                is_capital = False
            elif is_number:
                res += braille_to_num[substr]
            else:
                res += braille_to_letter[substr]

    return res


def main():
    if len(sys.argv) < 2:
        print(f"Usage: ./{sys.argv[0]} input")
        exit(1)

    is_english_to_braille = False
    if "." not in "".join(sys.argv[1:]):
        is_english_to_braille = True

    if is_english_to_braille:
        print(english_to_braille(sys.argv[1:]))
    else:
        print(braille_to_english(sys.argv[1]))


if __name__ == "__main__":
    main()
