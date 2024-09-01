import sys
# import re
import argparse

english_to_braille = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",

    # idk if its okay to store here
    ' ': "......",
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
}

# maybe it would be better to use a tree
braille_to_english_alpha = {
    "O.....": 'a',
    "O.O...": 'b',
    "OO....": 'c',
    "OO.O..": 'd',
    "O..O..": 'e',
    "OOO...": 'f',
    "OOOO..": 'g',
    "O.OO..": 'h',
    ".OO...": 'i',
    ".OOO..": 'j',
    "O...O.": 'k',
    "O.O.O.": 'l',
    "OO..O.": 'm',
    "OO.OO.": 'n',
    "O..OO.": 'o',
    "OOO.O.": 'p',
    "OOOOO.": 'q',
    "O.OOO.": 'r',
    ".OO.O.": 's',
    ".OOOO.": 't',
    "O...OO": 'u',
    "O.O.OO": 'v',
    ".OOO.O": 'w',
    "OO..OO": 'x',
    "OO.OOO": 'y',
    "O..OOO": 'z',
}
braille_to_english_digit = {
    "O.....": '1',
    "O.O...": '2',
    "OO....": '3',
    "OO.O..": '4',
    "O..O..": '5',
    "OOO...": '6',
    "OOOO..": '7',
    "O.OO..": '8',
    ".OO...": '9',
    ".OOO..": '0',
}

capital_follows = ".....O"
# decimal_follows = ".O...O" not needed i think
number_follows = ".O.OOO"
space_braille = "......"

def convert_english_to_braille(input_string):
    output = []
    is_digit_start = True
    for c in input_string:
        # if the character is a digit, appends the number follows braille symbol
        if c.isdigit() and is_digit_start:
            is_digit_start = False
            output.append(number_follows)
        # if the character is capital, appends the capital follows braille symbol
        elif c.isupper():
            output.append(capital_follows)
            c = c.lower()
        # if the character is whitespace, the characters following are no longer numbers
        elif c == ' ':
            is_digit_start = True

        output.append(english_to_braille[c])
    return ''.join(output)

# Assumes all inputs are valid
def convert_braille_to_english(input_string):
    index = 0
    output = []
    while index < len(input_string):
        sub_braille = input_string[index:index+6]

        if sub_braille == number_follows:
            # a digit sequence
            index += 6
            while index < len(input_string):
                sub_braille = input_string[index:index+6]
                if sub_braille == space_braille:
                    output.append(' ')
                    break
                else:
                    output.append(braille_to_english_digit[sub_braille])
                index += 6

        elif sub_braille == capital_follows:
            index += 6
            if index >= len(input_string): continue
            sub_braille = input_string[index:index+6]
            output.append(braille_to_english_alpha[sub_braille].upper())

        elif sub_braille == space_braille:
            output.append(' ')

        else:
            output.append(braille_to_english_alpha[sub_braille])

        index += 6
    return ''.join(output)

# set seems to be the fastest with all being second and regular expression being last
def is_braille(input_string):
    # return all(c in 'O.' for c in k)
    # return re.search('[^\.O]+', s)
    # return set(input_string) <= set('.O')

    # if it is divisible by 6 and only contains . or O
    return (len(input_string) % 6 == 0 and set(input_string) <= set('.O'))

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input_string> <input-string> ...")
        sys.exit(1)

    # concatenate all input into a single string separated by whitespace 
    args = []
    for i in range(1, len(sys.argv)):
        args.append(sys.argv[i])
    input_string = ' '.join(args)

    output_string = ''
    if (is_braille(input_string)):
        output_string = convert_braille_to_english(input_string)
    else:
        output_string = convert_english_to_braille(input_string)

    print(output_string)


if __name__ == "__main__":
    main()