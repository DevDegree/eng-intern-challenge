import argparse

braille_letters = {
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
}
braille_numbers = {
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

capital_letter = ".....O"
number_sign = ".O.OOO"

english_letters = {v: k for k, v in braille_letters.items()}
english_numbers = {v: k for k, v in braille_numbers.items()}


def main():
    parser = argparse.ArgumentParser(
        description="A script to process a string argument"
    )
    parser.add_argument("input_string", nargs="+", type=str, help="A string input")
    args = parser.parse_args()

    input_string = " ".join(args.input_string)

    if detect_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))


def detect_braille(string):
    braille = set(["O", "."])

    for char in string:
        if char not in braille:
            return False
    return True


def braille_to_english(string: str) -> str:
    chunks = [string[i : i + 6] for i in range(0, len(string), 6)]
    accumulator = ""

    start = 0
    while start < len(chunks):
        if chunks[start] == capital_letter:
            accumulator += braille_letters[chunks[start + 1]].upper()
            start += 2
        elif chunks[start] == number_sign:
            start += 1
            while start < len(chunks) and chunks[start] != "......":
                accumulator += braille_numbers[chunks[start]]
                start += 1
        else:
            accumulator += braille_letters[chunks[start]]
            start += 1

    return accumulator


def english_to_braille(string: str) -> str:
    accumulator = ""
    in_number = False
    for char in string:
        if char.isupper():
            accumulator += capital_letter
            accumulator += english_letters[char.lower()]
        elif char.isdigit():
            if not in_number:
                accumulator += number_sign
                in_number = True
            for digit in char:
                accumulator += english_numbers[digit]
        else:
            if char == " ":
                in_number = False
            accumulator += english_letters[char]

    return accumulator


if __name__ == "__main__":
    main()
