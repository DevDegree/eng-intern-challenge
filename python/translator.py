import sys

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', '.O.OOO': 'number', '.....O': 'capital'
}

braille_to_digit = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def is_braille(text):
    return all(c in 'O.' for c in text)

def translate_english_to_braille(text):
    braille_output = []
    number_mode = False
    for char in text:
        if char.isupper():
            braille_output.append(english_to_braille['capital'])
            char = char.lower()
        if char.isdigit() and not number_mode:
            braille_output.append(english_to_braille['number'])
            number_mode = True
        if not char.isdigit() and number_mode:
            number_mode = False
        braille_output.append(english_to_braille.get(char, '......'))
    return ''.join(braille_output)


def translate_braille_to_english(text):
    english_output = []
    number_mode = False
    i = 0
    while i < len(text):
        braille_char = text[i:i+6]
        if braille_char == english_to_braille['capital']:
            i += 6
            braille_char = text[i:i+6]
            char = braille_to_english.get(braille_char, '')
            english_output.append(char.upper())
        elif braille_char == english_to_braille['number']:
            number_mode = True
        else:
            if braille_char == '......':
                english_output.append(' ')
            elif number_mode and braille_char in braille_to_digit:
                english_output.append(braille_to_digit[braille_char])
            else:
                char = braille_to_english.get(braille_char, '')
                english_output.append(char)
                number_mode = False
        i += 6
    return ''.join(english_output)

def translate(text):
    if is_braille(text):
        return translate_braille_to_english(text)
    else:
        return translate_english_to_braille(text)

# Main
if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    translated_text = translate(input_text)
    print(translated_text)
