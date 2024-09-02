import sys

# **ASSUMPTION**
# 'Right' inputs are guaranteed
# given more time, error handling can be added

# map the brail encodings

# commands:
m_commands = {
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
}

m_commands_r = {
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number'
}

m_alpha = {
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
}

m_alpha_r = {
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

m_nums = {
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

m_nums_r = {
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

m_other = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}

m_other_r = {
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}


# method for converting BRAIL to English
# expects: input brail string
# outputs: decoded string
def brail_to_english(string):
    res = ''
    
    i = 0
    num_follows = False
    cap_follows = False
    while i < len(string):
        symbol = string[i:i+6]
        # print(symbol)
        # print(cap_follows)
        # print(num_follows)

        # print(m_commands_r['.....O'])
        # first check if the symbol is a command
        if symbol in m_commands_r:
            if m_commands_r[symbol] == 'capital':
                cap_follows = True
            elif m_commands_r[symbol] == 'number':
                num_follows = True
        else:
            if symbol in m_other_r and m_other_r[symbol] == ' ':
                num_follows = False

            if num_follows:
                res += m_nums_r[symbol]
            elif symbol in m_alpha_r:
                if cap_follows:  
                    res += m_alpha_r[symbol].upper()
                    cap_follows = False
                else:
                    res += m_alpha_r[symbol]
            elif symbol in m_other_r:
                res += m_other_r[symbol]

        i += 6

    return res


# method for converting English to Brail
# expects: input english string
# outputs: encoded string
def english_to_brail(string):
    res = ''

    # var for numbers
    prev_num = False

    for char in string:
        # check if character is an alphabet
        if char.isalpha():
            # check if character is uppercase
            if char.isupper():
                res += m_commands['capital']
            res += m_alpha[char.lower()]

        # check if character is a number
        elif char.isdigit():
            if not prev_num:
                res += m_commands['number']
                prev_num = True
            res += m_nums[char]
        
        # if character is not an alphabet or a number
        else:
            if char == ' ':
                prev_num = False
            res += m_other[char]
        
    return res

# Read input from command line arguments
# str_input = input()
str_input = " ".join(sys.argv[1:])

# Check if input is BRAIL or English
# if there is not 'O' or '.' in the input, then it cannot be brail
if 'O' not in str_input and '.' not in str_input:
    print(english_to_brail(str_input))
else:
    print(brail_to_english(str_input))