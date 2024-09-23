
# conversions
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

braille_to_english = {
    braille:char for char, braille in english_to_braille.items() if not char.isdigit()
}

braille_to_numbers = {
    braille:num for num, braille in english_to_braille.items() if num.isdigit()
}


def translate_to_english(string):
    translation = ''

    # flags to check if next character is in caps or a num
    caps_flag = False
    number_flag = False

    # splitting into 6 character blocks
    braille_chars = [string[i: i+6] for i in range(0, len(string), 6)]

    for braille in braille_chars:
        # invalid character
        if braille not in braille_to_english:
            continue
        # checking if next character will be in caps, a num or a space
        if braille_to_english[braille] == 'capital':
            caps_flag = True
        elif braille_to_english[braille] == 'number':
            number_flag = True
        elif braille_to_english[braille] == ' ':
            translation += ' '
            number_flag = False
        else:
            # adding translated value accordingly
            if caps_flag: translation += braille_to_english[braille].upper()
            elif number_flag: translation += braille_to_numbers[braille]
            else: translation += braille_to_english[braille]
            # reset flag
            caps_flag = False

    return translation