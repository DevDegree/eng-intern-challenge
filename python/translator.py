import sys

# define a dictionary that maps each letter of the alphabet to its corresponding Braille character
braille_dict_alpha = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', "-": '....OO', '/': '.O..O.','(':'O.O..O',')':'.O.OO.',':':'..OO..',';':'..O.O.','capital':'.....O','number':'.O.OOO'
}

# define a dictionary that maps each digit to its corresponding Braille character
braille_dict_num = {
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

braille_dict_alpha_reverse = {value: key for key, value in braille_dict_alpha.items()}
braille_dict_num_reverse = {value: key for key, value in braille_dict_num.items()}

#helper function
def is_number_braille(substring):
    return substring == braille_dict_alpha['number']

def is_capital_braille(substring):
    return substring == braille_dict_alpha['capital']

def is_space_braille(substring):
    return substring == braille_dict_alpha[' ']

def if_braille_format(user_input):
  if len(user_input) % 6 != 0:
    return False
  if set(user_input) != set(['O', '.']):
    return False
  else:
    return True

def convert_to_braille(user_input):
    converted_text = ""
    is_num = False
    # Iterate through the user input and convert each letter to its corresponding Braille character
    for character in user_input:
        # Handle uppercase characters
        if character.isupper():
            converted_text += braille_dict_alpha['capital']

        # Handle digits
        if character.isdigit():
            if not is_num:
                converted_text += braille_dict_alpha['number']
                is_num = True
            converted_text += braille_dict_num[character]
            continue

        # Reset number flag if a space is encountered
        if character == ' ':
            is_num = False

        # Convert lowercase letters to Braille
        converted_text += braille_dict_alpha[character.lower()]

    return converted_text
  
def convert_to_text(user_input):
    is_num = False
    is_capital = False
    converted_text = ""

    # Split string into 6-character substrings
    substrings = [user_input[i:i+6] for i in range(0, len(user_input), 6)]

    # Iterate through the substrings and convert each substring to its corresponding letter
    for substring in substrings:
        if is_number_braille(substring):
            is_num = True
            continue
        elif is_space_braille(substring):
            converted_text += braille_dict_alpha_reverse[substring]
            is_num = False
        elif is_num:
            converted_text += braille_dict_num_reverse[substring]
            continue
        elif is_capital_braille(substring):
            is_capital = True
            continue
        elif substring in braille_dict_alpha_reverse:
            if is_capital:
                converted_text += braille_dict_alpha_reverse[substring].capitalize()
                is_capital = False
            else:
                converted_text += braille_dict_alpha_reverse[substring]
        else:
            convert_to_braille(user_input)
            break

    return converted_text


if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print("no user input")
  else:
    user_input = ' '.join(sys.argv[1:])
    if if_braille_format(user_input):
      print(convert_to_text(user_input))
    else:
      print(convert_to_braille(user_input))
    