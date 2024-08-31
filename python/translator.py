import sys

# Braille mappings
BRAILLE_DICT = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......',
    'capital': '.....O',    'number': '.O.OOO'
}

# Reverse the Braille dictionary for Braille to English conversion
ENGLISH_DICT = {v: k for k, v in BRAILLE_DICT.items()}

def english_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(BRAILLE_DICT['capital'])
            if number_mode:
                number_mode = False
            result.append(BRAILLE_DICT[char.lower()])
        elif char.isdigit():
            if not number_mode:
                result.append(BRAILLE_DICT['number'])
                number_mode = True
            result.append(BRAILLE_DICT[chr(ord(char) - ord('0') + ord('a'))])
        elif char == ' ':
            result.append(BRAILLE_DICT[char])
            number_mode = False
    
    return ''.join(result)


def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == BRAILLE_DICT['capital']:
            capitalize_next = True
        elif chunk == BRAILLE_DICT['number']:
            number_mode = True
        elif chunk in ENGLISH_DICT:
            char = ENGLISH_DICT[chunk]
            if char.isalpha():
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                if number_mode:
                    char = str(ord(char) - ord('a'))
                    number_mode = False
            elif char == ' ':
                number_mode = False
            result.append(char)
        i += 6
    
    return ''.join(result)

def translate(input_string):
    if set(input_string).issubset({'O', '.'}):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    if input_string:
        result = translate(input_string)
        print(result, end='')  # Print without newline

