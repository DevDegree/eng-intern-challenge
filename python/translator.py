import sys


CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'


char_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

nums_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_to_char = {v: k for k, v in char_to_braille.items()}
braille_to_number = {v: k for k, v in nums_to_braille.items()}


def is_braille(text):
    return set(text).issubset({'O', '.'})

def convert_braille_to_english(braille_text):
    result = []
    num_follows = False
    capital_follows = False

    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]

        if braille_char == CAPITAL_FOLLOWS:
            capital_follows = True
            continue
        elif braille_char == NUMBER_FOLLOWS:
            num_follows = True
            continue
        elif braille_char == '......': 
            num_follows = False

        if num_follows:
            result.append(braille_to_number.get(braille_char, '?'))
        elif capital_follows:
            result.append(braille_to_char.get(braille_char, '?').upper())
            capital_follows = False
        else:
            result.append(braille_to_char.get(braille_char, '?'))

    return ''.join(result)

def convert_english_to_braille(english_text):
    """Convert English text to Braille"""
    result = []
    num_follows = False

    for char in english_text:
        if char.isalpha():
            if char.isupper():
                result.append(CAPITAL_FOLLOWS)
            result.append(char_to_braille[char.lower()])
        elif char.isdigit():
            if not num_follows:
                num_follows = True
                result.append(NUMBER_FOLLOWS)
            result.append(nums_to_braille[char])
        elif char == ' ':
            num_follows = False
            result.append(char_to_braille[char])

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        return

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        print(convert_braille_to_english(input_text))
    else:
        print(convert_english_to_braille(input_text))

if __name__ == '__main__':
    main()
