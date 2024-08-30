import sys

letter2Braille = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
               'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
               'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
               's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
               'y': 'OO.OOO', 'z': 'O..OOO', }

number2Braille = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
                  '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}


character2Braille = {'.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
                     ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', 
                     '(': 'O.O..O', ')': '.O.OO.', ' ': '......'}

braille2Letter = {v: k for k, v in letter2Braille.items()}
braille2Number = {v: k for k, v in number2Braille.items()}
braille2Character = {v: k for k, v in character2Braille.items()}

CAP = '.....O'
NUM = '.O.OOO'
SPACE = '......'

def isBraille(txt):
    """
    Determines if a given string is braille

    Parameters: txt = an input string
    Returns: A boolean indicating if the string is braille
    """
    
    s = set(txt)        # get unique elements in string  
    mod = len(txt) % 6      # string length is a multiple of 6

    # the string only contains O and . and length is a multiple of 6
    return len(s) == 2 and mod == 0 and 'O' in s and '.' in s

def convertToBraille(txt):
    """
    Convers a string of text to braille
    
    Parameters: txt = an input string
    Returns: a string with the braille representation of the text
    """

    output = ''
    numFlag = False
    for n in txt:
        if n.isupper():
            output += CAP   # add special capital character
            output += letter2Braille[n.lower()]
        elif n.islower():
            output += letter2Braille[n]
        elif n.isnumeric():
            if not numFlag:
                output += NUM   # add special number character
            numFlag = True
            output += number2Braille[n]
        else:
            output += character2Braille[n]
    return output

def convertToTxt(braille):
    """
    Convers a string of braille to txt
    
    Parameters: braille = an input string
    Returns: a string with the text representation of the braille
    """

    output = ''
    segments = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    capFlag = False
    numFlag = False

    for segment in segments:
        if segment == CAP:
            capFlag = True      # special cap flag
        elif segment == NUM:
            numFlag = True      # special num flag
        elif segment in braille2Letter.keys() and not numFlag:
            if capFlag:
                output += braille2Letter[segment].upper()
                capFlag = False
            else:
                output += braille2Letter[segment]
        elif segment in braille2Number.keys():
            output += braille2Number[segment]
        elif segment == SPACE:
            numFlag = False
            output += braille2Character[segment]
        else:
            output += braille2Character[segment]
    return output

def main():
    inStr = ' '.join(sys.argv[1:])
    if not isBraille(inStr):
        output = convertToBraille(inStr)
        print(output)
    else:
        output = convertToTxt(inStr)
        print(output)

if __name__ == '__main__':
    main()
