import sys

# ------------ Defining variables and constants ------------
brailleToEnglish = {
    # alphabet letters a - z
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
     # Space
    "......": " ",
    # decimal point
    ".O...O": "."
}

brailleToNums = {
    # Numbers (0 - 9) - Represented as a-j as well
    "O.....": "1",  # Same as 'a'
    "O.O...": "2",  # Same as 'b'
    "OO....": "3",  # Same as 'c'
    "OO.O..": "4",  # Same as 'd'
    "O..O..": "5",  # Same as 'e'
    "OOO...": "6",  # Same as 'f'
    "OOOO..": "7",  # Same as 'g'
    "O.OO..": "8",  # Same as 'h'
    ".OO...": "9",  # Same as 'i'
    ".OOO..": "0"  # Same as 'j'  
}

# same thing as above but are flipping the key and values
englishToBraille = {val: key for key, val in brailleToEnglish.items()}
numsToBraille = {val: key for key, val in brailleToNums.items()}

capitalFollows = ".....O"
numberFollows = ".O.OOO"

# ------------ Functions ------------
def determineInputType(input: str) -> str:
    '''
    We check for alphanumeric characters. If we have alphanumeric characters we know to go english -> braille.
    If we don't have any alphanumeric, we know to go from braille -> english.
    This function will assume english if braille is given with spaces

    param - input: a string with the input string we received
    return - "english" or "braille" depending on situation

    ex:
    input: 'hello'
    output: 'english'

    input: '0.....'
    output: 'braille'
    '''

    if all(char in "O." for char in input) and len(input) >= 6:
        return "braille"
    return "english"

def translateToBraille(input: str) -> str:
    '''
    Take each character in english and translate it into braille equivalent. Assumes that input characters are alphanumeric

    param - input: string with input string
    return - string of translation into braille

    ex:
    input: 'a'
    output: '0.....'

    '''
    translation = ""
    numbersFollowFlag = False

    for c in input:
        if c.isupper():
            translation += capitalFollows
        if c.isnumeric() and not numbersFollowFlag:
            numbersFollowFlag = True
            translation += numberFollows
        if c == " ":
            numbersFollowFlag = False
        
        if numbersFollowFlag:
            translation += numsToBraille[c]
        else:
            translation += englishToBraille[c.lower()]
    return translation
        
def translateToEnglish(input: str) -> str:
    '''
    Take every 6 characters of the input and put them together to create one character in braille. If input string is not divisible
    by 6, will return a simple error message.
    This function will use a fixed sliding window approach to focus on each 6 characters in the input string

    param - input: string with input string
    return - string of translation into braille

    ex:
    input: '.....00.....'
    output: 'A'
    '''
    input_len = len(input)
    translation = ""
    capitalFollowsFlag = False
    numbersFollowsFlag = False
    if input_len % 6 != 0:
        return "ERROR: A character is missing at least one braille symbol is missing"
    for R in range(6, input_len + 1, 6):
        char = input[R-6: R]
        # flag setting
        if char == capitalFollows:
            capitalFollowsFlag = True
            continue
        if char == numberFollows:
            numbersFollowsFlag = True
            continue
        if char == englishToBraille[" "]:
            numbersFollowsFlag = False
        
        # adding to translation
        if capitalFollowsFlag:
            translation += brailleToEnglish[char].upper()
            capitalFollowsFlag = False
        elif numbersFollowsFlag:
            translation += brailleToNums[char]
        else:
            translation += brailleToEnglish[char]

    return translation

# ------- main -----------
if __name__ == "__main__":
    args = sys.argv[1:]     #ignore 0 idx because it is script name
    input = " ".join(args)

    inputType = determineInputType(input)
    if inputType == 'english':
        output = print(translateToBraille(input))
    else:
        output = print(translateToEnglish(input))