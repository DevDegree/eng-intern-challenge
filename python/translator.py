# Braille to English dictionary
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}

# English to Braille dictionary
english_to_braille = {
    v: k for k, v in braille_to_english.items()
}

numbers_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_to_numbers = {
    v: k for k, v in numbers_to_braille.items()
}

def translate_to_braille(english_input):
    #probably have to add a bool for number follows
    number_mode = False
    res = ''
    for char in english_input:
        if char.isdigit() and not number_mode:
            res += '.O.OOO' + numbers_to_braille[char]
            number_mode = True
        elif char.isdigit() and number_mode:
            res += numbers_to_braille[char]
        elif char in english_to_braille:
            res += english_to_braille[char]
        elif char.isupper():
            res += '.....O' + english_to_braille[char.lower()]
        elif char == ' ':
            res += '......' 
            number_mode = False
    return res

def translate_to_english(braille_input):
    res = ''
    i = 0
    number_mode = False
    capital_mode = False

    while i < len(braille_input):
        braille_char = braille_input[i:i+6]
        if braille_char == '.....O':
            capital_mode = True
        elif braille_char == '.O.OOO':
            number_mode = True
        elif braille_char == '......':
            res += ' '
            number_mode = False
        elif number_mode:
            res += braille_to_numbers[braille_char]
        elif capital_mode:
            res += braille_to_english[braille_char].upper()
            capital_mode = False
        else:
            res += braille_to_english[braille_char]
        
        i += 6
    
    return res

#main
import sys
import re

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    seperator = ' '
    input_text = seperator.join(sys.argv[1:]) #extract input text
    braille_mode = bool(re.fullmatch(r'[O.]+', input_text)) #check if input is braille

    if braille_mode:
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))