import sys

BRAILLE_ENGLISH_MAP = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

ENGLISH_BRAILLE_MAP = {v: k for k, v in BRAILLE_ENGLISH_MAP.items()}

UPPERCASE_INDICATOR = '.....O'
NUMERIC_INDICATOR = '.O.OOO'

DIGIT_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def decode_braille(encoded_text):
    output = []
    index = 0
    capitalize_next = False
    numeric_mode = False
    
    while index < len(encoded_text):
        current_char = encoded_text[index:index+6]
        if current_char == UPPERCASE_INDICATOR:
            capitalize_next = True
        elif current_char == NUMERIC_INDICATOR:
            numeric_mode = True
        else:
            if numeric_mode:
                letter = BRAILLE_ENGLISH_MAP.get(current_char)
                if letter in DIGIT_MAP:
                    output.append(DIGIT_MAP[letter])
                else:
                    numeric_mode = False
                    output.append(letter.upper() if capitalize_next else letter)
            else:
                letter = BRAILLE_ENGLISH_MAP.get(current_char, '')
                output.append(letter.upper() if capitalize_next else letter)
            capitalize_next = False
        index += 6
    return ''.join(output)

def encode_braille(plain_text):
    output = []
    numeric_mode = False
    
    for char in plain_text:
        if char.isdigit():
            if not numeric_mode:
                output.append(NUMERIC_INDICATOR)
                numeric_mode = True
            letter = next(k for k, v in DIGIT_MAP.items() if v == char)
            output.append(ENGLISH_BRAILLE_MAP[letter])
        elif char.isalpha():
            if char.isupper():
                output.append(UPPERCASE_INDICATOR)
            output.append(ENGLISH_BRAILLE_MAP[char.lower()])
            numeric_mode = False
        elif char == ' ':
            output.append(ENGLISH_BRAILLE_MAP[char])
            numeric_mode = False
    
    return ''.join(output)

def convert_text(input_text):
    if set(input_text).issubset('O.'):
        return decode_braille(input_text)
    else:
        return encode_braille(input_text)
    
def run_translator():
    if len(sys.argv) < 2:
        print("To Use write the command in this format: python3 translator.py 'text to translate'")
        return
    input_text = ' '.join(sys.argv[1:])
    print(convert_text(input_text))

if __name__ == '__main__':
    run_translator()