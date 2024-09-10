import sys
import re

# Use hash maps to store the braille corresponding to each letter
alphaToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......' }

# Use hash maps to store the braille corresponding to each number
numericToBraille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..' }

# Special braille symbols
capitalFollows = '.....O'
numberFollows = '.O.OOO'
decimalFollows = ".O...O"

# We create two more hash maps using the ones above but flipping their keys and values.
# That way we can have quick look ups in the braille to English translation.
brailleToAlpha = {v: k for k, v in alphaToBraille.items()}
brailleToNumeric = {v: k for k, v in numericToBraille.items()}

def isStringBraille(input):
    """
    Gets whether or not the input is Braille by checking if the string
    contains only 'O' and '.' using regex.
    This is used to determine whether we translate from Braille or from English.

    Parameters:
    input (str): The string of either Braille or English.

    Returns:
    bool: True if the string is Braille, False otherwise.

    Example:
    >>> isStringBraille("Alice")
    False
    """
    return bool(re.fullmatch(r'[O.]*', input))

def convertStringToBraille(input):
    """
    Translates a given input into Braille from English.

    Parameters:
    input (str): The string containing characters from a-z or 0-9.

    Returns:
    str: The converted string containing characters 'O' or '.'

    Example:
    >>> convertStringToBraille("Hello World 42")
    .....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.........O.OOOOO.O..O.O...
    """
    brailleResult = ""
    isParsingNumber = False

    for char in input:
        if (char.isupper()):
            brailleResult += capitalFollows
        elif (char.isdigit() and not isParsingNumber):
            isParsingNumber = True
            brailleResult += numberFollows
        elif (char == " "):
            isParsingNumber = False

        if (isParsingNumber):
            brailleResult += numericToBraille[char]
        else:
            brailleResult += alphaToBraille[char.lower()]

    return brailleResult

def convertStringToEnglish(input):
    """
    Translates a given input from Braille to English.

    Parameters:
    input (str): The string containing characters 'O' and '.'

    Returns:
    str: The converted string containing characters a-z and 0-9.

    >>> convertStringToBraille(".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.........O.OOOOO.O..O.O...")
    Hello World 42
    """
    englishResult = ""
    isNextCharCapital = False
    isNextSequenceDigit = False

    for i in range(0, len(input), 6):
        currentBraille = input[i:i+6]

        if (currentBraille == capitalFollows):
            isNextCharCapital = True
            continue
        elif (currentBraille == numberFollows):
            isNextSequenceDigit = True
            continue

        if (isNextCharCapital):
            isNextCharCapital = False
            englishResult += brailleToAlpha[currentBraille].upper()
        elif (isNextSequenceDigit):
            englishResult += brailleToNumeric[currentBraille]
        else:
            englishResult += brailleToAlpha[currentBraille]

        if (currentBraille == alphaToBraille[" "]):
            isNextSequenceDigit = False

    return englishResult

def main():
    sentence = " ".join(sys.argv[1:])

    if (isStringBraille(sentence)):
        print(convertStringToEnglish(sentence))
    else:
        print(convertStringToBraille(sentence))

if __name__ == '__main__':
    main()
