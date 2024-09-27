
import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_capital = '.....O'
braille_number = '.O.OOO'

reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}


def is_braille(input_string):
    return all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0


def translate_braille_to_english(braille_string):
    english_output = []
    capital_mode = False
    number_mode = False
    
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i + 6]
        
        if braille_char == braille_capital:
            capital_mode = True
            continue
        if braille_char == braille_number:
            number_mode = True
            continue
        
        if number_mode:
            if braille_char in reverse_braille_numbers:
                english_output.append(reverse_braille_numbers[braille_char])
            number_mode = False if braille_char == '......' else number_mode 
        else:
            if braille_char in reverse_braille_alphabet:
                char = reverse_braille_alphabet[braille_char]
                if capital_mode:
                    english_output.append(char.upper())
                    capital_mode = False
                else:
                    english_output.append(char)

    return ''.join(english_output)


def translate_english_to_braille(english_string):
    braille_output = []
    for char in english_string:
        if char.isupper():
            braille_output.append(braille_capital)
            braille_output.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            braille_output.append(braille_number)
            braille_output.append(braille_numbers[char])
        else:
            braille_output.append(braille_alphabet[char])
    
    return ''.join(braille_output)


def main():
    input_string = sys.argv[1]

    if is_braille(input_string):
        result = translate_braille_to_english(input_string)
    else:
        result = translate_english_to_braille(input_string)
    
    print(result)


if __name__ == '__main__':
    main()
