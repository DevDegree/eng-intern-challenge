import os
from os import sys

''' 
As this is a smaller application used in the command line, we will hardcode
the dictionary for faster performance. If the application needed to be 
'''
#Hardcoded dictionary values
string_to_braille_dict = {
'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
#'.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':' : '..OO..', ';': '..O.O.', 
#'-': '....OO', '/' : '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(' : 'O.O..O', ')': '.O.OO.', 
}

number_to_braille_dict = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
'7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

operation_to_braille_dict = {
    'CF': '.....O', 
    #'DF': '.O...O', 
    'NF': '.O.OOO', 
}

braille_to_string_dict = dict()
for key, value in string_to_braille_dict.items():
    braille_to_string_dict[value] = key

braille_to_number_dict = dict()
for key,value in number_to_braille_dict.items():
    braille_to_number_dict[value] = key

braille_to_operation_dict = dict()
for key, value in operation_to_braille_dict.items():
    braille_to_operation_dict[value] = key

def convert_braille_to_string(arguments):
    number_follows_bool = False
    capital_follows_bool = False
    input_string = arguments[0]    
    x = 0
    output = ""

    while x < len(input_string):
        token = input_string[x:x + 6]

        if token in braille_to_operation_dict:
            if braille_to_operation_dict[token] == 'CF':
                capital_follows_bool = True
            elif braille_to_operation_dict[token] == 'NF':
                number_follows_bool = True
            else:
                output += braille_to_string_dict['.']
        elif token in braille_to_number_dict and number_follows_bool:
            output += braille_to_number_dict[token]

        elif token in braille_to_string_dict and capital_follows_bool:
            output += braille_to_string_dict[token].upper()
            capital_follows_bool = False

        elif token in braille_to_string_dict:
            output += braille_to_string_dict[token]
            if braille_to_string_dict[token] == ' ':
                number_follows_bool = False
        x += 6


    return output
    


def convert_string_to_braille(arguments):
    number_follows_bool = False
    input_string = " ".join(arguments)
    output = ""
    for token in input_string:
        for char in token:
            if char.isupper():
                output += operation_to_braille_dict['CF'] + string_to_braille_dict[char.lower()]
            elif char.isdigit() and not number_follows_bool:
                number_follows_bool = True
                output += operation_to_braille_dict['NF'] + number_to_braille_dict[char]
            elif char.isdigit():
                output += number_to_braille_dict[char]
            elif char == ' ':
                output += string_to_braille_dict[char]
                number_follows_bool = False
            else:
                output += string_to_braille_dict[char]

    return output


def isBraille(s):
    return s in braille_to_string_dict or s in braille_to_operation_dict
'''
'''
arguments = sys.argv[1:]
if len(arguments) == 0:
    exit()
#string to braille if len arguments > 1 (since braille is an uninterrupted stream of 'O' and '.'
#string to braille if arguments[0] % 6 != 0, (since braille is always composed of 6 characters)

argument = "".join(arguments)
is_braille = all(isBraille(arg) for arg in arguments)
    

if is_braille:
    output_string = convert_braille_to_string(arguments)
else:
    output_string = convert_string_to_braille(arguments)

print(output_string)
