import sys

braille_to_alpha = {
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
    '.....O': 'CAP',
    '.O.OOO': 'NUM',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
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
    '.OOO..': '0',
    '.O...O': '.',
    '......': ' '
}

def braile_to_alphabet(input: str):
    i = 0
    size = len(input)
    capital = False
    number = False
    output = ''
    while i < size:
        letter = input[i:i+6]

        if number:
            letter = braille_to_num[letter]
            if letter == ' ':
                number = False

        else:
            letter = braille_to_alpha[letter]
            if capital:
                capital = False
                letter = letter.upper()
            if letter == 'CAP':
                capital = True
                i += 6
                continue
            if letter == 'NUM':
                number = True
                i += 6
                continue
        output += letter
        i+=6
    return output


alpha_to_braille = dict((v,k) for k,v in braille_to_alpha.items())
num_to_braille = dict((v,k) for k,v in braille_to_num.items())

def alphanum_to_braille(input: str):
    number = False
    output = ''
    for i in input:
        if i.isdigit():
            if not number:
                output += alpha_to_braille['NUM']
                number = True
            output += num_to_braille[i]
        else:
            number = False
            if i.isupper():
                output += alpha_to_braille['CAP']
                i = i.lower()
            output += alpha_to_braille[i]
    return output


def detect(input: str):
    l = ''
    try:
        l = braile_to_alphabet(input)
    except(KeyError):
        try:
            l = alphanum_to_braille(input)
        except(KeyError):
            l = "Not a valid input"
    print(l)
    return


def proccess_args():
    if len(sys.argv) == 1:
        print("Need to have an argument")
        return
    input_arg = sys.argv[1]
    i = 2
    while i < len(sys.argv):
        input_arg += " " + sys.argv[i]
        i += 1
    detect(input_arg)
    return

if __name__ == "__main__":
    proccess_args()