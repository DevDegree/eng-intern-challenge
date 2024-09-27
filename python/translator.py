import sys


def isBraille(s):
    for c in s:
        if (c != 'O' and c != '.'):
            return False
    return True



def eToB(s):
    result = ""
    for c in s:
        result += eToBChar(c)
    return result

def eToBChar(c):
    result = ""
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

    isInNum = False

    if isinstance(c, int):
        if (not isInNum):
            isInNum = True
            result += ".O.OOO"
        result += nums[c]
        return result
    
    elif c == ' ':
        isInNum = False
        result += alphabet[c]
        return result
        

    elif c.isupper():
        result += ".....O"
        result += alphabet[c.lower()]
        return result
    else:
        result += alphabet[c]
        return result
        


    

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
    
def bToE(s):
    mods = {
        ".....O": "Cap",
        ".O.OOO": "Num"
    }

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
            i += 6
        elif c == ".....O":
            result += bToEChar(s[i+6:i+12],c)
            i += 12
        elif c == "......":
            num = False
            result += " "
            i += 6
        else:
            result += bToEChar(c,"")
            i += 6

    return result
        


def main():
    input_str = ' '.join(sys.argv[1:])
    if isBraille(input_str):
        print(bToE(input_str))
    else:
        print(eToB(input_str))

if __name__ == "__main__":
    main()