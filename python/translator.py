import sys


BRAILLE_CHARS = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',
}


BRAILLE_NUMS = {
    '0': '.OOO.O',   '1': 'O.....',    '2': 'O.O...',    '3': 'OO....', 
    '4': 'OO.O..',   '5': 'O..O..',    '6': 'OOO...',    '7': 'OOOO..',
    '8': 'O.OO..',   '9': '.OO...'
}

# Reverse mappings for Braille to char/num
BRAILLE_TO_CHAR = {v: k for k, v in BRAILLE_CHARS.items()}
BRAILLE_TO_NUM = {v: k for k, v in BRAILLE_NUMS.items()}

# Special symbols
CAPITAL_SYMBOL = '.....O'
NUMBER_SYMBOL = '.O.OOO'
DECIMAL_SYMBOL = '.O...O'
SPACE = '......'
DOT = '.O.O..'

# Translate English to Braille
def english_to_braille(text):
    result = []
    is_number_mode = False

    for char in text:
        if char.isupper():
            result.append(CAPITAL_SYMBOL)
            char = char.lower()

        if char.isdigit():
            if not is_number_mode:
                result.append(NUMBER_SYMBOL)
                is_number_mode = True
            result.append(BRAILLE_NUMS[char])
        elif char == '.':
            if is_number_mode:
                result.append(DECIMAL_SYMBOL)
            else:
                result.append(DOT)
        elif char == ' ':
            result.append(SPACE)
            is_number_mode = False
        else:
            if is_number_mode:
                is_number_mode = False
            if char in BRAILLE_CHARS:
                result.append(BRAILLE_CHARS[char])
            else:
                result.append(SPACE)  
    
    return ''.join(result)

# Translate Braille to English
def braille_to_english(braille):
    result = []
    chunks = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capitalize_next = False
    is_number_mode = False

    for chunk in chunks:
        if chunk == CAPITAL_SYMBOL:
            capitalize_next = True
        elif chunk == NUMBER_SYMBOL:
            is_number_mode = True
        elif chunk == DECIMAL_SYMBOL:
            if is_number_mode:
                result.append('.')
            else:
                result.append('?') 
        elif chunk == SPACE:
            result.append(' ')
            # is_number_mode = False
        elif is_number_mode:
            if chunk in BRAILLE_TO_NUM:
                result.append(BRAILLE_TO_NUM[chunk])
            else:
                is_number_mode = False
        elif chunk in BRAILLE_TO_CHAR:
            char = BRAILLE_TO_CHAR[chunk]
            if capitalize_next:
                result.append(char.upper())
                capitalize_next = False
            else:
                result.append(char)
        else:
            result.append('?') 

    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        return

    input_string = " ".join(sys.argv[1:])
    
    if all(c in 'O.' for c in input_string):
        result = braille_to_english(input_string)
    else:
        result = english_to_braille(input_string)
    
    print(result)

if __name__ == "__main__":
    main()
