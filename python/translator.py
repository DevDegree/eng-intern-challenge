import sys

##Translator
## Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille.
## For Braille, each character is stored as a series of O (the letter O) or . (a period).
## Store Braille symbols as a 6 character string reading left to right, line by line, starting at the top left. See examples below.

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

UPPERCASE_PREFIX = '.....O'
NUMBER_PREFIX = '.O.OOO'

BRAILLE_TO_ENGLISH = {v: k for k, v in {**ENGLISH_TO_BRAILLE, **NUMBER_TO_BRAILLE}.items()}

def is_braille(input_str):
    return all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0

def translate_braille_to_english(braille_str):
    english_text = []
    i = 0
    number_mode = False
    while i < len(braille_str):
        braille_char = braille_str[i:i+6]
        
        if braille_char == UPPERCASE_PREFIX:
            i += 6
            braille_char = braille_str[i:i+6]
            english_text.append(BRAILLE_TO_ENGLISH.get(braille_char, '?').upper())
        elif braille_char == NUMBER_PREFIX:
            number_mode = True
            i += 6
        else:
            if number_mode:
                english_text.append(BRAILLE_TO_ENGLISH.get(braille_char, '?'))
            else:
                english_text.append(BRAILLE_TO_ENGLISH.get(braille_char, '?'))
            number_mode = False
        i += 6
    return ''.join(english_text)

def translate_english_to_braille(english_str):
    braille_text = []
    number_mode = False
    for char in english_str:
        if char.isupper():
            braille_text.append(UPPERCASE_PREFIX)
            braille_text.append(ENGLISH_TO_BRAILLE[char.lower()])
        elif char.isdigit():
            if not number_mode:
                braille_text.append(NUMBER_PREFIX)
                number_mode = True
            braille_text.append(NUMBER_TO_BRAILLE[char])
        else:
            number_mode = False
            if char in ENGLISH_TO_BRAILLE:
                braille_text.append(ENGLISH_TO_BRAILLE[char])
            else:
                braille_text.append('......') 
    return ''.join(braille_text)

def translate(input_str):
    if is_braille(input_str):
        return translate_braille_to_english(input_str)
    else:
        return translate_english_to_braille(input_str)

if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:])
    print(translate(input_str))
