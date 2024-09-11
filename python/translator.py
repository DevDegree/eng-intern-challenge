#
# Braille Translater by Alex Elliott
# 2024-09-09
#
# Simple braille translate to convert english to braille and braille to english
# in the command line. Completed for the Winter 2025 Eng Intern Challenge Fall.
#

# Import libraries:
# sys, used for obtaining arguments
import sys
# re, used for checking validity of braille sequences with Regex statement
import re

# Braille special characters
brlCap = '.....O'
brlDec = '.O...O'
brlNum = '.O.OOO'

# HashMap/Dictionary to convert english characters to braille
# Best case O(1)
engToBrl = {
    'a': 'O.....', 
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'cap': brlCap,
    'dec': brlDec,
    'num': brlNum,
    ' ': '......'
}

# Create a reversed dictionary for the opposite conversion, braille to english
brlToEng = { }
# For each key in the original dictionary, make a new entry where the old value is the new key
# and the old key is the new value
for k in engToBrl:
    brlToEng[engToBrl[k]] = k

# Math to adjust numeric characters so that we can use our dictionaries, used ascii for easier 
# conversion, leads to an issue with the '0' character which is later accounted for
charAdj = ord('a')-ord('0')-1

# Convert english to braille
# Input english strings word by word and returns out the desired braille strings
def cvtEngToBrl(e):
    ret = ''
    # Use flag since we do not want to add a number special character before each number,
    # just each contiguous string of numbers
    numFlag = False
    # For each character in the String e
    for c in e: 
        # If space, clear flag
        if c == ' ':
            numFlag = False
        # Add the special braille chr and edit c to be lookup-able
        elif c.isupper():
            c = c.lower()
            ret += brlCap
        elif c.isnumeric() and not numFlag:
            numFlag = True
            ret += brlNum
        
        if numFlag or c.isnumeric():
            # Edge case where ascii is 0-9 but braille is 1-2-...-9-0
            # Correct by manually changing 0s
            if c == '0': 
                c = 'j'
            else:
                c = chr(ord(c)+charAdj)
        
        ret += engToBrl[c]
    return ret

# Convert braille to english
# Input a full braille string and returns
def cvtBrlToEng(b):
    ret = ''
    numFlag = False
    while len(b) >= 6:
        sub = b[0:6]
        b = b[6:]

        if sub == engToBrl[' ']:
            numFlag = False
        if sub == brlCap:
            sub = b[0:6]
            b = b[6:]
            ret += brlToEng[sub].upper()
        elif sub == brlNum:
            numFlag = True
            sub = b[0:6]
            b = b[6:]
        elif not numFlag:
            ret += brlToEng[sub]

        if numFlag:
            # Edge case where ascii is 0-9 but braille is 1-2-...-9-0
            # Correct by manually changing 0s
            if brlToEng[sub] == 'j':
                ret += '0'
            else:
                ret += chr(ord(brlToEng[sub])-charAdj)
    return ret

# Main method
def __main__():
    # Collect arguments from command line
    args = sys.argv
    args.pop(0) # Remove the first argument (file name)

    # Check which direction we are converting in
    braille = True
    for arg in args:
        # Check if string contains any other characters other than the braille ones
        if not re.match('^[.O]+$', arg):
            braille = False;
            break;
        # Check if string len is not a multiple of 6, then it is not braille
        if not len(arg)%6 == 0:
            braille = False;
            break;

    # Convert all of our arguments depending on the direciton
    output = ''

    if braille:
        output += cvtBrlToEng(args[0])
    else:
        if len(args) > 1: # If more than one argument
            for arg in args:
                output += cvtEngToBrl(arg)
                # If not the last argument, re add a space inbetween arguments
                # Arguments in commandline do not keep whitespace, they are just
                # assumed to be separate arguments so we will assume one space
                # was between them
                if not arg == args[-1]:
                    output += engToBrl[' ']
        else:
            output += cvtEngToBrl(args[0])
            
    print(output)

__main__()