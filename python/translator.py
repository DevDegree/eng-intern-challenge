
import sys
specialCases = {'capitalFollows': '.....O', 'decimalFollows': '', 'numberFollows': '.O.OOO'}

    #direct conversion dictionary for letters
alphanum_to_braile = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        ' ': '......',  # Space
        ',': '.O....',  # Comma
        ';': '.O.O..',  # Semicolon
        ':': '..OO..',  # Colon
        '.': '..OO.O',  # Period
        '?': '..O.OO',  # Question mark
        '!': '.OO.O.',  # Exclamation point
        '-': '....OO',  # Hyphen
        "'": '....O.',  # Apostrophe
        '“': '.O.OOO',  # Left quotation mark
        '”': '.OOO.O',  # Right quotation mark
        '(': '..OOO.',  # Left parenthesis
        ')': '..OOO.',  # Right parenthesis (same as left)
        '/': '..O..O',  # Forward slash
    }
num_to_braille = {
        '1': 'O.....', 
        '2': 'O.O...', 
        '3': 'OO....', 
        '4': 'OO.O..', 
        '5': 'O..O..',
        '6': 'OOO...', 
        '7': 'OOOO..', 
        '8': 'O.OO..', 
        '9': '.OO...', 
        'O': '.OOO..'
}
braille_to_alphanum = {
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
    '.O....': ',',
    '.O.O..': ';',
    '..OO..': ':',
    '..OO.O': '.',
    '..O.OO': '?',
    '.OO.O.': '!',
    '....OO': '-',
    '....O.': "'",
    '.O.OOO': '“',
    '.OOO.O': '”',
    '..OOO.': '(',
    '..OOO.': ')',
    '..O..O': '/',
}
braille_to_num = {
    'O.....': '1', 
    'O.O...': '2', 
    'OO....': '3', 
    'OO.O..': '4', 
    'O..O..': '5', 
    'OOO...': '6', 
    'OOOO..': '7', 
    'O.OO..': '8', 
    '.OO...': '9', 
    '.OOO..': 'O', }

def brailleToEng(s):
    englishTranslation = ""
    n = 6
    isCapital = False
    isNumeric = False
    letters = [s[i:i+n] for i in range(0, len(s), n)] 
    for l in letters:
        if l == "......":
            englishTranslation += ' '
            isNumeric = False
        elif l == ".....O":
            isCapital = True
            continue
        elif l == ".O.OOO":
            isNumeric = True 
            continue
        else:
            if isCapital:
                englishTranslation += braille_to_alphanum[l].upper()
                isCapital = False
            elif isNumeric:
                englishTranslation += braille_to_num[l]
            else: 
                englishTranslation += braille_to_alphanum[l]
    return englishTranslation
    
        
def engToBraille(s):
    brailleTranslation = ""
    numberFlag = False
    for c in s:
        if c.isupper():
            brailleTranslation += specialCases['capitalFollows'] + alphanum_to_braile[c.lower()]
        elif c.isdigit() :
            addition =  num_to_braille[c] if  numberFlag else specialCases['numberFollows'] + num_to_braille[c]
            numberFlag = True
            brailleTranslation +=  addition
        elif c.islower(): 
            brailleTranslation += alphanum_to_braile[c]
        elif c == ' ':
            brailleTranslation += '......'
            numberFlag = False 
        else: 
            brailleTranslation += alphanum_to_braile[c]
    return brailleTranslation
        

def translate(s):
    #check if braille or english
    if '.' in s:
        #braille
        return brailleToEng(s)
    else: 
        #english
        return engToBraille(s)
    
if __name__ == '__main__':
    inputString = ' '.join(sys.argv[1:])
    result = translate(inputString)
    print(result)