import sys

##Translator
## Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille.
## For Braille, each character is stored as a series of O (the letter O) or . (a period).
## Store Braille symbols as a 6 character string reading left to right, line by line, starting at the top left. See examples below.

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.O.O', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_PREFIX = {'CAPITAL': '.....O', 'NUMBER': '.O.OOO' }

def translate_english_to_braille(english_str):
    braille_text = []
    number_mode = False

    for char in english_str:
        if char.isdigit():
            if not number_mode:
                braille_text.append(BRAILLE_PREFIX['NUMBER'])
                number_mode = True
            braille_text.append(BRAILLE_NUMBERS[char])
        else:
            if number_mode and char != ' ':
                number_mode = False 
            if char.isupper():
                braille_text.append(BRAILLE_PREFIX['CAPITAL'])
                braille_text.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                braille_text.append(ENGLISH_TO_BRAILLE[char])

    return ''.join(braille_text)

def translate_braille_to_english(braille_str):
    english_text = []
    mode_tracker = 'pass'
    braille_to_english = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
    braille_to_numbers = {v: k for k, v in BRAILLE_NUMBERS.items()}

    for start_index in range(0, len(braille_str), 6):
        braille_character = braille_str[start_index:start_index + 6]

        if braille_character == BRAILLE_PREFIX['CAPITAL']:
            mode_tracker = 'CAPITAL'
        elif braille_character == BRAILLE_PREFIX['NUMBER']:
            mode_tracker = 'NUMBER'
        elif braille_character == '......':
            english_text.append(' ')
            mode_tracker = 'pass'
        else:
            if mode_tracker == 'CAPITAL':
                english_text.append(braille_to_english.get(braille_character, '?').upper())
                mode_tracker = 'pass'
            elif mode_tracker == 'NUMBER':
                english_text.append(braille_to_numbers.get(braille_character, '?'))
            else:
                english_text.append(braille_to_english.get(braille_character, '?'))

    return ''.join(english_text)

def is_braille(input_str):
    return all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0

def main():
    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        print(translate_braille_to_english(input_str))
    else:
        print(translate_english_to_braille(input_str))

if __name__ == '__main__':
    main()
