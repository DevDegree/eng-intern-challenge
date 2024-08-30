import sys

# Braille dictionary mapping for each letter (lowercase), number, and special symbols
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.',
    'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'cap': '.....O',  # Capitalization symbol
    'num': '.O.OOO',  # Number symbol
    ' ': '......'  # Space
}

# Reverse map Braille back to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Numbers mapping from 0 to 9
number_map = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

reverse_number_map = {v: k for k, v in number_map.items()}

def is_braille(input_str):
    # Simple check if input consists only of 'O', '.'
    return all(char in ['O', '.'] for char in input_str)
def translate_to_braille(input_str):
    translated = ""
    is_number = False

    for char in input_str:
        if char.isdigit():
            if not is_number:
                translated += braille_dict['num']
                is_number = True
            translated += braille_dict[number_map[char]]
        elif char.isalpha():
            if char.isupper():
                translated += braille_dict['cap']
            translated += braille_dict[char.lower()]
            is_number = False
        elif char == ' ':
            translated += braille_dict[' ']
            is_number = False

    return translated


def translate_to_english(input_str):
    translated = ""
    i = 0
    is_capital = False
    is_number = False

    while i < len(input_str):
        # Extract the current Braille cell (6 characters)

        braille_char = input_str[i:i + 6]
        if braille_char == braille_dict[' ']:
            translated += ' '
            is_number = False
        elif braille_char == braille_dict['cap']:
            is_capital = True
        elif braille_char == braille_dict['num']:
            is_number = True
        else:
            if is_number:
                translated += reverse_number_map[reverse_braille_dict[braille_char]]
            elif is_capital:
                translated += reverse_braille_dict[braille_char].upper()
                is_capital = False
            else:
                translated += reverse_braille_dict[braille_char]
        i += 6

    return translated


if __name__ == "__main__":
    # Join the command-line arguments into a single string
    input_str = ' '.join(sys.argv[1:])

    result = ""

    if is_braille(input_str):
        result = translate_to_english(input_str)
    else:
        result = translate_to_braille(input_str)

    # Output the result
    print(result)
