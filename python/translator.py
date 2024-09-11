# Author: Clara Zhang
# Email: clara.z.dev@gmail.com

import sys
from dictionary import b2e, e2b, isBrailleCapital, isBrailleNumber, brailleNumber, brailleCapital
from collections import Counter


def isBraille(string):
    """Check if a string is a valid Braille string."""
    return len(string) % 6 == 0 and set(string).issubset({'.', 'O'})


def braille2English_handleLetter(char, capital_lock):
    if capital_lock and 'a' <= char <= 'z':
        char = char.upper()
    return char


def braille2English_handleNumber(char, number_lock):
    if number_lock and 'a' <= char <= 'j':
        char = str(ord(char) - ord('a') + 1)
    return char


def convertBrailleToEnglish(braille_string):
    """Convert a Braille string to English"""
    capital_lock = False
    number_lock = False
    ans = []

    for i in range(0, len(braille_string), 6):
        group = braille_string[i:i+6]
        if isBrailleCapital(group):
            capital_lock = True
        elif isBrailleNumber(group):
            number_lock = True
        else:
            char = b2e[group]
            if char is None:
                # The symbol does not fit Braille characters
                return None
            
            char = braille2English_handleLetter(char, capital_lock)
            char = braille2English_handleNumber(char, number_lock)
            ans.append(char)

            if char == ' ':
                number_lock = False
            capital_lock = False
    
    return ''.join(ans)


def convertEnglishToBraille(english_string):
    ans = []
    number_lock = False

    for char in english_string:
        if char.isupper():
            ans.append(brailleCapital)
            ans.append(e2b[char.lower()])
        elif char.islower():
            ans.append(e2b[char])
        elif char.isdigit():
            if not number_lock:
                ans.append(brailleNumber)
                number_lock = True
            ans.append(e2b[char])
        elif char == ' ':
            number_lock = False
            ans.append(e2b[char])
        else:
            braille = e2b[char]
            if braille is None:
                return None
            ans.append(braille)

    return ''.join(ans)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    input_string = " ".join(arguments)

    result = None
    if isBraille(input_string):
        # Convert from Braille to English
        result = convertBrailleToEnglish(input_string)
    if result is None:
        # Convert from English to Braille
        # If the input appears to be Braille but cannot be decoded correctly, try processing it as English instead.
        result = convertEnglishToBraille(input_string)
    if result is None:
        result = 'Invalid input.'

    print(result)

