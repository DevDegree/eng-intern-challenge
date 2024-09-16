import sys

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.O....': 'i', '.OO...': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital', '.O.OOO': 'number', '.O...O': 'decimal'
}

BRAILLE_TO_NUMS = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.O....': '9', '.OO...': '0'
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
NUMS_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMS.items()}

def braille_to_english(braille_string):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille_string):
        char = braille_string[i:i+6]
        if char == ENGLISH_TO_BRAILLE['capital']:
            capitalize_next = True
            i += 6
        elif char == ENGLISH_TO_BRAILLE['number']:
            number_mode = True
            i += 6
        else:
            if number_mode:
                if BRAILLE_TO_ENGLISH[char] == ' ':
                    number_mode = False
                    result.append(' ')
                else:
                    result.append(BRAILLE_TO_NUMS[char])
            else:
                letter = BRAILLE_TO_ENGLISH[char]
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
            i += 6
    
    return ''.join(result)

def english_to_braille(english_string):
    result = []
    number_mode = False
    
    for char in english_string:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            result.append(NUMS_TO_BRAILLE[char])
        elif char.isalpha() or char.isspace():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital'])
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char])
        else:
            raise ValueError("Invalid character in input string")
    
    return ''.join(result)


input_string = ' '.join(sys.argv[1:])
if all(char in '.O' for char in input_string):
    print(braille_to_english(input_string))
else:
    print(english_to_braille(input_string))
