import re
import sys

braille_dict = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.O....',
    'J': '.OO...',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.O.O..',
    'T': '.OO...',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.O..OO',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    ' ': '......',
    '.': '..OO.O',
    ',': '..O...',
    ';': '..OO..',
    ':': '..O.O.',
    '!': '..OOO.',
    '?': '..OO..',
    "'": '...O..',
    '-': '....OO',
    '(': 'O.O..O',
    ')': '.O.OO.',
    '>': 'O..OO.',
    '<': '.OO..O',
}

braille_number_dict = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.O....',
    '0': '.OO...',
}

english_dict = {v: k for k, v in braille_dict.items()}

english_number_dict = {v: k for k, v in braille_number_dict.items()} 

BRAILLE_UPPER = '.....O'
BRAILLE_NUMBER = '.O.OOO'
BRAILLE_DECIMAL = '.0...0'

def main(text: str) -> str:
    '''
    Main function to translate the input text to Braille or English
    '''
    return translate_to_braille(text) if check_string(text) else translate_to_text(text)
    
def check_string(text: str) -> bool:
    '''
    Return True if text is in English, False if text is in Braille
    '''
    pattern = r'^[O.]+$'
    return not (bool(re.match(pattern, text)) and len(text) % 6 == 0)

def translate_to_braille(text: str) -> str:
    '''
    Translate the input text to Braille
    '''
    result = []
    is_numeric = False
    for char in text:
        if char.isupper():
            result.append(BRAILLE_UPPER)
            result.append(braille_dict.get(char.upper()))
        elif char.isnumeric():
            if not is_numeric:
                result.append(BRAILLE_NUMBER)
            is_numeric = True
            result.append(braille_number_dict.get(char))
        elif char == " ":
            is_numeric = False
            result.append("......")
        elif char == ".":
            result.append(BRAILLE_DECIMAL)
        else:
            result.append(braille_dict.get(char.upper()))
    return "".join(result)

def translate_to_text(text: str) -> str:
    '''
    Translate the input text to English
    '''
    result = []
    isNumber = False
    isCapital = False

    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]
        if braille_char == BRAILLE_NUMBER:
            isNumber = True
            continue
        elif braille_char == BRAILLE_UPPER:
            isCapital = True
        elif braille_char == BRAILLE_DECIMAL:
            result.append('.')
        elif braille_char == '......':
            result.append(' ')
            isNumber = False
            continue
        else:
            if isNumber:
                result.append(str(english_number_dict.get(braille_char)))
            else:
                if isCapital:
                    result.append(english_dict.get(braille_char).upper())
                    isCapital = False
                else:
                    result.append(english_dict.get(braille_char).lower())

    return "".join(result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = " ".join(sys.argv[1:])
        output = main(input)
        print(str(output))
    else:
        print("Usage: python3 translator.py <text>")
