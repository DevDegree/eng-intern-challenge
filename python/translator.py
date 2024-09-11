import sys

def translator(inputStr):
    english_dict = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
                    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
                    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
                    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
                    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
                    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
                    'y': 'OO.OOO', 'z': 'O..OOO', '0': '.OOO..', '1': 'O.....',
                    '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
                    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
                    ' ': '......'}

    braille_dict = {'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
                    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
                    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
                    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
                    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
                    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
                    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' '}

    braille_numbers = {'.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
                       'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'}
    capital_follows = '.....O'
    number_follows = '.O.OOO'
    english_mode = True
    output = ''

    first_symbol = inputStr[:6]

    if first_symbol in braille_dict or first_symbol == capital_follows or first_symbol == number_follows:
        english_mode = False

    if english_mode is False:
        i = 0
        capital_mode = False
        number_mode = False
        while i < len(inputStr):
            braille = inputStr[i: i + 6].upper()
            if braille == capital_follows:
                capital_mode = True
            elif braille == number_follows:
                number_mode = True
            elif capital_mode is True:
                output += braille_dict[braille].upper()
                capital_mode = False
            elif number_mode is True and braille_dict[braille] == ' ':
                number_mode = False
                output += braille_dict[braille]
            elif number_mode is True:
                output += braille_numbers[braille]
            else:
                output += braille_dict[braille]
            i += 6
    else:
        number_mode = False
        for letter in inputStr:
            if letter.isdigit() and number_mode is False:
                output += number_follows
                number_mode = True
            elif letter == ' ' and number_mode is True:
                number_mode = False
            elif letter.isupper():
                output += capital_follows
            else:
                pass
            output += english_dict[letter.lower()]
    return output


if __name__ == '__main__':
    char_strings = " ".join(sys.argv[1:])
    print(translator(char_strings))
