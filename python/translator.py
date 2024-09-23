import sys

translator = {
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
    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'}

translator2 = {
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
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    'OO...': '.9',
    '.OOO..': '0',
    '......': ' ',
    '.....O': 'capital',
    '.O.OOO': 'number'}

# check if input is valid braille
def is_braille(input_str):
    return all(c in 'O.' for c in input_str)

def translate_to_english(brailleInput):
    result = []
    isNum = False
    isCap = False
    i = 0

    while i < len(brailleInput):
        brailleChar = brailleInput[i:i+6]

        # check for number 
        if brailleChar == translator['number']:
            isNum = True
            i += 6

        # check for capital 
        elif brailleChar == translator['capital']:
            isCap = True
            i += 6

        # check for space in bsraille
        elif brailleChar == translator[' ']:
            result.append(' ')
            isNum = False
            isCap = False
            i += 6

        else:
            char = translator2.get(brailleChar, '?')
            if isNum:
                if char.isdigit():
                    # convert number to letter if in number mode
                    result.append(char)
                elif char.isalpha() and char in 'abcdefghij':
                    # convert letter to number if in number mode
                    result.append(char)
            else:
                if isCap:
                    result.append(char.upper())
                    isCap = False
                else:
                    result.append(char)
            i += 6

    return ''.join(result)

def translate_to_braille(english_str):
    result = []
    in_number_mode = False
    
    for char in english_str:
        if char.isdigit():
            # add number indicator if not alr in number mode
            if not in_number_mode:
                result.append(translator['number'])
                in_number_mode = True
            result.append(translator[char])
        elif char.isalpha():
            # capital letters should be handled by a capital indicator
            if char.isupper():
                result.append(translator['capital'])
                result.append(translator[char.lower()])
            else:
                result.append(translator[char])
            # exit number mode
            in_number_mode = False
        elif char == ' ':
            result.append(translator[' '])
            # reset number mode after space
            in_number_mode = False
    
    return ''.join(result)

def main():

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

main()

