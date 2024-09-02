import sys

# use a dictionary to map braille to non-braille
# assumptions: 
# the before decimal braille code comes before a period that is used to represent a decimal
# but does not appear when it is a period at the end of a sentence

letters_to_braille = {'a': 'O.....',
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
 'r': "O.OOO.",
 's': '.OO.O.',
 't': '.OOOO.',
 'u': 'O...OO',
 'v': 'O.O.OO',
 'w': '.OOO.O',
 'x': 'OO..OO',
 'y': 'OO.OOO',
 'z': 'O..OOO',
}

num_to_braille = {
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

symbols_to_braille = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    ">": 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}


# return True if text is in braille
def in_braille(input):
    braille_characters = set('O' + ".")
    input_characters = set(input)
    return braille_characters == input_characters

def translate_to_braille(input):
    letters_to_braille = {'a': 'O.....',
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
    'r': "O.OOO.",
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    }

    
    num_to_braille = {
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

    symbols_to_braille = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    ">": 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
    }

    capital_prefix = '.....O'  # prefix for capital letters
    number_prefix = '.O.OOO'   # prefix indicating numbers
    decimal_prefix = '.O...O'  # prefix for start of a decimal number 
    output = ""
    is_number = False

    for char in input:
        if char.isdigit():  # if character is a digit
            if not is_number:  # if it's the start of a number
                output += number_prefix  # add the number prefix
                is_number = True  # set flag to indicate number processing
            output += num_to_braille[char]  # add Braille translation for the digit
        elif char.isalpha():  # if character is a letter
            if char.isupper():  # letter is uppercase, add capital prefix
                output += capital_prefix 
                char = char.lower()  # convert to lowercase for Braille translation
            output += letters_to_braille[char]  # add Braille translation for the letter
            is_number = False  # reset to false, back to letters
        else:  # character is a symbol or space
            if char == '.':
                if is_number:  # if it's a "." used to represent a decimal not the end of a sentence
                    output += decimal_prefix  # add decimal prefix first
                output += symbols_to_braille.get(char, '')  # add the decimal Braille code
            else:
                output += symbols_to_braille.get(char, '')  # add Braille code for the symbol or space
                is_number = False  # reset is_number, not a number
    
    return output

def translate_from_braille(input):
    braille_to_letters = {
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
        'O..OOO': 'z'
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
        '.OOO..': '0'
    }


    braille_to_symbols = {
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
        '......': ' '
    }

    capital_prefix = '.....O'  # prefix for capital letters
    number_prefix = '.O.OOO'   # prefix indicating numbers
    decimal_prefix = '.O...O'  # prefix for start of a decimal number 

    is_number = False
    output = ""
    i = 0 # track current index in the braille text
    # each six characters is only one character

    while i < len(input):
        char = input[i:i+6]  # read next 6-dot braille character

        if char == capital_prefix:  # handle capital letter prefix
            i += 6  # skip 
            char = input[i:i+6]  # read letter
            output += braille_to_letters.get(char, '').upper()  # add it in capital
        elif char == number_prefix:  # handle number prefix
            is_number = True  # switch to number mode
        elif char == decimal_prefix:  # handle decimal point in numbers
            output += '.'  # add decimal point
        elif is_number and char in braille_to_num:  # translate numbers
            output += braille_to_num[char]
        elif char in braille_to_letters:  # translate letters
            output += braille_to_letters[char]
            is_number = False  # reset to letter mode
        elif char in braille_to_symbols:  # translate symbols
            output += braille_to_symbols[char]
            is_number = False  # reset to letter mode

        i += 6  # move to the next braille character

    return output

def concatenate_args(args):
    return ' '.join(args)

if __name__ == "__main__":
    
    input = concatenate_args(sys.argv[1:])  # Combine all arguments into a single string

    if in_braille(input):
        output = translate_from_braille(input)
    else: 
        output = translate_to_braille(input)
    print(output, end="")


