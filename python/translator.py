braille_map = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '.....O': 'CAPITAL', '.O.OOO': 'NUMBER', '......': ' '
}

english_map = {v: k for k, v in braille_map.items()}

number_map_braille = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

number_map_english = {v: k for k, v in number_map_braille.items()}

def is_braille(input_string):
    return all(char in 'O.' for char in input_string)

def convert_to_english(braille):
    output = []
    is_capital = False
    is_number = False

    for i in range(0, len(braille), 6):
        chunk = braille[i:i+6]
        letter = braille_map.get(chunk)

        if letter == 'CAPITAL':
            is_capital = True
        elif letter == 'NUMBER':
            is_number = True
        else:
            if is_number:
                output.append(number_map_braille.get(chunk, ''))
            elif is_capital:
                output.append(letter.upper())
                is_capital = False
            else:
                output.append(letter)

    return ''.join(output)

def convert_to_braille(english):
    output = []
    is_number = False

    for letter in english:
        if letter.isdigit():
            if not is_number:
                output.append(english_map['NUMBER'])
                is_number = True
            output.append(number_map_english[letter])
        else:
            if is_number:
                is_number = False
            if letter == ' ':
                output.append(english_map[' '])
            else:
                if letter.isupper():
                    output.append(english_map['CAPITAL'])
                output.append(english_map[letter.lower()])

    return ''.join(output)

def main():
    import sys
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(convert_to_english(input_string))
    else:
        print(convert_to_braille(input_string))

if __name__ == '__main__':
    main()

