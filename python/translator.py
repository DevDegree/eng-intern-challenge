import sys

def is_braille(s):
    return all(c in {'.', 'O'} for c in s)

def translate_braille_to_english(braille):
    english = []
    capitalize, number_mode = False, False
    letters = []
    for i in range(0, len(braille), 6):
        letters.append(braille[i:i+6])

    for braille_char in letters:
        if braille_char == ".....O":
            capitalize = True
        elif braille_char == ".O.OOO":
            number_mode = True
        elif braille_char == ".O...O":
            english.append(".")
        else:
            if capitalize:
                english.append(braille_to_english.get(braille_char, '').upper())
                capitalize = False
            elif number_mode:
                if braille_char == "......":
                    english.append(" ")
                    number_mode = False
                else:
                    english.append(braille_to_english_nums.get(braille_char, ''))
            else:
                english.append(braille_to_english.get(braille_char, ''))
    return ''.join(english)

def translate_english_to_braille(text):
    braille = []
    number_active = False

    for char in text:
        if char.isupper():
            braille.append(".....O")
            char = char.lower()
        if char.isdigit() and not number_active:
            braille.append(".O.OOO")
            number_active = True
        if char == " ":
            number_active = False
        braille.append(english_to_braille.get(char, english_to_braille_nums.get(char, '')))
    return ''.join(braille)

if __name__ == '__main__':
    
    input_string = ' '.join(sys.argv[1:])
    
    english_to_braille = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
        'z': 'O..OOO', ' ': '......',

        "Capital": ".....O",
        "Decimal": ".O...O",
        "Number": ".O.OOO",
    }

    english_to_braille_nums = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        ',': '.O....', ';': '.OO...', ':': '.O.O..', '.': '.O.OO.', '!': '.OO.O.',
        '?': '.OO..O', '-': '..O.O.', '/': '.O.O..', '(': '.O.O.O', ')': 'O..O.O', 
        '<': 'OO...O', '>': '..OO.O', 
    }

    braille_to_english = {value: key for key, value in english_to_braille.items()}
    braille_to_english_nums = {value: key for key, value in english_to_braille_nums.items()}

    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))
