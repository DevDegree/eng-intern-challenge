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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

braille_to_english_char = {v: k for k, v in english_to_braille.items() if k.isalpha() or k==' '}
braille_to_english_num = {v: k for k, v in english_to_braille.items() if k.isnumeric()}

caps_follow = '.....O'
nums_follow = '.O.OOO'

def translate_to_braille(message: str) -> str:
    braille_translation = []
    p_num = False

    for character in message:
        if character.isupper():
            braille_translation.append(caps_follow)
            character = character.lower()
        elif character.isdigit() and not p_num:
            braille_translation.append(nums_follow)
            p_num = True
        elif character==' ':
            p_num = False
        braille_translation.append(english_to_braille[character])
    return ''.join(braille_translation)


def translate_to_english(message: str) -> str:
    english_translation = []
    message_length = len(message)
    is_upper = False
    is_numeric = False

    for i in range(message_length//6):
        braile_char = message[i*6:(i+1)*6]
        if braile_char==caps_follow or braile_char==nums_follow:
            is_upper = braile_char==caps_follow
            is_numeric = braile_char==nums_follow
            continue

        if braile_char==english_to_braille[' ']:
            is_numeric = False

        char_to_add = braille_to_english_char[braile_char] if not is_numeric else braille_to_english_num[braile_char]

        if is_upper:
            char_to_add = char_to_add.upper()
            is_upper = False

        english_translation.append(char_to_add)
    return ''.join(english_translation)


def run_translator():
    if len(sys.argv) < 2:
        print('ERROR: no input given')
        return

    inputed_text = ' '.join(sys.argv[1:])
    
    if not ('.' in inputed_text):
        translated_text = translate_to_braille(inputed_text)
    else:
        translated_text = translate_to_english(inputed_text)
    
    print(translated_text)

if __name__ == '__main__':
    run_translator()

