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

TESTING = True

# define constants for braille -> english and english -> braille
# also need states for the following: capital follows, decimal follows, number follows

def braille_translate(braille):
    pass

def english_translate(text):
    pass

# determines whether it's braille or not.
def is_braille(input):
    l = len(input)
    os = input.count("O")
    dots = input.count(".")
    # checking according to the conditions at the top of the file
    if (l % 6) * 6 == l and os + dots == l and dots > 0:
        return True

# wrapper function that returns the output to the main execution.
# allows for testing using a test harness
def return_output(input):
    pass

# will be commented out for submission
def test_harness():
    cases = [
        # start with given cases
        ("Hello World", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."),
        ("42", ".O.OOOOO.O..O.O..."),
        (".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "Abc 123"),
        # my test cases below
    ]

    for case in cases:
        assert(return_output(case[1]) == case[2])
    
    print("testing mode: assertions passed.")

if __name__ == "__main__":
    # main execution
    if TESTING:
        test_harness()
    
