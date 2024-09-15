
# . -> dot, O -> raised dot

import sys

# braille -> letters (with space)
letter_braille_map = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',
    ' ' : '......' 
}

# can be done with list comprehension, but kept for clarity
# number -> braille
number_braille_map = {
    '1' : letter_braille_map['a'],
    '2' : letter_braille_map['b'],
    '3' : letter_braille_map['c'],
    '4' : letter_braille_map['d'],
    '5' : letter_braille_map['e'],
    '6' : letter_braille_map['f'],
    '7' : letter_braille_map['g'],
    '8' : letter_braille_map['h'],
    '9' : letter_braille_map['i'],
    '0' : letter_braille_map['j']
}

# 0 -> capital follows, 1 -> number input until space
modifier_map = {
    '.....O' : 0,
    '.O.OOO' : 1 
}

rev_modifier_map = { m : b for b, m in modifier_map.items()}

# braille -> letter
braille_letter_map = { b : l for l, b in letter_braille_map.items()}

# braille -> number
braille_number_map = { b : n for n, b in number_braille_map.items()}

'''
chunks a string into sections of 6 (with remainder)

returns a list
'''
def chunk_string(string):
    return list(string[0+i : 6 + i] for i in range(0, len(string), 6))

'''
Checks if a given input string is in braille or not.

If the input includes '.', it is braille. "English" specification does not include '.' so can safely
assume all input containing '.' is valid braille input
'''
def is_braille(string):
    return '.' in string

input_str = ' '.join(sys.argv[1:])

output_str = ''

# if input includes a period
if is_braille(input_str):
    chunked_input = chunk_string(input_str) # divide into sections of 6
    modifier = -1 # -1 -> normal, 0 -> next is uppercase, 1 number input until string
    for chunk in chunked_input:
        if chunk in modifier_map:
            modifier = modifier_map[chunk] # should set the modifier if it is one
        else:
            if modifier == 0:
                output_str += braille_letter_map[chunk].upper()
                modifier = -1 # remove the modifier
            elif modifier == 1:
                if chunk == '......':
                    modifier = -1
                    output_str += ' '
                output_str += braille_number_map[chunk]
            else:
                output_str += braille_letter_map[chunk]
else:
    # does 1234abcd include a space between the 1234 and abcde in braille?
    # maybe it's impossible input since we're translating to "English"?
    is_nums = False
    for char in input_str:
        if is_nums:
            if char in number_braille_map:
                output_str += number_braille_map[char]
            else:
                # no longer printing numbers
                is_nums = False
                output_str += letter_braille_map[' '] # append space? See explanation above
        else:
            if char.isupper():
                output_str += rev_modifier_map[0] # capital follows modifier
                output_str += letter_braille_map[char.lower()]
            # https://datagy.io/python-isdigit/ isdecimal seems like the "most" correct to use here
            elif char.isdecimal():
                is_nums = True
                output_str += rev_modifier_map[1] # numbers follow
            else:
                output_str += letter_braille_map[char] # everything other case should be fine here

print(output_str)