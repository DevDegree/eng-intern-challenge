import sys

# Braille encoding
BRAILLE_ENCODING = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..', 
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

BRAILLE_TO_ENGLISH_LETTERS = {
    'O.....': 'a',  'O.O...': 'b',  'OO....': 'c',  'OO.O..': 'd',  'O..O..': 'e',  'OOO...': 'f',  'OOOO..': 'g',  'O.OO..': 'h', 
    '.OO...': 'i',  '.OOO..': 'j',  'O...O.': 'k',  'O.O.O.': 'l',  'OO..O.': 'm',  'OO.OO.': 'n',  'O..OO.': 'o',  'OOO.O.': 'p', 
    'OOOOO.': 'q',  'O.OOO.': 'r',  '.OO.O.': 's',  '.OOOO.': 't',  'O...OO': 'u',  'O.O.OO': 'v',  '.OOO.O': 'w',  'OO..OO': 'x', 
    'OO.OOO': 'y',  'O..OOO': 'z',  
    '......': ' ',  '.....O': 'capital',  '.O.OOO': 'number'
}
BRAILLE_TO_ENGLISH_NUMBERS = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6','OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def english_to_braille(english_string):
    result = []
    number_mode = False

    for char in english_string:
        if char.isdigit():
            if not number_mode:
                result.append(BRAILLE_ENCODING['number'])
                number_mode = True
            result.append(BRAILLE_ENCODING[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(BRAILLE_ENCODING['capital'])
            result.append(BRAILLE_ENCODING[char.lower()])
        elif char == ' ':
            result.append(BRAILLE_ENCODING[' '])
            number_mode = False

    return ''.join(result)

def braille_to_english(braille_string):
    result = []
    number_mode = False
    i = 0

    while i < len(braille_string):
        braille_char = braille_string[i:i+6]
        if braille_char == BRAILLE_ENCODING['capital']:
            i += 6
            braille_char = braille_string[i:i+6]
            result.append(BRAILLE_TO_ENGLISH_LETTERS[braille_char].upper())
        elif braille_char == BRAILLE_ENCODING['number']:
            number_mode = True
        elif braille_char == BRAILLE_ENCODING[' ']:
            result.append(' ')
            number_mode = False  # Turn off number mode when a space is encountered
        else:
            if number_mode:
                num = BRAILLE_TO_ENGLISH_NUMBERS[braille_char]
                result.append(num)
            else:
                letter = BRAILLE_TO_ENGLISH_LETTERS[braille_char]
                result.append(letter)
                number_mode = False  # Only turn off number_mode when processing a non-number

        i += 6

    return ''.join(result)

if __name__ == '__main__':
    input_string = " ".join(sys.argv[1:])
    
    # Check if input is Braille (contains only 'O' and '.')
    if all(c in 'O.' for c in input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))