# Braille Translator
# This program translates English to Braille and vice versa.
# Aniket Mishra: ianiket23@gmail.com
# Shopify Technical Challenge 2024

# Import the sys module for command line arguments
import sys

# Constants
CAPITAL = '.....O'
NUMBER = '.O.OOO'
SPACE = '......'

ALPHA_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
}
NUM_DICT = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# This function expands the dictionary to include the key-value pairs in reverse.
# Arguments: None
# Returns: Expanded dictionaries
def dict_expander():
    alpha_dict_expanded = {}
    num_dict_expanded = {}

    for key, value in ALPHA_DICT.items():
        alpha_dict_expanded[value] = key
        alpha_dict_expanded[key] = value

    for key, value in NUM_DICT.items():
        num_dict_expanded[value] = key
        num_dict_expanded[key] = value

    return alpha_dict_expanded, num_dict_expanded

# This function translates English to Braille
# Arguments: English string, expanded dictionaries
def english_to_braille(english_string, alpha_dict_exp, num_dict_exp):
    braille_string = ''

    # This checks if the character is a number, and if it is seen for the first time in that sequence
    # it adds the NUMBER constant to the braille string
    # a num sequence is ended by a space
    is_num = False

    for char in english_string:
        # try-except block to handle if the char is not in the dictionary
        try:
            if char.isalpha():
                if char.isupper():
                    braille_string += CAPITAL
                    char = char.lower()
                braille_string += alpha_dict_exp[char]
            elif char.isnumeric():
                if not is_num:
                    braille_string += NUMBER
                    is_num = True
                braille_string += num_dict_exp[char]
            elif char == ' ':
                braille_string += SPACE
                # reset the is_num flag as the number sequence has ended
                is_num = False
        except KeyError:
            print(f"This '{char}' is not supported")
            sys.exit(1)

    return braille_string

def braille_to_english(braille_string, alpha_dict_exp, num_dict_exp):
    # overall complete string
    english_string = ''

    # temporary string to store the braille characters
    temp = ''

    # flags to check if the character is a capital letter
    is_capital = False

    # flags to check if the character is a number
    is_num = False

    # Looping as 1-indexed to take care of the divide by 6 condition
    for i in range(1, len(braille_string) + 1):
        temp += braille_string[i - 1]

        # if the character is a multiple of 6, it is a complete braille character
        if (i) % 6 == 0 and i != 0:
            if temp == SPACE:
                english_string += ' '
                is_num = False

            elif temp == CAPITAL:
                is_capital = True

            elif temp == NUMBER:
                is_num = True

            else:
                # try-except block to handle if the char is not in the dictionary
                try:
                    if is_num:
                        english_string += num_dict_exp[temp]
                    else:
                        if is_capital:
                            english_string += alpha_dict_exp[temp].upper()
                            is_capital = False
                        else:
                            english_string += alpha_dict_exp[temp]
                except KeyError:
                    print(f"This '{temp}' is not supported")
                    sys.exit(1)
            temp = ''

    return english_string

# main function
if __name__ == '__main__':
    alpha_dict_exp, num_dict_exp = dict_expander()

    if len(sys.argv) == 1:
        print("No runtime arguments given")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    if input_string[0] == '.' or input_string[0] == 'O':
        if len(input_string) % 6 != 0:
            print("Invalid Braille string")
            sys.exit(1)
        print(braille_to_english(input_string, alpha_dict_exp, num_dict_exp))
    else:
        print(english_to_braille(input_string, alpha_dict_exp, num_dict_exp))