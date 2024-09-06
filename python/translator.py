# Mappings between Braille and English characters
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'capital',  
    '.O.OOO': 'number',    
    '......': ' ',       
}

# Reverse mapping: English to Braille
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# Additional mappings for numbers 0-9
NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

def detect_input_type(input_str):
    """
    Detects if the input is in Braille or English.
    """
    if set(input_str) <= {'O', '.'}:
        return 'braille'
    return 'english'

def translate_to_braille(english_text):
    """
    Translates English text to Braille.
    """
    print(english_text)
    isNumber = False
    braille_output = []
    for char in english_text:
        if char.isdigit():
            if not isNumber:
                braille_output.append(ENGLISH_TO_BRAILLE['number'])
            braille_output.append(NUMBER_TO_BRAILLE[char])
            isNumber = True
        elif char.isupper():
            braille_output.append(ENGLISH_TO_BRAILLE['capital'])
            braille_output.append(ENGLISH_TO_BRAILLE[char.lower()])
            isNumber = False
        elif char == ' ':
            braille_output.append(ENGLISH_TO_BRAILLE[' '])
            isNumber = False
        else:
            braille_output.append(ENGLISH_TO_BRAILLE[char])
            isNumber = False
    return ''.join(braille_output)

def translate_to_english(braille_text):
    """
    Translates Braille text to English.
    """
    english_output = []
    is_capital = False
    is_number = False
    
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        
        if braille_char == ENGLISH_TO_BRAILLE['capital']:
            is_capital = True
            is_number = False
        elif braille_char == ENGLISH_TO_BRAILLE['number']:
            is_number = True
            is_capital = False
        elif braille_char == ENGLISH_TO_BRAILLE[' ']:
            english_output.append(' ')
            is_capital, is_number = False, False
        else:
            if is_number:
                english_output.append(BRAILLE_TO_NUMBER.get(braille_char, ''))
            else:
                char = BRAILLE_TO_ENGLISH.get(braille_char, '')
                if is_capital:
                    char = char.upper()
                english_output.append(char)
            is_capital = False
    
    return ''.join(english_output)

if __name__ == "__main__":
    import sys
    input_text = ' '.join(sys.argv[1:])
    
    if detect_input_type(input_text) == 'braille':
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))


