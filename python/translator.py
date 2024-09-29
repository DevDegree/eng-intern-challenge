import sys
from textwrap import wrap


braille_to_english = {
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
}

braille_to_english_chars = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "|",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

braille_to_english_nums = {
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

english_to_braille = {v: k for k, v in braille_to_english.items()}
english_to_braille_chars = {v: k for k, v in braille_to_english_chars.items()}
english_to_braille_nums = {v: k for k, v in braille_to_english_nums.items()}


def braille_to_text(braille):
    braille_strings = wrap(braille, width=6)
    english = ""
    is_next_capital = 0
    is_number = 0
    for s in braille_strings:
        if s == ".....O":
            is_next_capital = 1
        elif s == ".O...O":
            pass
        else:
            try:
                if is_next_capital:
                    english += braille_to_english[s].upper()
                    is_next_capital = 0
                else:
                    if s == ".O.OOO":
                        is_number = 1
                    else:
                        if s == "......":
                            is_number = 0
                        if is_number:
                            english += braille_to_english_nums[s]
                        elif s in braille_to_english:
                            english += braille_to_english[s]
                        else:
                            english += braille_to_english_chars[s]
            except KeyError:
                print(f"Error: {s} is not a valid braille character")
                sys.exit()
    print(english.strip())


def text_to_braille(text):
    braille = ""
    for i, char in enumerate(text):
        # print(char)
        try:
            if char.isnumeric():
                if i == 0 or not text[i - 1].isnumeric():
                    braille += ".O.OOO" + english_to_braille_nums[char]
                else:
                    braille += english_to_braille_nums[char]
            elif i < len(text) - 1 and char == "." and text[i + 1].isnumeric():
                braille += ".O...O" + english_to_braille_nums[char]
            elif not char.isalnum():
                braille += english_to_braille_chars[char]
            else:
                if char.isupper():
                    braille += ".....O" + english_to_braille[char.lower()]
                else:
                    # print(char)
                    # print(english_to_braille)
                    braille += english_to_braille[char]
        except KeyError:
            print(f"Error: {char} is not a valid braille character")
            sys.exit()
    print(braille.strip())


def main():
    input_str = " ".join(sys.argv[1:])
    is_braille = True
    for char in input_str:
        if char not in (".", "O", "o", " "):
            is_braille = False
            break
    if is_braille:
        if " " in input_str:
            input_str = input_str.replace(" ", "")
        if len(input_str) % 6 == 0:
            braille_to_text(input_str.upper())
        else:
            print("Error: Braille length not multiple of 6")
            sys.exit()
    else:
        text_to_braille(input_str)


if __name__ == "__main__":
    main()
