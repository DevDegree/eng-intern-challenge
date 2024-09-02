import sys

# cnstants 
CAPITAL_LETTER = '.....O'
NUMBER_PREFIX = '.O.OOO'
BLANK = '......'

# translation 
BRAILLE_ALPHA = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
}

BRAILLE_NUM = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

def create_reverse_dicts():
    """
    Generates reverse lookup dictionaries for Braille translation.
    """
    alpha_reverse = {}
    num_reverse = {}

    for letter, braille in BRAILLE_ALPHA.items():
        alpha_reverse[braille] = letter
        alpha_reverse[letter] = braille

    for digit, braille in BRAILLE_NUM.items():
        num_reverse[braille] = digit
        num_reverse[digit] = braille

    return alpha_reverse, num_reverse

def text_to_braille(text, alpha_rev_dict, num_rev_dict):
    """
    Converts regular text to Braille representation.
    """
    braille_result = ''
    is_number_sequence = False

    for char in text:
        if char.isalpha():
            if char.isupper():
                braille_result += CAPITAL_LETTER
                char = char.lower()
            braille_result += alpha_rev_dict[char]
            is_number_sequence = False
        elif char.isdigit():
            if not is_number_sequence:
                braille_result += NUMBER_PREFIX
                is_number_sequence = True
            braille_result += num_rev_dict[char]
        elif char == ' ':
            braille_result += BLANK
            is_number_sequence = False
        else:
            print(f"Character '{char}' is not supported.")
            sys.exit(1)

    return braille_result

def braille_to_text(braille, alpha_rev_dict, num_rev_dict):
    """
    Converts Braille representation back to regular text.
    """
    text_result = ''
    current_braille = ''
    is_capital = False
    is_number = False

    for index, char in enumerate(braille):
        current_braille += char

        if (index + 1) % 6 == 0:
            if current_braille == BLANK:
                text_result += ' '
                is_number = False
            elif current_braille == CAPITAL_LETTER:
                is_capital = True
            elif current_braille == NUMBER_PREFIX:
                is_number = True
            else:
                try:
                    if is_number:
                        text_result += num_rev_dict[current_braille]
                    else:
                        if is_capital:
                            text_result += alpha_rev_dict[current_braille].upper()
                            is_capital = False
                        else:
                            text_result += alpha_rev_dict[current_braille]
                except KeyError:
                    print(f"Braille character '{current_braille}' is not recognized.")
                    sys.exit(1)
            current_braille = ''

    return text_result

def main():
    alpha_rev_dict, num_rev_dict = create_reverse_dicts()

    if len(sys.argv) < 2:
        print("No input provided.")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])
    if input_str[0] in {'.', 'O'}:
        if len(input_str) % 6 != 0:
            print("Invalid Braille format.")
            sys.exit(1)
        print(braille_to_text(input_str, alpha_rev_dict,num_rev_dict))
    else:
        print(text_to_braille(input_str, alpha_rev_dict, num_rev_dict))

if __name__ == '__main__':
    main()