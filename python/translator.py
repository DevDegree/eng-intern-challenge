import sys

text = ' '.join(sys.argv[1:])

braille_alphabet = ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..', 'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.', 'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.', 'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO', 'O..OOO', 'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..', '.....O', '.O...O', '.O.OOO', '..OO.O', '..O...', '..O.OO', '..OOOO', '..OO..', '..O.O.', '....OO', '.O..O.', '.OO..O', 'O..OO.', 'O.O..O', '.O.OO.', '......']
english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'capital follows', 'decimal follows', 'number follows', '.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' ']


def translate(text: str) -> str:
    translated_text = ""

    # if text is Braille
    if not text.replace('.', '').replace('O', ''):
        
        length = len(text) // 6
        last_char = ''

        for i in range(length):
            char_index = braille_alphabet.index(text[i*6: (i+1)*6])

            if last_char == 'capital follows':
                char = english_alphabet[char_index].upper()
                last_char = char

            elif last_char == 'number follows':
                if char_index == 51: # check for space
                    char, last_char = ' ', ' '
                else:     
                    char = english_alphabet[char_index + 26]

            else:
                char = english_alphabet[char_index]

                if char.endswith('follows'):
                    last_char = char
                    continue

            translated_text += char

    # if text is English
    else:

        last_char = ''
        for char in text:

            if char.isnumeric() and not last_char.isnumeric():
                braille_char = '.O.OOO'

            elif char.isupper():
                char = char.lower()
                braille_char = '.....O'

            else:
                braille_char = ''
            
            last_char = char
            translated_text += braille_char + braille_alphabet[english_alphabet.index(char)]

    return translated_text

print(translate(text))