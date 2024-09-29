import sys

# Braille mappings
BRAILLE_TO_ENGLISH = {
        '......': ' ',
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y',
    'O..OOO': 'Z',
    '.....O': 'CAPITAL',
    '.O.OOO': 'NUMBER',
}

# Reverse mapping for English to Braille
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

def is_braille(text):
    return all(char in '.O' for char in text) and len(text) % 6 == 0

def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False


    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == ENGLISH_TO_BRAILLE['CAPITAL']:
            capitalize_next = True
        elif symbol == ENGLISH_TO_BRAILLE['NUMBER']:
            number_mode = True
        else:
            char = BRAILLE_TO_ENGLISH.get(symbol, '')
            if number_mode and char.isalpha():
                char = str('0123456789'.index(char))
            elif capitalize_next:
                char = char.upper()
                capitalize_next = False
            
            if char == ' ':
                number_mode = False
            
            result.append(char)
        
        i += 6

    return ''.join(result)

def english_to_braille(english):
    result = []
    number_mode = False

    for char in english:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['NUMBER'])
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE['JABCDEFGHI'[int(char)]])
        elif char.isspace():
            result.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
        else:
            if number_mode:
                number_mode = False
            
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['CAPITAL'])
                char = char.lower()
            
            result.append(ENGLISH_TO_BRAILLE.get(char.upper(), ''))

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        result = braille_to_english(input_text)
    else:
        result = english_to_braille(input_text)

    print(result)

if __name__ == "__main__":
    main()