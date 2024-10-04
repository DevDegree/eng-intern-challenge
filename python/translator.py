# Author: Christina N
import sys

braille_letter_dict = {

'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
'k':'O...O.', 'l': 'O.O.O.', 'm': 'O..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
'z': 'O..OOO', '.': '..O...', '!': '..OOO.', ':': '..OO..', '-': '....OO',
'/': '.OO..O.', '<': '.O..O.', '>': 'O.O..O', '(': 'O.O..O', ')': '.O.OO.',
' ': '......',
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
    'O..O.': 'm',
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
    '..O...': '.',
    '..OOO.': '!',
    '..OO..': ':',
    '....OO': '-',
    '.OO..O.': '/',
    '.O..O.': '<',
    'O.O..O': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}

braille_number_dict = {

'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
'6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'

}

# 
def braille_tokenizer(string):
    token_list = []
    token = ''
    counter = 0

    for i in range(len(string)):
        if counter == 6:
            counter = 0
            token_list.append(token)
            token = ''
        token += string[i]
        counter += 1

    if token:
        token_list.append(token)
    return token_list

#'capital': '.....0', 'decimal': '.0...0', 'number': '.0.000', 

def isBraille(string) :
    for i in string:
        if i != 'O' and i != '.':
            return False
    return True

def translator(string):
    translated = []
    isCap = False
    isNum = False

    if isBraille(string): # braille
        # read from list
        token_list = braille_tokenizer(string)
        # check if its a number, decimal or capital
        for i in range(len(token_list)):
            if token_list[i] == '.O.OOO': # then NUMBER
                # check the trans
                isNum = True
                continue
            elif token_list[i] == '.O...O': # then DECIMAL
                continue
            elif token_list[i] == '.....O': # then CAPITAL
                isCap = True
                continue
            elif token_list[i] in braille_letter_dict and not isNum: # then LETTER
                    translationToken = braille_letter_dict[token_list[i]]
                    # check
                    if isCap:
                        translated.append(translationToken.upper())
                        isCap = False
                    else: 
                        translated.append(translationToken)
            elif isNum :
                translationToken = braille_number_dict[token_list[i]] 
                translated.append(translationToken)

        # print translation
        print("Translation:", ''.join(translated))
    else: # english
        for char in string:
            # check if capital
            if char.isupper():
                translated.append('.....O') # capital
                isCap = True
            elif char.isdigit() :
                if not isNum:
                    translated.append('.O.OOO') 
                    isNum = True

            if char.lower() in braille_letter_dict: 
                    translated.append(braille_letter_dict[char.lower()])
            elif isNum and char in braille_number_dict:
                translated.append(braille_number_dict[char])
            else:
                translated.append('') # if char not found then append empty string

        print(''.join(translated))

if __name__ == "__main__":  # Main guard
        argument = sys.argv[1]
        translator(argument)