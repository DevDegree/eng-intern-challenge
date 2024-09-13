import sys 

braille_to_char_map = {
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
    'O...O.': 'k',
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
    'O..OOO': 'z'
}

num_to_braille_map = {
    '1': '.O.....',
    '2': '.O.O...',
    '3': '.OO....',
    '4': '.OO.O..',
    '5': '.O..O..',
    '6': '.OOO...',
    '7': '.OOOO..',
    '8': '.O.OO..',
    '9': '..OO...',
    '0': '..OOO..'
}

char_to_braille_map = {v: k for k, v in braille_to_char_map.items()}
braille_to_num_map = {v: k for k, v in num_to_braille_map.items()}
capital = '.....'
number_prefix = ""


def translate_to_braille(text):
    braille_output_list = []

    for i in text:
        if i.isdigit():
            braille_output_list.append(num_to_braille_map.get(i, ""))
        elif i.isupper():
            braille_output_list.append(capital)
            braille_output_list.append(char_to_braille_map.get(i.lower(), ""))
        else:
            braille_output_list.append(char_to_braille_map.get(i, ""))

    return " ".join(braille_output_list)


def translate_to_text(braille):
    braille_input = braille.split()
    text_output = ""
    i = 0

    while i < len(braille_input):
        if braille_input[i] == capital:
            i += 1
            if i < len(braille_input):
                text_output += braille_to_char_map.get(braille_input[i], "").upper()
        else:
            text_output += braille_to_char_map.get(braille_input[i], "?")
        i += 1
    
    return text_output


if __name__ == "__main__":
    input_str = " ".join(sys.argv[1:])
    
    if set(input_str).issubset({'O', '.', ' '}):
        print(translate_to_text(input_str))
    
    else:
        print(translate_to_braille(input_str))