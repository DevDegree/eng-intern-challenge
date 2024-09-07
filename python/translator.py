from typing import List
import sys

# NOTE: Did not implement translation of punctuation characters and decimal numbers since requirements did not specify.

# Check if the input string is valid braille
def checkBraille(strB: str):
    for char in strB:
        if char not in '.O':
            return False
    return True

# Convert between braile and english
def translate(strA: str):
    if len(strA) == 0:
        return ""
    
    # Dictionaries 
    english_to_braille = {
        'a': 'O.....',#
        'b': 'O.O...',#
        'c': 'OO....',#
        'd': 'OO.O..',#
        'e': 'O..O..',#
        'f': 'OOO...',#
        'g': 'OOOO..',#
        'h': 'O.OO..',#
        'i': '.OO...',#
        'j': '.OOO..',#
        'k': 'O...O.',#
        'l': 'O.O.O.',#
        'm': 'OO..O.',#
        'n': 'OO.OO.',#
        'o': 'O..OO.',#
        'p': 'OOO.O.',#
        'q': 'OOOOO.',#
        'r': 'O.OOO.',#
        's': '.OO.O.',#
        't': '.OOOO.',#
        'u': 'O...OO',#
        'v': 'O.O.OO',#
        'w': '.OOO.O',#
        'x': 'OO..OO',#
        'y': 'OO.OOO',#
        'z': 'O..OOO',#
        '0': '.OOO..',# 
        '1': 'O.....',#
        '2': 'O.O...',#
        '3': 'OO....',#
        '4': 'OO.O..',#
        '5': 'O..O..',#
        '6': 'OOO...',#
        '7': 'OOOO..',#
        '8': 'O.OO..',#
        '9': '.OO...',#
        ' ': '......'
    }

    braille_to_english = {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f',
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z',
        '......': ' '
    }

    braille_to_number = {
        '.OOO..': '0',
        'O.....': '1',
        'O.O...': '2',
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9'
    }

   #signals
    capSig = '.....O'
    numSig = '.O.OOO'

    toRet = ""
    numStatus = False
    capStatus = False

    if not checkBraille(strA):
        for i in range(len(strA)):
            if strA[i].isupper():
                toRet += capSig + english_to_braille[strA[i].lower()]
            elif strA[i].isdigit():
                if not numStatus:
                    numStatus = True
                    toRet += numSig + english_to_braille[strA[i]]
                else:
                    toRet += english_to_braille[strA[i]]
            elif strA[i] == " ":
                numStatus = False
                toRet += english_to_braille[strA[i]]
            else:
                toRet += english_to_braille[strA[i]]
    else:
        i = 0 
        while i < len(strA):
            if i + 6 <= len(strA):
                currStr = strA[i:i+6]

                if currStr == capSig:
                    capStatus = True
                    i += 6
                elif currStr == numSig:
                    numStatus = True
                    i += 6
                elif currStr == '......':
                    numStatus = False
                    toRet += ' '
                    i += 6
                elif currStr in braille_to_english or currStr in braille_to_number:
                    if capStatus:
                        char = braille_to_english[currStr]
                        char = char.upper()
                        capStatus = False
                    elif numStatus:
                        char = braille_to_number[currStr]
                    else:
                        char = braille_to_english[currStr]

                    toRet += char
                    i += 6

                else:
                    # Invalid character
                    i += 6
            else:
                break

    return toRet

## For debugging:
# if __name__ == "__main__":
#     strV = ".....O.....O.....OOO.O.O....O..O.....O.O.O..O.......OO.O.OO.O.O.O.OO..O."
#     strD = translate(strV)
#     print(strD)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Join all arguments into a single string, preserving spaces
        input_string = ' '.join(sys.argv[1:])
        # Translate the entire input string at once
        result = translate(input_string)
        print(result, end="")