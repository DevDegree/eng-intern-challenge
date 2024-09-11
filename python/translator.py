import sys
import string
ascii2b =       {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'}
b2ascii_char =  {'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z'}
b2ascii_nums =  {'.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'}
b2ascii_rest =  {'..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')', '......': ' '}
CAPITAL = '.....O'
DECIMAL = '.O...O'
NUMBER  = '.O.OOO'
SPACE = '......'

def itIsASCII(text):
    result = ""
    isNumber = False
    for char in text:
        if char.isupper():
            if isNumber:
                ... # invalid
            result += CAPITAL
            result += ascii2b[char.lower()]
        elif char.isdigit():
            if not isNumber:
                isNumber = True
                result += NUMBER
            result += ascii2b[char]
        elif char == " ":
            result += SPACE
            isNumber = False
        else:
            if isNumber:
                ... # invalid
            converted = ascii2b.get(char)
            if converted is None:
                ... # invalid
            else:
                result += converted
    return result
            

def assumeBraile(text):
    if len(text)%6 != 0:
        return itIsASCII(text)
    result = ""
    isCapital = False
    isNumber = False
    isDecimal = False
    i = 0
    while i < len(text):
        braille_six = text[i:i+6]
        if braille_six == SPACE:
            isCapital = False
            isNumber = False
            isDecimal = False
            result += " "
            i += 6
            continue
        
        if isCapital:
            isCapital = False
            converted = b2ascii_char.get(braille_six)
            if converted is None:
                return itIsASCII(text)
            i+=6
            result += converted.upper()
            continue
        elif isNumber:
            converted = b2ascii_nums.get(braille_six)
            if converted is None:
                if braille_six == DECIMAL:
                    isDecimal = True
                    i += 6
                    continue
                elif braille_six == ascii2b['.']:
                    i += 6
                    result += "."
                    continue
                return itIsASCII(text)
            i+=6
            result += converted
            continue
        elif isDecimal:
            isDecimal = False
            if braille_six == ascii2b['.']:
                i += 6
                result += "."
                continue
            elif braille_six == DECIMAL:
                i += 6
                result += ".."
                continue
            else:
                result += "."
                # no skip
        
        if braille_six == CAPITAL:
            isCapital = True
            i += 6
            continue
        elif braille_six == NUMBER:
            isNumber = True
            i += 6
            continue
        elif braille_six == DECIMAL:
            isDecimal = True
            i += 6
            continue

        converted = b2ascii_char.get(braille_six)
        if converted is None:
            converted = b2ascii_rest.get(braille_six)
            if converted is None:
                return itIsASCII(text)
        i += 6
        result += converted
    return result
        


text = " ".join(sys.argv[1:])
result = assumeBraile(text)
print(result, end="")