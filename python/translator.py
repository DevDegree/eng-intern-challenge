# dieter whittingham
# sep 12 2024

# email: whittinghamdieter@gmail.com

# braille translator

# notes:
# step 1: assume that the given input is braille.
# read from input 6 characters at a time. if a non-braille character is found
# or the input runs out before reading 6 characters, then we can confirm that
# the input is actually english.

# if it's determined that the input is english, restart the process, this time
# knowing that it's an english character. 

# special notes: the letter o has the same braille symbol as >.
# since instructions were not given to handle this case, i'll assume that
# the symbol in a numerical context is a >, otherwise it's an O.

# it's possible that an english test case contains only O's and .'s. that's why
# my method of verifying the validity of each braille character will properly
# determine whether it's braille or english.

# also note: in python, the first command line arg (index 0) is always the 
# name of the file. simply parse from index 1 onwards.

import sys

def braille_translate(braille):
    pass

def english_translate(text):
    pass

# wrapper function that returns the output to the main execution.
# allows for testing using a test harness
def return_output(input):
    pass

# will be commented out for submission
def test_harness():
    cases = [
        # start with given cases

    ]

if __name__ == "__main__":
    # main execution
    pass
