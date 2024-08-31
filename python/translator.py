import sys

def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}

english_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......' 
}

braille_to_english_map = invert_dictionary(english_to_braille_map)


decimal_to_braille_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


braille_to_decimal_map = invert_dictionary(decimal_to_braille_map)

capital_marker = '.....O'  
number_marker = '.O.OOO'

def translate_english_to_braille(english_text):
    braille_text = ""
    is_number_mode = False

    for char in english_text:
        if char.isdigit():
            if not is_number_mode:
                is_number_mode = True
                braille_text += number_marker
            braille_text += decimal_to_braille_map[char]
        else:
            if is_number_mode:
                is_number_mode = False
            if char.isupper():
                braille_text += capital_marker
                char = char.lower()
            braille_text += english_to_braille_map[char]

    return braille_text

def translate_braille_to_english(braille_text):
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    english_text = ""
    is_capital_mode = False
    is_number_mode = False

    for braille_char in braille_chars:
        if braille_char == capital_marker:
            is_capital_mode = True
            continue
        if braille_char == number_marker:
            is_number_mode = True
            continue
        if braille_char == english_to_braille_map[' ']:
            is_number_mode = False
            english_text += ' '
        elif is_number_mode:
            english_text += braille_to_decimal_map.get(braille_char, '?')
        else:
            english_char = braille_to_english_map.get(braille_char, '?')
            if is_capital_mode:
                english_char = english_char.upper()
                is_capital_mode = False
            english_text += english_char

    return english_text

def is_valid_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    if is_valid_braille(input_text):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))
