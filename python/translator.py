"""
English to Braille and Braille to English translator
"""

import sys

def translate_english_to_braille(phrase):
    english_chars_to_braille = {
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
        'k': 'O....O',
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
        'O': '.OOO..',
        'CAP': '.....O',
        'NUM': '.O.OOO',
        }

    braille_translation = [] # Save translated chars to list for efficiency
    num_mode = False

    for char in phrase:
        if char.isnumeric():
            if num_mode: # If num mode on append character as is
                braille_translation.append(english_chars_to_braille[char])
            else:
                num_mode = True # If curr char is numeric, turn on num mode, append Number follows char and numeric char
                braille_translation.extend([english_chars_to_braille['NUM'
                        ], english_chars_to_braille[char]])
        else:
            if num_mode:
                num_mode = False 

            if char.isupper():
                braille_translation.extend([english_chars_to_braille['CAP'
                        ], english_chars_to_braille[char.lower()]]) # If char is uppercase, append Capital follows char and char symbol
            else:
                braille_translation.append(english_chars_to_braille[char])

    return ''.join(braille_translation)


def translate_braille_to_english(phrase):
    braille_to_english_letters_mods = {
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
        'O....O': 'k',
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
        '......': ' ',
        '.....O': 'CAP',
        '.O.OOO': 'NUM',
        }

    braille_to_english_numbers = {
        'O.....': '1',
        'O.O...': '2',
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9',
        '.OOO..': 'O',
        }

    phrase_length = len(phrase)
    english_translation = [] # Save translated chars to list for efficiency
    num_mode = False
    cap_mode = False

    for index in range(6, phrase_length + 1, 6): # Multiples of 6 because braille chars are each 6 strings
        char = phrase[index - 6:index] 

        if num_mode: # If currently in number mode
            if char in braille_to_english_numbers: # Check if current char is braille number
                english_translation.append(braille_to_english_numbers[char])
            else:
                num_mode = False # If current char not braille number, turn off num mode and append translation
                english_translation.append(braille_to_english_letters_mods[char])
            continue

        if char in braille_to_english_letters_mods:
            if braille_to_english_letters_mods[char] == 'CAP':
                cap_mode = True # Set cap mode True if Capital letter follows char found
                continue

            if braille_to_english_letters_mods[char] == 'NUM':
                num_mode = True # Set num mode True if Number follows char found
                continue

            if cap_mode:
                english_translation.append(braille_to_english_letters_mods[char].upper()) # Set translation to upper case if in Capital letter mode
                cap_mode = False # End capital letter mode
                continue

            english_translation.append(braille_to_english_letters_mods[char])

    return ''.join(english_translation)


def non_braille_chars_present(phrase):
    """
    Return False if all characters in phrase are 'O' or '.' indicated phrase isn't braille, else return True
    """
    for char in phrase:
        if char != 'O' and char != '.':
            return True
    return False


def main():
    if len(sys.argv) >= 2: # Check if sys input arguments aren't empty
        user_input = " ".join(sys.argv[1:]) # Join input arguments with space delimiter
        if non_braille_chars_present(user_input):
            return translate_english_to_braille(user_input)
        return translate_braille_to_english(user_input)

sys.stdout.write(main())
