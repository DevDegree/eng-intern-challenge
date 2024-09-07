import re
import sys

alphabet_translation = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

brail_to_nums = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

brail_to_alphabet = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}

def word_to_brail(s):
    word = []
    state = 'alph'
    s = s.strip()
    
    for char in s:
        if char == ' ':
            word.append("......")
            continue
        
        if char.isdigit():
            if state != 'num':
                word.append('.O.OOO')  # Numeric indicator
                state = 'num'
            word.append(alphabet_translation[char])  # Translate the digit
        elif char.isalpha():
            if state != 'alph':
                state = 'alph'  # Reset back to alphabet state after numbers
            if char.isupper():
                word.append(".....O")  # Capital letter indicator
            word.append(alphabet_translation[char.lower()])
    
    return ''.join(word)


def brail_to_word(s):
    word = []
    state = 'alph'
    cells = [s[i:i + 6] for i in range(0, len(s), 6)]
    nextUpper = False

    for cell in cells:
        if cell == '......':
            word.append(" ")
            continue
        if state == 'alph':
            if cell == '.O.OOO':
                state = 'num'
                continue
            elif cell == '.....O':
                nextUpper = True
                continue
            else:
                if nextUpper:
                    word.append(brail_to_alphabet.get(cell, '?').upper())
                    nextUpper = False
                else:
                    word.append(brail_to_alphabet.get(cell, '?'))
        else:
            word.append(brail_to_nums.get(cell, '?'))
            
    return ''.join(word)


if len(sys.argv) > 1:
    test_string = ' '.join(sys.argv[1:])
    # Check if the input is already in braille format (only dots and 'O')
    if re.fullmatch(r'^[O.]+$', test_string):
        # Input is in braille format, convert to word
        print(brail_to_word(test_string))
    else:
        # Input is a word, convert to braille
        print(word_to_brail(test_string))

#not exactly sure how to format output so that it works with translator.test.py