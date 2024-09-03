# Author:Dina Yashaev

import sys

# Defining Braille characters to English alphabet
braille_alpha = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', 'O.O..O': '(',
    '.O.OO.': ')', '......': ' '
}
braille_nums = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
    '.OOO..': '0', '.OO..O': '<', 'O..OO.': '>',
}
# Instructions for Braille
CAPITAL = '.....O'
DECIMAL = '.O...O'
NUMBER = '.O.OOO'

# Inverse key and values from Braille characters to convert English to Braille
english_alpha = {val: key for key, val in braille_alpha.items()}
english_nums = {val: key for key, val in braille_nums.items()}


def language(input_text):
    return all(char == 'O' or char == '.' for char in input_text)


def trans_braille_to_eng(input_text):
    result_eng = ''
    i = 0
    temp = ''
    while i < len(input_text):
        temp += input_text[i]
        i += 1
        if len(temp) == 6:
            if temp == CAPITAL:
                result_eng += 'CAPITAL'
            elif temp == NUMBER:
                result_eng += 'NUMBER'
            elif temp == DECIMAL:
                result_eng += 'DECIMAL'
            else:
                if temp in braille_alpha:
                    result_eng += braille_alpha[temp]
                else:
                    result_eng += '?'
            temp = ''
    return result_eng


def trans_eng_to_braille(input_text):
    result_braille = ''
    number_mode = False
    for char in input_text:
        if char.isupper():
            result_braille += CAPITAL
            lower = char.lower()
            result_braille += english_alpha.get(lower, '?')
        elif char.isdigit():
            if not number_mode:
                result_braille += NUMBER
                number_mode = True
            result_braille += english_nums.get(char, '?')
        elif char == '.':
            result_braille += DECIMAL
            result_braille += english_alpha.get(char, '?')
        else:
            if char == ' ':
                number_mode = False
            result_braille += english_alpha.get(char, '?')
    return result_braille


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <text>")
        return

    input_text = ' '.join(sys.argv[1:]).strip()

    if language(input_text):
        print(trans_braille_to_eng(input_text))
    else:
        print(trans_eng_to_braille(input_text))


if __name__ == '__main__':
    main()


