import sys

text = {
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
    'cap': '.....O',
    'dec': '.O...O',
    'num': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..O.O',
    '(': 'O.O..O',
    ')': '.O.OO.'
}

braille = {
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
    '.....O': 'cap',
    '.O...O': 'dec',
    '.O.OOO': 'num',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..O.O': '>',
    'O.O..O': '(',
    '.O.OO.': ')'
}

letter_to_number = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0'
}


def translate(input):
    is_braille = True

    for char in input:
        if not (char == '.' or char == 'O'):
            is_braille = False
            print(char)
            break

    output = ""
    if len(input) % 6 == 0 and is_braille:
        n_chars = len(input)//6
        cap = False
        num = False

        for i in range(n_chars):
            matrix = input[i*6:(i*6)+6]
            
            if not num and cap and braille[matrix] != 'dec' and braille[matrix] != 'num' and braille[matrix] != 'cap':
                output += braille[matrix].upper()
                cap = False
            elif num and braille[matrix] == ' ':
                num = False
                output += ' '
            elif num and braille[matrix] != 'dec' and braille[matrix] != 'num' and braille[matrix] != 'cap':
                output += letter_to_number[braille[matrix]]
            elif braille[matrix] == 'cap':
                cap = True
            elif braille[matrix] == 'num':
                num = True
            elif braille[matrix] == 'dec':
                output += "."
            else:
                output += braille[matrix]
    else:
        number = False
        for char in input:
            if char.isupper():
                output += text['cap']
            elif char.isnumeric():
                output += text['num']
                number = True
            if number and char == '.':
                output += text['dec']
            elif number and char == ' ':
                number = False
            output += (text[char.lower()])

    return output

def main():
    inputs = sys.argv[1:]
    output = "".join(translate(input) for input in inputs)
    print(output)

if __name__ == "__main__":
    main()
