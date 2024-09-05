import sys
charToBrailleDict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
        '9': '.OO...', '0': '.OOO..', '.' : '..00.0', ',' :'..0...','?' :'..0.00','!':'..000.',':' : '..00..', ';' : '..0.0.', '-' : '....00',
        '/' :'.0..0.', '<' : '.00..0', '>' : '0..00.', '(' : '0.0..0' , ')' : '.0.00.' , 'capital' : '.....O' , 'number' : '.O.OOO'
    }
#dict which consist number and special characters
brailleToNumdict = {v: k for k, v in charToBrailleDict.items()}  
#dict which consist characters and special characters
brailleToCharDict = {
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
 '..00.0': '.',
 '..0...': ',',
 '..0.00': '?',
 '..000.': '!',
 '..00..': ':',
 '..0.0.': ';',
 '....00': '-',
 '.0..0.': '/',
 '.00..0': '<',
 '0..00.': '>',
 '0.0..0': '(',
 '.0.00.': ')'}

def convertEnglishtoBraille(s):
    output = ''
    isNumber = False
    for char in s:
        #is upper case then need to add upper code
        if char.isupper():
            output += charToBrailleDict['capital']
        #if first time number then need to add number and no need to number until find space and new number
        elif char.isnumeric() and not isNumber:
            output += charToBrailleDict['number']
            isNumber = True
        #if space means number processed. 
        elif char == ' ':
            isNumber = False
        output += charToBrailleDict[char.lower()]
    return output


def isBraille(s):
    for char in s:
        if not (char == 'O' or char == '.') :
            return False
    return True


def convertBrailleToEnglish(s) :
    output = ''
    isCapital = False
    isNumber = False
    for i in range(0, len(s), 6) :
        
        #if find capital braille then set capital true and skip that braille.
        if(brailleToNumdict[s[i:i+6]] == 'capital') :
            isCapital = True
            continue
        #if numbe braille find then set number true and skip that braille
        elif brailleToNumdict[s[i:i+6]] == 'number' :
            isNumber = True
            continue
        #once space braille find means number has been processed
        elif brailleToNumdict[s[i : i+ 6]] == ' ':
            isNumber = False
        #if capital letter then converted to upper
        if isCapital:
            output += brailleToCharDict[s[i : i+ 6]].upper()
            isCapital = False
        #if num then getting num from dict
        elif isNumber:
            output += brailleToNumdict[s[i : i+ 6]]
        #else case lower characters or special characters.
        else : 
            output += brailleToCharDict[s[i : i+ 6]]

    return output


if __name__ == "__main__":
    input = ' '.join(sys.argv[1:])
    
    #convert braille to english
    if isBraille(input):
        print(convertBrailleToEnglish(input))
    else:
        #convert english to braille
        print(convertEnglishtoBraille(input))