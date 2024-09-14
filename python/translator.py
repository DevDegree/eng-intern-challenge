import sys

# Braille to English Mapping (simplified)
braille_to_english = {
    'O.....': 'a',     # a
    'O.O...': 'b',     # b
    'OO....': 'c',     # c
    'OO.O..': 'd',     # d
    'O..O..': 'e',     # e
    'OOO...': 'f',     # f
    'OOOO..': 'g',     # g
    'O.OO..': 'h',     # h
    '.O.O..': 'i',     # i
    '.OOO..': 'j',     # j
    'O...O.': 'k',     # k
    'O.O.O.': 'l',     # l
    'OO..O.': 'm',     # m
    'OO.OO.': 'n',     # n
    'O..OO.': 'o',     # o
    'OOO.O.': 'p',     # p
    'OOOOO.': 'q',     # q
    'O.OOO.': 'r',     # r
    '.OO.O.': 's',     # s
    '.OOOO.': 't',     # t
    'O...OO': 'u',     # u
    'O.O.OO': 'v',     # v
    '.OOO.O': 'w',     # w
    'OO..OO': 'x',     # x
    'OO.OOO': 'y',     # y
    'O..OOO': 'z',     # z
    '......': ' ',     # space
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '|',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '.....O': 'CF',
    '.O...O': 'DF',
    '.O.OOO': 'NF'
}

braille_number = {
    'O.....': '1',    # 1
    'O.O...': '2',    # 2
    'OO....': '3',    # 3
    'OO.O..': '4',    # 4
    'O..O..': '5',    # 5
    'OOO...': '6',    # 6
    'OOO0..': '7',    # 7
    'O.OO..': '8',    # 8
    '.OO...': '9',    # 9
    '.OOO..': '0',    # 0
    '......': ' '
}

english_to_braille = {
    'a': 'O.....',     # a
    'b': 'O.O...',     # b
    'c': 'OO....',     # c
    'd': 'OO.O..',     # d
    'e': 'O..O..',     # e
    'f': 'OOO...',     # f
    'g': 'OOOO..',     # g
    'h': 'O.OO..',     # h
    'i': '.O.O..',     # i
    'j': '.OOO..',     # j
    'k': 'O...O.',     # k
    'l': 'O.O.O.',     # l
    'm': 'OO..O.',     # m
    'n': 'OO.OO.',     # n
    'o': 'O..OO.',     # o
    'p': 'OOO.O.',     # p
    'q': 'OOOOO.',     # q
    'r': 'O.OOO.',     # r
    's': '.OO.O.',     # s
    't': '.OOOO.',     # t
    'u': 'O...OO',     # u
    'v': 'O.O.OO',     # v
    'w': '.OOO.O',     # w
    'x': 'OO..OO',     # x
    'y': 'OO.OOO',     # y
    'z': 'O..OOO',     # z
    ' ': '......',     # space
    '1': 'O.....',    # 1
    '2': 'O.O...',    # 2
    '3': 'OO....',    # 3
    '4': 'OO.O..',    # 4
    '5': 'O..O..',    # 5
    '6': 'OOO...',    # 6
    '7': 'OOO0..',    # 7
    '8': 'O.OO..',    # 8
    '9': '.OO...',    # 9
    '0': '.OOO..',    # 0
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '|': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    'CF': '.....O',
    'DF': '.O...O',
    'NF': '.O.OOO'
}

def translate_to_braille(text):
    result = ""
    number = False
    for char in text:
        if char.isupper():
            result += english_to_braille['CF']
            result += english_to_braille[char.lower()]
        elif char.isnumeric() and not number:
            result += english_to_braille['NF']
            result += english_to_braille[char]
            number = True
        elif number and char ==".":
            result += english_to_braille['DF']
        elif number and char == " ":
            number = False 
            result += english_to_braille[" "]
        else:
            result += english_to_braille[char]
    return result

def translate_to_english(text):
    result = ""
    capital = False
    number = False
    for i in range(len(text)//6):
        symbol = text[i*6:i*6+6]
        if number:
            letter = braille_number[symbol]
            if letter == ' ':
                number = False
        else:
            letter = braille_to_english[symbol]
            if capital: 
                letter = letter.upper()
                capital = False
        if letter == "CF":
            capital = True
        elif letter == "DF":
            letter = '.'
        elif letter == "NF":
            number = True
        else:        
            result += letter
    return result

def main():
    if len(sys.argv) < 2:
        return
    input_text = sys.argv[1]
    for i in range(2, len(sys.argv)):
        input_text += " " + sys.argv[i]
    
    if all(c in '.O' for c in input_text) and len(input_text) % 6 == 0:
        # Assume input is Braille
        result = translate_to_english(input_text)
    else:
        # Assume input is English
        result = translate_to_braille(input_text)

    print(result)
main()

#CF a b c space NF 1 2 3 space x CF y z