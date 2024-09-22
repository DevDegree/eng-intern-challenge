import sys

# Note the special characters are not handled in this PR as requirement in README and https://github.com/DevDegree/eng-intern-challenge/issues/196

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
    # Simple check if input consists only of 'O', '.' and has valid Braille structure
    if len(input_str) % 6 != 0:
        return False

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
        elif char == ' ':
            translated += braille_dict[' ']
            is_number = False
        else:
            raise ValueError(f"Invalid character '{char}' in input. Only letters, digits, and spaces are allowed for English.")

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
            if is_capital:
                raise ValueError("Repeated capitalization marker detected.")
            is_capital = True
        elif braille_char == braille_dict['num']:
            if is_number:
                raise ValueError("Repeated number marker detected.")
            is_number = True
        elif braille_char in reverse_braille_dict:
            if is_number:
                # make sure a number after number follows symbol
                if reverse_braille_dict[braille_char] not in 'abcdefghijklmnopqrstuvwxyz':
                    raise ValueError(f"Expected a number after number marker, but got '{braille_char}'")
                translated += reverse_number_map[reverse_braille_dict[braille_char]]
            elif is_capital:
                # make sure a letter after letter follows symbol
                if reverse_braille_dict[braille_char] not in 'abcdefghijklmnopqrstuvwxyz':
                    raise ValueError(f"Expected a letter after capitalization marker, but got '{braille_char}'")
                translated += reverse_braille_dict[braille_char].upper()
                is_capital = False
            else:
                translated += reverse_braille_dict[braille_char]
        else:
            raise ValueError(f"Invalid Braille pattern '{braille_char}' encountered during translation.")

        i += 6

    return translated


if __name__ == "__main__":
    try:
        # Join the command-line arguments into a single string
        input_str = ' '.join(sys.argv[1:])

        # if no input then output None
        if input_str is None or input_str.strip() == "":
            print(None)
            sys.exit(0)

        result = ""

        if is_braille(input_str):
            result = translate_to_english(input_str)
        else:
            result = translate_to_braille(input_str)

        # Output the result
        print(result)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
