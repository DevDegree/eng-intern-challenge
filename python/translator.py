import sys

#english to braille map
english_to_braille = {
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

    'capital': '.....O',
    'decimal': '.0...0',
    'number': '.O.OOO',

    ' ': '......',
    ',': '..O...',
    ';': '..O.O.',
    ':': '..OO..',
    '.': '..00.0',
    '!': '..OO.O',
    '(': '0.0..0',
    ')': '.0.00.',
    '?': '..0.00',
    '-': '....O0',
    '/': '.0..0.',
    '<': '.00..0',
    '>': '0..00.',
}

#numbers to letters map
NUMBERS_TO_LETTERS = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j',
}

#mapping braille patterns to english letters
braille_to_english_map = {braille: letter for letter, braille in english_to_braille.items()}

#reverse mapping for braille digits to numeric characters
braille_to_number_map = {braille_letter: digit for digit, braille_letter in NUMBERS_TO_LETTERS.items()}

def isBraille(inputString):

    if len(inputString) % 6 != 0:
        return False
 

    #split input into substring of length 6
    braille_chars = [inputString[i:i+6] for i in range(0, len(inputString), 6)]
        
    #check if each substring only consists of braille characters
    return all(char in valid_braille_patterns for char in braille_chars)


def braille_to_english(inputString):
    translated_text = ''

    braille_chars = [inputString[i:i+6] for i in range(0, len(inputString), 6)]
   
    
    for braille_char in braille_chars:
            translated_text += braille_to_english_map[braille_char]
    
    return translated_text

def english_to_braille(inputString):
    translated_text = ''
    
    for char in inputString:
        translated_text += english_to_braille[char] + ' '
    
    return translated_text.strip()


def main():

    inputString = ' '.join(sys.argv[1:])

    if isBraille(inputString):
        result = braille_to_english(inputString)
    else:
        result = english_to_braille(inputString)

    print(result)