"""
English to Braille and Braille to English translator
"""


def translate_english_to_braille(phrase):
    english_chars_to_braille = {
        'a': '0.....',
        'b': '0.0...',
        'c': '00....',
        'd': '00.0..',
        'e': '0..0..',
        'f': '000...',
        'g': '0000..',
        'h': '0.00..',
        'i': '.00...',
        'j': '.000..',
        'k': '0....0',
        'l': '0.0.0.',
        'm': '00..0.',
        'n': '00.00.',
        'o': '0..00.',
        'p': '000.0.',
        'q': '00000.',
        'r': '0.000.',
        's': '.00.0.',
        't': '.0000.',
        'u': '0...00',
        'v': '0.0.00',
        'w': '.000.0',
        'x': '00..00',
        'y': '00.000',
        'z': '0..000',
        ' ': '......',
        '1': '0.....',
        '2': '0.0...',
        '3': '00....',
        '4': '00.0..',
        '5': '0..0..',
        '6': '000...',
        '7': '0000..',
        '8': '0.00..',
        '9': '.00...',
        '0': '.000..',
        'CAP': '.....0',
        'NUM': '.0.000',
        }

    braille_translation = []
    num_mode = False

    for char in phrase:
        if char.isnumeric():
            if num_mode:
                braille_translation.append(english_chars_to_braille[char])
            else:
                num_mode = True
                braille_translation.extend([english_chars_to_braille['NUM'
                        ], english_chars_to_braille[char]])
        else:
            if num_mode:
                num_mode = False
                braille_translation.append(english_chars_to_braille[' '
                        ])

            if char.isupper():
                braille_translation.extend([english_chars_to_braille['CAP'
                        ], english_chars_to_braille[char.lower()]])
            else:
                braille_translation.append(english_chars_to_braille[char])

    return ''.join(braille_translation)


def translate_braille_to_english(phrase):
    braille_to_english_letters_mods = {
        '0.....': 'a',
        '0.0...': 'b',
        '00....': 'c',
        '00.0..': 'd',
        '0..0..': 'e',
        '000...': 'f',
        '0000..': 'g',
        '0.00..': 'h',
        '.00...': 'i',
        '.000..': 'j',
        '0....0': 'k',
        '0.0.0.': 'l',
        '00..0.': 'm',
        '00.00.': 'n',
        '0..00.': 'o',
        '000.0.': 'p',
        '00000.': 'q',
        '0.000.': 'r',
        '.00.0.': 's',
        '.0000.': 't',
        '0...00': 'u',
        '0.0.00': 'v',
        '.000.0': 'w',
        '00..00': 'x',
        '00.000': 'y',
        '0..000': 'z',
        '......': ' ',
        '.....0': 'CAP',
        '.0.000': 'NUM',
        }

    braille_to_english_numbers = {
        '0.....': '1',
        '0.0...': '2',
        '00....': '3',
        '00.0..': '4',
        '0..0..': '5',
        '000...': '6',
        '0000..': '7',
        '0.00..': '8',
        '.00...': '9',
        '.000..': '0',
        }

    phrase_length = len(phrase)
    english_translation = []
    num_mode = False
    cap_mode = False

    for index in range(6, phrase_length + 1, 6):
        char = phrase[index - 6:index]

        if num_mode:
            if char in braille_to_english_numbers:
                english_translation.append(braille_to_english_numbers[char])
            else:
                num_mode = False
                english_translation.append(braille_to_english_letters_mods[char])
            continue

        if char in braille_to_english_letters_mods:
            if braille_to_english_letters_mods[char] == 'CAP':
                cap_mode = True
                continue

            if braille_to_english_letters_mods[char] == 'NUM':
                num_mode = True
                continue

            if cap_mode:
                english_translation.append(braille_to_english_letters_mods[char].upper())
                cap_mode = False
                continue

            english_translation.append(braille_to_english_letters_mods[char])

    return ''.join(english_translation)


def non_braille_chars_present(phrase):
    for char in phrase:
        if char != '0' and char != '.':
            return True
    return False


def main():
    phrase = input()

    if phrase:
        if non_braille_chars_present(phrase):
            return translate_english_to_braille(phrase)
        return translate_braille_to_english(phrase)
    return ''


print(main())
