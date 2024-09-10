import sys

# Braille dictionary for lowercase English letters
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# Reverse dictionary for Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Special symbols
capital_prefix = '.....O'
number_prefix = '.....OO'
number_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
reverse_number_dict = {v: k for k, v in number_dict.items()}


def translate_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            result.append(number_prefix)
            number_mode = True
        elif char.isalpha() and number_mode:
            number_mode = False

        if char.isupper():
            result.append(capital_prefix)
            result.append(braille_dict[char.lower()])
        elif char.isdigit():
            result.append(number_dict[char])
        else:
            result.append(braille_dict[char])

    return ''.join(result)


def translate_to_english(braille_text):
    result = []
    i = 0
    number_mode = False
    
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        
        if braille_char == capital_prefix:
            i += 6
            braille_char = braille_text[i:i+6]
            result.append(reverse_braille_dict[braille_char].upper())
        elif braille_char == number_prefix:
            number_mode = True
        elif number_mode:
            result.append(reverse_number_dict[braille_char])
            if braille_char == '......':  # Handle switching off number mode at spaces
                number_mode = False
        else:
            result.append(reverse_braille_dict.get(braille_char, ' '))
        
        i += 6

    return ''.join(result)


def main():
    input_text = ' '.join(sys.argv[1:])
    
    if 'O' in input_text or '.' in input_text:
        # Assuming it's Braille input
        print(translate_to_english(input_text))
    else:
        # Assuming it's English input
        print(translate_to_braille(input_text))


if __name__ == "__main__":
    main()

