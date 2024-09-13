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
eng_to_br = {x: y for y, x in braille_to_english.items()}

br_to_num = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
num_to_braille = {x: y for y, x in br_to_num.items()}

def isBraille(input_str):
    return all(char in 'O.' for char in input_str)

def translate_braille_to_english(input_str):
    eng_output = []
    building_num = False
    
    i = 0
    while i < len(input_str):
        br_char = input_str[i:i + 6]

        if br_char == eng_to_br['capital']:
            i += 6
            br_char = input_str[i:i + 6]
            eng_output.append(braille_to_english[br_char].upper())
        elif br_char == eng_to_br['number']:
            building_num = True
        elif br_char == eng_to_br[' ']:
            building_num = False
            eng_output.append(' ')
        else:
            if building_num:
                eng_output.append(br_to_num[br_char])
            else:
                eng_output.append(braille_to_english[br_char])

        i += 6

    return ''.join(eng_output)

def translate_english_to_braille(input_str):
    br_output = []
    building_num = False

    for char in input_str:
        if char.isupper():
            br_output.append(eng_to_br['capital'])
            br_output.append(eng_to_br[char.lower()])
        elif char.isdigit() and not building_num:
            building_num = True
            br_output.append(eng_to_br['number'])
            br_output.append(num_to_braille[char.lower()])
        elif char == ' ':
            building_num = False
            br_output.append(eng_to_br[' '])
        elif building_num:
            br_output.append(num_to_braille[char.lower()])
        else:
            br_output.append(eng_to_br[char])

    return ''.join(br_output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <strings_to_translate>")
        return

    input_str = ' '.join(sys.argv[1:])

    if isBraille(input_str):
        print(translate_braille_to_english(input_str))
    else:
        print(translate_english_to_braille(input_str))

if __name__ == '__main__':
    main()
