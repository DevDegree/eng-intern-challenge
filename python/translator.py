#!/usr/bin/env python3
import sys


english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  
    'capital': '.....O',  
    'number': '.O.OOO'  
}


number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}


braille_to_english_letters = {v: k for k, v in english_to_braille.items() if k.isalpha() or k == ' '}
braille_to_english_numbers = {v: k for k, v in number_to_braille.items()}

def translate_to_english(braille_input):
    translated_text = []
    braille_length = 6
    braille_chars = [braille_input[i:i + braille_length] for i in range(0, len(braille_input), braille_length)]

    word_mode = False
    number_mode = False

    for braille_char in braille_chars:
        if braille_char == english_to_braille['number']:
            number_mode = True
            word_mode = False  
            continue 

        elif braille_char == english_to_braille['capital']:
            word_mode = True
            number_mode = False  
            continue 

        if number_mode and braille_char in braille_to_english_numbers:
            translated_text.append(braille_to_english_numbers[braille_char])

        elif not number_mode and braille_char in braille_to_english_letters:
            char = braille_to_english_letters[braille_char]
            if word_mode:
                translated_text.append(char.upper())
                word_mode = False  
            else:
                translated_text.append(char)

        elif braille_char == '......':
            translated_text.append(' ')

        else:
            pass

    return ''.join(translated_text)

def translate_to_braille(english_input):
    translated_text = []
    number_mode = False

    for char in english_input:
        if char.isupper():
            translated_text.append(english_to_braille['capital'])
            translated_text.append(english_to_braille[char.lower()])
        elif char.isdigit():
            if not number_mode:
                translated_text.append(english_to_braille['number'])
                number_mode = True
            translated_text.append(number_to_braille[char])
        else:
            number_mode = False  
            translated_text.append(english_to_braille[char])
    return ''.join(translated_text)

def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

def main():
    if len(sys.argv) != 2:
        print("")
        return

    input_string = sys.argv[1]

    
    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
