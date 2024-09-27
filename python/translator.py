import sys

# Braille character mappings for letters, numbers, and special symbols
braille_dict = {
    'letters': {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO'
    },
    'nums': {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    },
    'special': {
        'capital': '.....O', 'number': '.O.OOO', 'space': '......', 
        'period': '..OO.O', 'comma': '..O...', 'question': '..O.OO', 'exclamation': '..OOO.', 
        'colon': '..OO..', 'semicolon': '..O.O.', 'dash': '....OO', 'slash': '.O..O.', 
        'lt': '.O.O.O', 'gt': 'O.O.O.', 'open_paren': 'O.O..O', 'close_paren': '.O.OO.'
    }
}

# Reversed mappings for translating Braille back to English
reverse_dict = {
    'letters': {v: k for k, v in braille_dict['letters'].items()},
    'nums': {v: k for k, v in braille_dict['nums'].items()},
    'special': {v: k for k, v in braille_dict['special'].items()}
}

def is_braille(input_str):
    """Checks if a string follows the Braille format by validating each 6-character cell."""
    if len(input_str) % 6 != 0:
        return False

    for i in range(0, len(input_str), 6):
        braille_cell = input_str[i:i+6]
        if braille_cell not in reverse_dict['letters'] and braille_cell not in reverse_dict['nums'] and braille_cell not in reverse_dict['special']:
            return False

    return True

def text_to_braille(english_text):
    """Converts English characters to Braille, handling digits, uppercase, and spaces."""
    braille_output = []
    num_mode = False

    for char in english_text:
        if char.isdigit():
            if not num_mode:
                braille_output.append(braille_dict['special']['number'])
                num_mode = True
            braille_output.append(braille_dict['nums'][char])

        elif char == ' ':
            braille_output.append(braille_dict['special']['space'])
            num_mode = False  # End number mode after space

        elif char.isupper():
            braille_output.append(braille_dict['special']['capital'])
            braille_output.append(braille_dict['letters'][char.lower()])
            num_mode = False  # End number mode after capital letter

        else:
            braille_output.append(braille_dict['letters'].get(char, '?'))  # Unknown characters
            num_mode = False  # End number mode after any non-digit/non-capital

    return ''.join(braille_output)

def braille_to_text(braille_input):
    """Converts Braille to English, interpreting number, capital, and space markers."""
    english_output = []
    num_mode = False
    cap_mode = False

    for i in range(0, len(braille_input), 6):
        braille_char = braille_input[i:i+6]
        if braille_char == braille_dict['special']['capital']:
            cap_mode = True

        elif braille_char == braille_dict['special']['number']:
            num_mode = True

        elif braille_char == braille_dict['special']['space']:
            num_mode = False
            cap_mode = False
            english_output.append(' ')

        else:
            if braille_char in (reverse_dict['letters'] if not num_mode else reverse_dict['nums']):
                char = (reverse_dict['letters'] if not num_mode else reverse_dict['nums'])[braille_char]

                if cap_mode:
                    char = char.upper()
                    cap_mode = False

                english_output.append(char)
            else:
                english_output.append('?')

    return ''.join(english_output)

def process_input(input_text):
    """Determines whether the input is Braille or English and translates it accordingly."""
    if is_braille(input_text):
        return braille_to_text(input_text)
    else:
        return text_to_braille(input_text)

def main():
    """Handles command-line input, translates, and displays the result."""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        return

    input_data = ' '.join(sys.argv[1:])
    translated_result = process_input(input_data)
    sys.stdout.write(translated_result)

if __name__ == "__main__":
    main()
