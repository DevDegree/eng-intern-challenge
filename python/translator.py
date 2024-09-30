import sys

class Status:
    is_number = False
    is_capital = False
    BRAILLE_CAPITAL = '.....O'
    BRAILLE_NUMBER = '.O.OOO'
    BRAILLE_SPACE = '......' 

# dictionaries to translate back and forth between langauges

numbersToBraille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

brailleToNumbers = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '......': ' '    
}

lettersToBraille = {
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
    'z': 'O..OOO'
}

brailleToLetters = {
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

# PRE: text must be a valid English string (only alphanumeric and spaces)
# POST: returns text translated to Braille
def translateToBraille(text):
    result = ''
    status = Status()
    for c in text:
        if (c == ' '):
            status.is_number = False
            result += status.BRAILLE_SPACE
        elif (c.isnumeric()):
            if (not status.is_number):
                result += status.BRAILLE_NUMBER
                status.is_number = True
            result += numbersToBraille.get(c)
        elif (c.isalpha()):
            if (c.isupper()):
                result += status.BRAILLE_CAPITAL
                c = c.lower()
            result += lettersToBraille.get(c)
    return result

# POST: updates status based on six string, returns whether status was set
def setStatus(six, status):
    if (six == Status.BRAILLE_CAPITAL):
        status.is_capital = True
        return True
    elif (six == Status.BRAILLE_NUMBER):
        status.is_number = True
        return True
    else:
        return False 

# PRE: six must be a valid Braille symbol
# POST: returns number or letter based on six character Braille string
def getChar(six, is_num):
    if (is_num):
        return brailleToNumbers.get(six)
    else:
        return brailleToLetters.get(six)

# POST: returns next character based on status, updates status        
def nextChar(c, status):
    ret = None
    if (status.is_capital):
        ret = c.upper()
        status.is_capital = False
    else:
        ret = c
    if (c == ' '):
        status.is_number = False
    return ret

# PRE: text must be valid Braille string 
# POST: returns text translated to English
def translateToEnglish(text):
    result = ''
    status = Status()
    for i in range(len(text) // 6):
        six = text[6 * i : 6 * i + 6]
        if (setStatus(six, status)):
            continue
        c = getChar(six, status.is_number)
        result += nextChar(c, status)
    return result

# POST: returns whether text is a Braille string
def isBraille(text):
    if (len(text) % 6 != 0):
        return False
    for c in text:
        if (c != 'O' and c != '.'):
            return False
    return True

# PRE: text must be valid Braille string or English string
# POST: returns translated text
def translate(text):
    if (isBraille(text)):
        return translateToEnglish(text)
    else:
        return translateToBraille(text)

args = sys.argv[1:]
# add space between each argument
text = ' '.join(args)
result = translate(text)
print(result)