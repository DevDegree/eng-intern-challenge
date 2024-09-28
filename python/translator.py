import sys

#_____________________________________________________________________________ GLOBAL CONSTANTS _____________________________________________________________________________#

ENGLISH_TO_BRAILLE = {
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
    ' ': '......',
    'NUM': '.O.OOO',
    'CAPITAL': '.....O'
}

NUM_TO_BRAILLE = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...'
}

BRAILLE_TO_ENGLISH = {val: key for key, val in ENGLISH_TO_BRAILLE.items()}

BRAILLE_TO_NUM = {val: key for key, val in NUM_TO_BRAILLE.items()}

BRAILLE_TERM_SIZE = 6

#_____________________________________________________________________________ GLOBAL FUNCTIONS _____________________________________________________________________________#

def is_braille(word : str) -> bool:
    """
    Checks if a word is braille.

    Parameters:
        - word (str)
            - the input word
    
    Returns:
        - valid_len checks if the word's length is a multiple of 6 (each braille character consists of 6 units)
        - valid_chars checks if the word only consists of "O" and "."
    """
    valid_len = len(word) % BRAILLE_TERM_SIZE == 0
    valid_chars = all(c in 'O.' for c in word)
    return valid_len and valid_chars
#_____________________________________________________________________________ MAIN PROGRAM _____________________________________________________________________________#

if __name__ == '__main__':
     # Concatenating all command line arguments into a single string - only relevant for english to braille, since braille is always just one string
    input_str = ' '.join(sys.argv[1:])

    # Setting a variable for the translated output
    translation = ''

    if is_braille(input_str):
        is_capital = False
        is_num = False

        for i in range(0, len(input_str), BRAILLE_TERM_SIZE):
            curr_braille = input_str[i:i+BRAILLE_TERM_SIZE]
            curr_english = BRAILLE_TO_ENGLISH[curr_braille]

            if curr_english == 'NUM':
                is_num = True
                continue
            elif curr_english == 'CAPITAL':
                is_capital = True
                continue
            elif curr_english == ' ':
                is_num = False
                translation += ' '
                continue

            if is_num:
                translation += BRAILLE_TO_NUM[curr_braille]
            elif is_capital:
                translation += curr_english.upper()
                is_capital = False
            else:
                translation += curr_english

        print(translation)

    else:
        is_num = False

        for char in input_str:
            if char.isdigit():
                if not is_num:
                    is_num = True
                    translation += ENGLISH_TO_BRAILLE['NUM']
                translation += NUM_TO_BRAILLE[char]
            elif char.isupper():
                char = char.lower()
                translation += ENGLISH_TO_BRAILLE['CAPITAL'] + ENGLISH_TO_BRAILLE[char]
            else:
                translation += ENGLISH_TO_BRAILLE[char]

        print(translation)
