import sys
import re

# Dictionary mapping English characters to their Braille translation
ENGLISH_TO_BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    
    ' ': '......',
    
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Constants for capital follows and number follows
BRAILLE_CAPITAL_FOLLOWS = '.....O'
BRAILLE_NUMBER_FOLLOWS = '.O.OOO'

# Reverse dictionary for English lookup
BRAILLE_TO_ENGLISH_DICT = {v: k for k, v in ENGLISH_TO_BRAILLE_DICT.items()}


def is_braille(input_string: str) -> bool:
    '''
    check if the input string is braille or not
    Args:
    input_string (str): the input string from the terminal
    Returns:
    bool: whether the input_string is braille or not
    '''
    braille_pattern = re.fullmatch(r'[O.]*', input_string)
    return bool(braille_pattern)


def english_to_braille(input_string: str) -> str:
    '''
    translates the english string to braille string
    Args:
    input_string (str): the input string from the terminal
    Returns:
    str: the translated string in braille
    '''
    braille_text = []
    is_number_follows = False

    for char in input_string:
        if re.fullmatch(r'[A-Z]', char):
            braille_text.append(BRAILLE_CAPITAL_FOLLOWS)
            braille_text.append(ENGLISH_TO_BRAILLE_DICT[char.lower()])
        elif re.fullmatch(r'[0-9]', char):
            if not is_number_follows:
                braille_text.append(BRAILLE_NUMBER_FOLLOWS)
                is_number_follows = True
            braille_text.append(ENGLISH_TO_BRAILLE_DICT[char])
        else:
            braille_text.append(ENGLISH_TO_BRAILLE_DICT[char])
            is_number_follows = False
            
    return ''.join(braille_text)

def braille_to_english(input_string: str) -> str:
    '''
    translates the braille text to English
    Args:
    input_string (str): the input string from the terminal
    Returns:
    str: translated string in English
    '''
    english_text = []
    is_number_follows = False
    is_capital_follows = False

    for i in range(0, len(input_string), 6):
        braille_symbol = input_string[i:i+6]
        print(braille_symbol)
        if braille_symbol == BRAILLE_CAPITAL_FOLLOWS:
            is_capital_follows = True
            continue
        
        if braille_symbol == BRAILLE_NUMBER_FOLLOWS:
            is_number_follows = True
            continue

        if braille_symbol == ENGLISH_TO_BRAILLE_DICT[' ']:
            english_text.append(' ')
            is_number_follows = False
            continue
                    
        if braille_symbol in BRAILLE_TO_ENGLISH_DICT:
            english_char = BRAILLE_TO_ENGLISH_DICT[braille_symbol]
            if is_number_follows:
                if re.fullmatch(r'[0-9]', english_char):
                    english_text.append(english_char)
            else:
                '''
                special check to ensure that we are not translating 'a-j' into '1-0' 
                when is_number_follow is false
                ''' 
                if re.fullmatch(r'[0-9]', english_char):
                    english_char = chr(ord('a') + (int(english_char) - 1))
                if is_capital_follows:
                    english_text.append(english_char.upper()) 
                    is_capital_follows = False
                else:
                    english_text.append(english_char)

    return ''.join(english_text)

def main():
    if len(sys.argv) < 2:
        print("Error: No input provided")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()
