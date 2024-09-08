import sys
from string import ascii_uppercase as uppercase
from string import digits as numbers

# a list tuples, which link English letters/symbols and their corresponding braille sequence
ALPHABET = [
    ('a', 'O.....'),
    ('b', 'O.O...'),
    ('c', 'OO....'),
    ('d', 'OO.O..'),
    ('e', 'O..O..'),
    ('f', 'OOO...'),
    ('g', 'OOOO..'),
    ('h', 'O.OO..'),
    ('i', '.OO...'),
    ('j', '.OOO..'),
    ('k', 'O...O.'),
    ('l', 'O.O.O.'),
    ('m', 'OO..O.'),
    ('n', 'OO.OO.'),
    ('o', 'O..OO.'),
    ('p', 'OOO.O.'),
    ('q', 'OOOOO.'),
    ('r', 'O.OOO.'),
    ('s', '.OO.O.'),
    ('t', '.OOOO.'),
    ('u', 'O...OO'),
    ('v', 'O.O.OO'),
    ('w', '.OOO.O'),
    ('x', 'OO..OO'),
    ('y', 'OO.OOO'),
    ('z', 'O..OOO'),
    ('^', '.....O'), # capital follows
    ('*', '.O...O'), # decimal follows
    ('#', '.O.OOO'), # number follows 
    ('O', '..OO.O'), 
    (',', '..O...'),
    ('?', '..O.OO'),
    ('!', '..OOO.'),
    (':', '..OO..'),
    (';', '..O.O.'),
    ('-', '....OO'),
    ('/', '.O..O.'),
    ('<', '.OO..O'),
    ('>', 'O..OO.'),
    ('(', 'O.O..O'),
    (')', '.O.OO.'),
    (' ', '......'),
    ('1', 'O.....'),
    ('2', 'O.O...'),
    ('3', 'OO....'),
    ('4', 'OO.O..'),
    ('5', 'O..O..'),
    ('6', 'OOO...'),
    ('7', 'OOOO..'),
    ('8', 'O.OO..'),
    ('9', '.OO...'),
    ('0', '.OOO..')
]

# a dictionary of letters that correspond to each number, if following a braille NUMBER FOLLOWS character
NUMBERS = {
    'a':'1',
    'b':'2',
    'c':'3',
    'd':'4',
    'e':'5',
    'f':'6',
    'g':'7',
    'h':'8',
    'i':'9',
    'j':'0'
}

# gets the corresponding 6-character braille sequence from ALPHABET given an English character
def get_braille(char):
    for letter in ALPHABET:
        if char == letter[0]:
            return letter[1]
    return 'OOOOOO'

# gets the corresponding English character from ALPHABET given a 6-character braille sequence
def get_english(char):
    for letter in ALPHABET:
        if char == letter[1]:
            return letter[0]
    return ' '

# the program assumes the string it is given is braille
IS_BRAILLE = True

# main script
# runs in O(n) time where n is the length of the arguement

# gets the argument, stores it as string
source_string = sys.argv[1]
for i in range(2, len(sys.argv)):
    source_string = source_string + ' ' + sys.argv[i]

# determines if this string is braille
for char in source_string: # a non-braille character appeared, so the string given is English, not braille
    if (not (char == 'O' or char == '.')):
        IS_BRAILLE = False

# translates the source string
translated_string = ""
if IS_BRAILLE:
    i = 0 # counter variable (i-th character)
    # iterate over the source string, 6 characters at a time
    while i < len(source_string):
        char = get_english(source_string[i:i+6])
        
        # if the i-th character is an uppercase letter
        if char == '^':
            i+=6
            translated_string = translated_string + (get_english(source_string[i:i+6])).upper()

        # if the i-th character is a number
        elif char == '#':
            while (i + 6 < len(source_string)):
                i+=6
                if (source_string[i:i+6] == '......'):
                    translated_string = translated_string + ' '
                translated_string = translated_string + NUMBERS[get_english(source_string[i:i+6])]
        
        # if the i-th character does not need any type of FOLLOWS symbol
        else:
            translated_string = translated_string + char
        i+=6 # increment counter

else:
    i = 0 # counter variable
    # iterate over the source string, 1 character at a time
    while i < len(source_string):
        char = source_string[i]

        # if the i-th character is an uppercase letter
        if char in uppercase:
            translated_string = translated_string + get_braille('^')
            translated_string = translated_string + get_braille(source_string[i].lower())

        # if the i-th character is a number
        elif char in numbers:
            translated_string = translated_string + get_braille('#')
            while (i < len(source_string)):
                translated_string = translated_string + get_braille(source_string[i])
                if (source_string[i] == ' '):
                    break
                i+=1

        # if the i-th character does not need any type of FOLLOWS symbol
        else:
            translated_string = translated_string + get_braille(char)
        i+=1 # increment counter
        
# print out translated string
print(translated_string)