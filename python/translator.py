import sys

english_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    
    # Numbers
    '#': '.O.OOO',  # Number sign
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    
    # Special characters
    '.': '.O.O.O',
    ',': '.O....',
    ';': '.OO...',
    ':': '.OO...',
    '!': '.O.OO.',
    '?': '.O..OO',
    "'": '.....O',
    '-': '..OO..',
    
    # Capital letter indicator
    '^': '.....O'  # Place this before a letter to capitalize it
}

# Create the reverse mapping
braille_to_english = {v: k for k, v in english_to_braille.items()}

def is_braille(input_string):
    return all(char in 'O.' for char in input_string)

def chunk_braille(braille_string):
    return [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]

def translate_to_braille(english_string):
    result = []
    number_mode = False
    for char in english_string:
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['#'])
                number_mode = True
            result.append(english_to_braille[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(english_to_braille['^'])
            result.append(english_to_braille[char.lower()])
        elif char == ' ':
            number_mode = False
            result.append(english_to_braille[char])
        else:
            if number_mode:
                number_mode = False
            result.append(english_to_braille.get(char, '......'))
    return ''.join(result)

def translate_to_english(braille_string):
    result = []
    chunks = chunk_braille(braille_string)
    capitalize_next = False
    number_mode = False
    for chunk in chunks:
        if chunk == '.....O':  # Capital indicator
            capitalize_next = True
        elif chunk == '.O.OOO':  # Number indicator
            number_mode = True
        else:
            char = braille_to_english.get(chunk, ' ')
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            if number_mode:
                if char == ' ':
                    number_mode = False
                elif char in 'abcdefghij':
                    char = str('0123456789'['abcdefghij'.index(char)])
            result.append(char)
    return ''.join(result)

def translate(input_string):
    if is_braille(input_string):
        return translate_to_english(input_string)
    else:
        return translate_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        result = translate(input_string)
        print(result)
    else:
        print("Please provide a string to translate.")
