import sys

braille_map_alpha = {
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
    ".....O": "CAP",
    ".O.OOO": "NUM",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

braille_map_num = {
    ".O...O": "DEC",
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
    ".O...O": ".",
    "......": " ",
    ".OO..O": "<",
    "O..OO.": ">",
}

alpha_to_braille = {v: k for k, v in braille_map_alpha.items()}
num_to_braille = {v: k for k, v in braille_map_num.items()}


def convertToEnglish(str):
    if (len(str) % 6) != 0:
        "Error: braille string is incorrect length"
        return

    res_str = ""

    CAP_FLAG = False
    NUM_FLAG = False

    i = 0

    while i < len(str):
        braille_seq = str[i : i + 6]
        if NUM_FLAG:
            if braille_seq in braille_map_num:
                res = braille_map_num[braille_seq]
                if res == " ":
                    NUM_FLAG = False
                res_str += res
        else:
            if braille_seq in braille_map_alpha:
                res = braille_map_alpha[braille_seq]
                if res == "CAP":
                    CAP_FLAG = True
                elif res == "NUM":
                    NUM_FLAG = True
                    CAP_FLAG = False
                else:
                    if CAP_FLAG:
                        res_str += res.upper()
                        CAP_FLAG = False
                    else:
                        res_str += res
        i += 6

    print(res_str)


def convertToBraill(str):

    res_str = ""

    NUM_FLAG = False

    for char in str:
        if char.isnumeric() and not NUM_FLAG:
            res_str += alpha_to_braille["NUM"]
            NUM_FLAG = True
        if NUM_FLAG:
            if char == " ":
                NUM_FLAG = False
            res_str += num_to_braille[char]
        else:
            if char.isupper():
                res_str += alpha_to_braille["CAP"]
                char = char.lower()
            res_str += alpha_to_braille[char]

    print(res_str)


def brailleCheck(string):
    for char in string:
        if char != "O" and char != ".":
            return False
    return True


def main():
    string = " ".join(sys.argv[1:])

    if brailleCheck(string):
        convertToEnglish(string)
    else:
        convertToBraill(string)


if __name__ == "__main__":
    main()
