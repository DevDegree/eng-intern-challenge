import sys

# Create all the key-value pairs
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' '
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

BRAILLE_TO_NUMBERS = {
    '.OOO..': '1', 'O.OO..': '2', 'OOO...': '3', 'OOO.O.': '4', 'O..OO.': '5',
    'OOOO..': '6', 'OOOOO.': '7', 'O.OOO.': '8', '.OOOO.': '9', '.OO.O.': '0'
}

NUMBERS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMBERS.items()}

CAPITALIZE = '.....O'

NUMBER_FOLLOWS = '.O.OOO'

def is_braile(text):
    pass

def translate_to_english(text):
    pass

def translate_to_braille(text):
    pass



def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:]) 

    if is_braille(input_string):
        translate_to_english(input_string)
    else:
        translate_to_braille(input_string)

if __name__ == '__main__':
    main()
