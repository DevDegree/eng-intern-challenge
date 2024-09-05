import sys

# Create a dictionary for alphabet to braille
# Do this by looping through arrays and mapping to a dict - as alphabet is 26 characters, time loss minimal
# generate one array containing alphabetical characters, one array containing braille symbols, one containing numerics: braille numerics are the same as braille alhpabet A - J, so just reuse those

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
]
braille = [
    "O.....",
    "O.O...",
    "OO....",
    "OO.O..",
    "O..O..",
    "OOO...",
    "OOOO..",
    "O.OO..",
    ".OO..",
    ".OOO..",
    "O...O.",
    "O.O.O.",
    "OO..O.",
    "OO.OO.",
    "O..OO.",
    "OOO.O.",
    "OOOOO.",
    "O.OOO.",
    ".OO.O.",
    ".OOOO.",
    "O...OO",
    "O.O.OO",
    ".OOO.O",
    "OO..OO",
    "OO.OOO",
    "O..OOO",
    "......",
]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# generate the dicts:

alphabet_to_braille = {}
braille_to_alphabet = {}
numbers_to_braille = {}
braille_to_numbers = {}

# loop through, filling in dict

for i in range(len(alphabet)):
    alphabet_to_braille[alphabet[i]] = braille[i]
    braille_to_alphabet[braille[i]] = alphabet[i]

for i in range(len(numbers)):
    numbers_to_braille[numbers[i]] = braille[i]
    braille_to_numbers[braille[i]] = numbers[i]

# create final dict for braille to check if number:
braille_modes = {".....O": "capitalize", ".O.OOO": "numerize"}
alpha_modes = {value: key for key, value in braille_modes.items()}


# create a function to check if braille input or if alphabet
def is_braille(input):
    # braille strings should exist in multiples of six
    if len(input) % 6 != 0:
        return False
    # additionally, braille strings should only consist of 'O' or '.'
    allowed = set("O.")
    if not set(input).issubset(allowed):
        return False
    # if other checks pass, string is braille
    return True


# create function to convert alphanumerics to braille
def convert_to_braille(input):
    res = ""
    number_flag = False
    for char in input:
        # check if is a number
        if char.isdigit():
            # if numberflag hasn't yet been set, swap the flag and insert the numerize braille symbol
            if not number_flag:
                number_flag = True
                res += alpha_modes["numerize"]
            # insert braille number key
            res += numbers_to_braille[char]
            # after number inserted, skip to next cycle
            continue
        # if char is a space, reset number flag for string
        if char == " ":
            number_flag = False
        # if char is capitalized, insert the capitalize braille symbol
        if char.isupper():
            res += alpha_modes["capitalize"]
            # then, convert char to lowercase so it can be found in the dict
            char = char.lower()
        # after all previous checks, insert char into result
        res += alphabet_to_braille[char]

    return res


def convert_to_alphanumerics(input):
    res = ""
    # as the string must be multiple of six, split the string into an array so each character can be easily parsed
    split = [input[i : i + 6] for i in range(0, len(input), 6)]
    # set flags for numerize
    number_flag = False
    capital_flag = False
    # loop through each segment
    for segment in split:
        # check if the character is a numerize or capitalize flag
        if segment == alpha_modes["numerize"]:
            number_flag = True
            continue
        elif segment == alpha_modes["capitalize"]:
            capital_flag = True
            continue

        # check if space - if a space, turn off the number flag and then insert segment then continue
        if segment == alphabet_to_braille[" "]:
            number_flag = False
            res += braille_to_alphabet[segment]
            continue
        # if the number flag is on, treat segment as a number and append
        if number_flag:
            res += braille_to_numbers[segment]
            continue

        # if all other checks allow to pass to this point, must be a character
        insertion = braille_to_alphabet[segment]
        # check if need to capitalize - if so, capitalize before insertion
        if capital_flag:
            insertion = insertion.upper()
            capital_flag = False
        # then insert
        res += insertion

    return res


# test to see each function is working
if __name__ == "__main__":
    test_string = "Abc 123 aBc"
    brail_equiv = convert_to_braille(test_string)
    print(brail_equiv)
    convert_back = convert_to_alphanumerics(brail_equiv)
    print(convert_back)
