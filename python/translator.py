import sys

# "Assuming that characters outside the technical requirements don't need to be supported"

# Maps for translation between braille and english characters
eng_to_brail_map = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    '1': 'O.....',    '2': 'O.O...',
    '3': 'OO....',    '4': 'OO.O..',    '5': 'O..O..',    '6': 'OOO...',
    '7': 'OOOO..',    '8': 'O.OO..',    '9': '.OO...',    '0': '.OOO..',
    ' ': '......'
}

brail_to_eng_map = {
    'O.....': 'a',    'O.O...': 'b',    'OO....': 'c',    'OO.O..': 'd',
    'O..O..': 'e',    'OOO...': 'f',    'OOOO..': 'g',    'O.OO..': 'h',
    '.OO...': 'i',    '.OOO..': 'j',    'O...O.': 'k',    'O.O.O.': 'l',
    'OO..O.': 'm',    'OO.OO.': 'n',    'O..OO.': 'o',    'OOO.O.': 'p',
    'OOOOO.': 'q',    'O.OOO.': 'r',    '.OO.O.': 's',    '.OOOO.': 't',
    'O...OO': 'u',    'O.O.OO': 'v',    '.OOO.O': 'w',    'OO..OO': 'x',
    'OO.OOO': 'y',    'O..OOO': 'z',    '......': ' '
}

brail_to_num_map = {
    'O.....': '1',    'O.O...': '2',    'OO....': '3',    'OO.O..': '4',
    'O..O..': '5',    'OOO...': '6',    'OOOO..': '7',    'O.OO..': '8',
    '.OO...': '9',    '.OOO..': '0'
}

# Special braille characters
caps_follows = ".....O"
num_follows = ".O.OOO"
space = "......"

def getBrailleString(englishString):

    """
    Converts an alphanumeric string into its Braille representation using 'O' & '.'.

    Args:
        englishString (str): A string containing only alphabets, numbers, and spaces.

    Returns:
        brailleString (str): A Braille string representation of the input string.
    """


    brailString = ""
    areParseNum = False

    for char in englishString:

        # If char is upperCase, insert a "caps_follows" braille char before
        if (char.isupper()): 
            brailString += caps_follows

        # If char is numeric and not "parse nums" flag not set, add "num_follows" char and set the flag
        elif (char.isnumeric() and not areParseNum):
            brailString += num_follows
            areParseNum = True
        # If char is space, turn off the "parse nums" flag
        elif (char == " "):
            areParseNum = False

        brailString += eng_to_brail_map[char.lower()]
    
    return brailString

def getEnglishString(brailleString):

    """
    Converts an Braille string into its alphanumeric representation.

    Args:
        brailleString (str): A Braille string containing only 'O' & '.'

    Returns:
        englishString (str): A english string representation of the input string.
    """

    nextCharNum = False
    nextCharCaps = False
    englishString = ""

    for i in range(0, len(brailleString), 6):

        brailLetter = brailleString[i:i+6]

        # if char is "caps_follows" set a next char is capital flag, and move to next iteration
        if (brailLetter == caps_follows):
            nextCharCaps = True
            continue
        # if char is "num_follows" set a "following chars are num" flag, and move to next iteration
        elif (brailLetter == num_follows):
            nextCharNum = True
            continue
        
        englishLetter = brail_to_eng_map[brailLetter] # get english equivalent of braille letter

        if (brailLetter == space): # If char is 'space', turn off "following chars are num" flag
            nextCharNum = False

        elif (nextCharCaps): # If nextCharCaps flag is set, then convert char to upper case
            englishLetter = englishLetter.upper()
            nextCharCaps = False

        elif (nextCharNum): # If nextCharNum flag is set, get the num equivalent of the braille
            englishLetter = brail_to_num_map[brailLetter]

        englishString += englishLetter
    
    return englishString

def isBraille(inputString):

    """
    Checks if input string is in Braille or English

    Args:
        inputString (str): a valid English or Braille string
    Returns:
        (bool): flag of whether string is Braille or not
    """

    for char in inputString:
        if (char != 'O' and char != '.'):
            return False
    return True

inputString = ' '.join(sys.argv[1:])
outputString = ""

if isBraille(inputString):
    outputString = getEnglishString(inputString)
else:
    outputString = getBrailleString(inputString)

print(outputString)
