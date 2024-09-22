import sys

CAP_FOLLOWS = ".....O"
NUM_FOLLOWS = ".O.OOO"
SPACE = "......"


def main():
    string = " ".join(sys.argv[1:])
    print(string)
    if string[0].isalpha() or string[0].isnumeric():
        edit = english_to_braille(string)
    else:
        edit = braille_to_english(string)
    print(edit)


def braille_to_english(string: str) -> str:
    full = ""
    sub = ""  # substring of 6 dots
    count = 0  # count up to 6
    caps = False
    nums = False
    lst = []
    for i in range(len(string)):
        ch = string[i]
        if count == 6:
            lst.append(sub)
            count = 0
            sub = ""
        sub += ch
        count += 1
    lst.append(sub)

    for i in lst:
        if i == SPACE:
            full = full + " "
            nums = False
        elif i == CAP_FOLLOWS:
            caps = True
        elif i == NUM_FOLLOWS:
            nums = True
        else:
            if caps:
                x = braille_alphabet(i)
                full = full + x
                caps = False
            elif nums:
                x = braille_numbers(i)
                full = full + x
            else:
                if i is not None:
                    x = braille_alphabet(i)
                    x = x.lower()
                    full = full + x

    return full


def english_to_braille(string: str) -> str:
    full = ""
    num = 0
    for ch in string:
        if ch == " ":
            full = full + SPACE
            num = 0
        elif ch.isalpha():
            if ch.isupper():
                full = full + CAP_FOLLOWS
                full = full + alpha_braille(ch)
            else:
                full = full + alpha_braille(ch).lower()
        else:
            if num == 0:
                full = full + NUM_FOLLOWS
                num += 1
            full = full + num_braille(ch)
    full = full.upper()
    return full


def braille_alphabet(ch: str) -> str:
    '''enter a letter in braille and get the english version'''
    if ch == "O.....":
        return "A"
    elif ch == "O.O...":
        return "B"
    elif ch == "OO....":
        return "C"
    elif ch == "OO.O..":
        return "D"
    elif ch == "O..O..":
        return "E"
    elif ch == "OOO...":
        return "F"
    elif ch == "OOOO..":
        return "G"
    elif ch == "O.OO..":
        return "H"
    elif ch == ".OO...":
        return "I"
    elif ch == ".OOO..":
        return "J"
    elif ch == "O...O.":
        return "K"
    elif ch == "O.O.O.":
        return "L"
    elif ch == "OO..O.":
        return "M"
    elif ch == "OO.OO.":
        return "N"
    elif ch == "O..OO.":
        return "O"
    elif ch == "OOO.O.":
        return "P"
    elif ch == "OOOOO.":
        return "Q"
    elif ch == "O.OOO.":
        return "R"
    elif ch == ".OO.O.":
        return "S"
    elif ch == ".OOOO.":
        return "T"
    elif ch == "O...OO":
        return "U"
    elif ch == "O.O.OO":
        return "V"
    elif ch == ".OOO.O":
        return "W"
    elif ch == "OO..OO":
        return "X"
    elif ch == "OO.OOO":
        return "Y"
    elif ch == "O..OOO":
        return "Z"
    else:
        print("there is an issue with braille_alphabet")


def braille_numbers(ch: str) -> str:
    """enter a letter in braille and return the corresponding english number"""
    if ch == "O.....":
        return "1"
    elif ch == "O.O...":
        return "2"
    elif ch == "OO....":
        return "3"
    elif ch == "OO.O..":
        return "4"
    elif ch == "O..O..":
        return "5"
    elif ch == "OOO...":
        return "6"
    elif ch == "OOOO..":
        return "7"
    elif ch == "O.OO..":
        return "8"
    elif ch == ".OO...":
        return "9"
    elif ch == ".OOO..":
        return "0"
    else:
        print("there is an issue with braille_numbers")


def alpha_braille(ch: str) -> str:
    ch = ch.upper()
    if ch == "A":
        return "O....."
    elif ch == "B":
        return "O.O..."
    elif ch == "C":
        return "OO...."
    elif ch == "D":
        return "OO.O.."
    elif ch == "E":
        return "O..O.."
    elif ch == "F":
        return "OOO..."
    elif ch == "G":
        return "OOOO.."
    elif ch == "H":
        return "O.OO.."
    elif ch == "I":
        return ".OO..."
    elif ch == "J":
        return ".OOO.."
    elif ch == "K":
        return "O...O."
    elif ch == "L":
        return "O.O.O."
    elif ch == "M":
        return "OO..O."
    elif ch == "N":
        return "OO.OO."
    elif ch == "O":
        return "O..OO."
    elif ch == "P":
        return "OOO.O."
    elif ch == "Q":
        return "OOOOO."
    elif ch == "R":
        return "O.OOO."
    elif ch == "S":
        return ".OO.O."
    elif ch == "T":
        return ".OOOO."
    elif ch == "U":
        return "O...OO"
    elif ch == "V":
        return "O.O.OO"
    elif ch == "W":
        return ".OOO.O"
    elif ch == "X":
        return "OO..OO"
    elif ch == "Y":
        return "OO.OOO"
    elif ch == "Z":
        return "O..OOO"
    else:
        print("there is an issue with alpha_braille")
    return ""


def num_braille(ch: str) -> str:
    nums = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..",
            "OOO...", "OOOO..", "O.OO..", ".OO..."]
    i = int(ch)
    return nums[i]


main()
