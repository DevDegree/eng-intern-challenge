import sys
from itertools import islice

to_braille_dict = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

to_eng_dict = dict(reversed(item) for item in to_braille_dict.items())

# removed     ">": "O..OO.",

digit_dict = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "O": ".OOO..",
}

reverse_digit_dict = dict(reversed(item) for item in digit_dict.items())

CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"


def main():
    answer = ""
    string = " ".join(sys.argv[1:])
    if determine_lang(string) == "english":
        answer = answer + to_braille(string)
    else:
        answer = answer + to_english(string)

    print(answer)


def determine_lang(string):
    found_english = False
    for letter in string:
        # if we find a non-braille letter, it's in english
        if letter != "O" and letter != ".":
            return "english"

    # if we only have Os and .s this is braille
    if not found_english:
        return "braille"


def to_braille(string):
    digit = False
    converted = ""
    for letter in string:
        # if we have a capital letter, add a CAPITAL_FOLLOWS first
        if letter.isupper():
            converted = converted + CAPITAL_FOLLOWS

        # if we have a number, add a NUM_FOLLOWS first
        if letter.isdigit() and not digit:
            converted = converted + NUMBER_FOLLOWS
            digit = True

        # if we had a number and hit a space, reset digit
        if letter == " " and digit:
            digit = False

        if digit:
            if letter == "0":
                converted = converted + digit_dict["O"]
            else:
                converted = converted + digit_dict[letter]

        else:
            converted = converted + to_braille_dict[letter.lower()]

    return converted


def to_english(string):
    converted = ""
    capitalize = False
    isDigit = False
    iterator = iter(string)
    # break up braille into gropus of 6
    while braille_letter := list(islice(iterator, 6)):
        braille_letter = "".join(braille_letter)

        # when CAPITAL_FOLLOWS, only next symbol is capitalized
        if braille_letter == CAPITAL_FOLLOWS:
            capitalize = True
            continue

        # # when NUM_FOLLOWS, all symbols are numbers till next space
        if braille_letter == NUMBER_FOLLOWS:
            isDigit = True
            continue

        if isDigit:
            if braille_letter == to_braille_dict[" "]:
                isDigit = False
                converted = converted + to_eng_dict[braille_letter]
            else:
                converted = converted + reverse_digit_dict[braille_letter]

        elif capitalize:
            converted = converted + to_eng_dict[braille_letter].upper()
            capitalize = False

        else:
            converted = converted + to_eng_dict[braille_letter]

    return converted


if __name__ == "__main__":
    main()


# expected_output =
# ".....O"
# "O....."  A
# "O.O..."  b
# "OO...."  c
# "......"
# ".O.OOO"
# "O....."  1
# "O.O..."  2
# "OO...."
# "......"
# "OO..OO"
# ".....O"
# "OO.OOO"
# "O..OOO"

# "Abc 1"

# "OOO.O."
# "OO.OOO"
# ".OOOO."
# "O.OO.."
