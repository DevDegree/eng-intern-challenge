import sys
import textwrap

braille_to_english = {
    '......': ' ', 
    'O.....': 'a', 
    'O.O...': 'b', 
    'OO....': 'c', 
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f', 
    'OOOO..': 'g', 
    'O.OO..': 'h', 
    '.OO...': 'i',
    '.OOO..': 'j', 
    'O...O.': 'k', 
    'O.O.O.': 'l', 
    'OO..O.': 'm', 
    'OO.OO.': 'n',
    'O..OO.': 'o', 
    'OOO.O.': 'p', 
    'OOOOO.': 'q', 
    'O.OOO.': 'r', 
    '.OO.O.': 's',
    '.OOOO.': 't', 
    'O...OO': 'u', 
    'O.O.OO': 'v', 
    '.OOO.O': 'w', 
    'OO..OO': 'x',
    'OO.OOO': 'y', 
    'O..OOO': 'z', 
    '.....O': 'CAPITAL', 
    '.O.OOO': 'NUMBER'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

number_map = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
              'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}

def is_braille(inp):
    """Check if the input is Braille (contains only 'O' and '.')"""
    return all(char in 'O.' for char in inp) and len(inp) % 6 == 0


def braille_to_text(inp):
    """Convert Braille to English text"""
    chunks = textwrap.wrap(inp, 6)  
    res = []
    capitalize_next = False
    number_mode = False

    for chunk in chunks:
        if chunk == english_to_braille['CAPITAL']:
            capitalize_next = True
        elif chunk == english_to_braille['NUMBER']:
            number_mode = True
        else:
            char = braille_to_english.get(chunk, '')
            if number_mode and char in 'abcdefghij':
                char = number_map[char]
            elif capitalize_next:
                char = char.upper()
                capitalize_next = False
            
            if char == ' ':
                number_mode = False
            res.append(char)

    return ''.join(res)

def text_to_braille(inp):
    """Convert English text to Braille"""
    res = []
    number_mode = False

    for char in inp:
        if char.isdigit():
            if not number_mode:
                res.append(english_to_braille['NUMBER'])
                number_mode = True
            res.append(english_to_braille[list(number_map.keys())[list(number_map.values()).index(char)]])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                res.append(english_to_braille['CAPITAL'])
            res.append(english_to_braille[char.lower()])
        elif char == ' ':
            if number_mode:
                number_mode = False
            res.append(english_to_braille[char])
        else:
            # Ignore unsupported characters
            pass

    return ''.join(res)

def translate(inp):
    """Determine input type and translate accordingly"""
    if is_braille(inp): return braille_to_text(inp)
    else: return text_to_braille(inp)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide a string to translate.')
    else:
        input_string = " ".join(sys.argv[1:])
        result = translate(input_string)
        if result is not None:
            print(result)
        else:
            sys.exit("Error: Unable to translate the input.")