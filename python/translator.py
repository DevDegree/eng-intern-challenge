import sys

ALPHABET_TO_BRAILLE = {
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
SPECIAL_CHARACTERS = {
    'number': '.O.OOO',
    'space' : '......',
    'capital' : '.....O'
}

NUMBERS_TO_BRAILLE = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

BRAILLE_TO_ALPHABET = {v: k for k, v in ALPHABET_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

def english_to_braille(input_string):
    curr_braille = ""
    is_number_mode = False
    for c in input_string:
        if c.isalpha():
            if is_number_mode:
                is_number_mode = False
            if c.isupper():
                curr_braille += SPECIAL_CHARACTERS['capital']
                c = c.lower()
            curr_braille += ALPHABET_TO_BRAILLE[c]
        elif c.isdigit():
            if not is_number_mode:
                curr_braille += SPECIAL_CHARACTERS['number']
                is_number_mode = True
            curr_braille += NUMBERS_TO_BRAILLE[c]
        elif c == ' ':
            curr_braille += SPECIAL_CHARACTERS['space']
            is_number_mode = False
    return curr_braille


def braille_to_english(braille_string):
    i = 0
    length = len(braille_string)
    result = ""
    is_number = False
    while i < length:
        braille_char = braille_string[i:i+6]

        if braille_char == SPECIAL_CHARACTERS['space']:
            result += ' '
            is_number = False
        elif braille_char == SPECIAL_CHARACTERS['capital']:
            i += 6
            braille_char = braille_string[i:i+6]
            result += BRAILLE_TO_ALPHABET.get(braille_char, '?').upper()
        elif braille_char == SPECIAL_CHARACTERS['number']:
            is_number = True
        else:
            if is_number:
                result += BRAILLE_TO_NUMBERS.get(braille_char, '?')
            else:
                result += BRAILLE_TO_ALPHABET.get(braille_char, '?')
        i += 6
    return result
def translate(input_string):

    if all(c in 'O.' for c in input_string): 
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])  
    if all(c in 'O.' for c in input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

