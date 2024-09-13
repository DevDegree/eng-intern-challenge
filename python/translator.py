import sys

# Mapping to English + Numbers
braille_to_eng = {
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
}

braille_to_num = {
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

# Mapping to Braille
eng_to_braille = {v: k for k, v in braille_to_eng.items()}

num_to_braille = {v: k for k, v in braille_to_num.items()}

capital = ".....O"
number = ".O.OOO"
space = "......"


def translate_to_braille(input_str):
    ans = ""
    isNum = False

    for i in range(len(input_str)):
        char = input_str[i]

        if char.isnumeric():
            if isNum == False:
                isNum = True
                ans += number
            ans += num_to_braille[char]
            continue

        if char.isnumeric() == False:
            isNum = False

        if char.isupper():
            ans += capital
            char = char.lower()

        if char == " ":
            ans += space
            continue

        ans += eng_to_braille[char]

    return ans


def translate_to_english(input_str):
    ans = ""
    isNum = False
    isCapital = False

    for i in range(0, len(input_str), 6):
        # Analyze six bits at once
        char = input_str[i : i + 6]
        if char == capital:
            isCapital = True
            continue
        elif char == number:
            isNum = True
            continue
        elif char == space:
            isNum = False
            ans += " "
            continue
        else:
            if isNum:
                ans += braille_to_num[char]
            else:
                if isCapital:
                    ans += braille_to_eng[char].upper()
                    isCapital = False
                    continue
                ans += braille_to_eng[char]

    return ans


def isInputBraille(input_str):
    if len(input_str) % 6 == 0:
        for i in range(0, len(input_str), 6):
            char = input_str[i : i + 6]
            if (
                (char in braille_to_eng)
                or (char in braille_to_num)
                or char == capital
                or char == number
                or char == space
            ):
                continue
            else:
                return False
        return True
    return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
        if isInputBraille(input_str):
            print(translate_to_english(input_str))
        else:
            print(translate_to_braille(input_str))
