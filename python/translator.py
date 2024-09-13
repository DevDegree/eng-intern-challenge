# dieter whittingham
# sep 12 2024

# email: whittinghamdieter@gmail.com

# braille translator

# notes:
# step 1: determine whether the input is braille.
# it's braille if the length is divisible by 6 and contains only Os and .s
# edge case: english input that only contains Os. then we know it's english
# since no braille character contains only Os.

# step 2: use the appropriate translation method, and print the output.

# also note: in python, the first command line arg (index 0) is always the 
# name of the file. simply parse from index 1 onwards.

# in the instructions, it says that the braille alphabet used will contain 
# letters a-z and nums 0-9, with caps, and spaces. 
# I will assume that this means that for both english and braille input,
# only these characters will be represented, i.e english input won't contain symbols.

import sys

TESTING = False

# define constants for braille -> english and english -> braille
# also need states for the following: capital follows, decimal follows, number follows

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
}

braille_to_nums = {
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

# need to construct a "reversed" dictionary for translation from english to braille
# in O(1) lookup

eng_to_braille = {value: key for key, value in braille_to_eng.items()}
nums_to_braille = {value: key for key, value in braille_to_nums.items()}

# lastly, define constants for number and capital follows, and space

NUMBER = ".O.OOO"
CAPITAL = ".....O"
SPACE = "......"

# translation under the assumption the input is valid braille
def braille_translate(braille):
    output = ""
    current = ""
    cap = False
    num = False
    i = 0
    while i < len(braille):
        # iterate 6 at a time.
        current = ""
        for _ in range(6):
            current += braille[i]
            i += 1
        # now have current text
        # cases: capital, num, space, other
        if current == CAPITAL:
            cap = True
        elif current == NUMBER:
            num = True
        elif current == SPACE:
            output += " "
            # reset num status
            num = False
        elif num:
            # number
            output += braille_to_nums[current]
        elif cap:
            # capital character
            output += braille_to_eng[current].upper()
            # reset
            cap = False
        else:
            # lowercase character
            output += braille_to_eng[current]
    return output

# translation under the assumption that input is valid english
def english_translate(text):
    # cases: space, number, capital, lowercase
    output = ""
    num = False # number state
    for letter in text:
        if letter in nums_to_braille:
            if not num:
                output += (NUMBER + nums_to_braille[letter])
            if num:
                output += nums_to_braille[letter] # don't add number prefix
            num = True
        elif letter == " ":
            output += SPACE
            # disable number prefix
            num = False
        elif letter.isupper():
            # uppercase letter
            output += (CAPITAL + eng_to_braille[letter.lower()])
        else:
            # lowercase
            output += eng_to_braille[letter]
    return output

# determines whether it's braille or not.
def is_braille(inp):
    l = len(inp)
    os = inp.count("O")
    dots = inp.count(".")
    # checking according to the conditions at the top of the file
    if l % 6 == 0 and os + dots == l and dots > 0:
        return True
    else:
        return False

# wrapper function that returns the output to the main execution.
# allows for testing using a test harness
def return_output(inp):
    if is_braille(inp):
        return braille_translate(inp)
    else:
        return english_translate(inp)

# will be commented out for submission
def test_harness():
    cases = [
        # start with given cases
        ("Hello world", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."),
        ("42", ".O.OOOOO.O..O.O..."),
        (".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "Abc 123"),
        # my test cases below
        ("Python 3", CAPITAL + eng_to_braille["p"] + eng_to_braille["y"] + \
         eng_to_braille["t"] + eng_to_braille["h"] + eng_to_braille["o"] + \
            eng_to_braille["n"] + SPACE + NUMBER + nums_to_braille["3"]),

        ("Numb3R5 543 999 0 1", CAPITAL + eng_to_braille["n"] + eng_to_braille["u"] + \
        eng_to_braille["m"] + eng_to_braille["b"] + NUMBER + nums_to_braille["3"] + CAPITAL + \
        eng_to_braille["r"] + nums_to_braille["5"] + SPACE + NUMBER +  nums_to_braille["5"] +\
        nums_to_braille["4"] + nums_to_braille["3"] + SPACE + NUMBER +  nums_to_braille["9"] +\
        nums_to_braille["9"] + nums_to_braille["9"] + SPACE + NUMBER + nums_to_braille["0"] +\
        SPACE + NUMBER + nums_to_braille["1"]),

        ("AAA3aa2A1 2", CAPITAL + eng_to_braille["a"] + CAPITAL + eng_to_braille["a"] +\
        CAPITAL + eng_to_braille["a"] + NUMBER + nums_to_braille["3"] + eng_to_braille["a"] +\
        eng_to_braille["a"] + nums_to_braille["2"] + CAPITAL + eng_to_braille["a"] + \
        nums_to_braille["1"] + SPACE + NUMBER + nums_to_braille["2"])
    ]

    for case in cases:
        print(case)
        s = return_output(case[0])
        print(s)
        print(s == case[1])
        assert(s == case[1])
    
    print("testing mode: assertions passed.")

if __name__ == "__main__":
    # main execution
    if TESTING:
        test_harness()
    # assume that if first argument is english, all arguments will be
    braille = is_braille(sys.argv[1])
    s = ""
    if braille:
        s = SPACE.join(sys.argv[1:])
    else:
        s = " ".join(sys.argv[1:])
    print(return_output(s))
    
