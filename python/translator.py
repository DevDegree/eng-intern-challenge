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
            res += numbers_to_braille[""]
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
    return


# test to see each function is working
if __name__ == "__main__":
    print(alphabet_to_braille["a"] + alphabet_to_braille["b"])
    print("There are " + str(len(braille)) + " braille characters in the dict.")
    test1 = is_braille("Hello")
    test2 = is_braille("O.....")
    test3 = is_braille("O......")
    print(test1)
    print(test2)
    print(test3)
    ### test4 = "Hello world"
    print(convert_to_braille("Hello world"))
