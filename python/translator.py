import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

english_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g',
    'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n',
    'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u',
    'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', '.....O': 'capital', '.O.OOO': 'number'
}


numbers_dict = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}


def english_to_braille(text):
    braille_output = ""
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output += braille_dict['number']
                number_mode = True
            braille_output += braille_dict[char]
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                braille_output += braille_dict['capital']
                braille_output += braille_dict[char.lower()]
            elif char == ' ':
                braille_output += braille_dict[' ']
            else:
                braille_output += braille_dict[char]
    return braille_output


def braille_to_english(braille_text):
    english_output = ""
    i = 0
    flag = False

    while i < len(braille_text):
        if flag:
            if braille_text[i:i+6] == braille_dict[' ']:
                english_output += ' '
                flag = False
            else:
                english_output += numbers_dict[english_dict[braille_text[i:i+6]]]
        elif braille_text[i:i+6] == braille_dict['number']:
            flag = True
        elif braille_text[i:i+6] == braille_dict['capital']:
            i += 6
            english_output += english_dict[braille_text[i:i+6]].upper()
        else:
            char = english_dict[braille_text[i:i+6]]
            english_output += char
        i += 6
    return english_output


def is_braille(input_string):
    valid_braille_characters = {'.', 'O'}
    for char in input_string:
        if char not in valid_braille_characters:
            return False
    return True


if __name__ == "__main__":
    cmd = sys.argv[1:]  
    input = ' '.join(cmd)
    if is_braille(input):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))
