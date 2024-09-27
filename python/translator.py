import sys

# Return True if string is Braille ('O' and '.' only)
# else Return False
def isBraille(s):
    for c in s:
        if (c != 'O' and c != '.'):
            return False
    return True


# Translates input string from English to Braille
def eToB(s):
    result = ""
    isInNum = False
    for c in s:
        if c.isdigit():
            if not isInNum:
                result += ".O.OOO"
                isInNum = True
            result += eToBChar(c)
        else:
            if isInNum:
                isInNum = False
            result += eToBChar(c)
    return result

# Translates english character to corresponding braille string
def eToBChar(c):
    alphabet = {
            'a': "O.....",
            'b': "O.O...",
            'c': "OO....",
            'd': "OO.O..",
            'e': "O..O..",
            'f': "OOO...",
            'g': "OOOO..",
            'h': "O.OO..",
            'i': ".OO...",
            'j': ".OOO..",
            'k': "O...O.",
            'l': "O.O.O.",
            'm': "OO..O.",
            'n': "OO.OO.",
            'o': "O..OO.",
            'p': "OOO.O.",
            'q': "OOOOO.",
            'r': "O.OOO.",
            's': ".OO.O.",
            't': ".OOOO.",
            'u': "O...OO",
            'v': "O.O.OO",
            'w': ".OOO.O",
            'x': "OO..OO",
            'y': "OO.OOO",
            'z': "O..OOO",
            ' ': "......"
            }
    nums = {           
            '0': ".OOO..",
            '1': "O.....",
            '2': "O.O...",
            '3': "OO....",
            '4': "OO.O..",
            '5': "O..O..",
            '6': "OOO...",
            '7': "OOOO..",
            '8': "O.OO..",
            '9': ".OO...",
            }

    if c.isdigit():
        return nums[c]
    
    elif c == ' ':
        return alphabet[c]
    elif c.isupper():
        return ".....O" + alphabet[c.lower()]
    else:
        return alphabet[c]
        


    


# Translates braille string to english string
def bToE(s):
    result = ""
    i = 0
    num = False

    while (i < len(s)):
        c = s[i:i+6]
        if c == ".O.OOO":
            num = True
            i += 6
            continue

        if num:
            result += bToEChar(c, ".O.OOO")
            num = False
            i += 6
        elif c == ".....O":
            result += bToEChar(s[i+6:i+12],c)
            i += 12
        elif c == "......":
            # num = False
            result += " "
            i += 6
        else:
            result += bToEChar(c,"")
            i += 6

    return result
        
# Translates 6 character braille string to corresponding english character
# modifier m specifies if Captialized or number
def bToEChar(c, m):
    upperCase = {
        'O.....': 'A',
        'O.O...': 'B',
        'OO....': 'C',
        'OO.O..': 'D',
        'O..O..': 'E',
        'OOO...': 'F',
        'OOOO..': 'G',
        'O.OO..': 'H',
        '.OO...': 'I',
        '.OOO..': 'J',
        'O...O.': 'K',
        'O.O.O.': 'L',
        'OO..O.': 'M',
        'OO.OO.': 'N',
        'O..OO.': 'O',
        'OOO.O.': 'P',
        'OOOOO.': 'Q',
        'O.OOO.': 'R',
        '.OO.O.': 'S',
        '.OOOO.': 'T',
        'O...OO': 'U',
        'O.O.OO': 'V',
        '.OOO.O': 'W',
        'OO..OO': 'X',
        'OO.OOO': 'Y',
        'O..OOO': 'Z',
        '......': ' '
    }    
    rest = {
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
        '......': ' ',
        ".O...O": "."
    }
    nums = {
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
    if m == ".....O":
        return upperCase[c]
    elif m == ".O.OOO":
        return nums[c]
    else:
        return rest[c]


def main():
    input_str = ' '.join(sys.argv[1:])
    if isBraille(input_str):
        print(bToE(input_str))
    else:
        print(eToB(input_str))

if __name__ == "__main__":
    main()