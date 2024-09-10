import sys

braille_dict = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # Punctuation
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',

    # Space
    ' ': '......'
}

# Special symbols
CAPITAL_PREFIX = '.....O'  
NUMBER_PREFIX = '.O.OOO'   
DECIMAL_PREFIX = '.O...O'  

braille_dict_inv = {v: k for k, v in braille_dict.items()}


def is_braille(text):
    return all(c in 'O. ' for c in text)


def english_to_braille(text):
    result = []
    number_mode = False
    for i, char in enumerate(text):
        if char.isupper():
            result.append(CAPITAL_PREFIX)
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_PREFIX)
                number_mode = True
            result.append(braille_dict[chr(ord('a') + (int(char) - 1) % 10)])
        
        elif char == '.' and i < len(text) - 1 and text[i + 1].isdigit():
            result.append(DECIMAL_PREFIX)
        elif char in braille_dict:
            if number_mode and char not in '0123456789.':
                number_mode = False 
            result.append(braille_dict[char])
        elif char == '.' and not number_mode:
            result.append(braille_dict['.'])

    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    number_mode = False
    capital_next = False

    while i < len(braille):
        current_segment = braille[i:i+6]

        if current_segment == CAPITAL_PREFIX:
            capital_next = True
            i += 6
            continue
        elif current_segment == NUMBER_PREFIX:
            number_mode = True
            i += 6
            continue

        if current_segment in braille_dict_inv:
            char = braille_dict_inv[current_segment]

            if number_mode:
                if 'a' <= char <= 'j':
                    if char == 'j':
                        char = '0'
                    else:
                        char = str(ord(char) - ord('a') + 1)
                else:
                    number_mode = False 

            if capital_next:
                char = char.upper()
                capital_next = False

            result.append(char)
        else:
            result.append('?')

        i += 6

    return ''.join(result)


def main():
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == '__main__':
    main()
