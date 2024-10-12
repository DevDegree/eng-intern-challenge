import sys

# maps english alphanumeric numbers and special characters to braille
e2b = {
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
    ' ': '......',
    'number': '.O.OOO',
    'capital': '.....O',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

#maps braille to english alphabet a-z as well as special characters
b2e = {
'.....O': 'capital',
'..OOOO': 'number',
'......': ' ',
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
}
#maps braille numbers to number
num2e = {
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
}


#translates braille to english
def B2E(input):
    result = ""
    number = False
    capital = False
    index = 0
    while index <= len(input) - 6:
        code = input[index:index+6]
        index += 6

        if code == e2b['capital']:
            capital = True
            continue
        
        elif code == e2b['number']:
            number = True
            continue
        elif code == e2b[' ']:
            number = False
            result += " "
        elif number:
            result += num2e.get(code)
        elif capital:
            result += b2e.get(code).upper()
            capital = False
        else:
            result += b2e.get(code)
    return result

#translates english to braille
def E2B(input):
    result = ""
    number = False
    for c in input:
        if c.isupper():
            result += e2b.get("capital")
            result += e2b.get(c.lower())
        elif c.isdigit():
            if number:
                result += e2b.get(c)
            else:
                number = True
                result += e2b.get("number")
                result += e2b.get(c)
        else:
            number = False
            result += e2b.get(c)
    return result

#checks if input is braille
def is_braille(s):
    valid_chars = {'O', '.'}
    if len(s) %6 == 0:
        for c in s:
            if c not in valid_chars:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        # Input is Braille, translate to English
        translated = B2E(input_str)
    else:
        # Input is English, translate to Braille
        translated = E2B(input_str)

    print(translated)
