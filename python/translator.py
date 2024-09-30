import sys


CAP = '.....O'
NUM = '.O.OOO'
FLOAT = '.O...O'
SPACE = '......'

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
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

number = {
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

braille_number = {v: k for k, v in number.items()}

alpha = {v: k for k, v in braille.items()}


def is_valid(input):
    # Check if input is braille
    correct_lenth = len(input) % 6 == 0
    valid_chars = all(c in 'O.' for c in input)
    return correct_lenth and valid_chars


def alpha_to_braille(input):
    # take alphabet input and print out braille
    output = ''
    i = 0
    while i < len(input):
        char = input[i]
        if char.isupper(): # for uppercase letters, add CAP
            output += CAP
            char = char.lower()
            output += braille[char]

        elif char.isdigit(): # for numbers, add NUM, and loop until the next char is not a digit, then add SPACE
            output += NUM
            output += number[char]
            if (i + 1) == len(input):
                return output
            while (i + 1) < len(input) and input[i+1].isdigit():
                output += number[input[i+1]]
                i += 1
            if i + 1 < len(input) and input[i+1] != ' ':
                output += SPACE

        else: # others (lowercase or symbols) translate directly
            if char not in braille:
                return TypeError('Invalid character')
            output += braille[char]
        i += 1

    return output


def braille_to_alpha(input):
    # take braille input and print out letters
    output = ''
    lst = [input[i:i+6] for i in range(0, len(input), 6)] # split input into 6 character chunks

    i = 0
    while i < len(lst):
        if lst[i] == CAP: # for CAP, add the next char as uppercase
            i += 1 # skip the indicator
            output += alpha[lst[i]].upper()
        elif lst[i] == NUM:
            i += 1 # skip the indicator
            while (lst[i] in braille_number) and (lst[i+1] != SPACE) and ((i+1) < len(lst)): # loop until the next char is not a number
                output += braille_number[lst[i]]
                i += 1
            output += braille_number[lst[i]]
        else:
            output += alpha[lst[i]]
        i += 1

    return output


def main():
    input = ' '.join(sys.argv[1:])
    if is_valid(input):
        # Test script:
        # python3 python/translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
        # python3 python/translator.py .O.OOOO.....OO...............O.OOOO......O.OO.O.
        # python3 python/translator.py .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
        print(braille_to_alpha(input))
    else:
        # Test script:
        # python3 python/translator.py Hello world
        # .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
        # python3 python/translator.py 13TS
        # .O.OOOO.....OO...............O.OOOO......O.OO.O.
        # python3 python/translator.py Abc 123 xYz
        print(alpha_to_braille(input))


if __name__ == "__main__":
    main()