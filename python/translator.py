import sys
import re

# Braille to English Translation Dictionary
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b',
    'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n',
    'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v',
    '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ',
}

BRAILLE_TO_NUMBERS = {
    'O.....': '1', 'O.O...': '2',
    'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0',
}


ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
NUMBERS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMBERS.items()}

def check_input_type(query):
    braille_pattern = re.compile(r'^[O.]+$')
    english_pattern = re.compile(r'^[A-Za-z0-9\s]+$')

    if braille_pattern.match(query):
        return convert_braille_to_english(query)
    elif english_pattern.match(query):
        return convert_english_to_braille(query)

def convert_braille_to_english(query):
    result = ''
    capitalize_next = False
    number_follows = False
    
    for i in range(0, len(query), 6):
        braille_char = query[i:i+6]
        
        if braille_char == '.....O':
            capitalize_next = True
            continue
        elif braille_char == '.O.OOO':
            number_follows = True
            continue
        
        if number_follows:
            if braille_char == '......':
                number_follows = False
                result += ' '
            else:
                result += BRAILLE_TO_NUMBERS.get(braille_char, "?")
        else:
            char = BRAILLE_TO_ENGLISH.get(braille_char,"?")
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char
    
    return result

def convert_english_to_braille(query):
    result = ''
    number_follows = False
    
    for char in query:
        if char.isdigit():
            if not number_follows: 
                result += '.O.OOO'
                number_follows = True
            result += NUMBERS_TO_BRAILLE.get(char, '')
        elif char.isalpha():
            if number_follows:  
                number_follows = False
            if char.isupper():
                result += '.....O' 
            result += ENGLISH_TO_BRAILLE.get(char.lower(), '')
        else:
            if number_follows: 
                number_follows = False
            result += ENGLISH_TO_BRAILLE.get(char, '')
    
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        print(check_input_type(query))
