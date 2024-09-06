import sys

# Define Braille translation dictionaries
english_to_braille = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', ' ': '......'
}

braille_numbers_and_signs = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '..O..O',
    '.': '.O...O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

braille_signifiers = {
    'CAPITAL': '.....O',  # Capitalization signifier
    'NUMBER': '.O.OOO',  # Number signifier
    'DECIMEL': '.O...O'  # Decimal point
}

def to_Braille(english_string):
    """
    Converts an English string to its corresponding Braille representation.

    Args:
        english_string (str): The input string to be translated to Braille.

    Returns:
        str: The translated Braille string.
    """
    braille_output = ""
    in_number_mode = False

    for char in english_string:
        if char.isdigit():
            if not in_number_mode:
                braille_output += braille_signifiers['NUMBER']
                in_number_mode = True
            braille_output += braille_numbers_and_signs.get(char, '')
        elif char in braille_numbers_and_signs:
            braille_output += braille_numbers_and_signs.get(char, '')
        elif char.isupper():
            braille_output += braille_signifiers['CAPITAL']
            braille_output += english_to_braille.get(char, '')
            in_number_mode = False
        elif char.islower() or char == ' ':
            braille_output += english_to_braille.get(char.upper(), '')
            in_number_mode = False
        else:
            braille_output += '?'  # Placeholder for unrecognized characters

    return braille_output

def to_String(braille_input):
    """
    Converts a Braille string to its corresponding English representation.

    Args:
        braille_input (str): The input Braille string to be translated to English.

    Returns:
        str: The translated English string.
    """
    braille_bit_length = 6
    result = ''
    braille_to_english_map = {v: k for k, v in english_to_braille.items()}
    braille_signifier_map = {v: k for k, v in braille_signifiers.items()}
    braille_numbers_and_signs_map = {v: k for k, v in braille_numbers_and_signs.items()}

    braille_bits = [braille_input[i:i + braille_bit_length] for i in range(0, len(braille_input), braille_bit_length)]
    is_cap = False
    is_num = False

    for braille in braille_bits:
        if braille == braille_signifiers['CAPITAL']:
            is_cap = True
            continue
        elif braille == braille_signifiers['NUMBER']:
            is_num = True
            continue
        elif braille == braille_signifiers['DECIMEL']:
            result += '.'
            is_num = True
            continue
        elif braille == '......':
            result += ' '
            is_num = False
            continue
        elif (braille in braille_to_english_map and is_num!=True):
            char = braille_to_english_map[braille]
            if is_cap:
                result += char.upper()
                is_cap = False
            else:
                result += char.lower()
        elif braille in braille_numbers_and_signs_map:
            result += braille_numbers_and_signs_map[braille]
        else:
            result += '?'  # Placeholder for unrecognized Braille patterns

    return result

def main():
    """
    Main function to handle input and output for the Braille translator.
    """
    input_string = " ".join(sys.argv[1:])

    # Determine if the input is likely Braille or English text
    if all(c in "O." for c in input_string):
        # Assume the input is Braille
        english_output = to_String(input_string)
        print(english_output)
    else:
        # Assume the input is English text
        braille_output = to_Braille(input_string)
        print(braille_output)

if __name__ == "__main__":
    main()
