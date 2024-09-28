

import sys
def is_brail(text):
    for char in text:
        if ord(char) not in [79,46]:
            return False
    return True

def braille_to_text(argument):
    text_letters = {
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
        '.....O': 'cap_follows',
        '.O.OOO': 'num_follows',
        '......': ' ',
    }
    
    text_nums = {
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


    text = ''
    in_number_mode = False
    i = 0
    while i < len(argument):
        char = argument[i:i+6]
        if text_letters[char] == 'num_follows':
            in_number_mode = True
            i += 6
            continue
        if in_number_mode:
            if char == '......':
                in_number_mode = False
                text += ' '
                i += 6
                continue
            text += text_nums[char]
            i += 6
            continue
        if text_letters[char] == 'cap_follows':
            i+=6
            text += text_letters[argument[i:i+6]].upper()
            i += 6
            continue
        text += text_letters[char]
        i += 6

    return text


def text_to_braille(argument):
    braille = {
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
        'cap_follows': '.....O',
        'num_follows': '.O.OOO',

    }

    braille_nums = {
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

    braille_text = ''
    i = 0
    while i < len(argument):
        if argument[i] == ' ':
                braille_text += braille[argument[i]]
                i += 1
                continue
        if argument[i].isdigit():
            braille_text += braille['num_follows'] + braille_nums[argument[i]]
            i += 1
            while i < len(argument) and argument[i] != ' ':
                braille_text += braille_nums[argument[i]]
                i += 1
            continue
        if argument[i].isupper():
            braille_text += braille['cap_follows'] + braille[argument[i].lower()]
            i += 1 
            continue
        braille_text += braille[argument[i]]
        i += 1 

    return braille_text


argument = ' '.join(sys.argv[1:])
if is_brail(argument): 
    result = braille_to_text(argument)
else:
    result = text_to_braille(argument)
print(result)

