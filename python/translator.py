import sys

BRAILLE_LETTER_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.O',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

BRAILLE_NUMBER_DICT = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.O....'
}

# Indicators
CAPITAL_INDICATOR = '.....O'
NUMBER_INDICATOR = '.O.OOO'
DECIMAL_INDICATOR = '.O...O'
SPACE_INDICATOR = '......'

# Reverse Braille dictionaries for translation from Braille to English
REVERSE_BRAILLE_LETTER_DICT = {v: k for k, v in BRAILLE_LETTER_DICT.items()}
REVERSE_BRAILLE_NUMBER_DICT = {v: k for k, v in BRAILLE_NUMBER_DICT.items()}

def translate_to_braille(text):
    braille = []
    is_number = False

    for char in text:
        if(char == ' '):
            braille.append(BRAILLE_LETTER_DICT[' '])
            is_number = False
            continue
        if char.isdigit(): 
            if not is_number:
                braille.append(NUMBER_INDICATOR)
                is_number = True
            braille.append(BRAILLE_NUMBER_DICT[char])
        else:
            is_number = False
            if char.lower() in BRAILLE_LETTER_DICT:
                if char.isupper():
                    braille.append(CAPITAL_INDICATOR)
                braille.append(BRAILLE_LETTER_DICT[char.lower()])
            else:
                braille.append(BRAILLE_LETTER_DICT[' '])  # Handle spaces
    return ''.join(braille)

def translate_to_english(braille):
    english = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    is_capital = False
    is_number = False
    
    for braille_char in braille_chars:
        if braille_char == SPACE_INDICATOR:
            english.append(' ')
            is_capital = False
            is_number = False
            continue
        if braille_char == CAPITAL_INDICATOR:
            is_capital = True
            continue
        if braille_char == NUMBER_INDICATOR:
            is_number = True
            continue
        if is_number:
            if braille_char in REVERSE_BRAILLE_NUMBER_DICT:
                english.append(REVERSE_BRAILLE_NUMBER_DICT[braille_char])
            else:
                english.append('?')  # Handle unrecognized Braille sequences
            
        elif braille_char in REVERSE_BRAILLE_LETTER_DICT:
            if is_capital:
                english.append(REVERSE_BRAILLE_LETTER_DICT[braille_char].upper())
                is_capital = False
            else:
                english.append(REVERSE_BRAILLE_LETTER_DICT[braille_char])
        else:
            english.append('?')  # Handle unrecognized Braille sequences
    
    return ''.join(english)

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = ' '.join(sys.argv[1:])
    
    if all(c in 'O.' for c in input_string):
        output = translate_to_english(input_string)
    else:
        output = translate_to_braille(input_string)

    print(output)

if __name__ == "__main__":
    main()
