import argparse
import sys

english_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",

    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",

    ' ': "......", '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.",
    ':': "..OO..", ';': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O",
    '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.",

}
braille_to_english = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
    "OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
    "O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
    "OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
    "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
    "O..OOO": 'z',
}
braille_to_sign = {
    "......": ' ', "..OO.O": '.', "..O...": ',', "..O.OO": '?', "..OOO.": '!',
    "..OO..": ':', "..O.O.": ';', "....OO": '-', ".O..O.": '/', ".OO..O": '<',
    "O..OO.": '>', "O.O..O": '(', ".O.OO.": ')',
}
braille_to_number = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5',
    "OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0',
}

capital_indicator = '.....O'
number_indicator = '.O.OOO'
decimal_indicator = '.O...O'
braille_space = '......'

def toEnglish(input):
    result = ""
    i = 0
    number_mode = False
    while i < len(input):
        braille_char = input[i:i+6]
        if braille_char == capital_indicator:
            i += 6
            braille_char = input[i:i+6]
            result += braille_to_english.get(braille_char, '').upper()
        elif number_mode and braille_char == decimal_indicator:
            result += '.'
        elif braille_char == number_indicator:
            number_mode = True
        elif braille_char == braille_to_english.get(' '):
            number_mode = False
            result += ' '
        else:
            if number_mode and braille_char in braille_to_number:
                result += braille_to_number[braille_char]
            elif braille_char in braille_to_english:
                result += braille_to_english[braille_char]
            elif braille_char in braille_to_sign:
                result += braille_to_sign[braille_char]

        i += 6
    return result
def toBraille(input):
    result = ""
    number_mode = False
    for c in input:
        if c == " ":
            result += braille_space
            number_mode = False
        if c == '.' and number_mode:
            result += decimal_indicator
        elif c.isupper():
            result += capital_indicator + english_to_braille.get(c.lower(), '')
            number_mode = False
        elif c.isdigit():
            if not number_mode:
                result += number_indicator
                number_mode = True
            result += english_to_braille.get(c, '')
        else:
            result += english_to_braille.get(c, '')
    return result
def main():
    parser = argparse.ArgumentParser(description='Process some input.')
    parser.add_argument('input', type=str, nargs='+', help='Input to translate')
    args = parser.parse_args()
    input_text = ' '.join(args.input)
    if all(c in 'O.' for c in input_text):
        print(toEnglish(input_text))
    else:
        print(toBraille(input_text))
        sys.exit(1)

if __name__ == "__main__":
    main()
