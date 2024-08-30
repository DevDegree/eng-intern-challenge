import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'capital',
    '.O.OOO': 'number',
    '.O...O': 'decimal',
    '......': ' ',
}
english_to_braille = {v: k for k, v in braille_to_english.items()}

braille_to_num = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
num_to_braille = {v: k for k, v in braille_to_num.items()}

def is_braille(input_string):
    return all(char in 'O.' for char in input_string)

def translate_braille_to_english(input_string):
    english_output = []
    building_num = False
    
    i = 0
    while i < len(input_string):
        braille_char = input_string[i:i + 6]

        if braille_char == english_to_braille['capital']:
            i += 6
            braille_char = input_string[i:i + 6]
            english_output.append(braille_to_english[braille_char].upper())
        elif braille_char == english_to_braille['number']:
            building_num = True
        elif braille_char == english_to_braille[' ']:
            building_num = False
            english_output.append(' ')
        else:
            if building_num:
                english_output.append(braille_to_num[braille_char])
            else:
                english_output.append(braille_to_english[braille_char])

        i += 6

    return ''.join(english_output)

def translate_english_to_braille(input_string):
    braille_output = []
    building_num = False

    for char in input_string:
        if char.isupper():
            braille_output.append(english_to_braille['capital'])
            braille_output.append(english_to_braille[char.lower()])
        elif char.isdigit() and not building_num:
            building_num = True
            braille_output.append(english_to_braille['number'])
            braille_output.append(num_to_braille[char.lower()])
        elif char == ' ':
            building_num = False
            braille_output.append(english_to_braille[' '])
        elif building_num:
            braille_output.append(num_to_braille[char.lower()])
        else:
            braille_output.append(english_to_braille[char])

    return ''.join(braille_output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <strings_to_translate>")
        return

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))

if __name__ == '__main__':
    main()

