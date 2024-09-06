
import sys
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',

    'capital': '.....O',
    'number': '.O.OOO'
}

braille_number_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

reverse_braille_dict = {v: k for k, v in braille_dict.items() if k not in '1234567890'}
reverse_braille_number_dict = {v: k for k, v in braille_number_dict.items()}
def translate_to_braille(english_string):
    braille_translation = []
    dig = False
    for char in english_string:
        if char.isupper():
            braille_translation.append(braille_dict['capital'])
            braille_translation.append(braille_dict[char.lower()])
            dig = False
        elif char.isdigit():
            if not dig:
                braille_translation.append(braille_dict['number'])
                dig = True
            braille_translation.append(braille_number_dict[char])
        else:
            dig = False
            braille_translation.append(
                braille_dict.get(char.lower(), '......'))
    return ''.join(braille_translation)


def translate_to_english(braille_string):
    braille_chars = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]
    english_translation = []
    capital_flag = False
    number_flag = False

    for char in braille_chars:
        if char == braille_dict['capital']:
            capital_flag = True
            continue
        elif char == braille_dict['number']:
            number_flag = True
            continue
        elif char == '......':
            english_translation.append(' ')
            number_flag = False
            continue

        if capital_flag:
            english_translation.append(reverse_braille_dict[char].upper())
            capital_flag = False
        elif number_flag:
            english_translation.append(reverse_braille_number_dict[char])
        else:
            english_translation.append(reverse_braille_dict.get(char, ' '))

    return ''.join(english_translation)



def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:]) 
    else:
        print("No arguments passed!")
        exit()
    english = False
    for letter in "abcdefghijklmnpqrstuvwxyz123456789":
        if letter in text.lower():
            english = True
            break
    if english:
        braille_translation = translate_to_braille(text)
        print(braille_translation)
    else:
        english_translation = translate_to_english(text)
        print(english_translation)

if __name__ == "__main__":
    main()