import sys

braille_to_char = {
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

braille_to_mode = {
    ".....O": "capital_follows",
    ".O.OOO": "number_follows",
}

char_to_braille = {v: k for k, v in braille_to_char.items()}
num_to_braille = {v: k for k, v in braille_to_num.items()}
mode_to_braille = {v: k for k, v in braille_to_mode.items()}


def translate_to_ascii(usr_input):
    """
    :param usr_input: ascii characters to be translated to braille
    :return: braille representation of the input
    """
    string_result = ""
    is_num_mode = False
    is_capital_mode = False

    for i in range(0, len(usr_input), 6):
        braille = usr_input[i:i + 6]
        if braille in braille_to_mode and braille_to_mode[braille] == "capital_follows":
            is_capital_mode = True
        elif braille in braille_to_mode and braille_to_mode[braille] == "number_follows":
            is_num_mode = True
        elif braille in braille_to_char and braille is char_to_braille[" "]:
            is_num_mode = False
        elif is_capital_mode and braille in braille_to_char:
            string_result += braille_to_char[braille].upper()
            is_capital_mode = False
        elif is_num_mode and braille in braille_to_num:
            string_result += braille_to_num[braille]
        else:
            string_result += braille_to_char[braille]
    return string_result


def translate_to_braille(usr_input):
    """
    :param usr_input: a  string to be translated to braille
    :return: ascii representation of the input
    """
    braille_result = ""
    is_num_mode = False
    for char in usr_input:
        if char.isalpha() and char.isupper():
            braille_result += mode_to_braille["capital_follows"]
            braille_result += char_to_braille[char.lower()]
        elif char.isalpha() and char.islower():
            braille_result += char_to_braille[char.lower()]
        elif char.isdigit():
            if not is_num_mode:
                is_num_mode = True
                braille_result += mode_to_braille["number_follows"]
            braille_result += num_to_braille[char]
        elif char.isspace():
            is_num_mode = False
            braille_result += char_to_braille[char]
    return braille_result


def is_braille(usr_input):
    """
    Return true if the string is braille.
    """
    chars = set(list(usr_input))
    return len(list(chars)) == 2 and "." in chars and "O" in chars


if __name__ == '__main__':
    args = " ".join(sys.argv[1:])
    res = ""
    if is_braille(args):
        res = translate_to_ascii(args)
    else:
        res = translate_to_braille(args)
    print(res)
